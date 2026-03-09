import stripe
import os
import time
from dotenv import load_dotenv
from hyper_layer import TitaniumHyperLayer
from marketing_layer import TitaniumMarketingEngine

load_dotenv(dotenv_path="~/.titanium_env")

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
hyper_engine = TitaniumHyperLayer(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
marketing_engine = TitaniumMarketingEngine()

def main_loop():
    print("💎 TITANIUM EMPIRE - V27 HYPER-DRIVE 💎")
    try:
        # 1. Pénzügyek
        balance = stripe.Balance.retrieve()
        current_eur = balance['available'][0]['amount'] / 100
        print(f"💰 Egyenleg: {current_eur} EUR")

        # 2. Értékesítés (E-mail)
        hyper_engine.deep_market_scan("SaaS Automation")
        
        # 3. Önhirdetés és Marketing
        marketing_engine.scan_forums_for_opportunities()
        marketing_engine.auto_post_promotion()
        
        # 4. Újrabefektetés
        marketing_engine.reinvest_check(current_eur)

    except Exception as e:
        print(f"⚠️ Hiba: {e}")

if __name__ == "__main__":
    while True:
        main_loop()
        time.sleep(3600) # Óránkénti teljes ciklus
