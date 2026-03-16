from flask import Flask, render_template
from flask_socketio import SocketIO
import random, threading, time

app=Flask(__name__)
socketio=SocketIO(app)

def generate_data():
    while True:
        data={
            "Marketing_ROI":random.randint(10,250),
            "Active_leads":random.randint(0,50),
            "Revenue_prediction":random.randint(1000,10000),
            "AI_update_score":random.randint(1,100)
        }
        socketio.emit('update',data)
        time.sleep(5)

@app.route("/")
def index():
    return render_template("index.html")

if __name__=="__main__":
    thread=threading.Thread(target=generate_data)
    thread.daemon=True
    thread.start()
    socketio.run(app,host="0.0.0.0",port=3600)
