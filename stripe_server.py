#!/usr/bin/env python3
import os, threading, subprocess, time
from dotenv import load_dotenv
from flask import Flask, jsonify
import stripe

load_dotenv(os.path.expanduser("~/.env"))
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY")

stripe.api_key = STRIPE_SECRET_KEY
app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Stripe él", "publishable_key": STRIPE_PUBLISHABLE_KEY})

@app.route("/create_payment_intent", methods=["POST"])
def create_payment_intent():
    try:
        intent = stripe.PaymentIntent.create(amount=1000, currency="usd", payment_method_types=["card"])
        return jsonify({"payment_intent_id": intent.id, "client_secret": intent.client_secret})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def run_flask():
    app.run(host="127.0.0.1", port=3001)

def run_localtunnel():
    time.sleep(3)
    proc = subprocess.Popen(["lt", "--port", "3001", "--print-requests"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in iter(proc.stdout.readline, b''):
        line = line.decode()
        if "https://" in line:
            url = line.split()[0]
            print(f"\n📡 Publikus URL: {url}\n")
            break

threading.Thread(target=run_flask, daemon=True).start()
threading.Thread(target=run_localtunnel, daemon=True).start()

while True:
    time.sleep(1)
