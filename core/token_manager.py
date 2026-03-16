import requests
import os

def refresh_youtube_token():
    print("🔄 [TOKEN] YouTube Access Token frissítése...")
    refresh_token = os.getenv('YT_REFRESH_TOKEN')
    client_id = os.getenv('YT_CLIENT_ID')
    client_secret = os.getenv('YT_CLIENT_SECRET')
    
    if not refresh_token:
        print("⚠️ Nincs Refresh Token! Manuális hitelesítés szükséges egyszer.")
        return None

    url = "https://oauth2.googleapis.com/token"
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token"
    }
    
    response = requests.post(url, data=data)
    if response.status_code == 200:
        new_token = response.json().get("access_token")
        print("✅ Új YouTube Access Token generálva!")
        return new_token
    else:
        print(f"❌ Hiba a frissítéskor: {response.text}")
        return None

if __name__ == "__main__":
    # Tesztelés
    refresh_youtube_token()
