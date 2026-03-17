import random

class NeuralMarketing:
    def __init__(self):
        self.campaign_stats = {
            "Enterprise_ERP": 0,
            "Legal_AI": 0,
            "Marketing_Agency": 0
        }
        self.learning_rate = 0.1

    def optimize_campaigns(self, conversion_data):
        # Öntanuló algoritmus: a sikeres kampányok súlyozása
        for campaign, profit in conversion_data.items():
            self.campaign_stats[campaign] += profit * self.learning_rate
        return sorted(self.campaign_stats.items(), key=lambda x: x[1], reverse=True)

    def generate_auto_ad(self, best_service):
        templates = [
            f"🚀 {best_service}: A jövő vállalati megoldása. Próbálja ki most!",
            f"💰 Maximalizálja profitját a Titanium {best_service} segítségével.",
            f"🤖 Az Ön cége készen áll? {best_service} integráció 24 órán belül."
        ]
        return random.choice(templates)
