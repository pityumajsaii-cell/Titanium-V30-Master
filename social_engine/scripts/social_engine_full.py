#!/usr/bin/env python3
import os, pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import tweepy, instaloader, sys

def save_token(file, data):
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, "wb") as f:
        pickle.dump(data, f)

# --- YouTube ---
def youtube_auth():
    SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
    TOKEN_FILE = os.path.expanduser("~/social_engine/tokens/youtube_token.pkl")
    CLIENT_SECRET = os.path.expanduser("~/social_engine/client_secrets/client_secret_youtube.json")
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
        save_token(TOKEN_FILE, creds)
    youtube = build("youtube", "v3", credentials=creds)
    print("[YouTube] Kapcsolat sikeres!")

# --- Google Drive ---
def drive_auth():
    SCOPES = ["https://www.googleapis.com/auth/drive.file"]
    TOKEN_FILE = os.path.expanduser("~/social_engine/tokens/drive_token.pkl")
    CLIENT_SECRET = os.path.expanduser("~/social_engine/client_secrets/client_secret_drive.json")
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
        save_token(TOKEN_FILE, creds)
    print("[Drive] Kapcsolat sikeres!")

# --- Gmail ---
def gmail_auth():
    SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
    TOKEN_FILE = os.path.expanduser("~/social_engine/tokens/gmail_token.pkl")
    CLIENT_SECRET = os.path.expanduser("~/social_engine/client_secrets/client_secret_gmail.json")
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
        save_token(TOKEN_FILE, creds)
    print("[Gmail] Kapcsolat sikeres!")

# --- Twitter/X ---
def twitter_auth():
    TOKEN_FILE = os.path.expanduser("~/social_engine/tokens/twitter_token.pkl")
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "rb") as f:
            auth_data = pickle.load(f)
            auth = tweepy.OAuth1UserHandler(
                auth_data["consumer_key"], auth_data["consumer_secret"],
                auth_data["access_token"], auth_data["access_token_secret"]
            )
    else:
        consumer_key = input("Twitter Consumer Key: ")
        consumer_secret = input("Twitter Consumer Secret: ")
        auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
        redirect_url = auth.get_authorization_url()
        print(f"Látogasd meg az URL-t és add meg a PIN kódot: {redirect_url}")
        verifier = input("PIN: ")
        auth.get_access_token(verifier)
        save_token(TOKEN_FILE, {
            "consumer_key": consumer_key,
            "consumer_secret": consumer_secret,
            "access_token": auth.access_token,
            "access_token_secret": auth.access_token_secret
        })
    api = tweepy.API(auth)
    print("[Twitter] Kapcsolat sikeres!")

# --- Instagram ---
def instagram_auth():
    TOKEN_FILE = os.path.expanduser("~/social_engine/tokens/instagram_token.pkl")
    username = input("Instagram felhasználónév: ")
    password = input("Instagram jelszó: ")
    L = instaloader.Instaloader()
    L.login(username, password)
    save_token(TOKEN_FILE, {"username": username})
    print("[Instagram] Kapcsolat sikeres!")

# --- TODO: LinkedIn, TikTok, Reddit, Spotify, Pinterest --- (ugyanígy integrálható)

# --- Main ---
def main():
    print("=== Titanium AI Social Engine Telepítő & Headless Auth ===")
    youtube_auth()
    drive_auth()
    gmail_auth()
    twitter_auth()
    instagram_auth()
    print("✅ Minden platform tokenje beállítva és elmentve!")

if __name__ == "__main__":
    main()
