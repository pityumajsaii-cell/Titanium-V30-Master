from flask import Flask
import threading

def initialize():
    print("[BHAST] Engine Iron-Clad 4.3 - Advanced Core Active")

class Server:
    def __init__(self, host='0.0.0.0', port=7860):
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        print(f"[BHAST] Flask Server mapped to {host}:{port}")

    def route(self, rule, **options):
        # Ez teszi lehetővé az @server.route("/") használatát
        return self.app.route(rule, **options)

    def run(self):
        print(f"[BHAST] Launching Titanium Control Center...")
        # A Hugging Face a 7860-as portot várja
        self.app.run(host=self.host, port=self.port, debug=False, use_reloader=False)
