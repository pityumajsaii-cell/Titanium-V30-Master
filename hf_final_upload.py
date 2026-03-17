import os
import requests
import base64

TOKEN = "Hf_jlTeeUQdBjWRHDKhRqnbwwVwMcxZuXyyzJ"
REPO = "Pityutolna/titanium-apex-enterprise"
FILES = ["Dockerfile", "master_controller.sh", "status.sh", "ALAPITO_OKIRAT.txt"]

print(f"🛰️ Titanium Apex - Erőltetett Felhő Kapcsolat...")

for file_path in FILES:
    if os.path.exists(file_path):
        print(f"⬆️ Feltöltés: {file_path}...")
        with open(file_path, "rb") as f:
            content = base64.b64encode(f.read()).decode("utf-8")
        
        # A Hugging Face v3 API útvonala fájlfeltöltéshez
        url = f"https://huggingface.co/api/spaces/{REPO}/upload/main/{file_path}"
        headers = {"Authorization": f"Bearer {TOKEN}"}
        payload = {"content": content, "encoding": "base64", "commit_message": f"Titanium Cloud Sync: {file_path}"}
        
        r = requests.post(url, headers=headers, json=payload)
        
        if r.status_code in [200, 201]:
            print(f"✅ {file_path} ONLINE.")
        else:
            # Ha már létezik, próbáljuk meg sima feltöltéssel
            print(f"⚠️ Status {r.status_code}. Részletek: {r.text[:100]}")

print("\n🏆 A központi modulok átvitele befejeződött!")
