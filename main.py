import os
import stripe
import requests
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram(message):
    if TELEGRAM_TOKEN and TELEGRAM_CHAT_ID:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        try:
            requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message})
        except Exception as e:
            print(f"Telegram error: {e}")

def check_and_payout():
    try:
        balance = stripe.Balance.retrieve()
        available = balance['available'][0]['amount'] / 100
        currency = balance['available'][0]['currency'].upper()
        
        status_msg = f"💎 TITANIUM STATUS: Egyenleg: {available} {currency}"
        print(status_msg)
        send_telegram(status_msg)
        
        if available >= 50:
            send_telegram(f"🚀 Kifizetés indítása: {available} {currency}")
            stripe.Payout.create(
                amount=int(available * 100),
                currency=currency.lower(),
            )
            send_telegram("✅ Sikeres kifizetés!")
    except Exception as e:
        print(f"Hiba: {e}")
        send_telegram(f"⚠️ Hiba: {e}")

if __name__ == "__main__":
    check_and_payout()
