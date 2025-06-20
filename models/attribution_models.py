# models/attribution_models.py

from collections import defaultdict
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from typing import List, Dict, Any

class AttributionEngine:
    def __init__(self):
        self.model = self._train_ml_attribution_model()
        self.feature_weights = {
            "touchpoint_order": 0.2,
            "time_between_touches": 0.1,
            "campaign_type": 0.1,
            "rep_involvement": 0.2,
            "deal_value": 0.4
        }

    def first_touch_attribution(self, journey):
        """100% credit to the first interaction"""
        if not journey:
            return {}
        return {journey[0]["channel"]: 1.0}

    def last_touch_attribution(self, journey):
        """100% credit to the final interaction"""
        if not journey:
            return {}
        return {journey[-1]["channel"]: 1.0}

    def linear_attribution(self, journey):
        """Equal credit across all touchpoints"""
        counts = defaultdict(int)
        for event in journey:
            counts[event["channel"]] += 1
        total = len(journey)
        return {k: v / total for k, v in counts.items()}

    def time_decay_attribution(self, journey, decay_rate=0.7):
        """More recent touches get more credit"""
        weights = [decay_rate ** (len(journey) - i - 1) for i in range(len(journey))]
        total_weight = sum(weights)
        attribution = defaultdict(float)
        for idx, event in enumerate(journey):
            attribution[event["channel"]] += weights[idx] / total_weight
        return dict(attribution)

    def position_based_attribution(self, journey):
        """40% to first, 40% to last, 20% distributed among middle touches"""
        attribution = defaultdict(float)
        if not journey:
            return attribution

        attribution[journey[0]["channel"]] += 0.4
        attribution[journey[-1]["channel"]] += 0.4

        if len(journey) > 2:
            weight = 0.2 / (len(journey) - 2)
            for event in journey[1:-1]:
                attribution[event["channel"]] += weight

        return dict(attribution)

    def _train_ml_attribution_model(self):
        """Train a model to determine optimal attribution weights"""
        X = []
        y = []

        for _ in range(1000):
            touchpoint_count = random.randint(1, 5)
            channel = random.choice(["google", "linkedin", "email", "content", "direct"])
            rep = random.choice(["Rep A", "Rep B", "Rep C", "Rep D"])
            campaign_type = random.choice(["awareness", "nurture", "conversion"])
            deal_value = random.uniform(10_000, 500_000)
            conversion_rate = {"google": 0.6, "linkedin": 0.5, "email": 0.3, "content": 0.2, "direct": 
0.65}[channel]

            # ✅ Fixed line using line continuation
            time_to_convert = (
                random.gauss(90, 30) if random.random() < conversion_rate 
                else random.gauss(180, 40)
            )

            feature_vector = [
                touchpoint_count,
                {"google": 0.8, "linkedin": 0.5, "email": 0.3, "content": 0.2, "direct": 0.65}[channel],
                {"Rep A": 0.9, "Rep B": 0.7, "Rep C": 0.4, "Rep D": 0.25}[rep],
                {"awareness": 0.3, "nurture": 0.6, "conversion": 0.8}[campaign_type],
                deal_value / 1e5  # Normalize deal value
            ]

            X.append(feature_vector)
            y.append(conversion_rate)

        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X, y)
        return model

    def ml_attribution(self, journey):
        """Use ML to determine optimal attribution based on full journey"""
        if not journey:
            return {}

        touchpoint_weights = defaultdict(float)
        base_features = [
            len(journey),
            0.7,  # Default channel quality
            0.5,  # Default rep performance
            0.5,  # Default campaign type
            200000 / 1e5  # Default normalized deal value
        ]

        for event in journey:
            channel = event["channel"]
            rep = event.get("rep", "Rep A")
            campaign_type = event.get("campaign_type", "nurture")
            deal_value = event.get("amount", 200000)

            feature_vector = [
                len(journey),
                {"google": 0.8, "linkedin": 0.5, "email": 0.3, "content": 0.2, "direct": 
0.65}.get(channel, 0.5),
                {"Rep A": 0.9, "Rep B": 0.7, "Rep C": 0.4, "Rep D": 0.25}.get(rep, 0.7),
                {"awareness": 0.3, "nurture": 0.6, "conversion": 0.8}.get(campaign_type, 0.5),
                deal_value / 1e5
            ]

            weight = self.model.predict([feature_vector])[0]
            touchpoint_weights[channel] += max(0.01, weight)

        total_weight = sum(touchpoint_weights.values())
        return {k: v / total_weight for k, v in touchpoint_weights.items()}
