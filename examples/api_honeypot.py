"""
HONEYPOT API SIMPLE - Script Educativo
=======================================
Este script crea un "honeypot" (trampa de miel) básico que simula una API
y registra todos los intentos de acceso, incluyendo posibles ataques.

¿QUÉ ES UN HONEYPOT?
Un honeypot es un sistema señuelo diseñado para:
- Atraer atacantes a un sistema falso
- Estudiar sus técnicas y herramientas
- Detectar actividad maliciosa
- Proteger sistemas reales desviando ataques

¿CÓMO FUNCIONA ESTE HONEYPOT?
1. Simula una API que parece real
2. Registra TODA la información de cada petición
3. Responde con errores 404 (como si las rutas no existieran)
4. Guarda los datos en un archivo JSON para análisis posterior

¿QUÉ INFORMACIÓN CAPTURA?
- Dirección IP del atacante/visitante
- Fecha y hora exacta del acceso
- Navegador/herramienta utilizada (User-Agent)
- Qué ruta intentó acceder
- Qué método HTTP usó (GET, POST, etc.)
- Todos los datos enviados (parámetros, formularios, JSON)
- Todas las cabeceras HTTP

¿QUÉ APRENDERÁS?
- Concepto de honeypots en seguridad
- Cómo interceptar peticiones con @app.before_request
- Registro detallado de actividad HTTP
- Análisis de intentos de ataque

REQUISITOS:
1. Instalar Flask: pip install flask
2. Crear certificados SSL:
   openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
3. Ejecutar con sudo (para usar puerto 443): sudo python api_honeypot.py

CÓMO PROBAR:
    curl -k https://127.0.0.1/api/usuarios
    curl -k -X POST https://127.0.0.1/api/login -d "user=admin&pass=123"

Luego revisa el archivo "registro_honeypot.json" para ver los datos capturados.
"""

# Importamos las librerías necesarias
from flask import Flask, request, jsonify  # Flask: para crear el servidor web
import json       # Para trabajar con archivos JSON
import os         # Para operaciones con archivos del sistema
from datetime import datetime  # Para obtener fecha y hora

# Creamos la aplicación Flask
app = Flask(__name__)

# CONFIGURACIÓN
# -------------
# Nombre del archivo donde guardaremos todos los registros de acceso
ARCHIVO_LOG = "registro_honeypot.json"


# FUNCIÓN DE REGISTRO
# --------------------
def guardar_log(data):
    """
    Guarda la información de cada petición HTTP en un archivo JSON.
    
    Esta función mantiene un historial de TODAS las peticiones recibidas,
    lo cual es crucial para analizar intentos de ataque o escaneos.
    
    Parámetros:
        data (dict): Diccionario con toda la información de la petición
    """
    # Si el archivo de logs no existe, lo creamos con una lista vacía
    if not os.path.exists(ARCHIVO_LOG):
        with open(ARCHIVO_LOG, "w") as f:
            json.dump([], f)

    # Leemos los logs existentes
    with open(ARCHIVO_LOG, "r") as f:
        logs = json.load(f)

    # Agregamos la nueva entrada al final de la lista
    logs.append(data)

    # Guardamos todo de nuevo en el archivo
    # indent=4 hace que el JSON sea legible (con formato)
    with open(ARCHIVO_LOG, "w") as f:
        json.dump(logs, f, indent=4)
    
    # Mostramos en consola que se registró un acceso
    print(f"[ACCESO REGISTRADO] IP: {data['ip_origen']} - Ruta: {data['ruta']}")


# INTERCEPTOR DE PETICIONES
# --------------------------
@app.before_request
def registrar_peticion():
    """
    Esta función se ejecuta AUTOMÁTICAMENTE antes de cada petición HTTP.
    
    El decorador @app.before_request hace que Flask llame a esta función
    antes de procesar cualquier solicitud, sin importar la ruta.
    
    Aquí capturamos toda la información posible del cliente (atacante/visitante).
    """
    # Creamos un diccionario con toda la información de la petición
    datos = {
        # Fecha y hora en formato ISO (ej: "2025-11-21T15:30:45.123456")
        # utcnow() usa tiempo UTC (coordinado universal)
        "momento": datetime.utcnow().isoformat(),
        
        # Dirección IP del cliente que hizo la petición
        # Esta es información CRÍTICA para identificar atacantes
        "ip_origen": request.remote_addr,
        
        # User-Agent: identifica el navegador/herramienta usada
        # Los atacantes a veces usan herramientas que se identifican claramente
        # Ejemplos: "curl/7.68.0", "python-requests/2.28.1", "Nmap Scripting Engine"
        "user_agent": request.headers.get("User-Agent"),
        
        # Método HTTP usado (GET, POST, PUT, DELETE, etc.)
        # Los atacantes suelen probar diferentes métodos
        "metodo": request.method,
        
        # Ruta/URL solicitada (ej: "/api/users", "/api/admin", etc.)
        # Analizar las rutas ayuda a identificar qué buscan los atacantes
        "ruta": request.path,
        
        # Parámetros en la URL (ej: en /api/users?id=5 sería {"id": "5"})
        # Los atacantes pueden intentar inyecciones SQL aquí
        "params_url": request.args.to_dict(),
        
        # Datos enviados en formularios HTML (POST con application/x-www-form-urlencoded)
        # Captura intentos de login falsos, etc.
        "formulario": request.form.to_dict(),
        
        # Datos enviados en formato JSON (muy común en APIs modernas)
        # silent=True evita errores si no es JSON válido
        "json_enviado": request.get_json(silent=True),
        
        # TODAS las cabeceras HTTP de la petición
        # Contiene información valiosa sobre el cliente
        "encabezados": dict(request.headers),
    }

    # Guardamos toda esta información en nuestro archivo de logs
    guardar_log(datos)


# ENDPOINTS DEL HONEYPOT
# -----------------------
@app.route("/api/", defaults={"path": ""})
@app.route("/api/<path:path>")
def todo_no_encontrado(path):
    """
    Endpoint comodín que captura TODAS las rutas bajo /api/.
    
    Este endpoint simula una API que no tiene recursos disponibles,
    respondiendo siempre con 404 (Not Found). Esto hace que el honeypot
    parezca una API real pero sin funcionalidad.
    
    Parámetros:
        path (str): Cualquier ruta que el usuario/atacante intente acceder
    
    Retorna:
        tuple: Error 404 en formato JSON
    
    EJEMPLOS DE RUTAS QUE CAPTURA:
        /api/users          → 404
        /api/admin          → 404
        /api/login          → 404
        /api/cualquier/cosa → 404
    """
    # Respondemos con un error 404 genérico
    # Esto hace que el atacante no sepa si la ruta existe o no
    return jsonify({"error": "Ruta no válida"}), 404


# PUNTO DE ENTRADA DEL PROGRAMA
# ------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("HONEYPOT API - SISTEMA DE DETECCIÓN INICIADO")
    print("=" * 70)
    print()
    print("Configuración:")
    print("  - Puerto: 443 (HTTPS)")
    print("  - Host: 0.0.0.0 (accesible desde cualquier IP)")
    print("  - Certificado SSL: cert.pem")
    print("  - Clave privada: key.pem")
    print(f"  - Archivo de registro: {ARCHIVO_LOG}")
    print()
    print("Estado: ACTIVO - Registrando todos los accesos")
    print()
    print("IMPORTANTE:")
    print("  - Ejecuta con sudo para usar el puerto 443")
    print("  - Todos los accesos se guardan en registro_honeypot.json")
    print("  - Revisa el archivo periódicamente para detectar ataques")
    print()
    print("Presiona Ctrl+C para detener")
    print("=" * 70)
    print()
    
    # Iniciamos el servidor Flask con HTTPS
    # host="0.0.0.0": acepta conexiones desde cualquier IP (no solo localhost)
    # port=443: puerto estándar HTTPS (requiere sudo)
    # ssl_context: archivos de certificado para cifrado SSL/TLS
    app.run(
        host="0.0.0.0",
        port=443,
        ssl_context=("cert.pem", "key.pem")
    )

# ANÁLISIS DE LOGS:
# -----------------
# Después de recopilar datos, busca patrones sospechosos:
#
# 1. ESCANEOS DE PUERTOS:
#    - Múltiples IPs intentando conectarse
#    - Peticiones a rutas comunes (/admin, /login, /api/v1)
#
# 2. INYECCIONES SQL:
#    - Parámetros con comillas, OR, UNION, SELECT, etc.
#    - Ejemplo: /api/users?id=1' OR '1'='1
#
# 3. HERRAMIENTAS AUTOMATIZADAS:
#    - User-Agent reveladores: sqlmap, Nmap, nikto, etc.
#    - Múltiples peticiones rápidas desde la misma IP
#
# 4. INTENTOS DE AUTENTICACIÓN:
#    - POST a /api/login, /api/auth, etc.
#    - Datos de formulario con "user", "pass", "admin"
#
# 5. PATH TRAVERSAL:
#    - Rutas con ../, ..\\, etc.
#    - Intentos de acceder a archivos del sistema
#
# COMANDO ÚTIL PARA ANALIZAR LOGS:
# jq '.[] | select(.metodo == "POST")' registro_honeypot.json
# (Muestra solo las peticiones POST usando jq)
