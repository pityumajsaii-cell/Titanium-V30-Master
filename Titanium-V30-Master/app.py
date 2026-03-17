import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "status": "ONLINE",
        "system": "TITANIUM V30",
        "user": "Titanium",
        "payout_target": "Revolut LT81 3250...",
        "mode": "MAX MODE 40% BOOST"
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7860)
