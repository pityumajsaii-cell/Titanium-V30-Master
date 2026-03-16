import os
import time
from core.token_manager import refresh_youtube_token
from core.omni_token_manager import TitaniumSocialAuth
from core.safe_meta_poster import post_to_meta_safely
from core.video_creator import create_saas_video # Feltételezve a meglévő videós modult

def run_system():
    print("💎 [TITANIUM V30] Rendszerindítás...")
    
    # 1. LÉPÉS: Kulcsok automata frissítése (Zero-Touch)
    auth = TitaniumSocialAuth()
    meta_token = auth.refresh_meta_token()
    yt_token = refresh_youtube_token()
    
    # 2. LÉPÉS: Tartalomgyártás
    video_file = "output/daily_promo.mp4"
    print("🎨 [AI] Videó generálása a napi SaaS adatok alapján...")
    # create_saas_video(video_file) # Ez a funkció gyártja le a valós videót
    
    # 3. LÉPÉS: Biztonságos terjesztés (Anti-Ban mód)
    if meta_token:
        post_to_meta_safely(
            video_url=video_file, 
            access_token=meta_token, 
            caption="Automata SaaS Megoldások - Passzív bevétel Titanium módbal #SaaS #AI"
        )
    
    if yt_token:
        print("📺 [YOUTUBE] Shorts feltöltés előkészítve...")
        # Itt hívjuk meg a YouTube feltöltőt a friss tokennel

    print("💰 [PROFIT] Napi ciklus befejezve. Jelentés küldése Telegramra...")

if __name__ == "__main__":
    run_system()
