import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

from csvparser import get_dataframe

df, cities = get_dataframe()
fuel_type = ['Diesel', 'Petrol']
diesel_cities, petrol_cities = cities
fuelDict = {fuel_type[0]:diesel_cities, fuel_type[1]:petrol_cities}

external_stylesheets = [
	{
		"href": "https://fonts.googleapis.com/css2?"
		"family=Lato:wght@400;700&display=swap",
		"rel": "stylesheet",
	},
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Fuel Analytics: Understand Fuel Prices!"

app.layout = html.Div(
	children=[
		html.Div(
			children=[
				html.Img(
					src="assets/fuel_icon.png", className="header-img"
				),
				html.H1(
					"Fuel Analytics", className="header-title"
				),
				html.P(
					"Analyze the prices of petrol and diesel "
						"in various cities of India between" 
						" 2001 to 2020.", className="header-description"
				),
			], className="header"
		),
		html.Div(
			children=[
				html.Div(
					children=[
						html.Div(children="Region", className="menu-title"),
						dcc.Dropdown(
							id="region-filter",
							options=[
								{"label":region, "value":region}
								for region in diesel_cities
							],
							value='Delhi',
							clearable=False,
							className="dropdown"
						),
					]
				),
				html.Div(
					children=[
						html.Div(children="Fuel Type", className="menu-title"),
						dcc.Dropdown(
							id="type-filter",
							options=[
								{"label":fuel, "value":fuel}
								for fuel in fuel_type
							],
							value='Diesel',
							clearable=False,
							searchable=False,
							className="dropdown"
						),
					]
				),
				html.Div(
					children=[
						html.Div(children="Date Range", className="menu-title"),
						dcc.DatePickerRange(
							id="date-range",
							min_date_allowed=df.date.min().date(),
							max_date_allowed=df.date.max().date(),
							start_date=df.date.min().date(),
							end_date=df.date.max().date(),
						),
					]
				),
			], 
			className='menu'
		),
		html.Div(
			children=[
				html.Div(
					children=dcc.Graph(
						id='price-chart', config={"displayModeBar": False}
					),
					className="card",
				),
			],
			className="wrapper",
		),
	]
)

@app.callback(
	Output('region-filter', 'options'),
	[Input('type-filter', 'value')]
)
def update_date_dropdown(name):
	return [{'label': i, 'value': i} for i in fuelDict[name]]


@app.callback(
	Output("price-chart", "figure"),
	[
		Input("region-filter", "value"),
		Input("type-filter", "value"),
		Input("date-range", "start_date"),
		Input("date-range", "end_date"),
	]
)
def update_chart(region, fuel, start_date, end_date):
	mask = (
		(df.city == region)
		& (df.fuel == fuel)
		& (df.date >= start_date)
		& (df.date <= end_date)
	)
	filtered_data = df.loc[mask, :]
	price_chart_figure = {
		"data": [
			{
				"x": filtered_data["date"],
				"y": filtered_data["rate"],
				"type": "lines",
				"hovertemplate": "$%{y:.2f}<extra></extra>",
			},
		],
		"layout": {
			"title": {
				"text": f"Average Price of {fuel} in {region}",
				"x": 0.05,
				"xanchor": "left",
			},
			"xaxis": {"fixedrange": True},
			"yaxis": {"tickprefix": "₹", "fixedrange": True},
			"colorway": ["#17B897"],
		},
	}

	return price_chart_figure

if __name__ == '__main__':
	app.run_server(debug=True)