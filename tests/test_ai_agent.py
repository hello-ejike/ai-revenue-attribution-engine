# tests/test_ai_agent.py

from agents.revenue_analyst import RevenueAnalystAgent
from models.forecasting_models import ForecastingEngine
from models.attribution_models import AttributionEngine

def main():
    analyst = RevenueAnalystAgent()
    
    # Mock deal
    mock_deal = {
        "deal_id": "D4",
        "amount": 150000,
        "channel": "email",
        "probability": 0.19,
        "rep": "Rep D"
    }
    
    # Mock historical data
    mock_historical = [
        {"amount": 150000, "timestamp": "2024-04-15T12:34:56Z"},
        {"amount": 180000, "timestamp": "2024-05-01T12:34:56Z"}
    ]
    
    print("\n🧠 AI Deal Analysis:")
    print(analyst.analyze_deal(mock_deal))
    
    print("\n📈 Channel Performance Summary:")
    print(analyst.explain_channel_performance({
        "google": 0.6,
        "linkedin": 0.5,
        "email": 0.3,
        "content": 0.2,
        "direct": 0.35
    }))
    
    print("\n📊 Forecast Summary:")
    print(analyst.summarize_forecast(mock_historical))

if __name__ == "__main__":
    main()
