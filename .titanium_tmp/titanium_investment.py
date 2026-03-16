#!/usr/bin/env python3
import os, time, random, threading, requests
from dotenv import load_dotenv

load_dotenv(os.path.expanduser("~/.titanium_env"))

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
INVESTOR_SHARE = 0.25

def notify(msg):
    try:
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            data={"chat_id": TELEGRAM_CHAT_ID, "text": msg}
        )
    except:
        pass

def get_revenue():
    return round(random.uniform(100, 500), 2)

def pay_investor(amount):
    investor_amount = round(amount * INVESTOR_SHARE, 2)
    notify(f"💸 Automatikus kifizetés befektetőnek: ${investor_amount}")

def revenue_monitor():
    while True:
        revenue = get_revenue()
        notify(f"📈 Titanium V30 új bevétel: ${revenue}")
        if revenue >= 100:
            pay_investor(revenue)
        time.sleep(60)

if __name__ == "__main__":
    notify("🚀 Titanium V30 Investment Manager elindult!")
    threading.Thread(target=revenue_monitor, daemon=True).start()
    while True:
        time.sleep(60)
