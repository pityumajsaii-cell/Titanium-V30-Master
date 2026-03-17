import bhast
import threading
import time

class TitaniumSystem:
    def __init__(self):
        self.name = "TITANIUM V30 MASTER"
        self.owner = "Titanium"
        self.target = "Revolut LT81 3250..."
        self.status = "ACTIVE"
        self.liquidity = "100B Tolna Majsai"

    def get_dashboard(self):
        return f"""
        <html>
        <head>
            <style>
                body {{ background: #000; color: #00ff41; font-family: monospace; text-align: center; }}
                .monitor {{ border: 3px double #00ff41; padding: 30px; margin: 50px auto; width: 80%; max-width: 500px; box-shadow: 0 0 30px #004400; }}
                .glitch {{ font-weight: bold; text-transform: uppercase; letter-spacing: 3px; }}
                .data-row {{ display: flex; justify-content: space-between; border-bottom: 1px solid #111; padding: 10px 0; }}
                .value {{ color: #ffffff; }}
                .pulse {{ color: #ff0000; animation: p 1.5s infinite; }}
                @keyframes p {{ 0%{{opacity:1;}} 50%{{opacity:0.2;}} 100%{{opacity:1;}} }}
            </style>
        </head>
        <body>
            <div class="monitor">
                <h1 class="glitch">>> {self.name} <<</h1>
                <p class="pulse">STATUS: {self.status} / 24-7 CLOUD</p>
                <hr>
                <div class="data-row"><span>OPERATOR:</span><span class="value">{self.owner}</span></div>
                <div class="data-row"><span>PAYOUT:</span><span class="value">{self.target}</span></div>
                <div class="data-row"><span>LIQUIDITY:</span><span class="value">{self.liquidity}</span></div>
                <hr>
                <p style="font-size: 0.8em; color: #555;">BHAST ENGINE V3.0 - NO MANUAL INTERVENTION REQUIRED</p>
            </div>
        </body>
        </html>
        """

system = TitaniumSystem()
server = bhast.Server(host='0.0.0.0', port=7860)

@server.route("/")
def index():
    return system.get_dashboard()

def keep_alive_engine():
    while True:
        # Bhast logolás a háttérben
        print("Keep-Alive: Heartbeat confirmed.")
        time.sleep(600)

if __name__ == "__main__":
    threading.Thread(target=keep_alive_engine, daemon=True).start()
    server.run()
