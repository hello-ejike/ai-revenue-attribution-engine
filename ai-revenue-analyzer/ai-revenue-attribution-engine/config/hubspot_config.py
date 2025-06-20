# config/hubspot_config.py

class HubSpotConfig:
    BASE_URL = "https://api.hubapi.com" 
    SCOPES = ["crm.objects.contacts.read", "crm.objects.deals.read", "marketing.events.read"]
    DEFAULT_HEADERS = {
        "Authorization": None,  # Will be set dynamically
        "Content-Type": "application/json"
    }