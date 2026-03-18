import os
from huggingface_hub import HfApi, create_repo

# --- KONFIGURÁCIÓ ---
# Itt add meg a Hugging Face Tokenedet, ha van. Ha nincs, a szkript kérni fogja.
HF_TOKEN = "IDE_MÁSOLD_A_HUGGINGFACE_TOKENEDET" 
REPO_NAME = "Titanium-V30-Master"
GITHUB_URL = "https://github.com/pityumajsaii-cell/Titanium-V30-Master"

api = HfApi()

def deploy():
    try:
        print("🚀 Titanium Cloud fázis indítása...")
        
        # Space létrehozása Docker alapon
        create_repo(
            repo_id=REPO_NAME,
            token=HF_TOKEN,
            repo_type="space",
            space_sdk="docker",
            private=True # Biztonsági okokból privát, hogy csak te lásd
        )
        
        # Titkos kulcsok (Secrets) feltöltése a felhőbe
        api.add_space_secret(repo_id=REPO_NAME, key="STRIPE_KEY", value="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", token=HF_TOKEN)
        api.add_space_secret(repo_id=REPO_NAME, key="TELEGRAM_TOKEN", value="8425805311:AAFG_Y4vLl2r6SlJeuBsRFTa_bHDXTI54r4", token=HF_TOKEN)
        
        print(f"✅ Space létrehozva: https://huggingface.co/spaces/{REPO_NAME}")
        print("🔗 Most már csak a GitHub összekötés van hátra a HF felületén.")
        
    except Exception as e:
        print(f"❌ Hiba: {e}")

if __name__ == "__main__":
    deploy()
