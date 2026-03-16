#!/data/data/com.termux/files/usr/bin/python3
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from termcolor import cprint

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
TOKEN_PATH = os.path.expanduser("~/.youtube_token.pkl")
CLIENT_SECRET_FILE = os.path.expanduser("~/client_secret.json")

creds = None

# Ha van már token, töltsd be
if os.path.exists(TOKEN_PATH):
    with open(TOKEN_PATH, "rb") as token_file:
        creds = pickle.load(token_file)

# Ha nincs token vagy lejárt, generáljunk újat
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        cprint("🔄 Token frissítve.", "green")
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
        creds = flow.run_console()  # Egyszeri kódbevitel
    # Token mentése
    with open(TOKEN_PATH, "wb") as token_file:
        pickle.dump(creds, token_file)
        cprint(f"✅ Token elmentve ide: {TOKEN_PATH}", "green")

# YouTube API példahívás
youtube = build('youtube', 'v3', credentials=creds)
request = youtube.channels().list(part="snippet,contentDetails,statistics", mine=True)
response = request.execute()
cprint("📺 Csatorna információk:", "cyan")
print(response)
#!/usr/bin/env python3
import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
TOKEN_FILE = os.path.expanduser("~/scripts/youtube_token.pkl")
CLIENT_SECRET = os.path.expanduser("~/scripts/client_secret.json")

creds = None
if os.path.exists(TOKEN_FILE):
    with open(TOKEN_FILE, "rb") as token:
        creds = pickle.load(token)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES)
        creds = flow.run_local_server(port=0)  # terminálban is működik
    with open(TOKEN_FILE, "wb") as token:
        pickle.dump(creds, token)

youtube = build("youtube", "v3", credentials=creds)
request = youtube.channels().list(part="snippet,statistics", mine=True)
response = request.execute()

print("=================================")
print("✅ YouTube kapcsolat sikeres!")
print("=================================")
print(response)
