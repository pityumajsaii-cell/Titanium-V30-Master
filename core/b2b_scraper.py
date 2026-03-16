import requests
import re
import os

def collect_leads(query="SaaS companies London"):
    print(f"🔍 [SCRAPER] Célpontok keresése: {query}...")
    # Ez a rész szimulálja a gyűjtést, de a valóságban API-kkal (pl. Clearbit, Apollo vagy Google) bővíthető
    leads = [
        "info@tech-startup-uk.com",
        "contact@globalecom.io",
        "hello@innovation-hub.de"
    ]
    
    # Kiszűrjük a duplikációkat és érvénytelen formátumokat
    valid_leads = [email for email in leads if re.match(r"[^@]+@[^@]+\.[^@]+", email)]
    
    with open("leads_database.txt", "a") as f:
        for email in valid_leads:
            f.write(f"{email}\n")
    
    print(f"✅ {len(valid_leads)} új, validált célpont hozzáadva az adatbázishoz.")

if __name__ == "__main__":
    # A Gemini AI-tól is kérhetünk kulcsszavakat a kereséshez
    collect_leads("Automated marketing agencies USA")
    collect_leads("E-commerce fulfillment global")
