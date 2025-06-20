# services/ai_service.py

import os
from typing import Any, Union

class AIService:
    def __init__(self):
        self.llm = self._initialize_llm()
    
    def _initialize_llm(self):
        """Initialize LLM with fallback logic"""
        try:
            # Try OpenAI first
            from langchain_community.llms import OpenAI
            if "OPENAI_API_KEY" in os.environ:
                print("🧠 Using GPT-4")
                return OpenAI(model="gpt-4", temperature=0.7)
            
            # Fallback to local Mistral model
            from langchain_ollama import OllamaLLM
            print("🧠 Using local Mistral model")
            return OllamaLLM(model="mistral", base_url="http://localhost:11435")
            
        except ImportError:
            print("🧠 LangChain not installed — using mock AI")
            return self._mock_llm
        except Exception as e:
            print(f"⚠️ LLM initialization failed: {e}")
            return self._mock_llm
    
    def _mock_llm(self, prompt: str) -> str:
        """Fallback mock LLM response generator"""
        if not prompt:
            return "No prompt provided"
        return f"Mock AI: {prompt[:200]}..."
    
    def generate(self, prompt: str) -> str:
        """Generate AI response with fallback handling"""
        if not prompt:
            return "No prompt provided"
        
        try:
            # Handle LangChain LLMs
            if hasattr(self.llm, 'invoke'):
                return self.llm.invoke(prompt)
            else:
                return self.llm(prompt)  # For mock LLM
        except Exception as e:
            print(f"⚠️ AI generation failed: {e}")
            return "Error generating AI output"
