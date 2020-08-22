import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from styling_items import StylingItems
from solver import random_board

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
app.title = 'Sudoku Solver'


app.layout = html.Div(
    children=[
        html.Div(StylingItems.navbar),
        html.Div(StylingItems.jumbotron),
        html.Div(StylingItems.selection_row),
        html.Div(StylingItems.editable_table),
    ]
)


@app.callback(
    Output(component_id='my_table', component_property='data'), 
    [
        Input("create-button", "n_clicks"), 
        Input('my-slider', 'value')
    ]
)
def update_output(data, value):
    blank_array = np.full((9, 9), 0)
    data = random_board(blank_array, value)
    return data


@app.callback(
    Output("solve-button-hidden-div",
           "children"), [Input("solve-button", "n_clicks")]
)
def on_button_click(value):
    print("solve_button_pushed".format(value))


if __name__ == "__main__":
    app.run_server(debug=True)
