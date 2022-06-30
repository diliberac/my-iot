#!/usr/bin/python3
import requests
import datetime
import time
import settings as sets
import plotly.express as px
import dash
import redis

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(
    html.Div([
        html.H2('IoT Temperature Dashboard'),
        html.Br(),
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=10*1000, # in milliseconds
            n_intervals=0
        )
    ])
)

@app.callback(Output('live-update-text', 'children'), Input('interval-component', 'n_intervals'))
def update_realtime(n):
    result = requests.get(sets.REALTIME_URL)
    print('Requesting realtime...')
    if result.status_code == 200:
        temperature = result.json()["temperature"]
        return html.Span("Temperature: " + temperature)

@app.callback(Output('live-update-graph', 'figure'), Input('interval-component', 'n_intervals'))
def update_graph_live(n):
    result = requests.get(sets.HISTORY_URL)
    print('Requesting history...')
    if result.status_code == 200:
        data = result.json()
        timestamp = [datetime.datetime.strptime(row['timestamp'], "%Y-%m-%d %H:%M:%S") for row in data]
        temperature = [row['value'] for row in data]
        fig = px.line(x=timestamp, y=temperature, labels={'x':'time', 'y':'celsius'})
        return fig  

@app.callback(Output('update_realtime', 'figure'), Input('interval-component', 'n_intervals'))
def update_realtime(n):
    r = redis.StrictRedis.from_url(sets.REALTIME_URL)
    return r.info()

if __name__ == '__main__':
    print('Staring dashboard...')
    app.run_server(host="0.0.0.0", port=8050, debug=False)