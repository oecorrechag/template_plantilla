from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc


Menu = dbc.Row(children=[
    html.Div([
        html.H3('Page Menu'),
        html.Br(),
        dcc.Dropdown({f'Page 2 - {i}': f'{i}' for i in ['London', 'Berlin', 'Paris']}, id='Page2Select1'),
        html.Br(),
    ]),
])


Page2Box1 = dbc.Row(children=[
    html.Div([
        html.Div(id='page2_info1'),
    ]),
])
@callback(
    Output('page2_info1', 'children'),
    Input('Page2Select1', 'value'),
    )
def display_value(Page2Select1):
    page2_info1 = f'You have selected {Page2Select1}'
    return page2_info1
