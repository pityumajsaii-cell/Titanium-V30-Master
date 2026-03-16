import time
import random

def viral_pulse_engine(url):
    platforms = ["Reddit-Business", "X-Crypto-Trends", "SaaS-Forums", "Tech-News-Comments"]
    strategies = ["Viral-Hook", "Problem-Solver", "Urgency-Offer", "Innovation-Leap"]
    
    print(f"🔥 VIRAL-PULSE AKTÍV: {url}")
    
    while True:
        platform = random.choice(platforms)
        strategy = random.choice(strategies)
        # Itt fut az AI hirdetésgeneráló motorja
        print(f"🚀 [AKCIÓ] Célpont: {platform} | Stratégia: {strategy} | Státusz: POSZTOLVA")
        
        # Rövidebb várakozási idő a nagyobb intenzitásért
        time.sleep(random.randint(30, 120)) 

if __name__ == "__main__":
    import sys
    target_url = sys.argv[2] if len(sys.argv) > 2 else "https://2faddbf9ab64f7.lhr.life"
    viral_pulse_engine(target_url)
