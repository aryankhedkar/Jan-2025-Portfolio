# pages/writing.py
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/writing")

layout = dbc.Container([
    html.H2("Writing & Publications", className="mt-4 mb-3 text-center"),
    html.P("""
        I frequently write about psychology, philosophy, and technology. Below are some 
        articles and essays that capture my perspective and insights.
    """, className="text-center mb-4"),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("On Resilience & Truth", className="card-title"),
                    html.P("A short reflection on personal growth amid adversity.", className="card-text"),
                    dbc.Button("Read Article", 
                               href="/assets/article1.pdf", 
                               external_link=True, 
                               color="info")
                ])
            ], className="mb-4 shadow-sm")
        ], md=6),

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Spirituality & Leadership", className="card-title"),
                    html.P("An exploration of how spiritual practice can inform leadership.", className="card-text"),
                    dbc.Button("Read Article", 
                               href="/assets/article2.pdf", 
                               external_link=True, 
                               color="info")
                ])
            ], className="mb-4 shadow-sm")
        ], md=6),
    ], className="mb-5"),

    dbc.Alert(
        "More articles coming soon! Stay tuned for my upcoming posts.",
        color="secondary",
        className="text-center"
    )
], fluid=True)
