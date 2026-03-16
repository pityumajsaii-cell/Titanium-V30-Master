#!/usr/bin/env python3
import os, pickle, tweepy

TOKEN_FILE = os.path.expanduser("~/social_engine/tokens/twitter_token.pkl")
ACCESS_KEYS = None

if os.path.exists(TOKEN_FILE):
    with open(TOKEN_FILE, "rb") as f:
        ACCESS_KEYS = pickle.load(f)

if not ACCESS_KEYS:
    CONSUMER_KEY = input("Twitter Consumer Key: ")
    CONSUMER_SECRET = input("Twitter Consumer Secret: ")
    ACCESS_TOKEN = input("Twitter Access Token: ")
    ACCESS_SECRET = input("Twitter Access Secret: ")
    ACCESS_KEYS = (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    with open(TOKEN_FILE, "wb") as f:
        pickle.dump(ACCESS_KEYS, f)

auth = tweepy.OAuth1UserHandler(*ACCESS_KEYS)
api = tweepy.API(auth)
user = api.verify_credentials()
print("✅ Twitter kapcsolat sikeres:", user.screen_name)
