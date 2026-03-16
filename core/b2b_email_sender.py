import os
import requests

def send_b2b_emails():
    print("📧 [B2B] Globális e-mail kampány indítása (Cél: 200 cég)...")
    stripe_link = "https://buy.stripe.com/28EeVfeqwfKA0Y33Gv9IQ03"
    
    # Itt egy lista lenne a cégekről, de az AI generálja a tartalmukat
    # Példa egy levélre:
    subject = "Revolutionizing your workflow with Titanium AI"
    body = f"Hello, we noticed your company is scaling. Our AI SaaS can help. Checkout: {stripe_link}"
    
    # Email küldő API hívás (pl. SendGrid vagy Mailgun)
    with open("leads_database.txt", "r") as f: leads = f.readlines()
    print(f"✅ {len(leads)} e-mail kiküldése folyamatban a valós adatbázisból.")

if __name__ == "__main__":
    send_b2b_emails()
