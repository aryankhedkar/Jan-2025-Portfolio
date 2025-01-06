#app.py

import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from dash import Input, Output, State

# ------------------------------------------------------------------------------
# 1. INITIALIZE APP
# ------------------------------------------------------------------------------
#
# Dash automatically loads any .css or .js files in the `assets` folder.
# We also load a minimal Bootstrap theme. We'll rely on our `assets/styles.css`
# for the main black/white styling, Google Fonts import, etc.

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],  # minimal base theme
    suppress_callback_exceptions=True
)

# ------------------------------------------------------------------------------
# 2. NAVIGATION BAR
# ------------------------------------------------------------------------------
#
# - Black background
# - White text
# - Accent color (#1da1f2) on hover or for brand highlight (handled in CSS)

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand("Aryan D. Khedkar", className="navbar-brand"),
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/", active="exact", className="nav-link mx-2"),
                    dbc.NavLink("Projects", href="/projects", active="exact", className="nav-link mx-2"),
                    dbc.NavLink("Writing", href="/writing", active="exact", className="nav-link mx-2"),
                    dbc.NavLink("My Story", href="/about_me", active="exact", className="nav-link mx-2"),
                    dbc.NavLink("Connect", href="/connect", active="exact", className="nav-link mx-2"),
                ],
                navbar=True,
                className="ms-auto"
            ),
        ],
        fluid=True
    ),
    color="black",
    dark=True,
    sticky="top",
    className="mb-4"
)

# ------------------------------------------------------------------------------
# 3. FOOTER
# ------------------------------------------------------------------------------
#
# - Black background
# - Subtle gray divider
# - White text, with hover effect to accent color in CSS

footer = html.Footer(
    dbc.Container(
        [
            html.Hr(className="bg-secondary"),
            # A short statement about you or your mission
            html.P(
                [
                    "© 2025 Aryan D. Khedkar | ",
                    html.Span("Guided by Truth, Courage and Love, I aim to strive towards the Ideal of Innovation.")
                ],
                className="m-0 text-center text-white"
            ),

            # Social / professional links
            html.Div(
                [
                    html.A(
                        "LinkedIn",
                        href="https://www.linkedin.com/in/aryankhedkar0000/",
                        target="_blank",
                        className="footer-link mx-2"
                    ),
                    html.A(
                        "GitHub",
                        href="https://github.com/aryankhedkar",
                        target="_blank",
                        className="footer-link mx-2"
                    ),
                    html.A(
                        "YouTube",
                        href="https://www.youtube.com/@aryankhedkar0000",
                        target="_blank",
                        className="footer-link mx-2"
                    ),
                ],
                className="text-center mt-3"
            ),
        ],
        fluid=True,
        className="py-4"
    ),
    style={"backgroundColor": "black"}
)

# ------------------------------------------------------------------------------
# 4. APP LAYOUT
# ------------------------------------------------------------------------------
#
# We place:
#   - our navbar at the top,
#   - dash.page_container for each page in the middle,
#   - our consistent footer at the bottom.

app.layout = html.Div(
    [
        navbar,
        dash.page_container,
        footer
    ]
)

@app.callback(
    Output("contact-feedback", "children"),
    Input("contact-submit", "n_clicks"),
    State("contact-name", "value"),
    State("contact-email", "value"),
    State("contact-message", "value")
)
def handle_form(n_clicks, name, email, message):
    if n_clicks > 0:
        # Example logic (send email or store data)
        return "Thanks, truly. The fact that you spent a few min of your day to reach out to me means a lot to me. I'll get back to you asap."
    return ""

# ------------------------------------------------------------------------------
# 5. RUN SERVER
# ------------------------------------------------------------------------------
#
# "debug=True" for development (live reload). 
# Switch to False (or remove) for production.

if __name__ == "__main__":
    app.run_server(debug=True)
