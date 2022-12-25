from dash import dcc, html, dash_table, Input, Output, callback
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px

import utils.funtionsGraph as fg 

Menu = dbc.Row(children=[
    html.Div([
        html.H3('Page Menu'),
        html.Br(),
        dcc.Dropdown(['Uno', 'Dos', 'Tres'], 'Uno', id='select_1'),
        html.Br(),
        dcc.Dropdown({f'{i}': f'{i}' for i in ['SF', 'Montreal']}, id='select_2'),
    ]),
])


Page1Box1 = dbc.Row(children=[
    html.Div([
        html.Div(id='page1_info1'),
    ]),
])
@callback(
    Output('page1_info1', 'children'),
    Input('filter_data', 'data'),
    Input('select_1', 'value'),
    )
def display_value(data, select_1):
    data = pd.read_json(data)
    page1_info1 = select_1
    return page1_info1


Page1Table = dbc.Row(children=[
    html.Div([
        html.Div(id='page1_info2'),
    ]),
])
@callback(
    Output('page1_info2', 'children'),
    Input('filter_data', 'data'),
    Input('select_2', 'value'),
    )
def display_value(data, select_2):
    data = pd.read_json(data)
    df2 = data[data['City'] == select_2]
    page1_info2 = html.Div([
        dash_table.DataTable(
            data=df2.to_dict("rows"),
            columns=[{"id": x, "name": x} for x in df2.columns],
            page_size=20,
            # style_table={'height': '400px', 'overflowY': 'auto'},
            style_cell={'textAlign': 'center'},
            style_header={
                'backgroundColor': 'white',
                'fontWeight': 'bold'
            }
        )
    ])
    return page1_info2


Page1Graph1 = dbc.Row(children=[
    html.Div([
        dcc.Graph(id='page1_grafico1', figure={})
    ]),
])
@callback(
    Output('page1_grafico1', 'figure'),
    Input('filter_data', 'data'),
    Input('select_2', 'value'),
    )
def display_value(data, select_2):
    data = pd.read_json(data)
    df2 = data[data['City'] == select_2]
    page1_grafico1 = fg.barras(df2, x="Fruit", y="Amount", color="City")
    return page1_grafico1

