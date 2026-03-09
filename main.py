import os
import stripe
import requests
from dotenv import load_dotenv

# Környezeti változók betöltése
load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram(message):
    if TELEGRAM_TOKEN and TELEGRAM_CHAT_ID:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message})

def check_and_payout():
    try:
        # Egyenleg ellenőrzése
        balance = stripe.Balance.retrieve()
        available = balance['available'][0]['amount'] / 100
        currency = balance['available'][0]['currency'].upper()
        
        status_msg = f"💎 TITANIUM STATUS: Egyenleg ellenőrizve: {available} {currency}"
        print(status_msg)
        
        # Ha van kifizethető összeg (pl. több mint 10 USD/EUR)
        if available > 10:
            send_telegram(f"🚀 Titanium Kifizetés Indítása: {available} {currency} -> Revolut")
            # Itt történik az automatikus kiutalás a Stripe alapértelmezett számlájára
            stripe.Payout.create(
                amount=int(available * 100),
                currency=currency.lower(),
            )
            send_telegram("✅ Tranzakció sikeres! Az összeg IN-TRANSIT státuszba került.")
        else:
            send_telegram(status_msg + " (Várakozás a küszöbértékre...)")

    except Exception as e:
        error_msg = f"⚠️ TITANIUM ERROR: {str(e)}"
        print(error_msg)
        send_telegram(error_msg)

if __name__ == "__main__":
    check_and_payout()
