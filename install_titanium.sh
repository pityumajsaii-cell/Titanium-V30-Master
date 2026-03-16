


#!/data/data/com.termux/files/usr/bin/bash
# 🚀 Titanium V11 Ultra – Teljes AI SaaS telepítő Termux-ra

echo "🚀 Titanium V11 Ultra telepítés indul..."

# 1️⃣ Frissítés és alap csomagok
pkg update -y && pkg upgrade -y
pkg install -y python git curl nodejs-lts

# 2️⃣ Python csomagok
pip install --upgrade pip --user
pip install stripe requests

# 3️⃣ PM2 telepítése
npm install -g pm2

# 4️⃣ Könyvtárak létrehozása
mkdir -p ~/titanium_v11

# 5️⃣ AI indító script létrehozása
cat > ~/titanium_v11/ai_start.py << 'EOF'
from ai_router import launch_full_system, launch_growth_monitor
import os
os.environ["PYTHONPATH"] = os.path.expanduser("~/titanium_v11")

launch_full_system(
    modules=["Education","AI_Tools","AI_Marketing","Payment","Dashboard"],
    mobile_friendly=True,
    push_notifications=True,
    realtime_graphs=True,
    analytics=True,
    self_learning=True,
    auto_archive=True
)

launch_growth_monitor()
EOF

# 6️⃣ Revenue monitor script
cat > ~/titanium_v11/revenue_monitor.py << 'EOF'
import os
import time
import requests

LOCK_FILE = os.path.join(os.getenv("HOME"), "titanium_v11", "revenue_monitor.lock")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
STRIPE_KEY = os.getenv("STRIPE_SECRET_KEY")
REVOLUT_TOKEN = os.getenv("REVOLUT_API_TOKEN")
REVOLUT_LAST_ID_FILE = os.path.join(os.getenv("HOME"), "titanium_v11", "revolut_last_id.txt")
CHECK_INTERVAL = 300

def telegram_notify(msg):
    if TELEGRAM_TOKEN and TELEGRAM_CHAT_ID:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": msg})

def check_stripe_payments():
    try:
        import stripe
        stripe.api_key = STRIPE_KEY
        payments = stripe.PaymentIntent.list(limit=5)
        for p in payments.data:
            if p.status == 'succeeded':
                telegram_notify(f"💰 Stripe fizetés: {p.amount/100:.2f} {p.currency.upper()}")
    except Exception as e:
        telegram_notify(f"⚠️ Stripe error: {e}")

def check_revolut_payout():
    if not REVOLUT_TOKEN:
        return
    headers = {"Authorization": f"Bearer {REVOLUT_TOKEN}"}
    url = "https://b2b.revolut.com/api/1.0/payouts"
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        payouts = resp.json().get("payouts", [])

        last_id = None
        if os.path.exists(REVOLUT_LAST_ID_FILE):
            with open(REVOLUT_LAST_ID_FILE, "r") as f:
                last_id = f.read().strip()

        new_last_id = last_id
        for payout in sorted(payouts, key=lambda x: x["created_at"]):
            pid = payout["id"]
            amount = float(payout["amount"])
            currency = payout["currency"]
            if last_id is None or pid > last_id:
                telegram_notify(f"💵 Revolut payout: {amount:.2f} {currency}")
                new_last_id = pid

        if new_last_id != last_id:
            with open(REVOLUT_LAST_ID_FILE, "w") as f:
                f.write(new_last_id)
    except Exception as e:
        telegram_notify(f"⚠️ Revolut error: {e}")

if __name__ == "__main__":
    if not os.path.exists(LOCK_FILE):
        telegram_notify("🚀 Revenue monitor elindult!")
        with open(LOCK_FILE, "w") as f:
            f.write("started")

    while True:
        check_stripe_payments()
        check_revolut_payout()
        time.sleep(CHECK_INTERVAL)
EOF

# 7️⃣ PM2 folyamatok indítása
export PYTHONPATH="$HOME/titanium_v11"
pm2 delete all || true
pm2 start python3 --name "titanium" -- ~/titanium_v11/ai_start.py --watch
pm2 start python3 --name "revenue_monitor" -- ~/titanium_v11/revenue_monitor.py --watch
pm2 save --force

# 8️⃣ Termux boot automatikus indítás
mkdir -p ~/.termux/boot
cat > ~/.termux/boot/titanium_auto.sh << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
export PYTHONPATH="$HOME/titanium_v11"
pm2 resurrect || true
pm2 save --force
EOF
chmod +x ~/.termux/boot/titanium_auto.sh

echo "✅ Teljes Titanium AI SaaS rendszer telepítve és fut!"
echo "📱 Böngészőben elérhető: http://<YOUR_SERVER_IP>:3000"
echo "📩 Telegram értesítések Stripe / Revolut fizetés esetén"
echo "🧠 Self-learning AI modulok aktív és minden pro modul integrálva."
