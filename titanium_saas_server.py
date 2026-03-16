#!/usr/bin/env python3
import os, threading, subprocess, time, smtplib
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
import stripe, paypalrestsdk, requests
import plotly.graph_objects as go

# .env betöltése
load_dotenv(os.path.expanduser("~/.env"))

# Flask app
app = Flask(__name__)
CORS(app)

# ================= Stripe =================
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY")
stripe.api_key = STRIPE_SECRET_KEY

# ================= PayPal =================
PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID")
PAYPAL_CLIENT_SECRET = os.getenv("PAYPAL_CLIENT_SECRET")
paypalrestsdk.configure({
    "mode": "sandbox",
    "client_id": PAYPAL_CLIENT_ID,
    "client_secret": PAYPAL_CLIENT_SECRET
})

# ================= Gemini / Crypto =================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ================= Fizetési endpointok =================
@app.route("/stripe/create_payment", methods=["POST"])
def stripe_create_payment():
    data = request.json
    amount = data.get("amount", 1000)
    try:
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency="usd",
            payment_method_types=["card"]
        )
        send_email_notification(f"Stripe fizetés létrehozva: {intent.id} (${amount/100})")
        return jsonify({"payment_intent_id": intent.id, "client_secret": intent.client_secret})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/paypal/create_payment", methods=["POST"])
def paypal_create_payment():
    data = request.json
    amount = data.get("amount", "10.00")
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {"payment_method": "paypal"},
        "transactions": [{"amount": {"total": amount, "currency": "USD"}}],
        "redirect_urls": {
            "return_url": "http://localhost:3001/paypal/execute",
            "cancel_url": "http://localhost:3001/paypal/cancel"
        }
    })
    if payment.create():
        send_email_notification(f"PayPal fizetés létrehozva: {payment.id} (${amount})")
        return jsonify({"paymentID": payment.id, "approval_url": payment.links[1].href})
    else:
        return jsonify({"error": payment.error}), 400

@app.route("/crypto/create_payment", methods=["POST"])
def crypto_create_payment():
    return jsonify({"message": "Kripto fizetés modul készen áll"})

# ================= Dashboard =================
@app.route("/dashboard")
def dashboard():
    fig = go.Figure(go.Bar(x=["Stripe","PayPal","Crypto"], y=[10,5,2]))
    return fig.to_html()

# ================= Email értesítés =================
def send_email_notification(message):
    try:
        import smtplib
        EMAIL_SMTP_SERVER = os.getenv("EMAIL_SMTP_SERVER")
        EMAIL_SMTP_PORT = int(os.getenv("EMAIL_SMTP_PORT",587))
        EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
        EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
        server = smtplib.SMTP(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)
        server.quit()
    except:
        pass

# ================= Flask futtatás =================
def run_flask():
    app.run(host="127.0.0.1", port=3001)

# ================= LocalTunnel / Ngrok =================
def run_tunnel():
    time.sleep(3)
    try:
        proc = subprocess.Popen(["lt", "--port", "3001", "--print-requests"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in iter(proc.stdout.readline, b''):
            line = line.decode()
            if "https://" in line:
                url = line.split()[0]
                print(f"\n📡 Publikus URL: {url}\n")
                break
    except Exception as e:
        print(f"Tunnel hiba: {e}")

# ================= Szálak =================
threading.Thread(target=run_flask, daemon=True).start()
threading.Thread(target=run_tunnel, daemon=True).start()

while True:
    time.sleep(1)
