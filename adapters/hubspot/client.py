# ai_revenue_attribution_engine/adapters/hubspot/client.py

from datetime import datetime, timedelta
import random
from faker import Faker

Faker.seed(42)
fake = Faker()

class HubSpotClient:
    def __init__(self):
        self.use_real_api = False
        print("⚠️ Running in mock mode — no HubSpot API connection")

    def get_deals(self):
        stages = ['qualifiedtobuy', 'presentationscheduled', 'decisionmakerboughtin', 'closedwon']
        channels = ["google", "linkedin", "email", "content", "direct"]

        return [{
            "id": f"D{i}",
            "properties": {
                "dealname": f"{fake.company()} {fake.catch_phrase()}",
                "amount": str(random.uniform(10_000, 500_000)),
                "dealstage": random.choice(stages),
                "created_at": (datetime.today() - timedelta(days=random.randint(1, 365))).isoformat()
            },
            "channel": random.choice(channels)
        } for i in range(1, 101)]

    def get_contacts(self):
        titles = ['CEO', 'CMO', 'Sales Director', 'Marketing Manager']

        return [{
            "id": f"CT{i}",
            "properties": {
                "email": fake.email(),
                "firstname": fake.first_name(),
                "lastname": fake.last_name(),
                "company": fake.company(),
                "jobtitle": random.choice(titles),
                "createdate": (datetime.today() - timedelta(days=random.randint(1, 365))).isoformat()
            }
        } for i in range(1, 101)]

    def get_associated_deals(self, contact_id):
        return [{
            "id": f"D{i}",
            "properties": {
                "dealname": f"Deal {i} for {contact_id}",
                "amount": str(random.uniform(10_000, 200_000)),
                "dealstage": random.choice(['qualifiedtobuy', 'closedwon']),
                "created_at": (datetime.today() - timedelta(days=random.randint(1, 30))).isoformat()
            },
            "channel": random.choice(["google", "linkedin", "email", "content", "direct"])
        } for i in range(1, random.randint(2, 5))]
