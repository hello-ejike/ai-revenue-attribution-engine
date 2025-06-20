# core/attribution.py
from typing import Protocol
from core.types import CampaignData, AttributionResult

class AttributionStrategy(Protocol):
    def calculate(self, data: List[CampaignData]) -> AttributionResult:
        ...

class RuleBasedAttribution:
    def calculate(self, data: List[CampaignData]) -> AttributionResult:
        # Simulated logic (replace with real model later)
        return {
            "channel_weights": {
                "google": 0.5,
                "meta": 0.3,
                "email": 0.2
            }
        }