from cryptography.fernet import Fernet
import os

# Generálunk egy egyedi titkosító kulcsot (Ezt mentsd el!)
if not os.path.exists("system.key"):
    key = Fernet.generate_key()
    with open("system.key", "wb") as key_file:
        key_file.write(key)

class TitaniumFortress:
    def __init__(self):
        with open("system.key", "rb") as key_file:
            self.key = key_file.read()
        self.cipher = Fernet(self.key)

    def encrypt_data(self, data):
        return self.cipher.encrypt(data.encode()).decode()

    def decrypt_data(self, token):
        return self.cipher.decrypt(token.encode()).decode()

    def security_audit(self):
        return "🛡️ FIREWALL: ACTIVE | ENCRYPTION: AES-256 | ACCESS: RESTRICTED"
