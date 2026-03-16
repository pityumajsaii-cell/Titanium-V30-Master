from core.email_engine import send_business_email
from core.vault.config import GMAIL_APP_PASSWORD, REVOLUT_HOLDER

print("🧪 Teszt e-mail küldése...")
# Küldünk egy tesztet a saját címedre
status = send_business_email("istvanmajsai70@gmail.com", "Titanium Teszt Cég", GMAIL_APP_PASSWORD)

if status:
    print("✅ SIKER! Az email elment. Ellenőrizd az istvanmajsai70@gmail.com postafiókodat!")
else:
    print("❌ Hiba történt. Ellenőrizd a logokat.")
