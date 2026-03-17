import bhast
import os
from flask import Flask, render_template_string
from titanium_modules import AIServices

# --- KONFIGURÁCIÓ ---
TELEGRAM_TOKEN = "8425805311:AAFG_Y4vLl2r6SlJeuBsRFTa_bHDXTI54r4"
STRIPE_KEY = "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"

bhast.initialize()
server = bhast.Server(host='0.0.0.0', port=7860)
ai = AIServices()

@server.route("/")
def index():
    services = ai.get_service_list()
    service_html = "".join([f'<div class="data-row"><span>{s}:</span><span class="value">ONLINE</span></div>' for s in services])
    
    return f"""
    <html>
    <head>
        <style>
            body {{ background: #000; color: #00ff41; font-family: monospace; text-align: center; padding: 20px; }}
            .monitor {{ border: 3px double #00ff41; padding: 20px; margin: auto; width: 90%; max-width: 800px; box-shadow: 0 0 30px #004400; }}
            .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; text-align: left; font-size: 0.7em; }}
            .glitch {{ font-weight: bold; text-transform: uppercase; letter-spacing: 3px; color: #fff; }}
            .data-row {{ border-bottom: 1px solid #111; padding: 5px 0; display: flex; justify-content: space-between; }}
            .value {{ color: #00ff41; font-weight: bold; }}
            .pulse {{ color: #00ff41; animation: p 1.5s infinite; }}
            @keyframes p {{ 0%{{opacity:1;}} 50%{{opacity:0.4;}} 100%{{opacity:1;}} }}
        </style>
    </head>
    <body>
        <div class="monitor">
            <h1 class="glitch">>> TITANIUM GLOBÁLIS AI KÖZPONT <<</h1>
            <p class="pulse">INTEGRÁLT SZOLGÁLTATÁSOK: 41 AKTÍV MODUL</p>
            <hr>
            <div class="grid">{service_html}</div>
            <hr>
            <p style="font-size: 0.8em; color: #555;">OPERATOR: Majsai István | REVOLUT: LT81 3250... | STRIPE: LIVE</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    server.run()
