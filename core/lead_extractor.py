import requests

class LeadHunter:
    def __init__(self):
        self.api_key = "rnd_V4lkViPnV8U8yz30eaEQ7KWItriZ" # Render API-n keresztüli scraping

    def find_business_leads(self, industry="marketing", location="Hungary"):
        print(f"🔍 [SYSTEM] Valós {industry} cégek keresése itt: {location}...")
        # Példa lead adatok (élesben itt egy scraping API fut)
        leads = [
            {"name": "TechSolutions Kft.", "email": "info@techsolutions.hu", "need": "IT automatizáció"},
            {"name": "Global Trade Bt.", "email": "contact@globaltrade.hu", "need": "Profit maximalizálás"}
        ]
        return leads

if __name__ == "__main__":
    hunter = LeadHunter()
    print(hunter.find_business_leads())
