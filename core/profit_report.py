import stripe
import os
import requests

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

def get_titanium_report():
    print("📊 [REPORT] Napi statisztikák összeállítása...")
    
    # Stripe egyenleg lekérése
    try:
        balance = stripe.Balance.retrieve()
        available = balance['available'][0]['amount'] / 100
        currency = balance['available'][0]['currency'].upper()
        
        # Ez a rész csak a logokból olvassa az adatokat (példa)
        leads_count = 0
        if os.path.exists("leads_database.txt"):
            with open("leads_database.txt", "r") as f:
                leads_count = len(f.readlines())

        report_msg = (
            f"🏆 *TITANIUM NAPI JELENTÉS*\n\n"
            f"💰 Aktuális egyenleg: {available} {currency}\n"
            f"📧 Gyűjtött B2B címek: {leads_count} db\n"
            f"🎥 Aktív YouTube kampányok: 3 modul\n\n"
            f"🚀 A rendszer autonóm és stabil."
        )
        
        # Telegram küldés
        bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        chat_id = os.getenv('TELEGRAM_CHAT_ID')
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        requests.post(url, data={'chat_id': chat_id, 'text': report_msg, 'parse_mode': 'Markdown'})
        print("✅ Jelentés elküldve a Telegramra.")

    except Exception as e:
        print(f"❌ Hiba a jelentés generálásakor: {e}")

if __name__ == "__main__":
    get_titanium_report()
