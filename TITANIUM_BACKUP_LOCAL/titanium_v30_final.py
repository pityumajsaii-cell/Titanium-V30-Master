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
