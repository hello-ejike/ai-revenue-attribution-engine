# adapters/csv_loader.py
import pandas as pd
from core.types import CampaignData

def load_campaign_data(path: str) -> List[CampaignData]:
    df = pd.read_csv(path)
    return df.to_dict(orient="records")  # type: ignore