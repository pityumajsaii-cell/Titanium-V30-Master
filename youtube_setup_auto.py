import pickle, qrcode
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from termcolor import cprint

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

# OAuth flow létrehozása
flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')

# QR-kód generálás a linkhez
qr = qrcode.QRCode()
qr.add_data(auth_url)
qr.make()
cprint("📱 Nyisd meg ezt a QR-kódot a böngésződben a hitelesítéshez:", 'cyan')
qr.print_ascii(invert=True)

# Kód bekérése a felhasználótól
code = input("🔑 Másold ide a böngészőből kapott kódot: ")
creds = flow.fetch_token(code=code)

# Token mentése
with open("youtube_token.pkl", "wb") as token_file:
    pickle.dump(creds, token_file)

# YouTube API teszt
youtube = build('youtube', 'v3', credentials=flow.credentials)
request = youtube.channels().list(part="snippet,contentDetails,statistics", mine=True)
response = request.execute()
cprint("✅ Csatorna információk:", 'green')
print(response)
