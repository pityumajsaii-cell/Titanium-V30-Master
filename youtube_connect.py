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
