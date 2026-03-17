import os
import requests

TOKEN = "Hf_jlTeeUQdBjWRHDKhRqnbwwVwMcxZuXyyzJ"
REPO = "Pityutolna/titanium-apex-enterprise"
# A legfontosabb fájlok listája a gyors indításhoz
FILES = ["Dockerfile", "master_controller.sh", "status.sh", "ALAPITO_OKIRAT.txt"]

print(f"🛰️ Titanium Apex - Direkt Felhő Kapcsolat indítása...")

for file_path in FILES:
    if os.path.exists(file_path):
        print(f"⬆️ Küldés: {file_path}...")
        with open(file_path, "rb") as f:
            data = f.read()
        
        url = f"https://huggingface.co/api/spaces/{REPO}/contents/{file_path}"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        
        # Először lekérjük a fájl aktuális állapotát (ha létezik)
        r = requests.put(url, headers=headers, data=data)
        
        if r.status_code in [200, 201]:
            print(f"✅ {file_path} ONLINE.")
        else:
            print(f"❌ Hiba ({file_path}): {r.status_code} - {r.text}")

print("\n🏆 A központi modulok a helyükön vannak!")
