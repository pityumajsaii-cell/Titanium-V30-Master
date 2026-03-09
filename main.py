import stripe
import os
import time
from dotenv import load_dotenv
from hyper_layer import TitaniumHyperLayer
from marketing_layer import TitaniumMarketingEngine
from enterprise_layer import TitaniumEnterpriseLayer

load_dotenv(dotenv_path="~/.titanium_env")

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
hyper_engine = TitaniumHyperLayer(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
marketing_engine = TitaniumMarketingEngine()
enterprise_layer = TitaniumEnterpriseLayer()

def enterprise_cycle():
    print("🏢 TITANIUM ENTERPRISE V28 - MULTI-FUNCTION RUN 🏢")
    try:
        # Pénzügyi státusz
        balance = stripe.Balance.retrieve()
        print(f"💰 Liquidity Check: OK")

        # 1. Funkció: Értékesítés
        hyper_engine.deep_market_scan("Global Enterprise Solutions")

        # 2. Funkció: Szabályozás figyelés
        enterprise_layer.compliance_scan()

        # 3. Funkció: Dokumentum elemzés demó indítása
        enterprise_layer.process_document("Invoice-Sample")

        # 4. Funkció: Önhirdetés
        marketing_engine.auto_post_promotion()

    except Exception as e:
        print(f"❌ Enterprise Hiba: {e}")

if __name__ == "__main__":
    while True:
        enterprise_cycle()
        time.sleep(3600)
