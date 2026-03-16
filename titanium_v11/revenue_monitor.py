import os
import time
import requests

LOCK_FILE = os.path.join(os.getenv("HOME"), "titanium_v11", "revenue_monitor.lock")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
STRIPE_KEY = os.getenv("STRIPE_SECRET_KEY")
REVOLUT_TOKEN = os.getenv("REVOLUT_API_TOKEN")
REVOLUT_LAST_ID_FILE = os.path.join(os.getenv("HOME"), "titanium_v11", "revolut_last_id.txt")
CHECK_INTERVAL = 300

def telegram_notify(msg):
    if TELEGRAM_TOKEN and TELEGRAM_CHAT_ID:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": msg})

def check_stripe_payments():
    try:
        import stripe
        stripe.api_key = STRIPE_KEY
        payments = stripe.PaymentIntent.list(limit=5)
        for p in payments.data:
            if p.status == 'succeeded':
                telegram_notify(f"💰 Stripe fizetés: {p.amount/100:.2f} {p.currency.upper()}")
    except Exception as e:
        telegram_notify(f"⚠️ Stripe error: {e}")

def check_revolut_payout():
    if not REVOLUT_TOKEN:
        return
    headers = {"Authorization": f"Bearer {REVOLUT_TOKEN}"}
    url = "https://b2b.revolut.com/api/1.0/payouts"
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        payouts = resp.json().get("payouts", [])

        last_id = None
        if os.path.exists(REVOLUT_LAST_ID_FILE):
            with open(REVOLUT_LAST_ID_FILE, "r") as f:
                last_id = f.read().strip()

        new_last_id = last_id
        for payout in sorted(payouts, key=lambda x: x["created_at"]):
            pid = payout["id"]
            amount = float(payout["amount"])
            currency = payout["currency"]
            if last_id is None or pid > last_id:
                telegram_notify(f"💵 Revolut payout: {amount:.2f} {currency}")
                new_last_id = pid

        if new_last_id != last_id:
            with open(REVOLUT_LAST_ID_FILE, "w") as f:
                f.write(new_last_id)
    except Exception as e:
        telegram_notify(f"⚠️ Revolut error: {e}")

if __name__ == "__main__":
    if not os.path.exists(LOCK_FILE):
        telegram_notify("🚀 Revenue monitor elindult!")
        with open(LOCK_FILE, "w") as f:
            f.write("started")

    while True:
        check_stripe_payments()
        check_revolut_payout()
        time.sleep(CHECK_INTERVAL)
