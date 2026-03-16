#!/usr/bin/env python3
import os, sys, time, logging, random, threading, json, smtplib
from email.mime.text import MIMEText
from flask import Flask

# --- Config ---
config_path = os.path.expanduser("~/enterprise_system/config")
if config_path not in sys.path:
    sys.path.append(config_path)
from stripe_keys import STRIPE_SECRET_KEY, STRIPE_PUBLISHABLE_KEY, STRIPE_BUY_LINK
import stripe
stripe.api_key = STRIPE_SECRET_KEY

# --- Logging ---
log_dir = os.path.expanduser("~/enterprise_system/logs")
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_dir, "system.log"),
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s"
)

# --- Subscriptions ---
subs_file = os.path.expanduser("~/enterprise_system/backup/subscriptions.json")
if os.path.exists(subs_file):
    with open(subs_file,"r") as f:
        subscriptions = json.load(f)
else:
    subscriptions = [{"id": f"Subscription_{i+1}", "stripe_customer": None, "balance": 0} for i in range(20)]

# --- Payment processing ---
def process_payments():
    while True:
        for sub in subscriptions:
            try:
                if sub["stripe_customer"] is None:
                    customer = stripe.Customer.create(description=sub["id"])
                    sub["stripe_customer"] = customer.id

                pm = "pm_card_visa" if STRIPE_SECRET_KEY.startswith("sk_test") else None
                amount_usd = random.randint(50, 500)
                amount_cents = amount_usd * 100

                pi = stripe.PaymentIntent.create(
                    amount=amount_cents,
                    currency='usd',
                    customer=sub["stripe_customer"],
                    payment_method_types=["card"],
                    description=f"{sub['id']} fizetés"
                )
                if pm:
                    stripe.PaymentIntent.confirm(pi.id, payment_method=pm)

                sub["balance"] += amount_usd
                msg = f'{sub["id"]}: új bevétel {amount_usd} USD, balance={sub["balance"]}'
                print(msg)
                logging.info(msg)
                send_email_notification(sub["id"], amount_usd)

            except Exception as e:
                logging.error(f"{sub['id']} fizetés hiba: {e}")

        with open(subs_file,"w") as f:
            json.dump(subscriptions,f)
        time.sleep(60)

# --- Email értesítés ---
def send_email_notification(sub_id, amount):
    try:
        EMAIL_USER = os.environ.get("EMAIL_USER")
        EMAIL_PASS = os.environ.get("EMAIL_PASS")
        msg = MIMEText(f"Új bevétel: {sub_id} → {amount} USD")
        msg['Subject'] = "Profi Nano Enterprise új bevétel"
        msg['From'] = EMAIL_USER
        msg['To'] = EMAIL_USER
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        logging.error(f"Email hiba: {e}")

# --- Flask dashboard ---
app = Flask(__name__)
REVOLUT_LINK = os.environ.get("REVOLUT_LINK")
REVOLUT_IBAN = os.environ.get("REVOLUT_IBAN")
REVOLUT_BIC = os.environ.get("REVOLUT_BIC")
REVOLUT_BANK = os.environ.get("REVOLUT_BANK")
ACCOUNT_NAME = os.environ.get("ACCOUNT_NAME")

@app.route("/dashboard")
def dashboard():
    html = "<h2>Profi Nano Enterprise Dashboard</h2>"
    html += "<ul>"
    for sub in subscriptions:
        html += f"<li>{sub['id']}: {sub['balance']} USD</li>"
    html += "</ul>"
    html += f'<p><strong>Stripe buy link:</strong> <a href="{STRIPE_BUY_LINK}" target="_blank">💳 Fizetés link</a></p>'
    html += f'<p><strong>Revolut fizetés:</strong> <a href="{REVOLUT_LINK}" target="_blank">💳 Fizetés link</a></p>'
    html += f"<p><strong>IBAN:</strong> {REVOLUT_IBAN} | <strong>BIC:</strong> {REVOLUT_BIC} | <strong>Bank:</strong> {REVOLUT_BANK} | <strong>Név:</strong> {ACCOUNT_NAME}</p>"
    return html

# --- Server start ---
if __name__ == "__main__":
    print("=== Profi Nano Enterprise + Stripe & Revolut + AI fut ===")
    threading.Thread(target=process_payments, daemon=True).start()

    port = 5000
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("0.0.0.0", port))
    except OSError:
        port = 5001
        print(f"Port 5000 foglalt, váltás port {port}-ra")
    s.close()
    app.run(host="0.0.0.0", port=port)
