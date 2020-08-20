import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np


class StylingItems():
    navbar = dbc.NavbarSimple(

        dbc.NavItem(dbc.NavLink("LinkedIn", href="https://www.linkedin.com/")),
        className="navbar navbar-expand-lg navbar-dark bg-dark"
    )

    jumbotron = dbc.Jumbotron(
        [
            dbc.Container(
                [
                    html.H1("Sudoku Solver", className="display-3"),
                    html.P("Solving Sudoku with the numpy array functions.",
                           className="lead"
                           ),
                ],
            )
        ],
        className="jumbotron"
    )

    board = np.array([[0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0]])

    columns = ["Column {}".format(x) for x in range(1, 10)]
    rows = ["Row {}".format(x) for x in range(1, 10)]
    board = pd.DataFrame(board, columns=columns, index=rows)

    editable_table = html.Div([
        dash_table.DataTable(
            id='typing_formatting_1',
            columns=[{"name": i, "id": i, "type": "numeric"}
                     for i in board.columns],
            data=board.to_dict('rows'),
            style_header = {'display': 'none'},
            editable=True,
            style_cell={'textAlign': 'center'},
            style_data={
                'whiteSpace': 'normal',
                'height': 'auto',
            },
            style_data_conditional=[
                {
                    'if': {'column_id': ["Column 1", "Column 2", "Column 3"], 'row_index': [3, 4, 5]},
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white'
                },
                {
                    'if': {'column_id': ["Column 4", "Column 5", "Column 6"], 'row_index': [0, 1, 2]},
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white'
                },
                {
                    'if': {'column_id': ["Column 4", "Column 5", "Column 6"], 'row_index': [6, 7, 8]},
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white'
                },
                {
                    'if': {'column_id': ["Column 7", "Column 8", "Column 9"], 'row_index': [3, 4, 5]},
                    'backgroundColor': 'rgb(30, 30, 30)',
                    'color': 'white'
                },
            ],
        )
    ])
