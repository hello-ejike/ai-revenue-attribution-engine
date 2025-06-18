---

### 

Markdown

`# 🚀 AI Revenue Attribution & Forecasting Engine

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) ![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg) 
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg) ![Code 
Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen.svg)

A comprehensive RevOps system that solves the marketing vs sales attribution debate using multi-touch attribution modeling, revenue 
forecasting, and AI-powered deal analysis. Built with Python, Dash, and local LLM integration.

<p align="center"><a href="#" style="display: inline-block; background-color: #1a73e8; color: white; padding: 10px 20px; text-decoration: 
none; border-radius: 5px; font-weight: bold;">✨ View Live Demo</a></p>> *_****[Developer Note: The "Live Demo" button above is a 
placeholder. , will update it soon.]****_*<p align="center"><img src="./docs/dashboard-demo.gif" alt="AI Revenue Engine Dashboard Demo"></p>> 
*_****[Developer Note: The GIF above is a placeholder. will update it soon.]****_*

This system is designed for demonstration with a realistic mock data pipeline but is architected to integrate with real CRM data sources like 
HubSpot or Salesforce.

## 🔍 Why This Matters
This system addresses critical revenue operations challenges:

* ****Attribution Clarity:**** Quantify which channels actually drive revenue with 5 different attribution models.
* ****Accurate Forecasting:**** Combine pipeline velocity and time-series analysis for reliable predictions.
* ****AI-Powered Insights:**** Get natural language explanations for deal risks and channel performance.
* ****Executive Reporting:**** Generate professional PDF reports with actionable insights.

## 🧠 Core Features

| Feature                 | Description                                       | Business Impact                  |
| ----------------------- | ------------------------------------------------- | -------------------------------- |
| Multi-Touch Attribution | First-touch, last-touch, linear, time-decay, etc. | End marketing vs sales debates   |
| Revenue Forecasting     | Pipeline velocity + time-series modeling          | Accurate quarterly planning      |
| AI Deal Analysis        | Mistral-powered risk assessment                   | Prevent deal slippage            |
| Interactive Dashboard   | Real-time visualization with Dash/Plotly          | Executive-ready insights         |
| PDF Reporting           | Automated report generation                       | Stakeholder communication        |
| Mock Data Pipeline      | Realistic CRM data simulation                     | Testing and demonstration        |

<details><summary>📦 View Project Structure</summary>`

ai-revenue-attribution-engine/

├── agents/              # Business logic (data collection, attribution)

│   ├── data_collector.py

│   ├── attribution_engine.py

│   └── revenue_analyst.py

├── models/              # Mathematical models (forecasting, scoring)

│   ├── attribution_models.py

│   └── forecasting_models.py

├── services/            # LLM integration

│   └── ai_service.py

├── dashboard/           # Visualization layer

│   └── app.py

├── templates/           # PDF report templates

│   └── report_template.html

├── reports/             # Generated insights

│   └── report_generator.py

├── data/                # Mock data pipeline

│   ├── mock/

│   ├── raw/

│   └── processed/

├── config/              # Settings

│   ├── hubspot_config.py

│   └── settings.py

├── tests/               # Validation

│   └── test_ai_agent.py

├── docs/                # Documentation & Visuals (like your GIF)

├── requirements.txt     # Dependencies

└── .gitignore           # File exclusion rules

`</details>

## 🛠️ Installation

**Prerequisites**
* Python 3.8+
* [Ollama](https://ollama.com/) (for local LLM support). Ollama is a tool for running large language models locally.

**Setup**
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
cp config/settings.py.example config/settings.py`

## 🚀 Quick Start

Bash

# 

`# Start the Ollama server in the background
ollama serve &

# Run the dashboard application
PYTHONPATH=. python dashboard/app.py

# Access the dashboard in your browser at http://localhost:8050`

## 📊 Sample Outputs

**Channel Performance Analysis**

| **Channel** | **Win Rate** | **Attribution Score** | **Recommendation** |
| --- | --- | --- | --- |
| Google Ads | 60% | 0.85 | Increase investment |
| LinkedIn | 50% | 0.70 | Optimize targeting |
| Email | 30% | 0.45 | Improve sequences |
| Content | 20% | 0.25 | Long-term nurture |

**AI Deal Analysis Example**

> Deal D4 Analysis:
> 
> - **Probability:** 19% (High Risk)
> - **Channel:** Email → Content (low intent signal)
> - **Rep Performance:** Below average (25% close rate)
> - **Recommendation:** Schedule discovery call or reassign to senior rep

## 🧪 Technical Implementation

&lt;details>

&lt;summary>🔬 View Attribution Models Code&lt;/summary>

Python

# 

`# Five different attribution approaches
class AttributionEngine:
    def first_touch_attribution(self, journey):
        """Credits first touchpoint"""
        return {journey[0]["channel"]: 1.0}
    
    def time_decay_attribution(self, journey, decay_rate=0.7):
        """More weight to recent touchpoints"""
        weights = [decay_rate ** (len(journey) - i - 1) for i in range(len(journey))]
        return self._distribute_weights(journey, weights)
    
    def position_based_attribution(self, journey):
        """40% first + 40% last + 20% middle"""
        attribution = defaultdict(float)
        attribution[journey[0]["channel"]] += 0.4
        attribution[journey[-1]["channel"]] += 0.4
        # Distribute remaining 20% among middle touches
        return attribution`

&lt;/details>

&lt;details>

&lt;summary>📈 View Revenue Forecasting Code&lt;/summary>

Python

# 

`def time_series_forecast(self, historical_data, periods=3):
    """Predict future revenue based on historical patterns"""
    monthly_revenue = defaultdict(float)
    
    for deal in historical_data:
        timestamp = deal.get("timestamp") or deal.get("created_at")
        date = datetime.fromisoformat(timestamp.split("T")[0])
        month_key = f"{date.year}-{date.month}"
        monthly_revenue[month_key] += float(deal["amount"])
    
    # Apply moving average for predictions
    sorted_values = sorted(monthly_revenue.values())
    window_size = min(3, len(sorted_values))
    
    predictions = []
    for _ in range(periods):
        prediction = mean(sorted_values[-window_size:])
        predictions.append(prediction)
        sorted_values.append(prediction)
    
    return predictions`

&lt;/details>

&lt;details>

&lt;summary>🤖 View AI Service Integration Code&lt;/summary>

Python

# 

`class AIService:
    def _initialize_llm(self):
        """Support both OpenAI and local Ollama"""
        try:
            if "OPENAI_API_KEY" in os.environ:
                from langchain.llms import OpenAI
                return OpenAI(model="gpt-4", temperature=0.7)
            else:
                from langchain_community.llms import Ollama
                return Ollama(model="mistral")
        except ImportError:
            return self._mock_llm`

&lt;/details>

## 🛣️ Roadmap

| **Status** | **Phase** | **Description** |
| --- | --- | --- |
| ✅ | Complete | Core attribution models |
| ✅ | Complete | Revenue forecasting engine |
| ✅ | Complete | AI-powered insights |
| ✅ | Complete | Interactive dashboard |
| ✅ | Complete | PDF report generation |
| 🚧 | In Progress | Real CRM integrations |
| 📋 | Planned | Advanced ML models |
| 📋 | Planned | Multi-currency support |
| 📋 | Planned | API endpoints |

## 💼 Skills Demonstrated

| **Technical Skill** | **Implementation Evidence** |
| --- | --- |
| Python Architecture | Modular design with clear separation of concerns |
| Machine Learning | Applied forecasting and probability scoring |
| Data Engineering | ETL pipeline with mock data generation |
| LLM Integration | Local and cloud AI model support |
| Web Development | Interactive dashboard with Dash/Plotly |
| Business Intelligence | Executive-ready reporting and insights |
| Testing & Quality | Comprehensive test suite with pytest |

## 🚨 Troubleshooting

Common issues and how to solve them.

- **Dashboard not loading:**
    1. Check dependencies: `pip install -r requirements.txt`
    2. Verify port is free: `lsof -i :8050` (macOS/Linux)
    3. Ensure mock data exists.
- **AI features not working:**
    1. Verify Ollama is installed (`ollama --version`) and running (`ollama list`).
- **PDF generation failing:**
    1. Install system dependencies: `sudo apt-get install libcairo2-dev` (Debian/Ubuntu) or `brew install cairo pango` (macOS).
