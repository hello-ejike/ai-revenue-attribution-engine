# models/forecasting_models.py

from typing import List, Dict, Union
from collections import defaultdict
from datetime import datetime
from statistics import mean

class ForecastingEngine:
    def __init__(self):
        self.time_horizon_days = 90

    def time_series_forecast(self, historical_data: List[Dict], periods=3) -> List[float]:
        monthly_revenue = defaultdict(float)

        for deal in historical_data:
            ts_str = deal.get("timestamp") or deal.get("created_at")
            if not ts_str:
                continue

            ts = datetime.fromisoformat(ts_str.split("T")[0])
            key = f"{ts.year}-{ts.month}"
            monthly_revenue[key] += float(deal["amount"])

        sorted_values = sorted(monthly_revenue.values())
        window_size = min(3, len(sorted_values))

        if not sorted_values:
            return [mean([10_000, 50_000])] * periods

        predictions = []
        for _ in range(periods):
            prediction = mean(sorted_values[-window_size:])
            predictions.append(prediction)
            sorted_values.append(prediction)

        return predictions
