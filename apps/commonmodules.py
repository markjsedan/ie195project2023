from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash
from dash.exceptions import PreventUpdate


from app import app

# THEBOOKSTORE_LOGO = "https://i.ibb.co/YRzTCN6/THE-BOOKSTORE-LOGO.png"


# CSS Styling for the NavLink components
navlink_style = {
    'color': '#fff'
}

navbar = dbc.Navbar(
    [
        html.A(
            dbc.Row(
                [
                    # dbc.Col(html.Img(src=THEBOOKSTORE_LOGO, height="70px")),
                    dbc.Col(dbc.NavbarBrand("UPD PSSO Reporting System", className="ms-2")),
                ],
                align="center",
                # className="g-0",
            ),
            href="/home",
            style={"textDecoration": "none", 'margin-left': '1.5em'}
        ),
        dbc.NavLink("|", href="/", style={'margin-left': '5em', 'margin-right': '3em', 'color': 'white'}),
        dbc.NavLink("Home", href="/home", style={'margin-left': '5em', 'margin-right': '3em', 'color': 'white'}),
        dbc.NavLink("File a Report", href="/report_filing", style={'margin-right': '3em', 'color': 'white'}),
    ],
    dark=True,
    # color="#014421"
    color="#7B1113",
)