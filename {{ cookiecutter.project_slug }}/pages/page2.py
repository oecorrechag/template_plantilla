from dash import html
import dash_bootstrap_components as dbc

from components.CallbacksPage2 import page2, grafica

layout2 = dbc.Container([

    html.Br(),
    html.H3('Page 2'),

    page2,

    grafica,

])
