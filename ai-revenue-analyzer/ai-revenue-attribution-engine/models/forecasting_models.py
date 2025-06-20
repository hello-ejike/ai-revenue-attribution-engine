# models/forecasting_models.py

from typing import List, Dict
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

class ForecastingEngine:
    def pipeline_velocity_forecast(self, historical_pipeline):
        """Forecast revenue based on conversion rates"""
        # Simplified version
        avg_deal_size = sum(d['amount'] for d in historical_pipeline) / len(historical_pipeline)
        win_rate = 0.3
        expected_deals = len(historical_pipeline) * win_rate
        return expected_deals * avg_deal_size

    def time_series_forecast(self, deal_amounts: List[float], steps=3):
        """Use ARIMA to forecast future revenue"""
        model = ARIMA(deal_amounts, order=(1,1,1))
        results = model.fit()
        forecast = results.forecast(steps=steps)
        return list(forecast)