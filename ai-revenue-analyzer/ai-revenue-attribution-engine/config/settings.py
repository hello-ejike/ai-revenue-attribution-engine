# config/settings.py

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    HUBSPOT_API_KEY = os.getenv("HUBSPOT_API_KEY")
    SQLITE_DB_PATH = os.getenv("SQLITE_DB_PATH", "data/revenue_attribution.db")
    DASHBOARD_PORT = int(os.getenv("DASHBOARD_PORT", "8050"))