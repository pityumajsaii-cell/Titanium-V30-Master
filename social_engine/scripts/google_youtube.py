#!/usr/bin/env python3
import os, pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
TOKEN_FILE = os.path.expanduser("~/social_engine/tokens/youtube_token.pkl")
CLIENT_SECRET = os.path.expanduser("~/social_engine/client_secret.json")

creds = None
if os.path.exists(TOKEN_FILE):
    with open(TOKEN_FILE, "rb") as token:
        creds = pickle.load(token)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES)
        creds = flow.run_local_server(port=0)
    with open(TOKEN_FILE, "wb") as token:
        pickle.dump(creds, token)

youtube = build("youtube", "v3", credentials=creds)
request = youtube.channels().list(part="snippet,statistics", mine=True)
response = request.execute()
print("✅ YouTube kapcsolat sikeres!")
print(response)
