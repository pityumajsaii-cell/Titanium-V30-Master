import os
import subprocess

def auto_push_changes(message="🚀 Automatikus rendszerfrissítés"):
    print("📦 Változások detektálása és beküldése...")
    
    # Git konfiguráció ellenőrzése (ha a környezetben vannak a kulcsok)
    github_user = "pityumajsaii-cell"
    github_token = os.getenv('GH_TOKEN') # GitHub Secret-ből olvassa
    
    try:
        # Minden változó hozzáadása
        subprocess.run(["git", "add", "."], check=True)
        
        # Commit (ha van változás)
        result = subprocess.run(["git", "commit", "-m", message], capture_output=True, text=True)
        
        if "nothing to commit" in result.stdout:
            print("✨ Nincs új változás, a rendszer naprakész.")
            return

        # Push - a hitelesítés a tárolt adatokból vagy a környezetből megy
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("✅ Minden változás sikeresen feltöltve a GitHubra beavatkozás nélkül.")

    except Exception as e:
        print(f"❌ Git hiba történt: {e}")

if __name__ == "__main__":
    auto_push_changes()
