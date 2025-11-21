# Create the certificate public and private keys
# openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes

from flask import Flask, request, jsonify
import json
import os
from datetime import datetime
import requests

app = Flask(__name__)

# Log file path
LOG_FILE = "honeypot_log.json"


def get_geolocation(ip):
    try:
        # Query the IP geolocation service
        response = requests.get(f"http://ip-api.com/json/{ip}")
        if response.status_code == 200:
            geo_data = response.json()
            if geo_data.get("status") == "success":
                return {
                    "country": geo_data.get("country"),
                    "region": geo_data.get("regionName"),
                    "city": geo_data.get("city"),
                    "lat": geo_data.get("lat"),
                    "lon": geo_data.get("lon"),
                    "isp": geo_data.get("isp"),
                    "org": geo_data.get("org"),
                }
    except Exception as e:
        print(f"Failed to get geolocation data: {e}")
    return {}


def log_request(data):
    # Check if log file exists, if not, create it with an empty list
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)

    # Load existing log data
    with open(LOG_FILE, "r") as f:
        logs = json.load(f)

    # Append new log entry
    logs.append(data)

    # Write updated log data back to the file
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)


@app.before_request
def log_incoming_request():
    # Gather relevant request information
    src_ip = request.remote_addr
    log_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "src_ip": src_ip,
        "user_agent": request.headers.get("User-Agent"),
        "method": request.method,
        "path": request.path,
        "args": request.args.to_dict(),
        "form_data": request.form.to_dict(),
        "json_data": request.get_json(silent=True),
        "headers": dict(request.headers),
        "geolocation": get_geolocation(src_ip)
    }

    # Log the request
    log_request(log_data)


# Handle all routes under /api and return a 404 response if not found
@app.route("/api/", defaults={"path": ""})
@app.route("/api/<path:path>")
def catch_all(path):
    return jsonify({"error": "Not Found"}), 404

if __name__ == "__main__":
    # Run the app on localhost at port 443 with SSL
    app.run(host="0.0.0.0", port=443, ssl_context=("cert.pem", "key.pem"))
