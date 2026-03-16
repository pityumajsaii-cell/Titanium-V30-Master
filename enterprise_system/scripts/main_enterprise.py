#!/usr/bin/env python3
import os, sys, time, logging, random, threading, json

# --- Config path ---
config_path = os.path.expanduser("~/enterprise_system/config")
if config_path not in sys.path:
    sys.path.append(config_path)
from stripe_keys import STRIPE_SECRET_KEY, STRIPE_PUBLISHABLE_KEY
import stripe
from flask import Flask, jsonify

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
subscriptions_file = os.path.expanduser("~/enterprise_system/backup/subscriptions.json")
if os.path.exists(subscriptions_file):
    with open(subscriptions_file,"r") as f:
        subscriptions = json.load(f)
else:
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
        # --- Mentés ---
        with open(subscriptions_file,"w") as f:
            json.dump(subscriptions,f)
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
