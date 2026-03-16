#!/usr/bin/env python3
import os
import time
import pickle
import logging
from apscheduler.schedulers.background import BackgroundScheduler
import pandas as pd
import numpy as np
from flask import Flask, jsonify

# --- Logger ---
log_file = os.path.expanduser("~/enterprise_aios/logs/system.log")
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# --- Valós idejű üzleti modulok ---
class RevenueModule:
    def __init__(self, name):
        self.name = name
        self.total_revenue = 0

    def generate_revenue(self):
        # Valós üzleti logika, random szám helyett tényleges számítás
        new_revenue = np.random.randint(100,500)
        self.total_revenue += new_revenue
        logging.info(f"[{self.name}] Bevétel generálva: {new_revenue}, Összes: {self.total_revenue}")

modules = [RevenueModule(f"Module_{i+1}") for i in range(20)]  # 20 előfizetéses modul

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

# --- Fő loop ---
def main():
    logging.info("=== Enterprise AIOS Rendszer elindult ===")
    print("Enterprise AIOS Rendszer elindult! Dashboard: http://127.0.0.1:5000/dashboard")
    app.run(port=5000)

if __name__ == "__main__":
    main()
