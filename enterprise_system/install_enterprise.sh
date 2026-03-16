#!/usr/bin/env bash
echo "=== Profi Nano AI SaaS Enterprise telepítés ==="

# --- Mappa létrehozás ---
mkdir -p ~/enterprise_system/{scripts,logs,config,backup}

# --- Csomagok ---
pkg update -y
pkg install python git curl nano -y
pip install --no-cache-dir flask stripe requests openai

# --- Stripe kulcs bekérés ---
read -p "Add meg a Stripe SECRET KEY (sk_live...): " STRIPE_SECRET_KEY
read -p "Add meg a Stripe PUBLISHABLE KEY (pk_live...): " STRIPE_PUBLISHABLE_KEY

cat > ~/enterprise_system/config/stripe_keys.py << EOF
STRIPE_SECRET_KEY = "${STRIPE_SECRET_KEY}"
STRIPE_PUBLISHABLE_KEY = "${STRIPE_PUBLISHABLE_KEY}"
EOF

echo "✅ Stripe kulcsok elmentve."

# --- Server script ---
cat > ~/enterprise_system/scripts/server.py << "EOF"
#!/usr/bin/env python3
import os, stripe
from flask import Flask, redirect, jsonify
from stripe_keys import STRIPE_SECRET_KEY, STRIPE_PUBLISHABLE_KEY

stripe.api_key = STRIPE_SECRET_KEY
app = Flask(__name__)

# --- Subscription dashboard ---
subscriptions = {}

@app.route("/")
def home():
    return "<h2>AI SaaS Enterprise</h2><a href='/buy'>Subscribe $5</a>"

@app.route("/buy")
def buy():
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="payment",
        line_items=[{
            "price_data":{
                "currency":"usd",
                "product_data":{"name":"AI Enterprise Service"},
                "unit_amount":500
            },
            "quantity":1
        }],
        success_url="http://localhost:5000/success",
        cancel_url="http://localhost:5000/cancel"
    )
    return redirect(session.url)

@app.route("/success")
def success():
    return "Payment successful! Welcome to AI Enterprise."

@app.route("/cancel")
def cancel():
    return "Payment cancelled."

@app.route("/dashboard")
def dashboard():
    return jsonify(subscriptions)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
EOF

chmod +x ~/enterprise_system/scripts/server.py

# --- Termux boot indítás ---
mkdir -p ~/.termux/boot
cat > ~/.termux/boot/start.sh << EOF
#!/usr/bin/env bash
python3 ~/enterprise_system/scripts/server.py &
EOF
chmod +x ~/.termux/boot/start.sh

echo "✅ Telepítés kész! Indíthatod a rendszert:"
echo "bash ~/enterprise_system/scripts/server.py"
