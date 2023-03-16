from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

import webbrowser

from apps import homes
from apps import report_filing as rf


CONTENT_STYLE = {
    "margin-top": "1em",
    "margin-left": "1em",
    "margin-right": "1em",
    "padding": "1em 1em",
}

app.layout = html.Div(
    [
        # Location Variable -- contains details about the url
        dcc.Location(id='url', refresh=True),
        cm.navbar,
        # Page Content -- Div that contains page layout
        html.Div(id='page-content', style=CONTENT_STYLE),
    ]
)

@app.callback(
    [
        Output('page-content', 'children')
    ],
    [
        Input('url', 'pathname')
    ]
)

def displaypage (pathname):
    # determines what element triggerred the fxn
    ctx = dash.callback_context
    if ctx.triggered:
        # name of the element that caused the trigger
        eventid = ctx.triggered[0]['prop_id'].split('.')[0]
        if eventid == 'url':
            if pathname == '/' or pathname == '/home':
                # If we are at the homepage, let us output 'home'
                returnlayout = home.layout
            elif pathname == '/report_filing':
                returnlayout = report_filing.layout
            else:
                returnlayout = "error404"
        else:
            raise PreventUpdate
    else:
        raise PreventUpdate

    return[returnlayout]

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050/', new=0, autoraise=True)
    app.run_server(debug=False)