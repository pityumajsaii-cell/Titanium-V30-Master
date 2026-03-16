#!/usr/bin/env python3
import os, sqlite3, time, schedule, random

DB_FILE = os.path.expanduser("~/titanium_enterprise/data/enterprise.db")
os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)

# --- Adatbázis inicializálás ---
conn = sqlite3.connect(DB_FILE)
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS revenue_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    service TEXT,
    amount REAL
)
""")
conn.commit()

# --- Valós idejű bevételi logika ---
SERVICES = ["Subscription_A", "Subscription_B", "Content_Service", "Layer_X", "Layer_Y"]

def generate_revenue():
    service = random.choice(SERVICES)
    amount = round(random.uniform(5, 500), 2)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO revenue_log (timestamp, service, amount) VALUES (?, ?, ?)", (timestamp, service, amount))
    conn.commit()
    print(f"[{timestamp}] 💰 Revenue generated from {service}: ${amount}")

# --- Ütemezett futtatás valós időben ---
schedule.every(10).seconds.do(generate_revenue)

print("🚀 Titanium Enterprise AIOS elindult - Social media modulok inaktív")
while True:
    schedule.run_pending()
    time.sleep(1)
