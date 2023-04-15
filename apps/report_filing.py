
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc

# store the layout objects into a variable named layout
layout = html.Div(
    [
        # html.H2('Select the type of report you want to file'),
        # html.Hr(),
        # html.Div(
        #     [
        #         html.Br(),
        #         html.H5(dbc.NavLink("- Spot Report", href="https://docs.google.com/forms/d/e/1FAIpQLSc2AfXLSmf71tl5bU3iSXemtpeTbJWWiwRCpBwImEQup0-75w/viewform")),
        #         html.Br(),
        #     ]
        # ),
        # html.Div(
        #     [
        #         html.H5('How to file a report?'),
        #         html.Ol("1. Select the type of report you want to submit from the drop-down options below."),
        #         html.Ol("2. Click 'Proceed to the Form' button. This will redirect you to a Google Form."),
        #         html.Ol("3. Fill in the Google Form with the necessary information."),
        #         html.Ol("4. Your report will be imported to a spreadsheet that can generate a printable copy."),
        #         html.Br(),
        #         html.Br(),
        #     ],
        #     style={
        #         # 'position': 'absolute',
        #         # 'width': '100%',
        #         'margin-left': '0 auto',
        #         'margin-right': '0 auto',
        #         # 'display': 'flex',
        #         'justify-content': 'center',
        #         # 'text-align': 'center',
        #     }
        # ), 
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
                # 'position': 'absolute',
                # 'width': '100%',
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
                                        dcc.Dropdown(id='process_type', 
                                        searchable=True, 
                                        options=
                                        [{'label': "After Action Report", 'value': 1},
                                        {'label': "Progress Report",'value': 2},
                                        {'label': "Rapid Damage and Needs Assessment", 'value': 3},
                                        {'label': "Spot Report", 'value': 4} ],
                                        className='text-secondary'
                                        ), 
                                    width=5
                                ), 
                                dbc.Col(dbc.Button("Proceed to the Form", id='report_link', outline=False, color="warning", className="me-1", n_clicks=0)),
                            ]
                        ),
                    ]
                )
            ],
            style={
                'width': '60%',
                'margin': '0 auto',
                'float': 'none',
            },
            className = 'card text-white bg-success mb-2'
        ),
    ],
    style={
        # 'position': 'absolute',
        # 'width': '100%',
        'margin-left': 'auto',
        'margin-right': 'auto'
    } 
)
