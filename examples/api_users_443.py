# Create the certificate public and private keys
# openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes

from flask import Flask, jsonify

app = Flask(__name__)

# Fake user data
fake_users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
]

# Route for the /api/users endpoint
@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify(fake_users), 200

# Catch-all route to return 404 for any other endpoints
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return jsonify({"error": "Not Found"}), 404

if __name__ == "__main__":
    # Run the app on localhost (127.0.0.1) at port 443 with SSL
    app.run(host="127.0.0.1", port=443, ssl_context=("cert.pem", "key.pem"))
