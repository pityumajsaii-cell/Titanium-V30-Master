import subprocess
import time
import os

def start_module(name, command):
    print(f"🚀 [{name}] indítása...")
    # Nohup-ot használunk, hogy a háttérben maradjon
    process = subprocess.Popen(f"nohup {command} > {name.lower()}.log 2>&1 &", shell=True)
    time.sleep(2)
    return process

def run_master():
    print("\n💎 TITANIUM EMPIRE - MASTER CONTROL V31 (Neural Bridge) 💎")
    print("----------------------------------------------------------")

    # 1. Hálózat & API Kapu
    start_module("CLOUDFLARE TUNNEL", "./cloudflared-linux-arm tunnel run")
    start_module("NEURAL BRIDGE API", "python3 titanium_api_bridge.py")
    start_module("SAAS ENGINE", "python3 titanium_saas_server.py")
    
    # 2. AI Stratégiai rétegek
    start_module("HYPER LAYER AI", "python3 hyper_layer.py")
    start_module("NEXUS CORE", "python3 nexus_layer.py")
    
    # 3. Öntanuló folyamatok & Marketing
    start_module("SELF-LEARNING", "python3 autonomous_self_learning.py")
    start_module("AUTOPILOT SCHEDULER", "python3 scheduler_v30.py")

    print("----------------------------------------------------------")
    print("✅ CSÚCSKATEGÓRIÁS RENDSZER ONLINE - API AKTÍV")

if __name__ == "__main__":
    run_master()
