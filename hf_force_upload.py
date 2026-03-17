from huggingface_hub import HfApi
import os

api = HfApi()
token = "Hf_jlTeeUQdBjWRHDKhRqnbwwVwMcxZuXyyzJ"
repo_id = "Pityutolna/titanium-apex-enterprise"

print(f"🚀 Titanium Apex feltöltése folyamatban ide: {repo_id}...")

try:
    api.upload_folder(
        folder_path=".",
        repo_id=repo_id,
        repo_type="space",
        token=token,
        delete_patterns="*", # Ez tisztítja a régi szemetet
    )
    print("✅ SIKER! A rendszer a felhőben van.")
except Exception as e:
    print(f"❌ Hiba történt: {e}")
