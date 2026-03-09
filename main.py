import stripe
import os
import time
from dotenv import load_dotenv
from apex_layer import TitaniumApexEngine
from nexus_layer import TitaniumNexusEngine

load_dotenv(dotenv_path="~/.titanium_env")

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
apex_engine = TitaniumApexEngine()
nexus_engine = TitaniumNexusEngine()

def nexus_operation():
    print("🛸 TITANIUM V32 - GLOBAL AI-NEXUS OPERATIONAL 🛸")
    try:
        # 1. Stratégiai elemzés
        apex_engine.optimize_strategy(0.92)
        
        # 2. Külső AI rendszerek státuszának ellenőrzése
        hubs = nexus_engine.list_active_hubs()
        
        # 3. Automatikus szolgáltatás-értékesítés (példa: Video AI)
        nexus_engine.bridge_to_global_market("Video-Marketing-AI", "High-Quality Corporate Ad")
        
        # 4. Stripe Pénzügyi Monitor
        balance = stripe.Balance.retrieve()
        amount = balance['available'][0]['amount'] / 100
        print(f"💰 Global Revenue Stream: {amount} {balance['available'][0]['currency'].upper()}")

    except Exception as e:
        print(f"❌ Nexus System Warning: {e}")

if __name__ == "__main__":
    while True:
        nexus_operation()
        time.sleep(3600) # Óránkénti globális szinkronizáció
