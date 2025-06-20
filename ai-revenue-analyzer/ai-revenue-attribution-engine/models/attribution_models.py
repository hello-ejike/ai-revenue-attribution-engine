# models/attribution_models.py

from typing import List, Dict

class AttributionEngine:
    def first_touch_attribution(self, journey: List[Dict]) -> Dict[str, float]:
        """100% credit to first interaction"""
        if not journey:
            return {}
        
        first = journey[0]["channel"]
        return {first: 1.0}

    def last_touch_attribution(self, journey: List[Dict]) -> Dict[str, float]:
        """100% credit to last interaction"""
        if not journey:
            return {}

        last = journey[-1]["channel"]
        return {last: 1.0}

    def linear_attribution(self, journey: List[Dict]) -> Dict[str, float]:
        """Equal credit across all touchpoints"""
        counts = {}
        for event in journey:
            channel = event["channel"]
            counts[channel] = counts.get(channel, 0) + 1
        
        total = len(journey)
        return {k: v / total for k, v in counts.items()}