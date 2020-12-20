import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
import datetime
import pandas as pd
from pandas_datareader import data as wb
import plotly.graph_objects as go
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.cryptocurrencies import CryptoCurrencies
key = 'X6UBMW7UKN8HP76V'
ts = TimeSeries(key, output_format='pandas')
ti = TechIndicators(key, output_format='pandas')
cc = CryptoCurrencies(key, output_format = 'pandas')
today = datetime.datetime.today()


ticker = "VTI"
source = "av-daily"
start = datetime.datetime(2010, 1, 1)
today = datetime.datetime.today()

ticker_data = wb.DataReader(ticker, source, start, end = today, api_key = key)
ticker_index = ticker_data.index
ticker_dataframe = pd.DataFrame(ticker_data, columns=ticker_data.columns)

ticker_dataframe.index = ticker_index

fig = go.Figure()

fig.add_trace(go.Candlestick(
    x = ticker_dataframe.index,
    open = ticker_dataframe['open'],
    high = ticker_dataframe['high'],
    low = ticker_dataframe['low'],
    close = ticker_dataframe['close'],
    name = ticker
))

layout = html.Div([
    html.H1('Page 1'),
    dcc.Input(
        id="ticker_input".format("text"),
        type="text",
        placeholder="input type {}".format("text"),
    ),
    html.Div(id="ticker_callback_output"),
    dcc.Graph(
        id='ticker-Candlestick-graph',
        figure=fig
    )
])

@app.callback(
    Output("ticker_callback_output", "children"),
    [Input("ticker_input".format("text"), "value")],
)
def cb_render(val):
    if val != None:
        return val

if __name__ == '__main__':
    app.run_server(debug=True)
