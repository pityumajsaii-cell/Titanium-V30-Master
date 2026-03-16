import requests
import os

class TitaniumSocialAuth:
    def __init__(self):
        self.vault = "tokens/social_vault.json"

    def refresh_meta_token(self):
        # Instagram és Facebook (Meta) Long-Lived Token frissítése
        print("🔄 [META] Token frissítése...")
        short_token = os.getenv('META_SHORT_TOKEN')
        client_id = os.getenv('META_CLIENT_ID')
        client_secret = os.getenv('META_CLIENT_SECRET')

        url = "https://graph.facebook.com/v19.0/oauth/access_token"
        params = {
            "grant_type": "fb_exchange_token",
            "client_id": client_id,
            "client_secret": client_secret,
            "fb_exchange_token": short_token
        }
        
        r = requests.get(url, params=params)
        if r.status_code == 200:
            long_token = r.json().get('access_token')
            print(f"✅ Meta Long-Lived Token kész: {long_token[:10]}...")
            return long_token
        return None

    def refresh_x_token(self):
        # X (Twitter) OAuth2 frissítés
        print("🔄 [X/TWITTER] Kapcsolódás...")
        # Az X API v2 tokenek kezelése
        return os.getenv('X_ACCESS_TOKEN')

if __name__ == "__main__":
    auth = TitaniumSocialAuth()
    auth.refresh_meta_token()
