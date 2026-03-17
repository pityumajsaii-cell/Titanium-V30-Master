import os
import time
import threading
import requests
from flask import Flask

app = Flask(__name__)

def keep_alive():
    while True:
        try:
            # Önmaga meghívása, hogy ne aludjon el a Space
            requests.get("http://localhost:7860/")
        except:
            pass
        time.sleep(600) # 10 perc

@app.route("/")
def home():
    return {
        "status": "ONLINE",
        "system": "TITANIUM V30 MASTER",
        "owner": "Titanium",
        "payout_target": "Revolut LT81 3250...",
        "uptime": "24/7 ACTIVE"
    }

if __name__ == "__main__":
    # Keep-alive szál indítása
    threading.Thread(target=keep_alive, daemon=True).start()
    app.run(host='0.0.0.0', port=7860)
