# pages/projects.py
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

dash.register_page(__name__, path="/projects")

# Sample data for Plotly demonstration
df = pd.DataFrame({
    "Project": ["Renewable Energy Forecasting", "Financial Risk Analysis", "Healthcare ML"],
    "Performance": [88, 92, 81]
})
fig = px.bar(df, x="Project", y="Performance", title="Project Performance Comparison")

layout = dbc.Container([
    html.H2("My Key Projects", className="mt-4 mb-3 text-center"),
    html.P("""
        Here are three of my main works. Click the links to see the pitch decks, 
        MVP demos, and business plans. If you have any questions, feel free to reach out!
    """, className="text-center mb-5"),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardImg(src="/assets/images/renewable_energy.jpg", top=True),  # Example image
                dbc.CardBody([
                    html.H4("Renewable Energy Forecasting", className="card-title"),
                    html.P("Predicting solar and wind energy outputs with ML.", className="card-text"),
                    dbc.Button("Pitch Deck", 
                               href="/assets/renewable_pitch.pdf", 
                               external_link=True, 
                               color="primary", 
                               className="m-1"),
                    dbc.Button("MVP Demo", 
                               href="/assets/renewable_mvp.pdf", 
                               external_link=True, 
                               color="secondary", 
                               className="m-1"),
                    dbc.Button("Business Plan", 
                               href="/assets/renewable_bp.pdf", 
                               external_link=True, 
                               color="dark", 
                               className="m-1")
                ])
            ], className="shadow-sm mb-4"),
        ], md=4),
        
        dbc.Col([
            dbc.Card([
                dbc.CardImg(src="/assets/images/finance.jpg", top=True),
                dbc.CardBody([
                    html.H4("Financial Risk Analysis", className="card-title"),
                    html.P("Quantitative research & predictive modeling for finance.", className="card-text"),
                    dbc.Button("Pitch Deck", 
                               href="/assets/finance_pitch.pdf", 
                               external_link=True, 
                               color="primary", 
                               className="m-1"),
                    dbc.Button("MVP Demo", 
                               href="/assets/finance_mvp.pdf", 
                               external_link=True, 
                               color="secondary", 
                               className="m-1"),
                    dbc.Button("Business Plan", 
                               href="/assets/finance_bp.pdf", 
                               external_link=True, 
                               color="dark", 
                               className="m-1")
                ])
            ], className="shadow-sm mb-4"),
        ], md=4),
        
        dbc.Col([
            dbc.Card([
                dbc.CardImg(src="/assets/images/healthcare.jpg", top=True),
                dbc.CardBody([
                    html.H4("Machine Learning in Healthcare", className="card-title"),
                    html.P("Faster diagnosis and optimized treatment plans.", className="card-text"),
                    dbc.Button("Pitch Deck", 
                               href="/assets/healthcare_pitch.pdf", 
                               external_link=True, 
                               color="primary", 
                               className="m-1"),
                    dbc.Button("MVP Demo", 
                               href="/assets/healthcare_mvp.pdf", 
                               external_link=True, 
                               color="secondary", 
                               className="m-1"),
                    dbc.Button("Business Plan", 
                               href="/assets/healthcare_bp.pdf", 
                               external_link=True, 
                               color="dark", 
                               className="m-1")
                ])
            ], className="shadow-sm mb-4"),
        ], md=4),
    ], className="mb-5"),

    html.H4("Archived Projects", className="mb-3 text-center"),
    dbc.Carousel(
        items=[
            {
                "key": "1",
                "header": "Archived Project 1",
                "img_src": "/assets/images/archived1.jpg",  
                "caption": html.A("View PDF", href="/assets/archived_proj1.pdf", target="_blank", className="text-white")
            },
            {
                "key": "2",
                "header": "Archived Project 2",
                "img_src": "/assets/images/archived2.jpg",
                "caption": html.A("View PDF", href="/assets/archived_proj2.pdf", target="_blank", className="text-white")
            },
        ],
        controls=True,
        indicators=True,
        interval=3000,  # 3 seconds per carousel item
        ride="carousel",
        className="mb-5"
    ),

    html.Hr(),
    html.H3("Project Performance Insights", className="text-center mb-3"),
    dcc.Graph(figure=fig, className="mb-5"),

], fluid=True)
