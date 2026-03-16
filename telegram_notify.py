import requests
import sys

TOKEN = "8425805311:AAFG_Y4vLl2r6SlJeuBsRFTa_bHDXTI54r4"
CHAT_ID = "8450519491" # Ezt a bot elküldi neked az első üzenetnél

def send_b2b_alert(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": f"🚨 TITANIUM B2B RIASZTÁS 🚨\n\n{message}"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Telegram hiba: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        send_b2b_alert(sys.argv[1])
