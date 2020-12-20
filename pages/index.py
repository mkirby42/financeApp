import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

layout = html.Div([
    dcc.Link('Go to Page 1', href='/page_1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page_2'),
])
