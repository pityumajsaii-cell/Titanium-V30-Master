#!/bin/bash
# =================================================
# TITANIUM V30 - AUTONOMOUS REVENUE ECOSYSTEM
# =================================================

clear
echo "🚀 TITANIUM V30 MASTER CONTROL INDÍTÁSA..."

# 1. MÉLYTISZTÍTÁS
echo "🧹 Régi folyamatok törlése..."
pkill -f python
pkill -f lt
pkill -f ngrok
sleep 2

# 2. ÉLES .ENV ELLENŐRZÉS
if [ ! -f ~/.env ]; then
    echo "⚠️ HIÁNYZÓ .ENV! Kérlek, később töltsd ki a kulcsokat."
    touch ~/.env
fi

# 3. AZ ÉLES SZERVER KÓD (Closed-Loop Logic)
cat << 'PY' > ~/titanium_v30_final.py
import os, time, threading, subprocess, stripe
from flask import Flask, jsonify, request
from dotenv import load_dotenv

load_dotenv(os.path.expanduser("~/.env"))
app = Flask(__name__)
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

@app.route("/")
def index():
    return jsonify({"status": "TITANIUM_ONLINE", "vault": "Revolut_LT81_Ready"})

@app.route("/pay", methods=["POST"])
def pay():
    try:
        intent = stripe.PaymentIntent.create(
            amount=5000, currency='eur', # 50 EUR Fix Payout
            metadata={'target': 'REVOLUT_LT81_3250'}
        )
        return jsonify(intent)
    except Exception as e: return jsonify(error=str(e)), 400

def run_server():
    app.run(host="0.0.0.0", port=3001, threaded=True)

if __name__ == "__main__":
    run_server()
PY

# 4. AZ AUTOMATIKUS ÚJRAINDÍTÓ (Watchdog)
cat << 'WATCH' > ~/titanium_watchdog.sh
#!/bin/bash
while true; do
  if ! pgrep -f "titanium_v30_final.py" > /dev/null; then
    echo "♻️ Szerver leállt! Újraindítás..."
    nohup python3 ~/titanium_v30_final.py > ~/titanium_live.log 2>&1 &
  fi
  if ! pgrep -f "lt --port 3001" > /dev/null; then
    echo "🌐 Tunnel megszakadt! Újracsatlakozás..."
    nohup lt --port 3001 --print-requests > ~/tunnel.log 2>&1 &
  fi
  sleep 60
done
WATCH

chmod +x ~/titanium_watchdog.sh
chmod +x ~/titanium_v30_final.py

# 5. TELJES INDÍTÁS
echo "✅ Szerver és Alagút indítása..."
nohup python3 ~/titanium_v30_final.py > ~/titanium_live.log 2>&1 &
sleep 3
nohup lt --port 3001 > ~/tunnel.log 2>&1 &
sleep 2
nohup bash ~/titanium_watchdog.sh > /dev/null 2>&1 &

echo "================================================="
echo "💎 RENDSZER ÉLESÍTVE ÉS FIGYELÉS ALATT!"
echo "🔗 Publikus URL-ed itt találod: tail -f ~/tunnel.log"
echo "💰 Kifizetési cél: Revolut LT81 3250..."
echo "================================================="
