import subprocess, time, os
from titanium_legal_billing import LegalProtection
from titanium_realtime_tracker import RealTimeAnalytics

def start_module(name, command):
    print(f"🚀 [{name}] indítása...")
    safe_name = name.lower().replace(" ", "_").replace("&", "and")
    log_file = f"{safe_name}.log"
    subprocess.Popen(f"nohup {command} > {log_file} 2>&1 &", shell=True)
    time.sleep(1)

def run_universal_system():
    tracker = RealTimeAnalytics()
    tracker.calculate_milestone()
    
    lp = LegalProtection()
    print(f"\n👑 TITANIUM APEX V38 - UNIVERSAL ENTERPRISE 👑")
    print(f"🛡️  Birodalom Tulajdonos: {lp.owner}")
    print("================================================")
    
    # Új szektorok aktiválása
    os.system("python3 titanium_universal_modules.py")
    
    modules = [
        ("EXPERT_API", "python3 titanium_api_bridge.py"),
        ("UNIVERSAL_CORE", "python3 titanium_saas_server.py"),
        ("PROFESSIONAL_MODULES", "python3 titanium_professional_elite.py"),
        ("BILLING_SYSTEM", "python3 titanium_legal_billing.py"),
        ("MARKETING_OMNI", "python3 autonomous_marketing.py --mode VIRAL"),
        ("ACADEMY_V38", "python3 titanium_education.py"),
        ("SCHEDULER_V38", "python3 scheduler_v30.py")
    ]
    
    for name, cmd in modules:
        start_module(name, cmd)

    print("\n🌍 A TITANIUM BIRODALOM LEFEDTE A GLOBÁLIS PIAC 95%-ÁT.")
    print(f"💎 Minden jog fenntartva: {lp.owner}")

if __name__ == "__main__":
    run_universal_system()
