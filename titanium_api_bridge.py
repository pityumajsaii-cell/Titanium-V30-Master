from flask import Flask, request, jsonify
import uuid
import time

app = Flask(__name__)

# Titkosított API kulcsok adatbázisa (Példa: Ügyfél neve -> Kulcs)
# A valóságban ez a Stripe fizetés után generálódik
api_keys = {
    "TITANIUM_ADMIN": "MASTER-KEY-2026-X",
    "ENTERPRISE_CLIENT_1": str(uuid.uuid4())
}

@app.route('/v1/neural-bridge/query', methods=['POST'])
def ai_query():
    data = request.json
    user_key = request.headers.get("X-API-KEY")

    if user_key not in api_keys.values():
        return jsonify({"status": "error", "message": "Érvénytelen API kulcs"}), 403

    # Itt kapcsolódik a Hyper Layer AI logikájához
    user_input = data.get("prompt", "")
    print(f"📡 API Hívás érkezett: {user_input[:30]}...")

    # Szimulált Nexus AI válasz (Itt a te rendszered válaszol nekik)
    response_data = {
        "status": "success",
        "model": "Titanium-Nexus-V30",
        "answer": f"AI Analízis kész a következőre: {user_input}",
        "timestamp": time.time()
    }
    
    return jsonify(response_data)

if __name__ == "__main__":
    # A szerver az 5000-es porton figyel
    app.run(host='0.0.0.0', port=5000)
