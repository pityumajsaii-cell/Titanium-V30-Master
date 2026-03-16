import os, time

MODULES = ["realtime_revenue", "ai_marketing_engine", "b2b_offer_generator", "lead_management", "global_dashboard"]

while True:
    for mod in MODULES:
        status = os.popen(f"pm2 describe {mod}").read()
        if "online" not in status:
            print(f"🔄 Újraindítás: {mod}")
            os.system(f"pm2 restart {mod}")
    time.sleep(60)
