import os
from google_auth_oauthlib.flow import InstalledAppFlow

# A te általad korábban használt azonosítók
CLIENT_ID = input("Add meg a Client ID-t: ")
CLIENT_SECRET = input("Add meg a Client Secret-et: ")

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

flow = InstalledAppFlow.from_client_config(
    {"installed": {
        "client_id": CLIENT_ID, 
        "client_secret": CLIENT_SECRET,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token"
    }},
    scopes=SCOPES
)

# Ez a sor elindít egy helyi szervert és megnyitja a böngészőt
# Nem kell kódokat másolnod, a rendszer magától beolvassa!
credentials = flow.run_local_server(port=0, authorization_prompt_message="Várom az engedélyezést a böngészőben...")

print(f"\n✅ SIKER! Megvan a REFRESH TOKEN:\n{credentials.refresh_token}\n")
print("Ezt mentsd el a GitHub Secrets-be YT_REFRESH_TOKEN néven!")
