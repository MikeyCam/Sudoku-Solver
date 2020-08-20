import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from styling_items import StylingItems

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])


app.layout = html.Div(
    children=[
        html.Div(StylingItems.navbar),
        html.Div(StylingItems.jumbotron),
        html.Div(StylingItems.editable_table),
            ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
