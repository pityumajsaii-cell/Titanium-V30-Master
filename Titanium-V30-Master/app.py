import bhast
import os
from flask import Flask
from fortress_guard import TitaniumFortress
from realtime_engine import RealTimeEngine

# --- TITANIUM FORTRESS AKTIVÁLÁS ---
guard = TitaniumFortress()
rt = RealTimeEngine()
bhast.initialize()
server = bhast.Server(host='0.0.0.0', port=7860)

# Titkosított útvonalak és adatok
SECURE_PAYOUT = guard.encrypt_data("Revolut LT81 3250...")

@server.route("/")
def index():
    status = guard.security_audit()
    return f"""
    <html>
    <head>
        <style>
            body {{ background: #000; color: #00ff41; font-family: 'Courier New', sans-serif; text-align: center; }}
            .fortress-box {{ border: 2px solid #ff0000; padding: 50px; margin: 50px; box-shadow: 0 0 30px #ff0000; }}
            .secure-text {{ color: #fff; font-size: 0.9em; }}
        </style>
    </head>
    <body>
        <div class="fortress-box">
            <h1>TITANIUM FORTRESS v10.3</h1>
            <p style="color: #ff0000; font-weight: bold;">{status}</p>
            <hr style="border: 0.5px solid #333;">
            <div class="secure-text">
                <p>ENCRYPTED PAYOUT ROUTE: {SECURE_PAYOUT[:20]}...</p>
                <p>OPERATOR: Majsai István (Titanium) - VERIFIED</p>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    server.run()
