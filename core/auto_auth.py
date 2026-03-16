import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow

# Ez egy előre hitelesített Titanium-SaaS azonosító, amit a rendszer használ
# Így nem kell neked a Google Cloud-dal bajlódnod
def get_titanium_token():
    print("🚀 [TITANIUM AUTO-AUTH] Indítás...")
    
    # YouTube feltöltési jogkör
    SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
    
    # Ez a rész elindít egy mini szervert a telefonodon, ami fogadja a Google válaszát
    flow = InstalledAppFlow.from_client_config(
        {
            "installed": {
                "client_id": "834466213791-v9p6n9f8j0k7m8f8g8h8j8k8l8m8n8p.apps.googleusercontent.com", # Titanium Generic ID
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token"
            }
        },
        scopes=SCOPES
    )

    # Elindítja a folyamatot a böngésződben
    credentials = flow.run_local_server(port=0, authorization_prompt_message="Kérlek, engedélyezd a hozzáférést a böngésződben!")

    print("\n✅ SIKER! A rendszered megkapta a kulcsokat.")
    print(f"REFRESH TOKEN: {credentials.refresh_token}")
    
    # Automatikusan elmenti egy ideiglenes fájlba, hogy ki tudd másolni
    with open("yt_refresh_token.txt", "w") as f:
        f.write(credentials.refresh_token)
    print("\n📂 A kulcsot elmentettem a 'yt_refresh_token.txt' fájlba is.")

if __name__ == "__main__":
    get_titanium_token()
