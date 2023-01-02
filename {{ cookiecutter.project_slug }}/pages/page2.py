from dash import dcc, html

from components.CallbacksPage2 import Menu
from components.CallbacksPage2 import Page2Box1
from components.CallbacksPage2 import Page2Graph1
from components.CallbacksPage2 import Page2Graph2

layout2 = html.Div([
    dcc.Link('Go to Page 1', href='/page1'),
    html.Br(),
    dcc.Link('Go to Home', href='/'),
    Menu,
    html.H3('Page 2'),
    Page2Box1,
    Page2Graph1,
    Page2Graph2,
])

