import bhast
import os
from flask import Flask
from titanium_modules import AIServices
from marketing_engine import NeuralMarketing
from quantum_core import QuantumCore
from galactic_core import GalacticScale
from realtime_engine import RealTimeEngine

# --- KONFIGURÁCIÓ ---
TELEGRAM_TOKEN = "8425805311:AAFG_Y4vLl2r6SlJeuBsRFTa_bHDXTI54r4"
STRIPE_KEY = "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"

bhast.initialize()
server = bhast.Server(host='0.0.0.0', port=7860)
ai = AIServices(STRIPE_KEY)
marketing = NeuralMarketing()
quantum = QuantumCore()
galactic = GalacticScale()
rt = RealTimeEngine()

@server.route("/")
def index():
    live_signal = rt.fetch_live_signals()
    perf = rt.optimize_performance()
    market = galactic.get_market_focus()
    
    return f"""
    <html>
    <head>
        <style>
            body {{ background: #000; color: #00ff41; font-family: 'Courier New', monospace; padding: 0; margin: 0; }}
            .realtime-header {{ background: #00ff41; color: #000; padding: 10px; font-weight: bold; letter-spacing: 5px; text-align: center; }}
            .main-frame {{ border: 2px solid #00ff41; margin: 20px; padding: 30px; box-shadow: 0 0 50px rgba(0,255,65,0.2); min-height: 80vh; }}
            .signal-box {{ border: 1px solid #ff9900; color: #ff9900; padding: 15px; margin-bottom: 20px; font-size: 1.1em; }}
            .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 30px; text-align: left; }}
            .stat-label {{ color: #888; font-size: 0.8em; text-transform: uppercase; }}
            .stat-value {{ color: #fff; font-size: 1.2em; border-bottom: 1px solid #222; margin-bottom: 10px; padding-bottom: 5px; }}
            .pulse {{ animation: p 1s infinite; }}
            @keyframes p {{ 0%{{opacity:1;}} 50%{{opacity:0.5;}} 100%{{opacity:1;}} }}
        </style>
    </head>
    <body>
        <div class="realtime-header">TITANIUM REAL-TIME APEX v9.0</div>
        <div class="main-frame">
            <div class="signal-box">
                <span class="pulse">●</span> {live_signal}
            </div>
            <div class="grid">
                <div>
                    <div class="stat-label">System Performance</div>
                    <div class="stat-value">{perf}</div>
                    <div class="stat-label">Market Focus</div>
                    <div class="stat-value">{market}</div>
                    <div class="stat-label">Operator Status</div>
                    <div class="stat-value">Majsai István (Titanium) - AUTHORIZED</div>
                </div>
                <div style="border-left: 1px solid #333; padding-left: 30px;">
                    <div class="stat-label">Active Payout Route</div>
                    <div class="stat-value">Revolut LT81 3250...</div>
                    <div class="stat-label">Financial Gateway</div>
                    <div class="stat-value">Stripe Live (Active)</div>
                    <div class="stat-label">Neural Status</div>
                    <div class="stat-value" style="color:#00ff41;">AUTONOMOUS GROWTH</div>
                </div>
            </div>
            <p style="margin-top: 40px; color: #444; font-size: 0.7em;">BHAST ENGINE v4.3 | CLOSED-LOOP INFRASTRUCTURE | QUANTUM-RESISTANT</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    server.run()
