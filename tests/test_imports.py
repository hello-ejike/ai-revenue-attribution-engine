import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

# Test all imports
try:
    from agents.data_collector import DataCollectorAgent
    from models.attribution_models import AttributionEngine
    from models.forecasting_models import ForecastingEngine
    from services.ai_service import AIService
    from dashboard.app import app
    print("✅ All imports working")
except Exception as e:
    print(f"❌ Import error: {e}")
