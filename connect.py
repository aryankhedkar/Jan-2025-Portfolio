import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# Register this page under "/connect"
dash.register_page(__name__, path="/connect")

layout = html.Div(
    [
        # -- PAGE HEADER --
        dbc.Container(
            [
                html.H2("Connect with Me", className="display-5 mb-4 text-center"),
                html.P(
                    "I'd love to hear from you! Whether you're interested in collaborating, "
                    "have a question, or just want to say hello, feel free to drop me a line.",
                    className="text-center text-muted mb-5"
                ),
            ],
            fluid=True
        ),

        # -- CONTACT FORM --
        dbc.Container(
            [
                dbc.Row(
                    [
                        # You could add a small additional note or direct contact details in one column
                        # and a contact form in the other.
                        dbc.Col(
                            [
                                dbc.Card(
                                    [
                                        dbc.CardHeader("Get in Touch"),
                                        dbc.CardBody(
                                            [
                                                # Name Input
                                                dbc.Row(
                                                    [
                                                        dbc.Label("Name", width=3, className="text-white"),
                                                        dbc.Col(
                                                            dbc.Input(
                                                                type="text",
                                                                placeholder="Elon Musk",
                                                                id="contact-name",
                                                                className="mb-3"
                                                            ),
                                                            width=9
                                                        ),
                                                    ],
                                                    className="mb-3"
                                                ),
                                                # Email Input
                                                dbc.Row(
                                                    [
                                                        dbc.Label("Email", width=3, className="text-white"),
                                                        dbc.Col(
                                                            dbc.Input(
                                                                type="email",
                                                                placeholder= "elonmusk@gmail.com",
                                                                id="contact-email",
                                                                className="mb-3"
                                                            ),
                                                            width=9
                                                        ),
                                                    ],
                                                    className="mb-3"
                                                ),
                                                # Message Input
                                                dbc.Row(
                                                    [
                                                        dbc.Label("Message", width=3, className="text-white"),
                                                        dbc.Col(
                                                            dbc.Textarea(
                                                                placeholder="Hey Aryan, I'd love to discuss...",
                                                                id="contact-message",
                                                                className="mb-3"
                                                            ),
                                                            width=9
                                                        ),
                                                    ],
                                                    className="mb-3"
                                                ),
                                                # Submit Button
                                                dbc.Button(
                                                    "Send Message",
                                                    color="primary",
                                                    id="contact-submit",
                                                    className="mt-3",
                                                    n_clicks=0
                                                ),
                                                # Feedback after submission
                                                html.Div(
                                                    id="contact-feedback",
                                                    className="mt-3 text-white"
                                                ),
                                            ]
                                        )
                                    ],
                                    className="mb-4 contact-card"
                                )
                            ],
                            md=6
                        ),

                        # OPTIONAL: Another column for direct contact details or a short personal note
                        dbc.Col(
                            [
                                dbc.Card(
                                    [
                                        dbc.CardHeader("Other Ways to Reach Me"),
                                        dbc.CardBody(
                                            [
                                                html.P(
                                                    "If forms aren't your thing, feel free to use any of the "
                                                    "platforms below to get in touch or follow my work:"
                                                ),
                                                dbc.ListGroup(
                                                    [
                                                        dbc.ListGroupItem(
                                                            [
                                                                html.Strong("LinkedIn: "),
                                                                html.Span("Connect or message me directly")
                                                            ],
                                                            href="https://www.linkedin.com/in/aryankhedkar0000/",
                                                            target="_blank",
                                                            className="bg-transparent text-white"
                                                        ),
                                                        dbc.ListGroupItem(
                                                            [
                                                                html.Strong("GitHub: "),
                                                                html.Span("Explore my code and projects")
                                                            ],
                                                            href="https://github.com/aryankhedkar",
                                                            target="_blank",
                                                            className="bg-transparent text-white"
                                                        ),
                                                        dbc.ListGroupItem(
                                                            [
                                                                html.Strong("YouTube: "),
                                                                html.Span("Check out my videos and demos")
                                                            ],
                                                            href="https://www.youtube.com/@aryankhedkar0000",
                                                            target="_blank",
                                                            className="bg-transparent text-white"
                                                        )
                                                    ],
                                                    flush=True
                                                )
                                            ]
                                        )
                                    ],
                                    className="mb-4 contact-card"
                                )
                            ],
                            md=6
                        )
                    ],
                    justify="center"
                )
            ],
            fluid=True
        )
    ]
)
