import dash
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(__name__, path="/about_me")

layout = html.Div(
    [
        # -----------------------------------------------------------------------------
        # 1. HERO / TITLE SECTION
        # -----------------------------------------------------------------------------
        html.Div(
            className="about-hero-section d-flex align-items-center justify-content-center text-center",
            children=[
                html.Div(className="hero-overlay"),  # optional overlay if you want a tinted bg
                html.Div(
                    className="hero-content p-5",
                    children=[
                        html.H1("About Me", className="display-4 mb-3"),
                        html.P(
                            "A glimpse into who I am—personally and professionally.",
                            className="lead"
                        ),
                    ],
                ),
            ],
        ),

        # -----------------------------------------------------------------------------
        # 2. MY LIFE STORY SO FAR (IMAGE + TEXT, SIDE BY SIDE)
        # -----------------------------------------------------------------------------
        dbc.Container(
            fluid=True,
            className="py-5",
            children=[
                dbc.Row(
                    [
                        # IMAGE in the left column
                        dbc.Col(
                            html.Div(
                                html.Img(
                                    src="/assets/images/sofaryan.jpg",
                                    className="img-fluid rounded shadow",
                                    style={
                                        "maxHeight": "400px",
                                        "objectFit": "cover",
                                        "marginBottom": "20px",
                                    },
                                ),
                                className="text-center"
                            ),
                            md=5,
                        ),

                        # TEXT in the right column
                        dbc.Col(
                            [
                                html.H2("My Life Story So Far", className="mb-4"),
                                html.P(
                                    """
                                    I was born and raised in a small city in India, the kind of place where
                                    the summers are scorching, the winters barely exist, and your neighbour knows
                                    your business before you do. Growing up in a professor’s home meant two things:
                                    books were everywhere, and dinners were more about debating than eating. 
                                    I spent most of my teenage years buried in textbooks, partly because I loved
                                    learning and partly because my grades were my ticket to a bigger world. That
                                    drive landed me in the top 1% globally in the International Baccalaureate and
                                    eventually brought me to Imperial College London to study Physics.
                                    """,
                                    className="mb-3"
                                ),
                                html.P(
                                    """
                                    But life isn’t all equations and experiments. Three months into university,
                                    I met Sofia, my college sweetheart, during a philosophy class. I handed her
                                    a copy of The Alchemist before she even liked me, but apparently, that move
                                    worked well ;) Fast forward, we're now married, planning our future family,
                                    and living out our own version of The Alchemist. It hasn't all been smooth
                                    sailing; I left university just before my finals to chase a startup dream, 
                                    got stuck in visa limbo, and had to start over. But every challenge has shaped
                                    who I am, and I wouldn’t trade those lessons for anything.
                                    """,
                                    className="mb-3"
                                ),
                            ],
                            md=7,
                            className="d-flex flex-column justify-content-center"
                        ),
                    ],
                    className="align-items-center"
                ),
            ],
        ),

        # -----------------------------------------------------------------------------
# 3. MY PROFESSIONAL JOURNEY (FULL-WIDTH TEXT BLOCK)
# -----------------------------------------------------------------------------
dbc.Container(
    fluid=True,
    className="about-page-content",  # Updated class for the dark background
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("My Professional Journey", className="mb-4"),
                        html.P(
                            """
                            Professionally, I'm all over the place in the best way—I'm a mini 
                            jack-of-all-trades. I've tinkered with AI to optimize renewable energy, 
                            pitched my heart out trying to secure big deals (failed every time but 
                            the learning was priceless), and even led a startup to the finals of the 
                            London Pitch Challenge. My work spans science, tech, and business—whether 
                            it's analyzing energy trends, validating solar software, or coding machine 
                            learning models for profit predictions. I love taking these messy, complex
                            problems and making them simple, elegant, data-driven solutions.
                            """,
                            className="mb-3"
                        ),
                        html.P(
                            """
                            But it's not all about numbers and tech. I've mentored students, shared my
                            research at conferences, and taught a class of 40 kids Math during the 
                            lockdown. My career so far has been a blend of strategy, hands-on work, and 
                            many late nights with my laptop and coffee. I'm currently diving into 
                            renewable energy and business intelligence, but my long-term goal? To make 
                            a dent in big issues like teenage mental health and our over-reliance on 
                            technology.
                            """,
                            className="mb-3"
                        ),
                    ],
                    md=8,
                    className="mx-auto"
                )
            ],
            className="justify-content-center"
        ),
    ],

        ),

        # -----------------------------------------------------------------------------
        # 4. MY QUIRKS (FULL-WIDTH TEXT BLOCK)
        # -----------------------------------------------------------------------------
        dbc.Container(
            fluid=True,
            className="py-5",
            children=[
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H2("My Quirks", className="mb-4 text-center"),
                                html.P(
                                    """
                                    I'm the guy who can dive into a deep conversation about life's meaning at any
                                    time—be it 2 AM, 6 AM, or a lazy Sunday afternoon. I read religious philosophy
                                    for fun, not because I’m particularly holy, but because it’s fascinating how
                                    stories shape us. I've also been known to geek out over physics analogies—
                                    ever heard someone compare love to quantum entanglement? Stick around, you might.
                                    """,
                                    className="mb-3 text-center"
                                ),
                                html.P(
                                    """
                                    When I’m not working or thinking, you’ll find me experimenting with stacks of
                                    books trying to figure out the most beautiful way to arrange them, going on 
                                    long walks with Sofia (we try to solve ALL the world’s problems on those walks), 
                                    or talking to a stranger in a cafe.
                                    """,
                                    className="mb-3 text-center"
                                ),
                                html.P(
                                    """
                                    I might over-analyse almost anything, but I balance that out with a good laugh 
                                    at life's absurdity. For me, life is about finding meaning through 
                                    responsibility, creating something worthwhile, and enjoying the small joys—
                                    like perfectly timed coffee (2 min 36 sec) or a well-timed dad joke (I'm 
                                    getting my practice in early).
                                    """,
                                    className="mb-3 text-center"
                                ),
                            ],
                            md=10,
                            className="mx-auto"
                        )
                    ],
                    className="justify-content-center"
                ),
            ],
        ),
    ]
)
