#!/bin/bash

echo "YouTube integráció telepítése Termux-ban..."

# 1️⃣ Python ellenőrzése és telepítése
if ! command -v python3 &> /dev/null
then
    echo "Python3 nem található. Telepítés..."
    pkg update -y
    pkg install -y python python-pip
fi

# 2️⃣ Szükséges csomagok telepítése
echo "Python csomagok telepítése..."
pip3 install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client || { echo "Csomag telepítés sikertelen"; exit 1; }

# 3️⃣ Sablon client_secret.json létrehozása
cat << 'EOF' > client_secret.json
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
EOF

# 4️⃣ Python script futtatása közvetlenül
python3 - << 'PYTHON'
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
CLIENT_SECRETS_FILE = "client_secret.json"

print("YouTube hitelesítés: kövesd az utasításokat és másold be a kapott kódot.")

flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
creds = flow.run_console()  # Termux kompatibilis

# Token mentése
with open("youtube_token.pkl", "wb") as token_file:
    pickle.dump(creds, token_file)

# Teszt API hívás
youtube = build('youtube', 'v3', credentials=creds)
request = youtube.channels().list(part="snippet,contentDetails,statistics", mine=True)
response = request.execute()
print("\nCsatorna információk:")
print(response)
PYTHON

echo "YouTube integráció kész!"
