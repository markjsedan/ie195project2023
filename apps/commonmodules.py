from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash
from dash.exceptions import PreventUpdate


from app import app

navlink_style = {
    'color': '#fff'
}

PSSO_LOGO = "https://www.linkpicture.com/q/psso-logo.png"
HOME_LOGO = "https://pasteboard.co/8U8XVb2n5E2J.png"
REPORT_LOGO = "https://pasteboard.co/AVtmHA1mhwAL.png"

navbar = dbc.Navbar(
    [
        html.A(
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PSSO_LOGO, height="60px")),
                    dbc.Col(html.H3(dbc.NavbarBrand("UPD PSSO Online Reporting System v 1.0", className="ms-1"))),
                ],
                align="center",
                # className="g-0",
            ),
            href="/home",
            style={"textDecoration": "none", 'margin-left': 'auto', 'margin-right': 'auto'}
        ),
        # dbc.NavLink("|", href="/", style={'margin-left': '2em', 'margin-right': '2em', 'color': 'white'}),
        # dbc.NavLink("Home", href="/home", style={'margin-left': '2em', 'margin-right': '2em', 'color': 'white'}),
        # dbc.NavLink("File a Report", href="/report_filing", style={'margin-left': '2em','margin-right': 'auto', 'color': 'white'}),
    ],
    dark=True,
    # color="#014421"
    color="danger",
)