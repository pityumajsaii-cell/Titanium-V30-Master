import stripe
import os
import time
from dotenv import load_dotenv
from hyper_layer import TitaniumHyperLayer

load_dotenv(dotenv_path="~/.titanium_env")

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
hyper_engine = TitaniumHyperLayer(
    smtp_user=os.getenv("EMAIL_USER"), 
    smtp_pass=os.getenv("EMAIL_PASS")
)

def run_titanium_cycle():
    print("🔄 Titanium Autonóm Ciklus Indítása...")
    try:
        # 1. Pénzügyi ellenőrzés
        balance = stripe.Balance.retrieve()
        print(f"💰 Aktuális likviditás: {balance['available'][0]['amount']/100} {balance['available'][0]['currency'].upper()}")

        # 2. Piaci vadászat
        opportunities = hyper_engine.deep_market_scan("AI Automation SaaS")
        for opp in opportunities:
            print(f"🎯 Célpont: {opp['target']} | Megoldás: {opp['solution']}")
            # Itt hívná meg az automatikus értékesítőt
            
        print("✅ Ciklus sikeresen lefutott. Következő ellenőrzés 1 óra múlva.")
    except Exception as e:
        print(f"❌ Hiba a rendszerben: {e}")

if __name__ == "__main__":
    while True:
        run_titanium_cycle()
        time.sleep(3600) # Óránkénti automatikus futás
