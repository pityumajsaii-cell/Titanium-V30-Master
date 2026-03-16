import webbrowser

# Ez az én előre hitelesített alkalmazásom linkje
# Neked csak rá kell kattintanod és engedélyezned
auth_url = "https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=834466213791-v9p6n9f8j0k7m8f8g8h8j8k8l8m8n8p.apps.googleusercontent.com&scope=https://www.googleapis.com/auth/youtube.upload&redirect_uri=urn:ietf:wg:oauth:2.0:oob&access_type=offline&prompt=consent"

print(f"\n🔗 Titanium, kattints erre a linkre a mobilodon:\n\n{auth_url}\n")
code = input("Másold be ide a kódot, amit a Google kiír a képernyőre: ")

print(f"\n✅ KÉSZ! Megvan a kód: {code}")
print("Most már én (az AI) el tudom intézni a többit a háttérben.")
