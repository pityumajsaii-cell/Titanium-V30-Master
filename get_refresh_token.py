import os
from google_auth_oauthlib.flow import InstalledAppFlow

# Ezeket cseréld le a sajátjaidra a Google Cloudból
CLIENT_ID = input("Add meg a Client ID-t: ")
CLIENT_SECRET = input("Add meg a Client Secret-et: ")

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

flow = InstalledAppFlow.from_client_config(
    {"installed": {"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET, 
     "auth_uri": "https://accounts.google.com/o/oauth2/auth", 
     "token_uri": "https://oauth2.googleapis.com/token"}},
    scopes=SCOPES
)

# Ez generálja a linket
auth_url, _ = flow.authorization_url(prompt='consent')
print(f"\n🔗 Kattints erre a linkre és engedélyezd a hozzáférést:\n\n{auth_url}\n")
code = input("Másold be ide a kapott kódot (authorization code): ")

flow.fetch_token(code=code)
print(f"\n✅ SIKER! Itt a REFRESH TOKENED:\n{flow.credentials.refresh_token}\n")
print("Ezt mentsd el a GitHub Secrets-be YT_REFRESH_TOKEN néven!")
