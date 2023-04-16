import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import logging 
from flask import Flask, send_from_directory


server = Flask(__name__, static_folder='static')
app = dash.Dash(__name__, external_stylesheets=["assets/bootstrap.css"])

app.config.suppress_callback_exceptions = True

app.css.config.serve_locally = True

app.scripts.config.serve_locally = True

app.title = 'UP Diliman PSSO Online Reporting System'

app.iconbitmap = "https://www.linkpicture.com/q/psso-logo.png"
@server.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(server.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)