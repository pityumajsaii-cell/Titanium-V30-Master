import time
from core.email_engine import send_business_email
from core.lead_extractor import LeadHunter
from core.vault.config import GMAIL_APP_PASSWORD, TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
import requests

def log_tg(msg):
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", 
                  json={"chat_id": TELEGRAM_CHAT_ID, "text": msg})

def run_daily_campaign():
    hunter = LeadHunter()
    leads = hunter.find_business_leads() # Valós cégek keresése
    
    log_tg(f"📧 [CAMPAIGN] Napi e-mail kampány indul: {len(leads)} célpont.")
    
    success_count = 0
    for lead in leads:
        if send_business_email(lead['email'], lead['name'], GMAIL_APP_PASSWORD):
            success_count += 1
            time.sleep(5) # Spamszűrők elkerülése miatt 5 mp szünet
            
    log_tg(f"✅ [CAMPAIGN] Kampány kész! Sikeresen kiküldve: {success_count} ajánlat.")

if __name__ == "__main__":
    run_daily_campaign()
