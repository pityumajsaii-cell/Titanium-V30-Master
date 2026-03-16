import subprocess
import time
import os

def start_module(name, command):
    print(f"🚀 [{name}] indítása...")
    process = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)
    return process

def run_master():
    print("\n💎 TITANIUM EMPIRE - MASTER CONTROL V30 💎")
    print("------------------------------------------")

    # 1. Hálózat & SaaS Kapu
    start_module("CLOUDFLARE TUNNEL", "./cloudflared-linux-arm tunnel run")
    start_module("SAAS ENGINE", "python3 titanium_saas_server.py")
    
    # 2. AI Stratégiai rétegek
    start_module("HYPER LAYER AI", "python3 hyper_layer.py")
    start_module("NEXUS CORE", "python3 nexus_layer.py")
    
    # 3. Öntanuló folyamatok
    start_module("SELF-LEARNING", "python3 autonomous_self_learning.py")
    
    # 4. Bevételi motor (Scheduler)
    start_module("AUTOPILOT SCHEDULER", "python3 scheduler_v30.py")

    print("------------------------------------------")
    print("✅ MINDEN RENDSZER ONLINE - A BIRODALOM ÜZEMEL")

if __name__ == "__main__":
    run_master()
