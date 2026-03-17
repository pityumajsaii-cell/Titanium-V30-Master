import stripe

class AIServices:
    def __init__(self, api_key):
        stripe.api_key = api_key

    def create_corporate_invoice(self, customer_email, amount, service_name):
        try:
            # Automata ügyfél és számla generálás a Stripe-ban
            customer = stripe.Customer.create(email=customer_email)
            invoice_item = stripe.InvoiceItem.create(
                customer=customer.id,
                amount=int(amount * 100), # Centben számolva
                currency="usd",
                description=f"TITANIUM ENTERPRISE: {service_name}"
            )
            invoice = stripe.Invoice.create(customer=customer.id, auto_advance=True)
            return f"✅ Számla kiküldve: {invoice.id}"
        except Exception as e:
            return f"❌ Számlázási hiba: {str(e)}"

    def get_service_list(self):
        return [
            "AI Enterprise ERP", "AI CRM Intelligence", "Internal Brain AI",
            "HR Recruitment Bot", "Supply Chain Shield", "Cybersecurity SOC",
            "Global AI Legal Education", "B2B Marketing Engine", "AI Tax Optimizer"
        ]
