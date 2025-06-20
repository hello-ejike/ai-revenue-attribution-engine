# agents/data_collector.py

import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

class HubSpotClient:
    def get_associated_deals(self, contact_id):
        """Simulate fetching deals from HubSpot"""
        return [{
            "id": f"D{random.randint(1, 100)}",
            "properties": {
                "dealname": f"{fake.company()} {fake.catch_phrase()}",
                "amount": str(random.uniform(10_000, 500_000)),
                "dealstage": random.choice(['qualifiedtobuy', 'presentationscheduled', 
'decisionmakerboughtin', 'closedwon']),
                "created_at": (datetime.today() - timedelta(days=random.randint(1, 365))).isoformat()
            },
            "channel": random.choice(["google", "linkedin", "email", "content", "direct"]),
            "rep": random.choice(["Rep A", "Rep B", "Rep C", "Rep D"])
        } for _ in range(1, random.randint(2, 5))]

class DataCollectorAgent:
    def __init__(self):
        self.hubspot = HubSpotClient()
        self._contact_journeys = []

    def enrich_contact_journeys(self) -> list:
        """Simulate customer journeys with ML-friendly features"""
        contacts = [{
            "id": f"C{i}",
            "email": fake.email(),
            "company": fake.company()
        } for i in range(1, 20)]

        for contact in contacts[:10]:
            contact_id = contact["id"]
            try:
                associated_deals = self.hubspot.get_associated_deals(contact_id)
                for deal in associated_deals:
                    touchpoints = random.randint(1, 6)  # Number of marketing touches
                    deal_age = random.randint(30, 180)  # Deal cycle time in days
                    converted = random.random() > 0.5  # Simulated conversion
                    amount = float(deal["properties"]["amount"])

                    journey = []
                    current_date = datetime.fromisoformat(deal["properties"]["created_at"].split("T")[0])

                    for step in range(touchpoints):
                        journey.append({
                            "step": step + 1,
                            "channel": random.choice(["google", "linkedin", "email", "content", 
"direct"]),
                            "timestamp": (current_date - timedelta(days=deal_age // touchpoints * (step + 
1))).isoformat(),
                            "rep": deal["rep"],
                            "deal_id": deal["id"],
                            "amount": amount,
                            "converted": converted
                        })

                    self._contact_journeys.extend(journey)
            except Exception as e:
                print(f"⚠️ Error fetching journey for contact {contact_id}: {e}")

        return self._contact_journeys
