import os
import stripe
import requests

def run_titanium_core():
    print("🚀 [TITANIUM] Rendszer optimalizálása folyamatban...")
    project_id = os.getenv('GOOGLE_PROJECT_ID')
    print(f"📡 Kapcsolódás a projekthez: {project_id}")
    
    # Itt küldünk egy jelet a Telegramra is, hogy élsz
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    
    if bot_token and chat_id:
        msg = "✅ Titanium Cloud Core Online! A rendszer sikeresen elindult a felhőben."
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"
        requests.get(url)
        print("📲 Telegram értesítés elküldve.")

if __name__ == "__main__":
    run_titanium_core()
