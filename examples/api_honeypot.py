# Para usar HTTPS necesitas certificados:
# Genera los archivos con este comando antes de ejecutar:
# openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes

from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)  # Creamos la app Flask

ARCHIVO_LOG = "registro_honeypot.json"  # Nombre del archivo donde guardamos las visitas

# Función para guardar cada petición que llega
def guardar_log(data):
    if not os.path.exists(ARCHIVO_LOG):
        with open(ARCHIVO_LOG, "w") as f:
            json.dump([], f)  # Si no existe, creamos una lista vacía

    with open(ARCHIVO_LOG, "r") as f:
        logs = json.load(f)  # Leemos los logs existentes

    logs.append(data)  # Agregamos la nueva entrada

    with open(ARCHIVO_LOG, "w") as f:
        json.dump(logs, f, indent=4)  # Guardamos todo actualizado

# Esta función se ejecuta automáticamente antes de cada petición
@app.before_request
def registrar_peticion():
    datos = {
        "momento": datetime.utcnow().isoformat(),
        "ip_origen": request.remote_addr,
        "user_agent": request.headers.get("User-Agent"),
        "metodo": request.method,
        "ruta": request.path,
        "params_url": request.args.to_dict(),
        "formulario": request.form.to_dict(),
        "json_enviado": request.get_json(silent=True),
        "encabezados": dict(request.headers),
    }

    guardar_log(datos)  # Guardamos la información

# Ruta simulada de API: responde 404 a todo
@app.route("/api/", defaults={"path": ""})
@app.route("/api/<path:path>")
def todo_no_encontrado(path):
    return jsonify({"error": "Ruta no válida"}), 404

# Ejecutamos la app con soporte SSL
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, ssl_context=("cert.pem", "key.pem"))
