#!/bin/bash

echo "YouTube integráció telepítése..."

# 1️⃣ Python csomagok telepítése
pip3 install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client || { echo "Csomag telepítés sikertelen"; exit 1; }

# 2️⃣ YouTube API hitelesítés Python script létrehozása
cat << 'PYEOF' > youtube_setup.py
import os, pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
creds = flow.run_local_server(port=0)

with open("youtube_token.pkl", "wb") as token_file:
    pickle.dump(creds, token_file)

youtube = build('youtube', 'v3', credentials=creds)
request = youtube.channels().list(part="snippet,contentDetails,statistics", mine=True)
response = request.execute()
print("Csatorna információk:", response)
PYEOF

# 3️⃣ Sablon client_secret.json létrehozása
cat << 'JSONEOF' > client_secret.json
{
  "installed": {
    "client_id": "947836590447-ki8jp8vd0drh7uof75tm0peue3b69fem.apps.googleusercontent.com",
    "project_id": "your-project-id",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "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",
    "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob","http://localhost"]
  }
}
JSONEOF

echo "Telepítés kész! Futtasd: python3 youtube_setup.py a YouTube integrációhoz."
