#home.py

import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/")

layout = html.Div(
    [
        # -- HERO SECTION --
        html.Div(
            className="hero-section d-flex align-items-center justify-content-center text-center",
            children=[
                html.Div(className="hero-overlay"),
                html.Div(
                    className="hero-content",
                    children=[
                        html.Img(
                            src="/assets/images/profile.jpg",
                            className="profile-pic mb-3"
                        ),
                        html.H1(
                            "Aryan D. Khedkar",
                            className="hero-title"
                        ),
                        html.P(
                            "Imperial Physics Graduate | Entrepreneur | Business Intelligence ML Analyst",
                            className="hero-subtitle"
                        ),
                        # New vision statement
                        html.P(
                            "Combining Human Ingenuity with Machine Intelligence "
                            "in Sustainable Energy",
                            className="vision-text mt-4"
                        ),
                        dbc.Button(
                            "View My Work",
                            href="/projects",
                            color="primary",
                            className="mt-3 hero-cta-btn btn-lg"
                        )
                    ]
                ),
            ],
        ),



        # -- SNAPSHOT SECTION --
        html.Div(
            className="experience-section",  # <-- new wrapper
            children=[
                dbc.Container(
                    [
                        html.H2(
                            "Snapshot of My Experience",
                            className="mt-5 mb-3 text-center"
                        ),
                        html.P(
                            """
                            I am a physics graduate from Imperial College London with certifications 
                            in Data Analytics, Business Intelligence, and a deep learning specialization.
                            My passion lies in bridging science, technology, and business to create
                            sustainable, data-driven solutions.
                            """,
                            className="lead text-center mb-5"
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.Card(
                                        [
                                            dbc.CardHeader("Physics at Imperial"),
                                            dbc.CardBody(
                                                html.P("Strong foundation in theoretical and applied physics.")
                                            ),
                                            dbc.CardLink("View Projects", href="/projects", className="stretched-link")
                                            ],
                                            className="card-item text-center mb-4",
                                            style={"cursor": "pointer"}
                                            )                                    
                                    
                                ),
                                dbc.Col(
                                    dbc.Card(
                                        [
                                            dbc.CardHeader("Data Analytics & BI"),
                                            dbc.CardBody(
                                                html.P("Certified by Google with hands-on analytics experience.")
                                            ),
                                            dbc.CardLink("View Projects", href="/projects", className="stretched-link")
                                            ],
                                            className="card-item text-center mb-4",
                                            style={"cursor": "pointer"}
                                            )
                                ),

                                dbc.Col(
                                    dbc.Card(
                                        [
                                            dbc.CardHeader("Deep Learning Specialization"),
                                            dbc.CardBody(
                                                html.P("Stanford & DeepLearning.AI's advanced ML curriculum.")
                                            ),
                                        dbc.CardLink("View Projects", href="/projects", className="stretched-link")
                                            ],
                                            className="card-item text-center mb-4",
                                            style={"cursor": "pointer"}
                                            )
                                )
                                ],
                            justify="center"
                        ),
                    ],
                    fluid=True
                ),
            ],
        ),
    ]
)
