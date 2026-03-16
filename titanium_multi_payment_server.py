#!/usr/bin/env python3
import os, threading, subprocess, time
from dotenv import load_dotenv
from flask import Flask, jsonify, request
import stripe, paypalrestsdk, requests

# .env betöltése
load_dotenv(os.path.expanduser("~/.env"))

# Flask app
app = Flask(__name__)

# ================== STRIPE ==================
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY")
stripe.api_key = STRIPE_SECRET_KEY

# ================== PAYPAL ==================
PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID")
PAYPAL_CLIENT_SECRET = os.getenv("PAYPAL_CLIENT_SECRET")
paypalrestsdk.configure({
    "mode": "sandbox",
    "client_id": PAYPAL_CLIENT_ID,
    "client_secret": PAYPAL_CLIENT_SECRET
})

# ================== GEMINI / CRYPTO ==================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ================== ENDPOINTOK ==================

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
        return jsonify({"paymentID": payment.id, "approval_url": payment.links[1].href})
    else:
        return jsonify({"error": payment.error}), 400

@app.route("/crypto/create_payment", methods=["POST"])
def crypto_create_payment():
    return jsonify({"message": "Kripto fizetés modul készen áll"})

@app.route("/")
def index():
    return jsonify({"message": "Titanium V30 Multi-Payment rendszer él", "stripe_key": STRIPE_PUBLISHABLE_KEY})

# Flask futtatás
def run_flask():
    app.run(host="127.0.0.1", port=3001)

# LocalTunnel futtatás
def run_localtunnel():
    time.sleep(3)
    proc = subprocess.Popen(["lt", "--port", "3001", "--print-requests"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in iter(proc.stdout.readline, b''):
        line = line.decode()
        if "https://" in line:
            url = line.split()[0]
            print(f"\n📡 Publikus URL: {url}\n")
            break

# Szálak indítása
threading.Thread(target=run_flask, daemon=True).start()
threading.Thread(target=run_localtunnel, daemon=True).start()

while True:
    time.sleep(1)
