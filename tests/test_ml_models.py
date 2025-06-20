# tests/test_ml_models.py

import numpy as np
from models.forecasting_models import ForecastingEngine
from agents.data_collector import DataCollectorAgent
from models.attribution_models import AttributionEngine

def test_deal_probability_scoring():
    """Test deal probability scoring with valid input"""
    engine = ForecastingEngine()
    mock_deal = {
        "deal_id": "D4",
        "channel": "google",
        "rep": "Rep A",
        "touchpoints": 3,
        "deal_age": 60,
        "amount": 250000
    }
    
    result = engine.deal_probability_scoring([mock_deal])
    assert len(result) == 1
    assert 0.05 <= result[0]["probability"] <= 0.95
    print("✅ ML model outputs valid probability")

def test_model_accuracy():
    """Test model accuracy with synthetic data"""
    engine = ForecastingEngine()
    metrics = engine.evaluate_model()
    print(f"🧠 Model Accuracy: {metrics['accuracy']:.2f}, ROC-AUC: {metrics['roc_auc']:.2f}")

def test_attribution_scoring():
    """Test attribution model with journey data"""
    collector = DataCollectorAgent()
    journeys = collector.enrich_contact_journeys()

    attribution_engine = AttributionEngine()
    result = attribution_engine.ml_attribution(journeys[:1])
    print("📈 ML Attribution:", {k: f"{v:.2%}" for k, v in result.items()})
    assert sum(result.values()) > 0.95 and sum(result.values()) < 1.05

if __name__ == "__main__":
    print("🧪 Running ML Model Tests")
    test_deal_probability_scoring()
    test_model_accuracy()
    test_attribution_scoring()
    print("�� All tests complete.")
