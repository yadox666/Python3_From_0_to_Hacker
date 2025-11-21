"""
API REST SEGURA CON HTTPS (Puerto 443) - Script Educativo
==========================================================
Este script crea una API REST que usa HTTPS (conexión segura cifrada)
en el puerto 443, el puerto estándar para tráfico web seguro.

¿QUÉ ES HTTPS?
HTTPS = HTTP + SSL/TLS (cifrado)
Es la versión segura de HTTP que cifra la comunicación entre cliente
y servidor, protegiendo los datos de ser interceptados.

¿POR QUÉ USAR EL PUERTO 443?
- Puerto estándar para HTTPS (como 80 es para HTTP)
- Los navegadores usan automáticamente 443 para URLs con https://
- No requiere especificar el puerto en la URL

¿QUÉ APRENDERÁS?
- Diferencia entre HTTP (puerto 80) y HTTPS (puerto 443)
- Cómo usar certificados SSL/TLS en Flask
- Por qué el cifrado es importante en APIs
- Cómo crear certificados autofirmados para desarrollo

REQUISITOS:
1. Instalar Flask: pip install flask
2. Crear certificados SSL con este comando en la terminal:
   openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
3. Ejecutar con permisos de administrador (sudo) porque el puerto 443 es privilegiado

CÓMO PROBAR ESTE SCRIPT:
1. Ejecuta: sudo python api_users_443.py
2. Abre tu navegador: https://127.0.0.1/api/users
3. O usa curl: curl -k https://127.0.0.1/api/users
   (La opción -k ignora la advertencia del certificado autofirmado)

NOTA: Los navegadores mostrarán una advertencia de seguridad porque el
certificado es autofirmado (no está firmado por una autoridad certificadora).
Esto es normal en desarrollo, pero en producción debes usar certificados válidos.
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

@app.route("/api/users", methods=["GET"])
def obtener_usuarios():
    """
    Endpoint principal: Devuelve la lista de todos los usuarios.
    
    RUTA: /api/users
    MÉTODO HTTP: GET (se usa para obtener información)
    PROTOCOLO: HTTPS (conexión cifrada)
    
    Retorna:
        tuple: (datos_json, codigo_estado)
               - datos_json: Lista de usuarios en formato JSON
               - codigo_estado: 200 (significa "OK, petición exitosa")
    
    EJEMPLO DE USO:
        Desde el navegador: https://127.0.0.1/api/users
        Desde curl: curl -k https://127.0.0.1/api/users
        
    NOTA: El candado 🔒 en el navegador indica que la conexión es segura.
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
    
    Este endpoint maneja todas las URLs que NO son /api/users
    Por ejemplo: /, /api/productos, /otra/ruta, etc.
    
    Parámetros:
        ruta (str): La ruta que el usuario intentó acceder
    
    Retorna:
        tuple: (mensaje_error_json, codigo_estado)
               - mensaje_error_json: Mensaje de error en JSON
               - codigo_estado: 404 (significa "No encontrado")
    
    EJEMPLO:
        Si visitas https://127.0.0.1/cualquier-cosa
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
    print("API REST SEGURA (HTTPS) - SERVIDOR INICIADO")
    print("=" * 70)
    print()
    print("Configuración:")
    print("  - Host: 127.0.0.1 (localhost, solo accesible desde este equipo)")
    print("  - Puerto: 443 (puerto estándar HTTPS)")
    print("  - Protocolo: HTTPS (conexión cifrada con SSL/TLS)")
    print("  - Certificado: cert.pem")
    print("  - Clave privada: key.pem")
    print()
    print("Endpoints disponibles:")
    print("  - GET /api/users  → Obtener lista de todos los usuarios")
    print()
    print("Prueba la API:")
    print("  - Navegador: https://127.0.0.1/api/users")
    print("  - Curl:      curl -k https://127.0.0.1/api/users")
    print()
    print("IMPORTANTE:")
    print("  - Debes ejecutar con sudo: sudo python api_users_443.py")
    print("  - Los navegadores mostrarán advertencia (certificado autofirmado)")
    print("  - Esto es normal en desarrollo, acepta la advertencia para continuar")
    print()
    print("Presiona Ctrl+C para detener el servidor")
    print("=" * 70)
    print()
    
    # Iniciamos el servidor Flask
    # host="127.0.0.1": solo acepta conexiones desde este equipo (localhost)
    # port=443: puerto estándar para HTTPS (requiere permisos de administrador)
    # ssl_context: tupla con los archivos de certificado y clave privada
    #              Estos archivos permiten el cifrado SSL/TLS
    # debug=False: modo producción (cambia a True para desarrollo)
    app.run(
        host="127.0.0.1", 
        port=443, 
        ssl_context=("cert.pem", "key.pem"),
        debug=False
    )

# DIFERENCIAS ENTRE HTTP Y HTTPS:
# --------------------------------
# HTTP (Puerto 80):
#   - Tráfico sin cifrar (texto plano)
#   - Cualquiera puede interceptar y leer los datos
#   - No verifica la identidad del servidor
#   - Usado solo para sitios sin datos sensibles
#
# HTTPS (Puerto 443):
#   - Tráfico cifrado con SSL/TLS
#   - Los datos están protegidos contra interceptación
#   - Verifica la identidad del servidor con certificados
#   - Obligatorio para login, pagos, datos personales
#
# CÓMO FUNCIONA SSL/TLS:
# ----------------------
# 1. Cliente se conecta al servidor
# 2. Servidor envía su certificado (cert.pem)
# 3. Cliente verifica el certificado
# 4. Se establece una clave de cifrado compartida
# 5. Toda la comunicación posterior está cifrada
#
# CERTIFICADOS EN PRODUCCIÓN:
# ---------------------------
# Para producción, NO uses certificados autofirmados.
# Usa servicios como:
# - Let's Encrypt (gratuito, renovación automática)
# - Cloudflare SSL (gratuito)
# - Certificados comerciales (Digicert, GoDaddy, etc.)
