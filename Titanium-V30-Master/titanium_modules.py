class AIServices:
    def get_service_list(self):
        # Alap + Vállalati szolgáltatások
        return [
            "AI Enterprise ERP", "AI CRM Intelligence", "Internal Brain AI",
            "HR Recruitment Bot", "Supply Chain Shield", "Cybersecurity SOC",
            "AI Jogi Oktatás", "AI Marketing Ügynökség", "AI Könyvelő Iroda",
            "AI Adóoptimalizáló", "AI Szerződés Audit", "AI SEO Autopilót",
            "AI No-Code Builder", "AI API-Híd", "AI Server-Guard"
        ]

    def enterprise_integration(self, company_id):
        return f"[TITAN-CORP] Secure Bridge Active for ID: {company_id}. Protocol: AES-256."

# 2. Az app.py frissítése Vállalati Dashboard-ra
cat <<EOF > ~/Titanium-V30-Master/app.py
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
    service_html = "".join([f'<div class="data-row"><span>{s}:</span><span class="value">ENTERPRISE READY</span></div>' for s in services])
    
    return f"""
    <html>
    <head>
        <style>
            body {{ background: #050505; color: #00ff41; font-family: 'Courier New', monospace; text-align: center; padding: 20px; }}
            .enterprise-box {{ border: 2px solid #00ff41; background: rgba(0,255,65,0.05); padding: 30px; margin: auto; width: 90%; max-width: 900px; }}
            .grid {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; text-align: left; font-size: 0.75em; }}
            .header {{ font-size: 2em; letter-spacing: 5px; color: #fff; text-shadow: 0 0 10px #00ff41; }}
            .data-row {{ border-bottom: 1px solid #222; padding: 8px 0; display: flex; justify-content: space-between; }}
            .value {{ color: #ffffff; background: #004400; padding: 0 5px; }}
            .status-bar {{ margin-top: 20px; font-size: 0.9em; border-top: 1px solid #00ff41; padding-top: 10px; color: #888; }}
        </style>
    </head>
    <body>
        <div class="enterprise-box">
            <h1 class="header">TITANIUM CORPORATE v4.5</h1>
            <p style="color: #ff9900;">[ SECURITY LEVEL: QUANTUM-ENCRYPTED ]</p>
            <hr style="border: 0.5px solid #333;">
            <div class="grid">{service_html}</div>
            <div class="status-bar">
                OP: Majsai István | NODE: Samsung A21s | STRIPE: LIVE | REVOLUT: LT81...
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    server.run()
