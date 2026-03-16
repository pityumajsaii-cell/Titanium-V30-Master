import random
class AdsAPI:
    def __init__(self):
        self.campaigns = []

    def create_campaign(self, platform, budget, audience):
        campaign_id = f"{platform}_{random.randint(1000,9999)}"
        print(f"[AdsAPI] Kampány létrehozva: {campaign_id}, Platform: {platform}, Budget: ${budget}, Audience: {audience}")
        self.campaigns.append((campaign_id, platform, budget, audience))
        return campaign_id

    def optimize_campaign(self, campaign_id):
        print(f"[AdsAPI] Kampány optimalizálás: {campaign_id}")
