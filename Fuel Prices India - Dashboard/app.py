import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from csvparser import get_dataframe

df = get_dataframe()

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
						"in India between 2001 to 2020.", className="header-description"
				),
			], className="header"
		)
	]
)

if __name__ == '__main__':
	app.run_server(debug=True)