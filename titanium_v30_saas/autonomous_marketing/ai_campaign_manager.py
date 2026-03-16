import time, random, threading
from modules import email_campaigns, social_auth_manager, stripe_manager, autonomous_marketing
from predictive_layer import predictive_ai

class AICampaignManager:
    def __init__(self):
        self.running = True

    def generate_recipients(self):
        # AI-alapú felhasználói szegmentáció prediktív réteggel
        top_segment = predictive_ai.predict_best_segment()
        return [f"user{top_segment}_{random.randint(1,1000)}@example.com" for _ in range(random.randint(5, 12))]

    def run(self):
        while self.running:
            recipients = self.generate_recipients()
            print(f"[AICampaign] {len(recipients)} felhasználónak kampány indítása...")
            revenue_total = 0
            engagement_total = 0
            for r in recipients:
                email_campaigns.send(r)
                engagement_total += 1
                payment = random.randint(5,50)
                stripe_manager.charge(payment)
                revenue_total += payment
            content = f"AI poszt {random.randint(1,1000)}"
            social_auth_manager.post(content)
            autonomous_marketing.run()
            predictive_ai.log_campaign_result(revenue_total, engagement_total)
            time.sleep(random.randint(15,30))  # következő ciklus

if __name__ == "__main__":
    manager = AICampaignManager()
    threading.Thread(target=manager.run, daemon=True).start()
    print("[AICampaign] AI kampány manager prediktív réteggel fut.")
    while True:
        time.sleep(1)
