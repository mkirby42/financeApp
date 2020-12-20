import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app
from pages import page_1, page_2

navbar = dbc.NavbarSimple(
    brand = 'Stonks',
    brand_href = '/',
    children = [],
    color = "primary",
    sticky = 'top',
    dark = True,
)

footer = dbc.Container(
    dbc.Row(
        dbc.Col()
    )
)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    dbc.Container(id='page-content', className='mt-4'),
    html.Hr(),
    footer
])

homepage_layout = html.Div([
    dcc.Link('Go to Page 1', href='pages/page_1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='pages/page_2'),
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/pages/page_1':
        return page_1.layout
    elif pathname == '/pages/page_2':
        return page_2.layout
    elif pathname == '/':
        return homepage_layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
