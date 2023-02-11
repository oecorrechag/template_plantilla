from dash import html
import dash_bootstrap_components as dbc

from components.CallbacksPage1 import page1

layout1 = dbc.Container([

    html.Br(),
    html.H3('Page 1'),

    page1,

])
