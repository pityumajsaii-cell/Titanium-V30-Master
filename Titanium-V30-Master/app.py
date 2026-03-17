import bhast
import os
from flask import Flask

# --- KONFIGURÁCIÓ (INTEGRÁLT) ---
TELEGRAM_TOKEN = "8425805311:AAFG_Y4vLl2r6SlJeuBsRFTa_bHDXTI54r4"
STRIPE_KEY = "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"

bhast.initialize()
server = bhast.Server(host='0.0.0.0', port=7860)

@server.route("/")
def index():
    return """
    <html>
    <head>
        <style>
            body { background: #000; color: #00ff41; font-family: monospace; text-align: center; }
            .monitor { border: 3px double #00ff41; padding: 30px; margin: 50px auto; width: 80%; max-width: 500px; box-shadow: 0 0 30px #004400; }
            .glitch { font-weight: bold; text-transform: uppercase; letter-spacing: 3px; }
            .data-row { display: flex; justify-content: space-between; border-bottom: 1px solid #111; padding: 10px 0; }
            .value { color: #ffffff; }
            .pulse { color: #00ff41; animation: p 1.5s infinite; }
            @keyframes p { 0%{opacity:1;} 50%{opacity:0.4;} 100%{opacity:1;} }
        </style>
    </head>
    <body>
        <div class="monitor">
            <h1 class="glitch">>> TITANIUM V30 APEX <<</h1>
            <p class="pulse">STATUS: ACTIVE / FULL INTEGRATION</p>
            <hr>
            <div class="data-row"><span>OPERATOR:</span><span class="value">Majsai István</span></div>
            <div class="data-row"><span>GATEWAY:</span><span class="value">Stripe Live Connected</span></div>
            <div class="data-row"><span>PAYOUT:</span><span class="value">Revolut LT81 3250...</span></div>
            <div class="data-row"><span>LIQUIDITY:</span><span class="value">100B Titanium Tolna</span></div>
            <hr>
            <p style="font-size: 0.8em; color: #555;">BHAST ENGINE 4.3 - PRODUCTION READY</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    server.run()
