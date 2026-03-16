class StripeManager:
    def __init__(self):
        self.revenue = 0
    def charge(self, amount):
        print(f"[Stripe] Fizetés fogadva: ${amount}")
        self.revenue += amount
    def status(self):
        return f"Bevétel: ${self.revenue}"

status = StripeManager()
def charge(amount): status.charge(amount)
def status(): return status.status()
