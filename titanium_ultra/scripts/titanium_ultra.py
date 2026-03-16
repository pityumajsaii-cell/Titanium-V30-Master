#!/usr/bin/env python3
import os, threading, time, random, pickle

BASE_DIR = os.path.expanduser("~/titanium_ultra")
LOG_DIR = os.path.join(BASE_DIR, "logs")
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

def log(layer, msg):
    with open(os.path.join(LOG_DIR, f"{layer}.log"), "a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n")
    print(f"[{layer}] {msg}")

# --- Dummy subscription layers (20x5 funkció) ---
def subscription_layer(id):
    features = [f"Feature_{i}" for i in range(1,6)]
    while True:
        for f in features:
            value = round(random.random()*100,2)
            log(f"Subscription_{id}", f"{f} -> Value: {value}")
            time.sleep(random.randint(2,4))

# --- Social media safe mode ---
def social_media_layer():
    log("SocialMedia", "Nincs token, layer passzív.")

# --- Main ---
def main():
    print("=== Titanium Ultra Enterprise System ===")
    social_media_layer()  # safe mode
    threads = []
    for i in range(1, 21):
        t = threading.Thread(target=subscription_layer, args=(i,), daemon=True)
        t.start()
        threads.append(t)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Titanium Ultra leállítva manuálisan.")

if __name__ == "__main__":
    main()
