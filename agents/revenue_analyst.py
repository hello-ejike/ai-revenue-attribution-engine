# agents/revenue_analyst.py

from services.ai_service import AIService
from models.attribution_models import AttributionEngine

class RevenueAnalystAgent:
    def __init__(self):
        self.ai_service = AIService()
        self.attribution_engine = AttributionEngine()
    
    def analyze_deal(self, deal: dict) -> str:
        """Get AI explanation for low-probability deals"""
        attribution = self.attribution_engine.first_touch_attribution([deal])
        first_touch = list(attribution.keys())[0] if attribution else "Unknown"
        
        prompt = f"""
        Deal ID: {deal.get('deal_id', 'N/A')}
        Amount: ${float(deal.get('amount', 0)):,.2f}
        Channel: {deal.get('channel', 'N/A')}
        Probability: {deal.get('probability', 0) * 100:.1f}%
        
        First Touch: {first_touch}
        Sales Rep: {deal.get('rep', 'N/A')}
        
        Explain why this deal has low probability to close.
        Provide actionable steps to improve chances.
        Keep response concise and business-friendly.
        """
        
        return self.ai_service.generate(prompt)
    
    def explain_channel_performance(self, channel_weights: dict) -> str:
        """AI explanation of channel ROI"""
        prompt = f"""
        Here's our channel performance:
        {channel_weights}

        Explain which channels are working well, where investment should go,
        and what changes marketing/sales should make.
        """
        
        return self.ai_service.generate(prompt)
    
    def summarize_forecast(self, forecast_data: list) -> str:
        """Generate plain English summary of revenue forecast"""
        prompt = f"""
        Our forecast over the next 90 days is:
        {forecast_data}

        Summarize this in business terms with possible implications.
        """
        
        return self.ai_service.generate(prompt)
