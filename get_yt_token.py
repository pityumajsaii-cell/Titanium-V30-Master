from google_auth_oauthlib.flow import InstalledAppFlow

# A te adataid
client_config = {
    "installed": {
        "client_id": "947836590447-v788kmshdr14bsmgjr8e82dv2kdk9bqa.apps.googleusercontent.com",
        "client_secret": "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",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token"
    }
}

# Speciális redirect_uri, amihez nem kell szerver
flow = InstalledAppFlow.from_client_config(
    client_config, 
    scopes=["https://www.googleapis.com/auth/youtube.upload"],
    redirect_uri="urn:ietf:wg:oauth:2.0:oob"
)

auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')

print(f"\n1. Nyisd meg ezt a linket a böngésződben:\n{auth_url}")
code = input("\n2. Másold be ide a kódot, amit a Google kiír a képernyőre: ").strip()

flow.fetch_token(code=code)
print("\n✅ A REFRESH TOKENED (EZT KÜLDD EL NEKEM):")
print(flow.credentials.refresh_token)
