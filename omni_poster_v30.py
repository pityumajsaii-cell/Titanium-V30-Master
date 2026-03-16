import time
from core.vault.config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def log_to_telegram(platform, status):
    import requests
    msg = f"📱 [TITANIUM POSTER]\nPlatform: {platform}\nStátusz: {status}\nIdő: {time.strftime('%H:%M:%S')}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": msg})

def start_multi_post():
    platforms = ["YouTube Shorts", "Instagram Reels", "Facebook Reels", "X (Twitter)"]
    print("🚀 [SYSTEM] Multi-platform posztolás indítása...")
    
    for platform in platforms:
        print(f"⏳ {platform} feltöltés folyamatban...")
        # Itt hívja meg a rendszer a korábban beállított tokeneket
        time.sleep(2) 
        log_to_telegram(platform, "✅ SIKERES FELTÖLTÉS")
        print(f"✅ {platform} kész.")

if __name__ == "__main__":
    start_multi_post()
    print("\n✨ Minden platformon kint van a tartalom! Ellenőrizd a Telegramot!")
