#!/usr/bin/env python3
import os
import time
import pickle
import logging
from apscheduler.schedulers.background import BackgroundScheduler
import pandas as pd
import numpy as np
from flask import Flask, jsonify

STATE_FILE = os.path.expanduser("~/enterprise_aios/state/system_state.pkl")

# --- Logger ---
log_file = os.path.expanduser("~/enterprise_aios/logs/system.log")
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# --- Valós idejű üzleti modul ---
class RevenueModule:
    def __init__(self, name, total_revenue=0):
        self.name = name
        self.total_revenue = total_revenue

    def generate_revenue(self):
        new_revenue = np.random.randint(100,500)
        self.total_revenue += new_revenue
        logging.info(f"[{self.name}] Bevétel generálva: {new_revenue}, Összes: {self.total_revenue}")
        save_state()

# --- Állapot mentés és visszatöltés ---
def save_state():
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    pickle.dump(modules, open(STATE_FILE, "wb"))

def load_state():
    if os.path.exists(STATE_FILE):
        return pickle.load(open(STATE_FILE, "rb"))
    return [RevenueModule(f"Module_{i+1}") for i in range(100)]  # 100 modul

# --- Modulok betöltése ---
modules = load_state()

# --- Ütemezett futtatás ---
scheduler = BackgroundScheduler()
for m in modules:
    scheduler.add_job(m.generate_revenue, "interval", seconds=10)
scheduler.start()

# --- Flask Dashboard ---
app = Flask(__name__)

@app.route("/dashboard")
def dashboard():
    data = {m.name: m.total_revenue for m in modules}
    return jsonify(data)

# --- Main ---
def main():
    logging.info("=== Enterprise AIOS Maximalizált Rendszer elindult ===")
    print("Enterprise AIOS Maximalizált Rendszer elindult!")
    print("Dashboard: http://127.0.0.1:5000/dashboard")
    app.run(port=5000)

if __name__ == "__main__":
    main()
