"""
API REST SIMPLE DE USUARIOS - Script Educativo
===============================================
Este script crea una API REST básica que devuelve una lista de usuarios.

¿QUÉ ES UNA API REST?
Una API REST es un servicio web que permite a aplicaciones comunicarse entre sí
usando el protocolo HTTP. Es como un "menú" de funciones que tu aplicación ofrece.

¿QUÉ APRENDERÁS?
- Cómo crear un servidor web con Flask
- Qué son los endpoints (rutas) de una API
- Cómo devolver datos en formato JSON
- Qué son los códigos de estado HTTP (200, 404)
- Cómo manejar peticiones GET

REQUISITOS:
1. Instalar Flask: pip install flask

CÓMO PROBAR ESTE SCRIPT:
1. Ejecuta este script: python api_users.py
2. Abre tu navegador y visita: http://127.0.0.1:8000/users
3. También puedes usar curl desde la terminal:
   curl http://127.0.0.1:8000/users
"""

# Importamos las librerías necesarias
from flask import Flask, jsonify  # Flask: para crear el servidor web
                                   # jsonify: para convertir datos Python a JSON

# Creamos la aplicación Flask
# __name__ le dice a Flask dónde está ubicado nuestro código
app = Flask(__name__)

# DATOS DE EJEMPLO
# ----------------
# Esta es una lista de diccionarios que simula una base de datos de usuarios
# En una aplicación real, estos datos vendrían de una base de datos
usuarios_falsos = [
    {
        "id": 1,
        "nombre": "Alicia García",
        "email": "alicia@ejemplo.com"
    },
    {
        "id": 2,
        "nombre": "Roberto Martínez",
        "email": "roberto@ejemplo.com"
    },
    {
        "id": 3,
        "nombre": "Carlos López",
        "email": "carlos@ejemplo.com"
    },
]


# DEFINICIÓN DE ENDPOINTS (RUTAS)
# --------------------------------

@app.route("/users", methods=["GET"])
def obtener_usuarios():
    """
    Endpoint principal: Devuelve la lista de todos los usuarios.
    
    RUTA: /users
    MÉTODO HTTP: GET (se usa para obtener información)
    
    Retorna:
        tuple: (datos_json, codigo_estado)
               - datos_json: Lista de usuarios en formato JSON
               - codigo_estado: 200 (significa "OK, petición exitosa")
    
    EJEMPLO DE USO:
        Desde el navegador: http://127.0.0.1:8000/users
        Desde curl: curl http://127.0.0.1:8000/users
    """
    # jsonify() convierte nuestra lista de Python a formato JSON
    # JSON es el formato estándar para intercambiar datos en APIs
    # El 200 es el código HTTP que significa "éxito"
    return jsonify(usuarios_falsos), 200


@app.route("/", defaults={"ruta": ""})
@app.route("/<path:ruta>")
def capturar_otras_rutas(ruta):
    """
    Endpoint comodín: Captura cualquier otra ruta que no exista.
    
    Este endpoint maneja todas las URLs que NO son /users
    Por ejemplo: /, /algo, /otra/ruta, etc.
    
    Parámetros:
        ruta (str): La ruta que el usuario intentó acceder
    
    Retorna:
        tuple: (mensaje_error_json, codigo_estado)
               - mensaje_error_json: Mensaje de error en JSON
               - codigo_estado: 404 (significa "No encontrado")
    
    EJEMPLO:
        Si visitas http://127.0.0.1:8000/cualquier-cosa
        Recibirás: {"error": "Ruta no encontrada"} con código 404
    """
    # Devolvemos un error 404 (Not Found) para rutas que no existen
    return jsonify({"error": "Ruta no encontrada"}), 404


# PUNTO DE ENTRADA DEL PROGRAMA
# ------------------------------
if __name__ == "__main__":
    """
    Este bloque solo se ejecuta si ejecutas el script directamente
    (no cuando lo importas como módulo en otro script)
    """
    print("=" * 70)
    print("API REST DE USUARIOS - SERVIDOR INICIADO")
    print("=" * 70)
    print()
    print("Configuración:")
    print("  - Host: 127.0.0.1 (localhost, solo accesible desde este equipo)")
    print("  - Puerto: 8000")
    print("  - Protocolo: HTTP")
    print()
    print("Endpoints disponibles:")
    print("  - GET /users  → Obtener lista de todos los usuarios")
    print()
    print("Prueba la API:")
    print("  - Navegador: http://127.0.0.1:8000/users")
    print("  - Curl:      curl http://127.0.0.1:8000/users")
    print()
    print("Presiona Ctrl+C para detener el servidor")
    print("=" * 70)
    print()
    
    # Iniciamos el servidor Flask
    # host="127.0.0.1": solo acepta conexiones desde este equipo (localhost)
    # port=8000: el servidor escuchará en el puerto 8000
    # debug=False: modo producción (cambia a True para desarrollo)
    app.run(host="127.0.0.1", port=8000, debug=False)
