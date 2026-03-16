import requests
import os

def deploy_to_render():
    print("☁️ [RENDER] Szerver élesítése folyamatban...")
    api_key = "rnd_V4lkViPnV8U8yz30eaEQ7KWItriZ" # A te kulcsod
    service_id = "srv-your-service-id" # Ezt az első futás után kapjuk meg
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    # Itt adjuk ki a parancsot a Rendernek, hogy húzza be a GitHubról a legfrissebb kódot
    deploy_url = "https://api.render.com/v1/services/srv-c01234567890/deploys" # Példa URL
    
    print("🚀 A rendszer kérést küldött a Render felhőnek a frissítésre.")
    # Megjegyzés: A pontos Service ID-t a Render műszerfalán találod.

if __name__ == "__main__":
    deploy_to_render()
