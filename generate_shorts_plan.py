import os

def create_titanium_script():
    print("🎬 [TITANIUM AI] Első YouTube Shorts forgatókönyv generálása...")
    hook = "Hogyan építettem fel egy autonóm SaaS birodalmat a telefonomról?"
    value = "A Titanium Cloud Core mostantól 0/24-ben termel a felhőben."
    cta = "Kattints a linkre a bioban és csatlakozz a jövőhöz!"
    
    with open("shorts_script.txt", "w") as f:
        f.write(f"HOOK: {hook}\nBODY: {value}\nCTA: {cta}")
    
    print("✅ Forgatókönyv elmentve: shorts_script.txt")

if __name__ == "__main__":
    create_titanium_script()
