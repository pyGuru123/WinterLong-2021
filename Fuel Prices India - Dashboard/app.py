import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

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
						id='petrol-chart', config={"displayModeBar": False}
					),
					className="card",
				),
			],
			className="wrapper",
		),
	]
)

@app.callback(
	dash.dependencies.Output('region-filter', 'options'),
	[dash.dependencies.Input('type-filter', 'value')]
)
def update_date_dropdown(name):
	return [{'label': i, 'value': i} for i in fuelDict[name]]




if __name__ == '__main__':
	app.run_server(debug=True)