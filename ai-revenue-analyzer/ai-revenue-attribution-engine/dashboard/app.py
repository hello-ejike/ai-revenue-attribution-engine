# dashboard/app.py

import dash
from dash import html, dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("AI Revenue Attribution Dashboard"),
    dcc.Tabs(id="tabs", value='attribution', children=[
        dcc.Tab(label='Attribution Overview', value='attribution'),
        dcc.Tab(label='Revenue Forecast', value='forecast'),
        dcc.Tab(label='Pipeline Health', value='pipeline'),
        dcc.Tab(label='Executive Summary', value='summary')
    ]),
    html.Div(id='tab-content')
])

if __name__ == '__main__':
    app.run_server(debug=True)