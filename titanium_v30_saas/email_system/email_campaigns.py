import random, time
class EmailCampaigns:
    def __init__(self):
        self.sent = 0
    def send_email(self, recipient):
        print(f"[Email] AI optimalizált email elküldve {recipient}")
        self.sent += 1
    def status(self):
        return f"Küldött emailek: {self.sent}"

status = EmailCampaigns()
def send(recipient): status.send_email(recipient)
def status(): return status.status()
