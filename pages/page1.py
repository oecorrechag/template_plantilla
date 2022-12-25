from dash import dcc, html

import dash_bootstrap_components as dbc

from components.CallbacksPage1 import Menu
from components.CallbacksPage1 import Page1Box1
from components.CallbacksPage1 import Page1Table
from components.CallbacksPage1 import Page1Graph1

layout1 = html.Div([

    dcc.Link('Go to Page 2', href='/page2'),
    html.Br(),
    dcc.Link('Go to Home', href='/'), 

    Menu,
    html.H3('Page 1'),

    dbc.Row(children=[
        Page1Box1,
        Page1Table, 
        Page1Graph1,
    ]),


])