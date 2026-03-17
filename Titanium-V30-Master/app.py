import bhast
import os
from flask import Flask
from titanium_modules import AIServices
from marketing_engine import NeuralMarketing
from quantum_core import QuantumCore

# --- KONFIGURÁCIÓ ---
TELEGRAM_TOKEN = "8425805311:AAFG_Y4vLl2r6SlJeuBsRFTa_bHDXTI54r4"
STRIPE_KEY = "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"

bhast.initialize()
server = bhast.Server(host='0.0.0.0', port=7860)
ai = AIServices(STRIPE_KEY)
marketing = NeuralMarketing()
quantum = QuantumCore()

@server.route("/")
def index():
    prediction = quantum.predict_market()
    services = ai.get_service_list()
    
    service_html = "".join([f'<div class="data-row"><span>{s}:</span><span class="value">QUANTUM ACTIVE</span></div>' for s in services[:12]])
    
    return f"""
    <html>
    <head>
        <style>
            body {{ background: #000; color: #00ff41; font-family: 'Courier New', monospace; text-align: center; padding: 20px; overflow-x: hidden; }}
            .empire-container {{ border: 5px double #00ff41; background: radial-gradient(circle, #001100 0%, #000 100%); padding: 40px; margin: auto; width: 95%; max-width: 1200px; box-shadow: 0 0 100px #00ff41; }}
            .quantum-header {{ font-size: 3.5em; font-weight: 900; letter-spacing: 15px; text-shadow: 0 0 20px #00ff41; margin: 0; }}
            .status-grid {{ display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 20px; margin-top: 30px; }}
            .stat-card {{ border: 1px solid #00ff41; padding: 15px; background: rgba(0,255,65,0.1); }}
            .prediction-bar {{ background: #00ff41; color: #000; font-weight: bold; padding: 10px; margin: 20px 0; font-size: 1.2em; }}
            .data-row {{ border-bottom: 1px solid #111; padding: 5px 0; display: flex; justify-content: space-between; font-size: 0.8em; }}
            .value {{ color: #fff; }}
            .glow {{ animation: g 2s infinite; }}
            @keyframes g {{ 0%{{text-shadow: 0 0 5px #00ff41;}} 50%{{text-shadow: 0 0 30px #00ff41;}} 100%{{text-shadow: 0 0 5px #00ff41;}} }}
        </style>
    </head>
    <body>
        <div class="empire-container">
            <h1 class="quantum-header glow">TITANIUM SINGULARITY</h1>
            <p style="letter-spacing: 5px;">V7.0 GLOBAL DOMINANCE LAYER</p>
            <div class="prediction-bar">{prediction}</div>
            <div class="status-grid">
                <div class="stat-card"><span>LIQUIDITY</span><br><b style="color:#fff;">MAXIMUM</b></div>
                <div class="stat-card"><span>ARBITRAGE</span><br><b style="color:#fff;">ACTIVE</b></div>
                <div class="stat-card"><span>NODES</span><br><b style="color:#fff;">1000+ VIRTUAL</b></div>
                <div class="stat-card"><span>UPTIME</span><br><b style="color:#fff;">INFINITY</b></div>
            </div>
            <hr style="border: 0.5px solid #00ff41; margin: 30px 0;">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; text-align: left;">
                <div>{service_html}</div>
                <div style="border-left: 1px solid #00ff41; padding-left: 20px;">
                    <p><b>[NEURAL ADAPTATION]:</b> Optimal</p>
                    <p><b>[REVOLUT ENDPOINT]:</b> Secure</p>
                    <p><b>[STRIPE GATEWAY]:</b> 100% Operational</p>
                    <p style="color: #ff9900;"><b>[ALERT]:</b> Opportunity detected in APAC market.</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    server.run()
