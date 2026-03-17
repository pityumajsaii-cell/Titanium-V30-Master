import bhast
import os
from flask import Flask
from titanium_modules import AIServices
from marketing_engine import NeuralMarketing
from quantum_core import QuantumCore
from galactic_core import GalacticScale

# --- KONFIGURÁCIÓ ---
TELEGRAM_TOKEN = "8425805311:AAFG_Y4vLl2r6SlJeuBsRFTa_bHDXTI54r4"
STRIPE_KEY = "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"

bhast.initialize()
server = bhast.Server(host='0.0.0.0', port=7860)
ai = AIServices(STRIPE_KEY)
marketing = NeuralMarketing()
quantum = QuantumCore()
galactic = GalacticScale()

@server.route("/")
def index():
    market = galactic.get_market_focus()
    healing = galactic.self_healing_check()
    services = ai.get_service_list()
    
    return f"""
    <html>
    <head>
        <style>
            body {{ background: #000; color: #00ff41; font-family: 'Segoe UI', monospace; text-align: center; margin: 0; padding: 0; }}
            .galactic-frame {{ border: 10px solid #111; background: linear-gradient(180deg, #000 0%, #001a00 100%); min-height: 100vh; padding: 40px; }}
            .title {{ font-size: 4em; font-weight: bold; color: #fff; letter-spacing: 20px; text-shadow: 0 0 30px #00ff41; }}
            .market-banner {{ background: #00ff41; color: #000; padding: 15px; font-weight: bold; margin: 20px auto; width: 80%; }}
            .core-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 40px; }}
            .core-card {{ border: 1px solid #00ff41; padding: 20px; background: rgba(0,0,0,0.5); box-shadow: inset 0 0 20px #004400; }}
            .status-led {{ height: 10px; width: 10px; background: #00ff41; border-radius: 50%; display: inline-block; margin-right: 10px; box-shadow: 0 0 10px #00ff41; }}
            .footer {{ position: fixed; bottom: 10px; width: 100%; font-size: 0.7em; color: #333; }}
        </style>
    </head>
    <body>
        <div class="galactic-frame">
            <h1 class="title">TITANIUM GALACTIC</h1>
            <div class="market-banner">{market}</div>
            <div class="core-grid">
                <div class="core-card"><h3>SCALABILITY</h3><p>DYNAMIC CLOUD ACTIVE</p></div>
                <div class="core-card"><h3>INTEGRITY</h3><p>{healing}</p></div>
                <div class="core-card"><h3>DIVERSIFICATION</h3><p>MULTI-ASSET READY</p></div>
            </div>
            <hr style="border: 0.5px solid #222; margin: 50px 0;">
            <div style="text-align: left; padding: 0 10%; display: grid; grid-template-columns: 1fr 1fr; gap: 50px;">
                <div>
                    <h2 style="color:#fff;"><span class="status-led"></span>AI REVENUE AGENTS</h2>
                    <p>Executing high-frequency enterprise billing...</p>
                    <p>Stripe Status: <b>LIVE - UNLIMITED</b></p>
                </div>
                <div style="border-left: 1px solid #333; padding-left: 30px;">
                    <h2 style="color:#fff;"><span class="status-led"></span>QUANTUM PREDICTION</h2>
                    <p>Next Growth Spike: <b>APAC FINANCIAL SECTOR</b></p>
                    <p>Current Payout Path: <b>Revolut LT81...</b></p>
                </div>
            </div>
        </div>
        <div class="footer">OPERATOR: MAJSAI ISTVÁN | SYSTEM: TITANIUM EMPIRE v8.0</div>
    </body>
    </html>
    """

if __name__ == "__main__":
    server.run()
