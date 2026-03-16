import time, threading
from modules import email_campaigns, stripe_manager, social_auth_manager, autonomous_marketing

class RevenueOptimizer:
    def __init__(self):
        self.last_email = 0
        self.last_social = 0
        self.last_campaign = 0

    def optimize(self):
        while True:
            # AI logika: email küldés optimalizálás
            if self.last_email + 10 < time.time():
                email_campaigns.send("client@example.com")
                self.last_email = time.time()

            # Social posztolás optimalizálás
            if self.last_social + 20 < time.time():
                social_auth_manager.post("Új AI posztolás")
                self.last_social = time.time()

            # Autonomous kampány futtatása
            if self.last_campaign + 30 < time.time():
                autonomous_marketing.run()
                self.last_campaign = time.time()

            # Bevétel monitorozás és AI javaslat
            revenue_status = stripe_manager.status()
            print(f"[Optimizer] Current revenue: {revenue_status}")
            time.sleep(5)

if __name__ == "__main__":
    print("[Optimizer] AI bevétel-optimalizáló modul indítva")
    RevenueOptimizer().optimize()
