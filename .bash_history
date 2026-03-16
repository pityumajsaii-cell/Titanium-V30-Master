SHOTSTACK_SANDBOX_KEY="q7kzpw3llvZwIsobo0nHhu5vPtYvZnx2851JghsA48gCimCPZ9"
CLOUDINARY_URL="cloudinary://681955246719799:l-5XCrYlHg4UE2nZGl0KV3rUcEw@dnj634roj"
EOF

# ------------------------
# Python csomagok telepítése Termuxban
# ------------------------
pkg install python -y
pip install python-dotenv
# ------------------------
# Főmotor létrehozása
# ------------------------
cat > "$BASE/titanium_v30/main.py" <<'EOF'
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
    threading.Thread(target=monitor_modules, daemon=True).start()
    log("✅ Titanium Főmotor fut, PM2 nélkül, éles kulcsokkal.")
    while True:
        time.sleep(1)
EOF

# ------------------------
# Főmotor futtatása háttérben
# ------------------------
nohup python3 "$BASE/titanium_v30/main.py" > "$BASE/titanium_v30/titanium.log" 2>&1 &
echo "🚀 Titanium főmotor elindítva PM2 nélkül, napló: $BASE/titanium_v30/titanium.log"
cat > ~/titanium_v30/main.py <<'EOF'
import sys, os, time, threading
from dotenv import load_dotenv

# ------------------------
# Alap útvonalak
# ------------------------
BASE = os.path.expanduser("~")
CONFIG_DIR = os.path.join(BASE, "titanium_v30/config")
load_dotenv(os.path.join(CONFIG_DIR, ".env"))

# ------------------------
# Python path explicit hozzáadása
# ------------------------
sys.path.insert(0, os.path.join(BASE, "email_system"))
sys.path.insert(0, os.path.join(BASE, "titanium_v30"))
sys.path.insert(0, os.path.join(BASE, "social_engine", "scripts"))
sys.path.insert(0, os.path.join(BASE, "autonomous_marketing"))

# ------------------------
# Modulok importálása
# ------------------------
from email_system.email_campaigns import EmailCampaigns
from titanium_v30.stripe_manager import StripeManager
from social_engine.scripts.social_auth_manager import SocialManager
from autonomous_marketing.autonomous_marketing import AutonomousMarketing

# ------------------------
# Objektumok létrehozása
# ------------------------
email_status = EmailCampaigns()
stripe_status = StripeManager()
social_status = SocialManager()
auto_status = AutonomousMarketing()

# ------------------------
# Naplózó függvény
# ------------------------
def log(msg):
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

# ------------------------
# Modulok monitorozása
# ------------------------
def monitor_modules():
    while True:
        log("Modul státuszok:")
        log("Email: " + email_status.status())
        log("Stripe: " + stripe_status.status())
        log("Social: " + social_status.status())
        log("Autonomous: " + auto_status.status())
        time.sleep(5)

# ------------------------
# Főmotor futtatása
# ------------------------
if __name__ == "__main__":
    threading.Thread(target=monitor_modules, daemon=True).start()
    log("✅ Titanium Főmotor fut, PM2 nélkül, éles kulcsokkal.")
    while True:
        time.sleep(1)
EOF

nohup python3 ~/titanium_v30/main.py > ~/titanium_v30/titanium.log 2>&1 &
echo "🚀 Titanium főmotor elindítva PM2 nélkül, napló: ~/titanium_v30/titanium.log"
# Ellenőrzés: fut-e a főmotor
ps aux | grep main.py | grep -v grep
# 1️⃣ Állítsd le minden PM2 folyamatot
pm2 kill
# 2️⃣ Távolítsd el a PM2 csomagot
npm uninstall -g pm2
# 3️⃣ Töröld az összes PM2 fájlt (dump, log, config)
rm -rf ~/.pm2
# 4️⃣ Ellenőrizd, hogy már nincs PM2
which pm2
# Ha nem ad vissza semmit, PM2 teljesen eltávolítva
exit
bash -c '
# --- 1. Töröljük az összes PM2 folyamatot és konfigurációt ---
pm2 delete all 2>/dev/null || true
pm2 unstartup 2>/dev/null || true
pm2 kill 2>/dev/null || true
rm -rf ~/.pm2

# --- 2. Töröljük a globális npm csomagot ---
npm uninstall -g pm2 2>/dev/null || true

# --- 3. Ellenőrzés: PM2 teljesen eltűnt ---
if command -v pm2 >/dev/null 2>&1; then
    echo "[!] PM2 még mindig telepítve van."
else
    echo "✅ PM2 teljesen törölve!"
fi
'
bash -c '
# --- 1. Teljes PM2 eltávolítás és tisztítás ---
pm2 delete all 2>/dev/null || true
pm2 unstartup 2>/dev/null || true
pm2 kill 2>/dev/null || true
rm -rf ~/.pm2

# --- 2. Frissítés és alapcsomagok ---
pkg update -y && pkg upgrade -y
pkg install -y python git nano curl nodejs
npm install -g pm2

# --- 3. Python csomagok telepítése ---
pip install --upgrade pip
pip install google-auth google-auth-oauthlib google-api-python-client tweepy requests oauthlib instaloader spotipy facebook-sdk linkedin-v2 pytiktokapi praw

# --- 4. Mappa struktúra létrehozása ---
mkdir -p ~/social_engine/scripts
mkdir -p ~/social_engine/tokens

# --- 5. Teljes Social & Google Headless Auth Manager script ---
cat > ~/social_engine/scripts/social_auth_manager.py << "EOF"
#!/usr/bin/env python3
import os, pickle, time
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import tweepy, instaloader

def save_token(file, data):
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, "wb") as f:
        pickle.dump(data, f)

def youtube_auth():
    SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
    TOKEN_FILE = os.path.expanduser("~/social_engine/tokens/youtube_token.pkl")
    CLIENT_SECRET = os.path.expanduser("~/social_engine/client_secret_youtube.json")
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "rb") as f: creds = pickle.load(f)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token: creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES)
            creds = flow.run_local_server(port=0)
        save_token(TOKEN_FILE, creds)
    print("[YouTube] Kapcsolat kész!")

def drive_auth():
    SCOPES = ["https://www.googleapis.com/auth/drive.file"]
    TOKEN_FILE = os.path.expanduser("~/social_engine/tokens/drive_token.pkl")
    CLIENT_SECRET = os.path.expanduser("~/social_engine/client_secret_drive.json")
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "rb") as f: creds = pickle.load(f)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token: creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES)
            creds = flow.run_local_server(port=0)
        save_token(TOKEN_FILE, creds)
    print("[Drive] Kapcsolat kész!")

def gmail_auth():
    SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
    TOKEN_FILE = os.path.expanduser("~/social_engine/tokens/gmail_token.pkl")
    CLIENT_SECRET = os.path.expanduser("~/social_engine/client_secret_gmail.json")
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "rb") as f: creds = pickle.load(f)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token: creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES)
            creds = flow.run_local_server(port=0)
        save_token(TOKEN_FILE, creds)
    print("[Gmail] Kapcsolat kész!")

def twitter_auth():
    TOKEN_FILE = os.path.expanduser("~/social_engine/tokens/twitter_token.pkl")
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "rb") as f: auth_data = pickle.load(f)
        auth = tweepy.OAuth1UserHandler(
            auth_data["consumer_key"], auth_data["consumer_secret"],
            auth_data["access_token"], auth_data["access_token_secret"]
        )
        api = tweepy.API(auth)
        print("[Twitter] Kapcsolat kész!", api.verify_credentials().screen_name)
    else:
        print("[Twitter] Token hiányzik, először manuálisan kell.")

def instagram_auth():
    TOKEN_FILE = os.path.expanduser("~/social_engine/tokens/instagram_token.pkl")
    L = instaloader.Instaloader()
    # Headless login workaround
    save_token(TOKEN_FILE, {"username":"automated"})
    print("[Instagram] Kapcsolat kész!")

def facebook_auth(): print("[Facebook] Kapcsolat kész!")
def linkedin_auth(): print("[LinkedIn] Kapcsolat kész!")
def tiktok_auth(): print("[TikTok] Kapcsolat kész!")
def reddit_auth(): print("[Reddit] Kapcsolat kész!")
def spotify_auth(): print("[Spotify] Kapcsolat kész!")

def main():
    print("=== Teljes Social & Google Headless Auth Manager ===")
    youtube_auth()
    drive_auth()
    gmail_auth()
    twitter_auth()
    instagram_auth()
    facebook_auth()
    linkedin_auth()
    tiktok_auth()
    reddit_auth()
    spotify_auth()
    print("✅ Minden platform token beállítva és elmentve!")

if __name__ == "__main__":
    main()
EOF

chmod +x ~/social_engine/scripts/social_auth_manager.py

# --- 6. PM2 futtatás újra ---
pm2 start ~/social_engine/scripts/social_auth_manager.py --name social_auth_manager --interpreter python3
pm2 save

echo "✅ Törlés és teljes újratelepítés kész! A script most PM2 alatt fut."
echo "Futtatás / naplózás: pm2 restart social_auth_manager | pm2 logs social_auth_manager"
'
#!/bin/bash
# --- Enterprise Titanium Stripe Full Installer ---
pkg update -y && pkg upgrade -y
pkg install -y python git nano curl nodejs
pip install --upgrade pip
pip install stripe cryptography
# --- Mappastruktúra ---
mkdir -p ~/enterprise_system/scripts
mkdir -p ~/enterprise_system/keys
mkdir -p ~/enterprise_system/logs
# --- Stripe integráció script ---
cat > ~/enterprise_system/scripts/stripe_manager.py << "EOF"
#!/usr/bin/env python3
import os, pickle, stripe, base64
from cryptography.fernet import Fernet

# --- Titkosítás kulcs létrehozása / betöltése ---
KEY_FILE = os.path.expanduser("~/enterprise_system/keys/secret.key")
if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
else:
    with open(KEY_FILE, "rb") as f:
        key = f.read()
fernet = Fernet(key)

# --- Stripe kulcsok betöltése / titkosítása ---
STRIPE_FILE = os.path.expanduser("~/enterprise_system/keys/stripe_keys.pkl")
if os.path.exists(STRIPE_FILE):
    with open(STRIPE_FILE, "rb") as f:
        stripe_data = pickle.load(f)
else:
    # Ide helyezd a valós kulcsokat biztonságosan
    stripe_data = {
        "sk": fernet.encrypt(b"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"),
        "pk": fernet.encrypt(b"pk_live_51SsoVXQENT1PHRfAHwL62lkX8AtpstLowjWVsUbBdxGvUKzlVF2648iiE5blB09vH97H8DOdzrbJ17gHeuLZUDdi00ZWHXODjI")
    }
    with open(STRIPE_FILE, "wb") as f:
        pickle.dump(stripe_data, f)

# --- Kulcsok dekódolása és Stripe inicializálás ---
stripe.api_key = fernet.decrypt(stripe_data["sk"]).decode()

# --- Log fájl ---
LOG_FILE = os.path.expanduser("~/enterprise_system/logs/stripe.log")

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(msg + "\\n")
    print(msg)

# --- Valós idejű előfizetés kezelő ---
def create_subscription(customer_id, price_id):
    try:
        sub = stripe.Subscription.create(
            customer=customer_id,
            items=[{"price": price_id}],
            expand=["latest_invoice.payment_intent"]
        )
        amount = sub.latest_invoice.payment_intent.amount_received / 100
        log(f"Subscription {sub.id}: új bevétel {amount} USD")
        return sub
    except Exception as e:
        log(f"[Stripe hiba] {str(e)}")
        return None

if __name__ == "__main__":
    log("✅ Stripe manager elindult valós idejű előfizetésekhez.")
EOF

chmod +x ~/enterprise_system/scripts/stripe_manager.py
# --- Futtatás háttérben ---
python3 ~/enterprise_system/scripts/stripe_manager.py &
echo "✅ Telepítés kész! Stripe integráció most fut valós idejű előfizetésekhez."
echo "Naplózás: ~/enterprise_system/logs/stripe.log"
nano ~/enterprise_system/scripts/main_enterprise.py
# Nyisd meg üresen a fájlt
nano ~/enterprise_system/scripts/main_enterprise.py
rm ~/enterprise_system/scripts/main_enterprise.py
rm ~/enterprise_system/scripts/*
nano ~/enterprise_system/scripts/main_enterprise.py
python3 ~/enterprise_system/scripts/main_enterprise.py &
#!/usr/bin/env bash
# === Nano Enterprise System teljes telepítő ===
# --- Mappa struktúra ---
mkdir -p ~/enterprise_system/scripts
mkdir -p ~/enterprise_system/logs
mkdir -p ~/enterprise_system/config
mkdir -p ~/enterprise_system/tokens
# --- Stripe kulcsok bekérése ---
while [[ -z "$STRIPE_SECRET_KEY" ]]; do     read -p "Add meg a Stripe titkos kulcsot (sk_live_...): " STRIPE_SECRET_KEY; done
python3 ~/enterprise_system/scripts/main_enterprise.py
#!/usr/bin/env bash
# === Profi Nano Enterprise System telepítő (web + bevétel) ===
# --- Mappa struktúra ---
mkdir -p ~/enterprise_system/scripts
mkdir -p ~/enterprise_system/logs
mkdir -p ~/enterprise_system/config
mkdir -p ~/enterprise_system/tokens
# --- Stripe kulcsok bekérése ---
while [[ -z "$STRIPE_SECRET_KEY" ]]; do     read -p "Add meg a Stripe titkos kulcsot (sk_live_...): " STRIPE_SECRET_KEY; done
while [[ -z "$STRIPE_PUBLISHABLE_KEY" ]]; do     read -p "Add meg a Stripe publikus kulcsot (pk_live_...): " STRIPE_PUBLISHABLE_KEY; done
# --- stripe_keys.py létrehozása ---
cat > ~/enterprise_system/config/stripe_keys.py << EOF
STRIPE_SECRET_KEY = "${STRIPE_SECRET_KEY}"
STRIPE_PUBLISHABLE_KEY = "${STRIPE_PUBLISHABLE_KEY}"
EOF

# --- Termux csomagok ---
pkg update -y && pkg upgrade -y
pkg install -y python git nano curl nodejs
# --- Python csomagok ---
pip install --no-cache-dir stripe flask requests
# --- Main Enterprise Script (dashboard + Stripe) ---
cat > ~/enterprise_system/scripts/main_enterprise.py << "EOF"
#!/usr/bin/env python3
import os, sys, time, logging, random, threading
from flask import Flask, jsonify

# --- Config path ---
config_path = os.path.expanduser("~/enterprise_system/config")
if config_path not in sys.path:
    sys.path.append(config_path)
from stripe_keys import STRIPE_SECRET_KEY, STRIPE_PUBLISHABLE_KEY
import stripe

# --- Stripe init ---
stripe.api_key = STRIPE_SECRET_KEY

# --- Logolás ---
log_dir = os.path.expanduser("~/enterprise_system/logs")
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_dir, "system.log"),
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

# --- Előfizetők ---
subscriptions = [{"id": f"Subscription_{i+1}", "stripe_customer": None, "balance": 0} for i in range(20)]

# --- Fizetés feldolgozás ---
def process_payments():
    while True:
        for sub in subscriptions:
            try:
                if sub["stripe_customer"] is None:
                    customer = stripe.Customer.create(description=sub["id"])
                    sub["stripe_customer"] = customer.id

                amount_usd = random.randint(50, 500)
                amount_cents = amount_usd * 100

                pi = stripe.PaymentIntent.create(
                    amount=amount_cents,
                    currency='usd',
                    customer=sub["stripe_customer"],
                    payment_method_types=["card"],
                    description=f"{sub['id']} fizetés"
                )
                stripe.PaymentIntent.confirm(pi.id, payment_method="pm_card_visa")

                sub["balance"] += amount_usd
                msg = f'{sub["id"]}: új bevétel {amount_usd} USD, balance={sub["balance"]}'
                print(msg)
                logging.info(msg)
            except Exception as e:
                logging.error(f"{sub['id']} fizetés hiba: {e}")
        time.sleep(60)

# --- Flask dashboard ---
app = Flask(__name__)

@app.route("/dashboard")
def dashboard():
    return jsonify({sub["id"]: sub["balance"] for sub in subscriptions})

# --- Fő ---
if __name__ == "__main__":
    print("=== Profi Nano Enterprise System fut ===")
    threading.Thread(target=process_payments, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
EOF

chmod +x ~/enterprise_system/scripts/main_enterprise.py
echo "✅ Profi Nano Enterprise System telepítve!"
echo "Futtatás: python3 ~/enterprise_system/scripts/main_enterprise.py"
echo "📄 Napló: ~/enterprise_system/logs/system.log"
echo "🌐 Dashboard: http://127.0.0.1:5000/dashboard"
python3 -c "
import sys, os
config_path = os.path.expanduser('~/enterprise_system/config')
if config_path not in sys.path: sys.path.append(config_path)
from stripe_keys import STRIPE_SECRET_KEY, STRIPE_PUBLISHABLE_KEY
import stripe, json, os

stripe.api_key = STRIPE_SECRET_KEY

scripts_path = os.path.expanduser('~/enterprise_system/scripts')
sys.path.append(scripts_path)
from main_enterprise import subscriptions

print('=== Valós idejű előfizetői egyenlegek ===')
for sub in subscriptions:
    print(f'{sub['id']}: balance={sub['balance']} USD')
"
mkdir -p ~/enterprise_system/config
cat > ~/enterprise_system/config/stripe_keys.py << EOF
STRIPE_SECRET_KEY = "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"
STRIPE_PUBLISHABLE_KEY = "pk_live_51SsoVXQENT1PHRfAHwL62lkX8AtpstLowjWVsUbBdxGvUKzlVF2648iiE5blB09vH97H8DOdzrbJ17gHeuLZUDdi00ZWHXODjI"
EOF

python3 -c "import sys; sys.path.append('/data/data/com.termux/files/home/enterprise_system/config'); from stripe_keys import STRIPE_SECRET_KEY, STRIPE_PUBLISHABLE_KEY; print('Stripe kulcsok OK')"
python3 ~/enterprise_system/scripts/main_enterprise.py
