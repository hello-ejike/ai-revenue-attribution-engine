# 🚀 AI Revenue Attribution & Forecasting Engine

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) ![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg) ![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg) ![Code Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen.svg)

A comprehensive RevOps system that solves the marketing vs sales attribution debate using multi-touch attribution modeling, revenue forecasting, and AI-powered deal analysis. Built with Python, Dash, and local LLM integration.

This system is designed for demonstration with a realistic mock data pipeline but is architected to integrate with real CRM data sources like HubSpot or Salesforce.

## 🔍 Why This Matters

This system addresses critical revenue operations challenges:

- **Attribution Clarity:** Quantify which channels actually drive revenue with 5 different attribution models
- **Accurate Forecasting:** Combine pipeline velocity and time-series analysis for reliable predictions
- **AI-Powered Insights:** Get natural language explanations for deal risks and channel performance
- **Executive Reporting:** Generate professional PDF reports with actionable insights

## 🧠 Core Features

| Feature                 | Description                                        | Business Impact                  |
|-------------------------|----------------------------------------------------|---------------------------------|
| Multi-Touch Attribution | First-touch, last-touch, linear, time-decay, etc. | End marketing vs sales debates   |
| Revenue Forecasting     | Pipeline velocity + time-series modeling          | Accurate quarterly planning      |
| AI Deal Analysis        | Mistral-powered risk assessment                   | Prevent deal slippage            |
| Interactive Dashboard   | Real-time visualization with Dash/Plotly          | Executive-ready insights         |
| PDF Reporting           | Automated report generation                       | Stakeholder communication        |
| Mock Data Pipeline      | Realistic CRM data simulation                     | Testing and demonstration        |

<details>
<summary>📦 View Project Structure</summary>

```
ai-revenue-attribution-engine/
├── agents/              # Business logic
├── models/              # Mathematical models
├── services/            # LLM integration
├── dashboard/           # Visualization layer
├── templates/           # PDF report templates
├── reports/             # Generated insights
├── data/                # Mock data pipeline
├── config/              # Settings
├── tests/               # Validation
├── docs/                # Documentation & Visuals
├── requirements.txt     # Dependencies
└── .gitignore           # File exclusion rules
```

</details>

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/) (for local LLM support)

### Setup

```bash
# Clone repository
git clone https://github.com/your-username/ai-revenue-attribution-engine.git
cd ai-revenue-attribution-engine

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Pull the required local LLM from Ollama
ollama pull mistral

# Configure settings
cp config/settings.py.example config/settings.py
```

## 🚀 Quick Start

```bash
# Start the Ollama server in the background
ollama serve &

# Run the dashboard application
PYTHONPATH=. python dashboard/app.py

# Access the dashboard in your browser at http://localhost:8050
```

You will see:
- Channel performance chart
- Revenue forecast line graph with confidence intervals
- A sortable table of at-risk deals
- AI-powered explanations for deal performance

## 📊 Sample Outputs

### Channel Performance Analysis

| Channel    | Win Rate | ML Attribution Score | Confidence |
|------------|----------|---------------------|------------|
| Google Ads | 60%      | 0.73               | High       |
| LinkedIn   | 50%      | 0.52               | Medium-High|
| Email      | 30%      | 0.41               | Low        |
| Content    | 20%      | 0.27               | Very Low   |
| Direct     | 35%      | 0.36               | Medium     |

### AI Deal Analysis Example

**Deal D4 Analysis:**

- **Probability:** 19% (High Risk)
- **Channel Path:** Content → Email (historically low-intent signals)
- **Rep Performance:** Assigned to Rep D (historical 25% close rate)
- **AI Recommendation:** High-touch intervention required. Requalify via LinkedIn call or escalate to a senior rep for review.

## 🧪 Technical Implementation

<details>
<summary>🔬 View Advanced Attribution Engine Code</summary>

The system uses a RandomForestRegressor to learn the importance of different touchpoints based on features like channel type, rep performance, and campaign, providing a more nuanced attribution score than standard models.

```python
# models/attribution_models.py
from sklearn.ensemble import RandomForestRegressor

class AttributionEngine:
    def __init__(self):
        self.model = self._train_ml_attribution_model()

    def _train_ml_attribution_model(self):
        """Train model on synthetic data with business features"""
        # ... (synthetic data generation logic) ...
        model = RandomForestRegressor(n_estimators=100)
        model.fit(X, y)
        return model

    def ml_attribution(self, journey):
        """Use ML to determine optimal attribution weights for a customer journey"""
        touchpoint_weights = defaultdict(float)
        for event in journey:
            # ... (feature vector creation for each touchpoint) ...
            weight = self.model.predict([feature_vector])[0]
            touchpoint_weights[event["channel"]] += max(0.01, weight)

        total_weight = sum(touchpoint_weights.values())
        return {k: v / total_weight for k, v in touchpoint_weights.items()}
```

</details>

<details>
<summary>📈 View Enhanced Forecasting Engine Code</summary>

The engine combines a SARIMAX time-series model for baseline predictions with a Monte Carlo simulation to generate robust confidence intervals, offering a probable range for future revenue, not just a single number.

```python
# models/forecasting_models.py
from xgboost import XGBClassifier
from statsmodels.tsa.statespace.sarimax import SARIMAX

class ForecastingEngine:
    def deal_probability_scoring(self, journeys):
        """Score individual deals using a trained XGBoost model"""
        # ... (feature engineering and prediction logic) ...
        return results

    def monte_carlo_simulation(self, historical_data, periods=3, simulations=100):
        """Generate confidence intervals for the forecast using Monte Carlo"""
        results = []
        for _ in range(simulations):
            sample_data = random.choices(historical_data, k=len(historical_data))
            simulation = self.time_series_forecast(sample_data, periods)
            results.append(simulation)

        lower = [np.percentile([r[i] for r in results], 10) for i in range(periods)]
        mean = [np.mean([r[i] for r in results]) for i in range(periods)]
        upper = [np.percentile([r[i] for r in results], 90) for i in range(periods)]

        return {"low": lower, "mean": mean, "high": upper}
```

</details>

## 🧱 Core Technical Decisions

| Feature              | Implementation        | Why?                                                                          |
|----------------------|-----------------------|-------------------------------------------------------------------------------|
| ML Deal Scoring      | XGBoost Classifier    | High performance and interpretability for deal risk factors                  |
| Attribution Models   | Five standard models + one ML model | Provides both explainable rules and data-driven insights         |
| Time-Series Forecast | SARIMAX + Monte Carlo | Offers robust predictions with statistically sound confidence levels        |
| Local AI Insights    | Ollama + Mistral     | Ensures data privacy and cost-free, powerful text generation                |
| PDF Reports          | WeasyPrint + Jinja2  | Creates professional, template-driven reports without a browser              |
| Mock Data Generation | Faker library with custom providers | Simulates realistic CRM patterns for effective development/testing |

## 🛣️ Roadmap

| Status | Phase               | Description                                      |
|--------|---------------------|--------------------------------------------------|
| ✅     | Core Attribution Models | First-touch, last-touch, linear, time-decay, position-based |
| ✅     | Revenue Forecasting | Time-series + Monte Carlo simulation           |
| ✅     | AI-Powered Insights | Local LLM integration                           |
| ✅     | Interactive Dashboard | Dash/Plotly visualization                      |
| ✅     | PDF Reporting       | Automated report generation                     |
| 🚧     | XGBoost Integration | Finalize ML attribution accuracy improvements   |
| 📋     | HubSpot API         | Implement real CRM data integration connector   |
| 📋     | Deployment          | Deploy live demo on Render.com                 |
| 📋     | Documentation       | Create full technical write-up in /docs        |

## 💼 Skills Demonstrated

| Skill                    | Evidence                                                |
|--------------------------|---------------------------------------------------------|
| Python Architecture      | Modular design with clear separation of concerns       |
| Machine Learning         | XGBoost, RandomForest, feature engineering, SARIMAX    |
| Data Engineering         | ETL pipeline, mock data generation                      |
| LLM Integration          | Local Mistral model via Ollama for private insights    |
| Web Development          | Dash/Plotly interactive dashboard                       |
| Business Intelligence    | Executive-ready outputs and KPIs                       |
| Testing & Validation     | Unit tests for core ML models                          |
| Documentation            | Comprehensive README explaining business impact         |

## 🚨 Troubleshooting

### 1. Dashboard not loading

- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check that port 8050 is free: `lsof -i:8050` (macOS/Linux)
- Verify mock data has been generated in the `data/mock/` directory

### 2. ML models not working

- You may need to install specific libraries like XGBoost: `pip install xgboost`
- Try reinstalling key packages: `pip install --no-cache-dir scikit-learn pandas`
- Run the tests to isolate issues: `PYTHONPATH=. python tests/test_ml_models.py`

### 3. PDF generation failing

This often requires external dependencies:

- **Linux (Debian/Ubuntu):** `sudo apt-get install libcairo2-dev libpango1.0-dev`
- **macOS:** `brew install cairo pango`
- **Windows:** Install the GTK+ runtime

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/your-amazing-feature`
5. Open a Pull Request

Contributions are welcome!

## 📄 License

This project is licensed under the MIT License. Feel free to use this for learning or as a foundation for your own projects.
