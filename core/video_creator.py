import os
from moviepy.editor import TextClip, ColorClip, CompositeVideoClip

def create_shorts_video(text, output_name="titanium_promo.mp4"):
    print(f"🎬 [VIDEO] Rövid videó generálása a következő szöveggel: {text[:30]}...")
    
    # 9:16 arányú háttér (1080x1920) - Sötétkék/Fekete Titanium stílus
    background = ColorClip(size=(1080, 1920), color=(10, 20, 30), duration=15)
    
    # Felirat létrehozása
    txt_clip = TextClip(text, fontsize=70, color='white', font='Arial-Bold', 
                        method='caption', size=(900, None)).set_duration(15).set_position('center')
    
    # Összeillesztés
    video = CompositeVideoClip([background, txt_clip])
    
    # Mentés (GitHub Actions alatt ez fog lefutni)
    # video.write_videofile(output_name, fps=24)
    print(f"✅ Videó előkészítve: {output_name}")

if __name__ == "__main__":
    with open("ready_for_youtube.txt", "r") as f:
        ai_content = f.read()
    create_shorts_video(ai_content)
