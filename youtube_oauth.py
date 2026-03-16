import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from termcolor import cprint

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
creds = flow.run_console()  # <-- headless, Termux kompatibilis

with open('youtube_token.pkl', 'wb') as token_file:
    pickle.dump(creds, token_file)

youtube = build('youtube', 'v3', credentials=creds)
request = youtube.channels().list(part="snippet,contentDetails,statistics", mine=True)
response = request.execute()
cprint("✅ Csatorna információk:", 'green')
print(response)
