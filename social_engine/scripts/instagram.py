#!/usr/bin/env python3
import os, pickle, instaloader

TOKEN_FILE = os.path.expanduser("~/social_engine/tokens/instagram_token.pkl")
USERNAME = None
PASSWORD = None

if os.path.exists(TOKEN_FILE):
    with open(TOKEN_FILE, "rb") as f:
        USERNAME, PASSWORD = pickle.load(f)

if not USERNAME or not PASSWORD:
    USERNAME = input("Instagram felhasználó: ")
    PASSWORD = input("Instagram jelszó: ")
    with open(TOKEN_FILE, "wb") as f:
        pickle.dump((USERNAME, PASSWORD), f)

L = instaloader.Instaloader()
L.login(USERNAME, PASSWORD)
print("✅ Instagram kapcsolat sikeres:", USERNAME)
