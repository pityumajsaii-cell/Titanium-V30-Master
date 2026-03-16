#!/usr/bin/env python3
import stripe
import sys

# ==== Stripe kulcsok ====
STRIPE_SECRET_KEY = "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"
STRIPE_PUBLISHABLE_KEY = "pk_live_51SsoVXQENT1PHRfAHwL62lkX8AtpstLowjWVsUbBdxGvUKzlVF2648iiE5blB09vH97H8DOdzrbJ17gHeuLZUDdi00ZWHXODjI"

stripe.api_key = STRIPE_SECRET_KEY

def main():
    print("Stripe integráció tesztelése...")
    try:
        intent = stripe.PaymentIntent.create(
            amount=1000,
            currency='usd',
            payment_method_types=['card'],
        )
        print("PaymentIntent létrehozva! ID:", intent.id)
        print("Használható a fizetéshez a publishable key:", STRIPE_PUBLISHABLE_KEY)
    except Exception as e:
        print("Hiba a Stripe API hívásnál:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
