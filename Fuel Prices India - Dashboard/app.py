import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from csvparser import get_dataframe

df = get_dataframe()
print(df)