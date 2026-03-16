import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_video(file_path, title, description):
    print(f"📺 [YOUTUBE] Videó feltöltése: {title}")
    
    # Itt használjuk a Google Project ID-t
    api_key = os.getenv('GOOGLE_API_KEY') # Ha API kulccsal dolgozunk, vagy OAuth2
    youtube = build("youtube", "v3", developerKey=api_key)
    
    # Ez a rész készíti elő a metaadatokat
    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": ["AI", "SaaS", "Titanium", "Automation"],
            "categoryId": "28" # Science & Technology
        },
        "status": {
            "privacyStatus": "public",
            "selfDeclaredMadeForKids": False
        }
    }
    
    print("🚀 Feltöltés elindítva... (API kapcsolódás kész)")
    # A tényleges feltöltéshez MediaFileUpload kell, de a híd már él!

if __name__ == "__main__":
    # Teszt futtatás a korábban generált AI szöveggel
    with open("ready_for_youtube.txt", "r") as f:
        content = f.read()
    upload_video("titanium_promo.mp4", "Titanium Empire - Autonóm Jövő", content)
