import time, threading
from modules import email_campaigns, stripe_manager, social_auth_manager, autonomous_marketing

def monitor_modules():
    while True:
        print("[Titanium] Modul státuszok:")
        for name, mod in [("Email", email_campaigns), ("Stripe", stripe_manager),
                          ("Social", social_auth_manager), ("Autonomous", autonomous_marketing)]:
            status = mod.status() if hasattr(mod,'status') else "N/A"
            print(f"{name} modul: {status}")
        time.sleep(5)

if __name__ == "__main__":
    threading.Thread(target=monitor_modules, daemon=True).start()
    print("[Titanium] Főmotor fut, minden modul felügyelve.")
    while True:
        time.sleep(1)
