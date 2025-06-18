# ai_revenue_attribution_engine/models/attribution_models.py

from collections import defaultdict

class AttributionEngine:
    def first_touch_attribution(self, journey):
        if not journey:
            return {}
        return {journey[0]["channel"]: 1.0}

    def last_touch_attribution(self, journey):
        if not journey:
            return {}
        return {journey[-1]["channel"]: 1.0}

    def linear_attribution(self, journey):
        counts = defaultdict(int)
        for event in journey:
            counts[event["channel"]] += 1
        total = len(journey)
        return {k: v / total for k, v in counts.items()}
