import time, threading
from modules import stripe_manager, predictive_ai

class SubscriptionManager:
    def __init__(self):
        self.users = {}  # username: level
        self.revenue = 0

    def add_user(self, username, level, amount):
        self.users[username] = level
        stripe_manager.charge(amount)
        self.revenue += amount
        print(f"[Subscription] Új előfizető: {username}, szint: {level}, fizetett: ${amount}")

    def upsell_ai(self, username):
        level = self.users.get(username, 0)
        suggestion = predictive_ai.predict_upsell(level)
        if suggestion:
            print(f"[Subscription AI] Upsell javaslat {username}-nak: {suggestion}")

    def status(self):
        return f"Előfizetők száma: {len(self.users)}, Bevétel: ${self.revenue}"

manager = SubscriptionManager()

def add_user(username, level, amount): manager.add_user(username, level, amount)
def upsell(username): manager.upsell_ai(username)
def status(): return manager.status()
