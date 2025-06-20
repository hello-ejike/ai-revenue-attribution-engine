# dashboard/app.py

import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from pathlib import Path
import sys

# Add root to path
sys.path.append(str(Path(__file__).parent.parent))

# Import local modules
from agents.data_collector import DataCollectorAgent
from models.attribution_models import AttributionEngine
from models.forecasting_models import ForecastingEngine

# Initialize agents
collector = DataCollectorAgent()
attribution_engine = AttributionEngine()
forecasting_engine = ForecastingEngine()

# Generate mock journeys
try:
    journeys = collector.enrich_contact_journeys()
except Exception as e:
    print(f"⚠️ Running in mock mode — no real data: {e}")
    journeys = [{
        "deal_id": f"D{i}",
        "amount": random.uniform(10_000, 500_000),
        "channel": random.choice(["google", "linkedin", "email", "content", "direct"]),
        "rep": random.choice(["Rep A", "Rep B", "Rep C", "Rep D"]),
        "touchpoints": random.randint(1, 6),
        "deal_age": random.randint(30, 180),
        "converted": random.random() > 0.5
    } for i in range(1, 10)]

# Build channel performance
channel_weights = {
    "google": random.uniform(0.4, 0.8),
    "linkedin": random.uniform(0.3, 0.7),
    "email": random.uniform(0.1, 0.3),
    "content": random.uniform(0.2, 0.4),
    "direct": random.uniform(0.2, 0.5)
}

# Build forecast data
try:
    forecast_data = forecasting_engine.time_series_forecast([
        {"amount": j["amount"], "timestamp": j["timestamp"]} for j in journeys
    ])
except Exception as e:
    forecast_data = [240000, 260000, 220000]

# Build deal probabilities
try:
    deal_probabilities = forecasting_engine.deal_probability_scoring(journeys)
except Exception as e:
    deal_probabilities = [{
        "deal_id": "D4",
        "probability": 0.19,
        "rep": "Rep D",
        "channel": "email"
    }]

# Build risk table
risk_deals = pd.DataFrame([
    {
        "Deal ID": d["deal_id"],
        "Probability": f"{d['probability']:.2%}",
        "Channel": d["channel"],
        "Rep": d["rep"]
    } for d in deal_probabilities if d["probability"] < 0.3
])

# Build app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SLATE],
    title="RevOps Dashboard"
)

server = app.server

app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("AI Revenue Attribution & Forecasting Engine"), className="mb-4 
text-center")),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id='channel-performance', figure=px.bar(...)), width=6),
        dbc.Col(dcc.Graph(id='forecast-summary', figure=px.line(...)), width=6)
    ]),
    
    dbc.Row([
        dbc.Col(html.H3("At-Risk Deals (<30%)")),
        dbc.Col(html.Div([dbc.Table.from_dataframe(risk_deals)]))
    ]),
    
    dbc.Row([
        dbc.Col(dbc.Button("Refresh Dashboard", id="refresh-btn", color="primary"))
    ])

], fluid=True, style={"padding": "20px", "background-color": "#121212"})
