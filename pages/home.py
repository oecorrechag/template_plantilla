from dash import dcc, html

from components.CallbacksHome import Modal

home = html.Div([
    html.H3('Home Page'),
    dcc.Link('Go to Page 1', href='/page1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page2'),

    Modal

    ])
