from dash import html
import dash_bootstrap_components as dbc
from utils.consts import GITHUB_PROFILE, LINKEDIN_PROFILE, about_me_text


about = dbc.Container([

    dbc.Row([
        dbc.Col(className="col col-md-10 offset-md-1 col-lg-8 offset-lg-2 pt-2", children=[

            dbc.Card(
                dbc.CardBody([
                        dbc.Row([

                            dbc.Col(className="col-12 col-md-6 mb-4", children=[

                                html.Img(className="img-fluid", src="./assets/pc.jpg" , style={"border-radius":6})

                            ]),

                            dbc.Col(className="col-12 col-md-6 mb-4", children=[

                                html.H4("Who am I?", className="card-title"),
                                html.Small("A student", className="card-subtitle"),
                                html.P(about_me_text, className="card-text"),
                                
                                html.A(html.Img(src='assets\icons\github.png', width="72px", height="72px"), id='moving', href=GITHUB_PROFILE),
                                html.A(html.Img(src='assets\icons\linkedin.png', width="90px", height="90px"), href=LINKEDIN_PROFILE),

                            ]),
                        ]),
                    ]
                ),
            )

        ])
    ]),
])
