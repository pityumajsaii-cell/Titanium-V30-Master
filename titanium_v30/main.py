import sys, os, time, threading
from dotenv import load_dotenv

BASE = os.path.expanduser("~")
CONFIG_DIR = os.path.join(BASE, "titanium_v30/config")
load_dotenv(os.path.join(CONFIG_DIR, ".env"))

sys.path.insert(0, os.path.join(BASE, "email_system"))
sys.path.insert(0, os.path.join(BASE, "titanium_v30"))
sys.path.insert(0, os.path.join(BASE, "social_engine", "scripts"))
sys.path.insert(0, os.path.join(BASE, "autonomous_marketing"))

from email_system.email_campaigns import EmailCampaigns
from titanium_v30.stripe_manager import StripeManager
from social_engine.scripts.social_auth_manager import SocialManager
from autonomous_marketing.autonomous_marketing import AutonomousMarketing

email_status = EmailCampaigns()
stripe_status = StripeManager()
social_status = SocialManager()
auto_status = AutonomousMarketing()

def log(msg):
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def monitor_modules():
    while True:
        log("Modul státuszok:")
        log("Email: " + email_status.status())
        log("Stripe: " + stripe_status.status())
        log("Social: " + social_status.status())
        log("Autonomous: " + auto_status.status())
        time.sleep(5)

if __name__ == "__main__":
    try:
        threading.Thread(target=monitor_modules, daemon=True).start()
        log("✅ Titanium Főmotor fut, PM2 nélkül, éles kulcsokkal.")
        while True:
            time.sleep(1)
    except Exception as e:
        log(f"❌ Hiba: {e}")
