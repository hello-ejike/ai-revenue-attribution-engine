# agents/data_collector.py

from typing import List, Dict
from adapters.hubspot.client import HubSpotClient

class DataCollectorAgent:
    def __init__(self):
        self.hubspot = HubSpotClient()
        self._contact_journeys = []
    
    def collect_deals_data(self) -> List[Dict]:
        return self.hubspot.get_deals()
    
    def collect_contacts_data(self) -> List[Dict]:
        return self.hubspot.get_contacts()
    
    def enrich_contact_journeys(self) -> List[Dict]:
        if not self._contact_journeys:
            contacts = self.collect_contacts_data()
            used_deals = set()
            
            for contact in contacts[:20]:
                contact_id = contact["id"]
                try:
                    associated_deals = self.hubspot.get_associated_deals(contact_id)
                    
                    for deal in associated_deals:
                        if deal["id"] in used_deals:
                            continue
                        used_deals.add(deal["id"])
                        
                        self._contact_journeys.append({
                            "contact_id": contact_id,
                            "deal_id": deal["id"],
                            "channel": deal["channel"],
                            "timestamp": deal["properties"]["created_at"],
                            "amount": float(deal["properties"]["amount"]),
                            "stage": deal["properties"]["dealstage"]
                        })
                except Exception as e:
                    print(f"Error fetching journey for contact {contact_id}: {e}")
        
        return self._contact_journeys
