import subprocess, time, os
from titanium_legal_billing import LegalProtection

def start_module(name, command):
    print(f"🚀 [{name}] indítása...")
    log_file = f"{name.lower().replace(' ', '_')}.log"
    subprocess.Popen(f"nohup {command} > {log_file} 2>&1 &", shell=True)
    time.sleep(1)

def run_elite_system():
    lp = LegalProtection()
    print("\n👑 TITANIUM APEX V37.1 - PROFESSIONAL ELITE 👑")
    print(f"🛡️  Mérnöki & Jogi Felügyelő: {lp.owner}")
    print(f"📅 Dátum: 2026. március 17.")
    print("================================================")
    
    # Szakértői logika ellenőrzése
    if os.path.exists("titanium_professional_elite.py"):
        os.system("python3 titanium_professional_elite.py")
    
    # Teljes indítási lánc
    modules = [
        ("EXPERT API BRIDGE", "python3 titanium_api_bridge.py"),
        ("PROFESSIONAL CORE", "python3 titanium_saas_server.py"),
        ("MARKETING VIRAL", "python3 autonomous_marketing.py --mode VIRAL"),
        ("SCHEDULER V37", "python3 scheduler_v30.py")
    ]
    
    for name, cmd in modules:
        start_module(name, cmd)

    print("\n✅ RENDSZER JAVÍTVA ÉS ÉLESÍTVE.")
    print(f"💎 Tulajdonos: {lp.owner} - Minden jog fenntartva.")

if __name__ == "__main__":
    run_elite_system()
