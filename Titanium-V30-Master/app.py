import bhast
import os
from flask import Flask, request, jsonify
from titanium_modules import AIServices

# --- KONFIGURÁCIÓ ---
TELEGRAM_TOKEN = "8425805311:AAFG_Y4vLl2r6SlJeuBsRFTa_bHDXTI54r4"
STRIPE_KEY = "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"

bhast.initialize()
server = bhast.Server(host='0.0.0.0', port=7860)
ai = AIServices(STRIPE_KEY)

@server.route("/")
def index():
    services = ai.get_service_list()
    service_html = "".join([f'<div class="data-row"><span>{s}:</span><span class="value">ACTIVE & BILLABLE</span></div>' for s in services])
    
    return f"""
    <html>
    <head>
        <style>
            body {{ background: #000; color: #00ff41; font-family: 'Courier New', monospace; text-align: center; padding: 20px; }}
            .enterprise-box {{ border: 2px solid #00ff41; background: rgba(0,255,65,0.05); padding: 30px; margin: auto; width: 95%; max-width: 1000px; box-shadow: 0 0 50px #004400; }}
            .header {{ font-size: 2.5em; letter-spacing: 10px; color: #fff; text-shadow: 0 0 20px #00ff41; margin-bottom: 5px; }}
            .sub-header {{ color: #00ff41; font-size: 1.2em; margin-bottom: 20px; border-bottom: 1px solid #00ff41; display: inline-block; padding: 0 20px; }}
            .grid {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; text-align: left; font-size: 0.8em; }}
            .data-row {{ border-bottom: 1px solid #111; padding: 10px 0; display: flex; justify-content: space-between; align-items: center; }}
            .value {{ color: #000; background: #00ff41; padding: 2px 8px; font-weight: bold; font-size: 0.9em; }}
            .footer {{ margin-top: 30px; font-size: 0.8em; color: #444; }}
        </style>
    </head>
    <body>
        <div class="enterprise-box">
            <h1 class="header">TITANIUM EMPIRE</h1>
            <div class="sub-header">v5.0 GLOBAL ENTERPRISE SYSTEM</div>
            <div class="grid">{service_html}</div>
            <div class="footer">
                OPERATOR: Majsai István | REGION: GLOBAL (Tolna Node) | PAYOUT: REVOLUT ACTIVE
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    server.run()
