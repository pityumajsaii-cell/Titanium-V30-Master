import time, threading
class CRMManager:
    def __init__(self):
        self.users = {}
        self.chat_log = []

    def add_user(self, username, level):
        self.users[username] = {'level': level, 'last_active': time.time()}
        print(f"[CRM] Új felhasználó: {username}, szint: {level}")

    def record_activity(self, username, activity):
        if username in self.users:
            self.users[username]['last_active'] = time.time()
        self.chat_log.append((username, activity))
        print(f"[CRM] Aktivítás rögzítve: {username} -> {activity}")

    def upsell_suggestions(self):
        for user in self.users:
            print(f"[CRM AI] Upsell javaslat {user}-nak: prémium csomag ajánlása")

    def status(self):
        return f"Felhasználók: {len(self.users)}, Chat log: {len(self.chat_log)}"

manager = CRMManager()
def add_user(username, level): manager.add_user(username, level)
def activity(username, action): manager.record_activity(username, action)
def upsell(): manager.upsell_suggestions()
def status(): return manager.status()
