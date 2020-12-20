import datetime
import json
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from pages import index
from pages import page_1
from pages import page_2

external_stylesheets = [
    dbc.themes.LUX,

    # for social media icons
    'https://use.fontawesome.com/releases/v5.9.0/css/all.css',
]

meta_tags=[
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
]

app = dash.Dash(__name__,
    external_stylesheets = external_stylesheets,
    meta_tags=meta_tags
    )

app.config.suppress_callback_exceptions = True
app.title = 'Matt Kirby'
server = app.server

navbar = dbc.NavbarSimple(
    brand = 'MATT KIRBY',
    brand_href = '/',
    children = [
        dbc.Col(
            html.P(
                [
                    html.A(html.I(className='page 1'), href='/pages.page_1', style = dict(color = "white")),
                ],
                className='lead'
            )
        )],
    color = "primary",
    sticky = 'top',
    dark = True,
)


footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('Contact', className='mr-2'),
                    html.A(html.I(className='fas fa-envelope-square mr-1'), href='mailto:mkirby3@angelo.edu'),
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/mkirby42'),
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/matt-kirby-ml/'),
                    html.A(html.I(className='fab fa-twitter-square mr-1'), href='https://twitter.com/matt42kirby'),
                ],
                className='lead'
            )
        )
    )
)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    dbc.Container(id='page-content', className='mt-4'),
    html.Hr(),
    footer
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/page_1':
        return page_1.layout
    elif pathname == '/page_2':
        return page_2.layout
    else:
        return dcc.Markdown('## Page not found')


if __name__ == '__main__':
    app.run_server(debug=True)
