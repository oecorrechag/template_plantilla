from dash import dcc, html

# from components import menu

from components.CallbacksPage1 import Menu
from components.CallbacksPage1 import Page1Box1
from components.CallbacksPage1 import Page1Table
from components.CallbacksPage1 import Page1Graph1

layout1 = html.Div([

    html.Br(),
    dcc.Link('Go to Page 2', href='/page2'),
    html.Br(),
    dcc.Link('Go to Home', href='/'), 

    # menu.layout_menu,
    Menu,
    html.H3('Page 1'),

    # menu.layout_menu1,
    # menu.layout_menu2,
    # menu.layout_menu3,
    Page1Box1,
    Page1Table, 
    Page1Graph1,

])