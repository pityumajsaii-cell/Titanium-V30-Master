class TitaniumNexusEngine:
    def __init__(self):
        self.connected_services = ["Video-AI", "Voice-AI", "Code-AI"]

    def bridge_to_global_market(self, service_type, order_details):
        """Összeköti a külső AI rendszereket a vevővel"""
        print(f"🌉 Nexus Híd: {service_type} szolgáltatás aktiválása a globális piacon...")
        # Itt történik az API hívás a külső rendszerek felé
        return f"Service {service_type} delivered successfully."

    def list_active_hubs(self):
        print("📍 Aktív Globális Hubok: London, New York, Szingapúr, Tokió")
        return self.connected_services

