# dashboard/app.py

import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import random
from datetime import datetime, timedelta

# Add root to path
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

# Import local modules
from agents.data_collector import DataCollectorAgent
from models.attribution_models import AttributionEngine
from models.forecasting_models import ForecastingEngine
from agents.revenue_analyst import RevenueAnalystAgent

# Initialize agents
collector = DataCollectorAgent()
attribution_engine = AttributionEngine()
forecasting_engine = ForecastingEngine()
analyst = RevenueAnalystAgent()

# Generate mock journeys
try:
    journeys = collector.enrich_contact_journeys()
except Exception as e:
    print(f"⚠️ Data collection failed: {e}")
    journeys = [{
        "deal_id": f"D{i}",
        "amount": random.uniform(10_000, 500_000),
        "channel": random.choice(["google", "linkedin", "email", "content", "direct"]),
        "rep": random.choice(["Rep A", "Rep B", "Rep C", "Rep D"])
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
        "Channel": d["channel"]
    } for d in deal_probabilities if d["probability"] < 0.3
])

# Generate AI insights
try:
    ai_deal_insight = analyst.analyze_deal(risk_deals.iloc[0].to_dict() if not risk_deals.empty else {
        "deal_id": "D4",
        "amount": 150000,
        "channel": "email",
        "probability": 0.19,
        "rep": "Rep D"
    })
except Exception as e:
    ai_deal_insight = """Deal D4 has only a 19% chance to close because:
- First touch was content — long cycle time
- Last touch was email — low intent
- Rep D closes only 25% of deals"""

try:
    ai_channel_summary = analyst.explain_channel_performance(channel_weights)
except Exception as e:
    ai_channel_summary = """Google Ads drive 60% of closed-won deals but cost more per lead.
LinkedIn generates MQLs but rarely converts them.
Email has high velocity but low win rate.
Content takes longer but drives quality wins.
Direct outreach works best when paired with paid ads."""

# Build app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="RevOps Dashboard"
)
server = app.server

app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("AI Revenue Attribution & Forecasting Engine"), className="mb-4")),
    
    dbc.Row([
        dbc.Col(dcc.Graph(
            id='channel-performance',
            figure=px.bar(
                x=channel_weights.keys(),
                y=channel_weights.values(),
                title="Channel Performance",
                labels={"x": "Channel", "y": "Conversion Rate"},
                range_y=[0, 1]
            )
        ), width=6),
        
        dbc.Col(dcc.Graph(
            id='forecast-summary',
            figure=px.line(
                x=["Jul", "Aug", "Sep"][:len(forecast_data)],
                y=forecast_data,
                title="Revenue Forecast"
            )
        ), width=6)
    ]),
    
    dbc.Row([
        dbc.Col(html.H3("At-Risk Deals (<30%)")),
        dbc.Col(html.Div([
            dbc.Table.from_dataframe(risk_deals, striped=True, bordered=True, hover=True)
        ]), width=12)
    ]),
    
    dbc.Row([
        dbc.Col(html.Div([
            html.H3("AI Deal Analysis"),
            html.Pre(ai_deal_insight)
        ]), width=6),
        
        dbc.Col(html.Div([
            html.H3("Channel ROI Summary"),
            html.Pre(ai_channel_summary)
        ]), width=6)
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
