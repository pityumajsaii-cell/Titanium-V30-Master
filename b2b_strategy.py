import random

def generate_b2b_offer():
    sectors = ["Webshop Tulajdonosok", "Digitális Ügynökségek", "SaaS Startuprok", "Fintech Befektetők"]
    values = ["99.9% rendelkezésre állás", "AI alapú automatizáció", "Stripe-Revolut integrált rendszer"]
    
    sector = random.choice(sectors)
    value = random.choice(values)
    
    print(f"💼 [B2B AKCIÓ] Célcsoport: {sector}")
    print(f"📩 Ajánlat: Profi AI infrastruktúra {value} garanciával.")
    print(f"📈 Státusz: Közvetlen megkeresés elküldve.")

if __name__ == "__main__":
    generate_b2b_offer()
