import bhast
import os
from flask import Flask
from titanium_modules import AIServices
from marketing_engine import NeuralMarketing

# --- KONFIGURÁCIÓ ---
TELEGRAM_TOKEN = "8425805311:AAFG_Y4vLl2r6SlJeuBsRFTa_bHDXTI54r4"
STRIPE_KEY = "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"

bhast.initialize()
server = bhast.Server(host='0.0.0.0', port=7860)
ai = AIServices(STRIPE_KEY)
marketing = NeuralMarketing()

@server.route("/")
def index():
    services = ai.get_service_list()
    # Szimulált tanulási adat a dashboardhoz
    best_campaign = marketing.optimize_campaigns({"Legal_AI": 50, "Enterprise_ERP": 120})[0][0]
    auto_ad = marketing.generate_auto_ad(best_campaign)

    service_html = "".join([f'<div class="data-row"><span>{s}:</span><span class="value">AI OPTIMIZED</span></div>' for s in services])
    
    return f"""
    <html>
    <head>
        <style>
            body {{ background: #000; color: #00ff41; font-family: 'Courier New', monospace; text-align: center; padding: 20px; }}
            .enterprise-box {{ border: 2px dashed #00ff41; background: rgba(0,20,0,0.8); padding: 30px; margin: auto; width: 95%; max-width: 1100px; box-shadow: 0 0 40px #00ff41; }}
            .header {{ font-size: 2.8em; color: #fff; text-shadow: 0 0 15px #00ff41; }}
            .ad-scanner {{ background: #111; border: 1px solid #444; padding: 15px; margin: 20px 0; font-style: italic; color: #ff9900; }}
            .grid {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; text-align: left; }}
            .data-row {{ border-bottom: 1px solid #222; padding: 8px 0; display: flex; justify-content: space-between; }}
            .value {{ color: #000; background: #00ff41; padding: 0 10px; border-radius: 3px; }}
            .brain-status {{ font-weight: bold; color: #00d4ff; text-transform: uppercase; margin-bottom: 10px; }}
        </style>
    </head>
    <body>
        <div class="enterprise-box">
            <h1 class="header">TITANIUM NEURAL EMPIRE</h1>
            <div class="brain-status">🧠 AI MARKETING ENGINE: LEARNING MODE ACTIVE</div>
            <div class="ad-scanner">
                [AUTO-GENERATED AD]: "{auto_ad}"
            </div>
            <div class="grid">{service_html}</div>
            <hr style="border: 0.5px solid #222; margin-top: 20px;">
            <p style="font-size: 0.8em; color: #666;">
                NEURAL CORE v6.0 | OPERATOR: Majsai István | STRIPE: LIVE | REVOLUT: LT81...
            </p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    server.run()
