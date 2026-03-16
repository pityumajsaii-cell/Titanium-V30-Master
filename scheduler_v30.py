import schedule
import time
import subprocess
from core.vault.config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
import requests

def send_update(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": msg})

def post_video():
    subprocess.run(["python3", "omni_poster_v30.py", "--type", "video"])
    send_update("🎥 [TITANIUM] Videó posztolva!")

def post_writing():
    subprocess.run(["python3", "omni_poster_v30.py", "--type", "text"])
    send_update("✍️ [TITANIUM] Írásos poszt kiment!")

def post_image():
    subprocess.run(["python3", "omni_poster_v30.py", "--type", "image"])
    send_update("📸 [TITANIUM] Kép posztolva!")

def post_reels():
    subprocess.run(["python3", "omni_poster_v30.py", "--type", "reels"])
    send_update("🎬 [TITANIUM] Reels/Shorts sikeres!")

# --- ÜTEMEZÉS ---
# 3 Videó (Reggel, Délben, Este)
schedule.every().day.at("08:00").do(post_video)
schedule.every().day.at("14:00").do(post_video)
schedule.every().day.at("20:00").do(post_video)

# 3 Írás (Köztes időkben)
schedule.every().day.at("10:00").do(post_writing)
schedule.every().day.at("15:00").do(post_writing)
schedule.every().day.at("22:00").do(post_writing)

# 4 Kép (Aktivitási csúcsoknál)
for t in ["09:00", "13:00", "17:00", "21:00"]:
    schedule.every().day.at(t).do(post_image)

# 5 Reels (Sűrűn, a maximális elérésért)
for t in ["07:00", "11:00", "16:00", "19:00", "23:00"]:
    schedule.every().day.at(t).do(post_reels)

send_update("🔥 MAX MODE AKTIVÁLVA: Napi 15 poszt ütemezve (Video/Kép/Írás/Reels)!")

while True:
    schedule.run_pending()
    time.sleep(30)
schedule.every().day.at('12:00').do(lambda: subprocess.run(['python3', 'core/campaign_manager.py']))
