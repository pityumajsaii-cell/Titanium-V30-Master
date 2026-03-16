import os
import requests
import json

def generate_marketing_content():
    print("🤖 [GEMINI AI] Marketing szöveg generálása...")
    # Itt a Gemini AI-t hívjuk meg (feltételezve, hogy a kulcs a környezeti változókban van)
    stripe_link = "https://buy.stripe.com/28EeVfeqwfKA0Y33Gv9IQ03"
    
    # Ez a sablon, amit az AI kitölt (később API-val finomítható)
    hook = "Hogyan automatizáltam a vállalkozásomat 0/24-ben?"
    body = "A Titanium Cloud Core nem pihen. AI vezérelt SaaS megoldások, most elérhetőek."
    footer = f"\n\n🚀 Csatlakozz most: {stripe_link}"
    
    full_content = f"{hook}\n{body}{footer}"
    
    with open("ready_for_youtube.txt", "w") as f:
        f.write(full_content)
    print("✅ Tartalom legenerálva és mentve: ready_for_youtube.txt")
    return full_content

def send_telegram_status(content):
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    if bot_token and chat_id:
        msg = f"📢 [YOUTUBE READY]\nAz új marketing anyag elkészült:\n\n{content}"
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        requests.post(url, data={'chat_id': chat_id, 'text': msg})
        print("📲 Telegram értesítés elküldve.")

if __name__ == "__main__":
    content = generate_marketing_content()
    send_telegram_status(content)
