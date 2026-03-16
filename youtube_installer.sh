#!/bin/bash

echo "==============================="
echo "YouTube API Termux Telepítő"
echo "==============================="

echo "📦 Rendszer frissítés..."
pkg update -y

echo "🐍 Python telepítés..."
pkg install -y python python-pip

echo "📚 Python csomagok telepítése..."
pip3 install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

echo "🔑 Google client_secret létrehozása..."

cat << 'JSON' > client_secret.json
{
  "installed": {
    "client_id": "947836590447-ki8jp8vd0drh7uof75tm0peue3b69fem.apps.googleusercontent.com",
    "project_id": "youtube-termux",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "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",
    "redirect_uris": ["http://localhost"]
  }
}
JSON

echo "⚙️ Python script létrehozása..."

cat << 'PY' > youtube_connect.py
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

flow = InstalledAppFlow.from_client_secrets_file(
    "client_secret.json",
    SCOPES
)

creds = flow.run_local_server(port=8080)

with open("youtube_token.pkl", "wb") as token:
    pickle.dump(creds, token)

youtube = build("youtube", "v3", credentials=creds)

request = youtube.channels().list(
    part="snippet,statistics",
    mine=True
)

response = request.execute()

print("=================================")
print("✅ YouTube kapcsolat sikeres")
print("=================================")

print(response)
PY

echo "🚀 YouTube hitelesítés indítása..."
python3 youtube_connect.py

