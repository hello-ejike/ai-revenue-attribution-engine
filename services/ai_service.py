# services/ai_service.py

import os
import random
from datetime import datetime, timedelta

class AIService:
    def __init__(self):
        self.llm = self._initialize_llm()
    
    def _initialize_llm(self):
        """Initialize LLM with fallback logic"""
        try:
            # Try OpenAI first
            from langchain.llms import OpenAI
            if "OPENAI_API_KEY" in os.environ:
                print("🧠 Using GPT-4")
                return OpenAI(model="gpt-4", temperature=0.7)
            
            # Fallback to local Mistral model
            from langchain_community.llms import Ollama
            print("🧠 Using local Mistral model")
            return Ollama(model="mistral", base_url="http://localhost:11435")
            
        except ImportError:
            print("🧠 LangChain not installed — using mock AI")
            return self._mock_llm
        except Exception as e:
            print(f"⚠️ LLM initialization failed: {e}")
            return self._mock_llm
    
    def _mock_llm(self, prompt: str) -> str:
        """Fallback mock LLM with pattern-based responses"""
        if not prompt:
            return "No prompt provided"
        
        prompt_lower = prompt.lower()
        
        # Channel performance mock response
        if "channel" in prompt_lower or "attribution" in prompt_lower:
            return """Mock Channel Analysis:
Google Ads: 60% closed-won deals
LinkedIn: 15% actual conversions
Email: High volume but low intent
Content: Long cycle time but quality wins
Direct: Strong final touch performance

Recommendation: Increase Google Ads investment, improve email nurturing
"""
        # Deal analysis mock response
        elif "deal" in prompt_lower or "probability" in prompt_lower:
            return """Mock Deal Analysis:
Deal D4 has only 19% chance to close because:
- First touch was content — long cycle time
- Last touch was email — low intent
- Rep D closes only 25% of deals

Action Plan:
1. Requalify via LinkedIn call
2. Send personalized demo video
3. Escalate to senior rep
"""
        # Default mock response
        else:
            return f"Mock AI: {prompt[:200]}..."
    
    def generate(self, prompt: str) -> str:
        """Generate AI response with fallback handling"""
        if not prompt:
            return "No prompt provided"
        
        try:
            # Handle LangChain LLMs
            if hasattr(self.llm, 'invoke'):
                return self.llm.invoke(prompt)
            # Handle custom mock LLM
            elif callable(self.llm):
                return self.llm(prompt)
            else:
                return "Error: Invalid LLM implementation"
        except Exception as e:
            print(f"⚠️ AI generation failed: {e}")
            return "Error generating AI output"

# 🔍 Test Block for AI Service
if __name__ == "__main__":
    ai = AIService()
    
    # Test 1: Channel analysis prompt
    print("\n📈 Channel Performance Summary:")
    channel_weights = {
        "google": 0.6,
        "linkedin": 0.5,
        "email": 0.3,
        "content": 0.2,
        "direct": 0.35
    }
    print(ai.generate(f"""
    Here's our channel performance data:
    {channel_weights}

    Explain which channels are working well, where investment should go,
    and what changes marketing/sales should make.
    """))
    
    # Test 2: Deal analysis prompt
    print("\n🧠 Deal Analysis:")
    mock_deal = {
        "deal_id": "D4",
        "amount": 150000,
        "channel": "email",
        "probability": 0.19,
        "rep": "Rep D"
    }
    print(ai.generate(f"""
    Deal ID: {mock_deal['deal_id']}
    Amount: ${float(mock_deal['amount']):,.2f}
    Channel: {mock_deal['channel']}
    Probability: {mock_deal['probability'] * 100:.1f}%
    
    Sales Rep: {mock_deal['rep']}
    
    Explain why this deal has low probability to close.
    Provide actionable steps to improve chances.
    Keep response concise and business-friendly.
    """))
    
    # Test 3: Forecast analysis prompt
    print("\n📊 Forecast Summary:")
    print(ai.generate("""
    Our forecast shows $240K in July, $260K in August, and $220K in September.
    There's a 85% chance we'll hit our Q3 number of $720K.
    
    Summarize this in business terms with implications.
    """))
