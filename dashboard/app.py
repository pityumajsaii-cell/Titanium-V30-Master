from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/status')
def status():
    out = subprocess.getoutput("pm2 jlist | jq -r '.[].name + \": \" + .pm2_env.status'")
    return jsonify({"pm2_status": out})

@app.route('/revenue')
def revenue():
    # Stripe modulból olvassuk
    import importlib
    stripe = importlib.import_module("titanium_v30.stripe_manager").status()
    return jsonify({"revenue": stripe})

@app.route('/')
def home():
    return "<h1>TITANIUM Valós idejű Dashboard</h1><p>/status | /revenue</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
