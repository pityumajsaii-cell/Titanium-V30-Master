import time, threading, random
from global_ads_api import AdsAPI
from modules import predictive_ai

class AIAdsManager:
    def __init__(self):
        self.ads_api = AdsAPI()
        self.running = True

    def generate_audience(self):
        top_segment = predictive_ai.predict_best_segment()
        return f"user_segment_{top_segment}"

    def run(self):
        while self.running:
            for platform in ["GoogleAds", "FacebookAds", "TikTokAds"]:
                audience = self.generate_audience()
                budget = random.randint(50,200)
                campaign_id = self.ads_api.create_campaign(platform, budget, audience)
                self.ads_api.optimize_campaign(campaign_id)
            time.sleep(20)  # következő kör

if __name__ == "__main__":
    manager = AIAdsManager()
    threading.Thread(target=manager.run, daemon=True).start()
    print("[AIAdsManager] AI globális hirdetés manager fut.")
    while True:
        time.sleep(1)
