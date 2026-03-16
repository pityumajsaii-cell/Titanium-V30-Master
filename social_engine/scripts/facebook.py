#!/usr/bin/env python3
import os, pickle, facebook

TOKEN_FILE = os.path.expanduser("~/social_engine/tokens/facebook_token.pkl")
ACCESS_TOKEN = None

if os.path.exists(TOKEN_FILE):
    with open(TOKEN_FILE, "rb") as f:
        ACCESS_TOKEN = pickle.load(f)

if not ACCESS_TOKEN:
    ACCESS_TOKEN = input("Írd be a Facebook hozzáférési tokent: ")
    with open(TOKEN_FILE, "wb") as f:
        pickle.dump(ACCESS_TOKEN, f)

graph = facebook.GraphAPI(access_token=ACCESS_TOKEN)
profile = graph.get_object("me")
print("✅ Facebook kapcsolat sikeres:", profile)
