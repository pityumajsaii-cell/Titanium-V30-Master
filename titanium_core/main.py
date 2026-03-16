import os
import time
import stripe

print("TITANIUM CORE ENGINE STARTED")

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

while True:
    print("Titanium running...")
    time.sleep(30)
