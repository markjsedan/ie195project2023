import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import webbrowser
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from app import app


layout = html.Div(
    [
        html.Div(
            [
                html.H5('How to file a report?'),
                html.Span("Select the type of report from the drop-down options below and click the 'Proceed to the Form' button."),
                html.Br(),
                html.Span("This will redirect you a Google Form where you can input the necessary information for the report."),
                html.Br(),
                html.Br(),
                html.Br(),
            ],
            style={
                'margin-left': '0 auto',
                'margin-right': '0 auto',
                # 'display': 'flex',
                'justify-content': 'center',
                'text-align': 'center',
            }
        ), 
        dbc.Card(
            [
                # dbc.CardHeader(html.H3("Select Type of Report", style={'fontWeight': 'bold', 'align':'center'})),
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Label(html.H6("Select Type of Report"), width=3),
                                dbc.Col(
                                        dcc.Dropdown(id='report_type', 
                                        searchable=True, 
                                        options=
                                        [{'label': "After Action Report", 'value': 1},
                                        {'label': "Progress Report",'value': 2},
                                        {'label': "Rapid Damage and Needs Assessment", 'value': 3},
                                        {'label': "Spot Report", 'value': 4},
                                        {'label': "PSSO Reporting and Requesting Form", 'value':5} ],
                                        className='text-secondary'
                                        ), 
                                    width=6
                                ), 
                                dbc.Col(dbc.Button("Proceed to the Form", id='report_link_button', outline=False, color="warning", className="me-1", n_clicks=0)),
                            ]
                        ),
                    ]
                )
            ],
            style={
                'width': '65%',
                'margin': '0 auto',
                'float': 'none',
            },
            className = 'card text-white bg-success mb-2'
        ),
    ],
    style={
        'margin-left': 'auto',
        'margin-right': 'auto'
    } 
)

@app.callback(
    [
        Output('report_link_button', 'href')
    ],
    [
        Input('report_link_button', 'n_clicks')
    ],
    [
        State('report_type', 'value')
    ]
)
def toggle_output(proceedbtn,report_type):
    ctx = dash.callback_context
    if ctx.triggered:
        eventid = ctx.triggered[0]['prop_id'].split('.')[0]
        href = None
    else:
        raise PreventUpdate
    
    if eventid == "report_link_button" and proceedbtn:
        if report_type == 1:
            href = "https://docs.google.com/forms/d/e/1FAIpQLScHo-b7de3RK2pFPTpxV0TaEsym216XUkLZjnL22ggqxk7MDA/viewform"
        elif report_type == 2:
            href = "https://docs.google.com/forms/d/e/1FAIpQLScMT6gECU76QWBVZrC0WG4FYUJ17qfwRj-aBACcZ0b5IILu-g/viewform"
        elif report_type == 3:
            href = "https://docs.google.com/forms/d/e/1FAIpQLScEHEDz9_13pbRvuGBazgBwGXctjB_Pan-5aDZsB1_kY7fqgQ/viewform"
        elif report_type == 4:
            href = "https://docs.google.com/forms/d/e/1FAIpQLSc2AfXLSmf71tl5bU3iSXemtpeTbJWWiwRCpBwImEQup0-75w/viewform"
        elif report_type == 5:
            href = "https://docs.google.com/forms/d/e/1FAIpQLSdJbxf6i81Fjgj32t6buZXGObWns9GL3EJoerCu3Hi89OeQyA/viewform"
    else:
        raise PreventUpdate 
    
    return [href]