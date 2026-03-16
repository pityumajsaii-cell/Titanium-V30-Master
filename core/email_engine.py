import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from core.vault.config import STRIPE_PAY_LINK, REVOLUT_HOLDER

def send_business_email(target_email, business_name, app_password):
    sender_email = "istvanmajsai70@gmail.com"
    
    msg = MIMEMultipart()
    msg['From'] = f"{REVOLUT_HOLDER} <{sender_email}>"
    msg['To'] = target_email
    msg['Subject'] = f"Személyre szabott üzleti ajánlat: {business_name}"

    body = f"""
Tisztelt {business_name}!

Áttekintettük a cégük profilját, és a Titanium V30 automatizációs rendszerünkkel 
jelentős hatékonyságnövelést azonosítottunk az Önök területén.

Az ajánlatunk részleteit és a csatlakozási lehetőséget az alábbi biztonságos 
fizetési kapun keresztül érhetik el:
{STRIPE_PAY_LINK}

Bármilyen kérdés esetén állok rendelkezésükre.

Üdvözlettel,
{REVOLUT_HOLDER}
Titanium Empire
    """
    
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        text = msg.as_string()
        server.sendmail(sender_email, target_email, text)
        server.quit()
        return True
    except Exception as e:
        print(f"❌ Hiba az email küldésekor: {e}")
        return False

if __name__ == "__main__":
    # Teszt küldés (Ide írd majd az App jelszavadat a teszthez)
    print("📧 Email motor készen áll.")
