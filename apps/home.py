
from dash import html


# store the layout objects into a variable named layout
layout = html.Div(
    [
        html.H2('Welcome to UP Diliman Public Safety and Security Office (PSSO) Reporting System'),
        html.Hr(),
        html.Div(
            [
                html.Span(
                "Thru this app, you can manage a database of movies that are classified according to genres.",
                ),
                html.Br(),
                html.Br(),
                html.Span(
                    "Contact the owner if you need assistance!",
                    style={'font-style':'italic'}
                ),
            ]
        )
    ]
)