"""
HONEYPOT API CON GEOLOCALIZACIÓN - Script Educativo
====================================================
Este script crea un "honeypot" (trampa de miel) que simula una API falsa.
Su propósito es detectar y registrar intentos de acceso no autorizados.

¿QUÉ ES UN HONEYPOT?
Un honeypot es un sistema señuelo que parece vulnerable para atraer atacantes
y estudiar sus técnicas, sin poner en riesgo sistemas reales.

REQUISITOS PREVIOS:
1. Instalar Flask: pip install flask
2. Instalar requests: pip install requests
3. Crear certificados SSL con este comando:
   openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
4. Ejecutar con permisos de administrador (sudo) si usas el puerto 443
"""

# Importamos las librerías necesarias
from flask import Flask, request, jsonify  # Flask: para crear el servidor web
import json  # Para trabajar con archivos JSON
import os  # Para operaciones con el sistema operativo
from datetime import datetime  # Para obtener la fecha y hora actual
import requests  # Para hacer peticiones HTTP a APIs externas

# Creamos la aplicación Flask (nuestro servidor web)
app = Flask(__name__)

# CONFIGURACIÓN DEL SCRIPT
# ------------------------
# Nombre del archivo donde guardaremos los registros de accesos
ARCHIVO_REGISTRO = "honeypot_log.json"


def obtener_geolocalizacion(direccion_ip):
    """
    Obtiene información de geolocalización de una dirección IP.
    
    Esta función consulta un servicio web gratuito (ip-api.com) que nos dice
    desde dónde está conectándose el usuario (país, ciudad, proveedor, etc.)
    
    Parámetros:
        direccion_ip (str): La dirección IP a consultar (ej: "192.168.1.1")
    
    Retorna:
        dict: Diccionario con datos de ubicación, o {} si hay error
    """
    try:
        # Hacemos una petición HTTP a la API de geolocalización
        url = f"http://ip-api.com/json/{direccion_ip}"
        respuesta = requests.get(url)
        
        # Verificamos que la petición fue exitosa (código 200 = OK)
        if respuesta.status_code == 200:
            # Convertimos la respuesta JSON en un diccionario de Python
            datos_geograficos = respuesta.json()
            
            # Verificamos que la consulta fue exitosa
            if datos_geograficos.get("status") == "success":
                # Creamos un diccionario con los datos más importantes
                informacion_ubicacion = {
                    "pais": datos_geograficos.get("country"),
                    "region": datos_geograficos.get("regionName"),
                    "ciudad": datos_geograficos.get("city"),
                    "latitud": datos_geograficos.get("lat"),
                    "longitud": datos_geograficos.get("lon"),
                    "proveedor_internet": datos_geograficos.get("isp"),
                    "organizacion": datos_geograficos.get("org"),
                }
                return informacion_ubicacion
                
    except Exception as error:
        # Si algo sale mal, mostramos el error
        print(f"Error al obtener datos de geolocalización: {error}")
    
    # Si hubo algún error, retornamos un diccionario vacío
    return {}


def guardar_registro(datos):
    """
    Guarda los datos de un acceso en el archivo de registro.
    
    Esta función almacena toda la información de cada petición HTTP que
    recibe nuestro servidor en un archivo JSON.
    
    Parámetros:
        datos (dict): Diccionario con la información a guardar
    """
    # Verificamos si el archivo de registro existe
    if not os.path.exists(ARCHIVO_REGISTRO):
        # Si no existe, lo creamos con una lista vacía
        with open(ARCHIVO_REGISTRO, "w") as archivo:
            json.dump([], archivo)
    
    # Leemos los registros existentes del archivo
    with open(ARCHIVO_REGISTRO, "r") as archivo:
        registros_existentes = json.load(archivo)
    
    # Añadimos el nuevo registro a la lista
    registros_existentes.append(datos)
    
    # Guardamos la lista actualizada en el archivo
    # indent=4 hace que el JSON sea más legible (con sangría)
    with open(ARCHIVO_REGISTRO, "w") as archivo:
        json.dump(registros_existentes, archivo, indent=4)
    
    # Mostramos en la consola que se guardó un nuevo registro
    print(f"[NUEVO ACCESO] IP: {datos['ip_origen']} - Ruta: {datos['ruta_solicitada']}")


@app.before_request
def registrar_peticion_entrante():
    """
    Esta función se ejecuta ANTES de cada petición HTTP que reciba el servidor.
    
    El decorador @app.before_request hace que Flask ejecute esta función
    automáticamente antes de procesar cualquier solicitud.
    
    Aquí capturamos toda la información del atacante/visitante.
    """
    # Obtenemos la dirección IP del cliente que está haciendo la petición
    ip_cliente = request.remote_addr
    
    # Creamos un diccionario con toda la información de la petición
    datos_registro = {
        # Fecha y hora actual en formato ISO (ej: "2025-11-21T10:30:45")
        "fecha_hora": datetime.utcnow().isoformat(),
        
        # IP del cliente
        "ip_origen": ip_cliente,
        
        # User-Agent: información sobre el navegador/herramienta usada
        "navegador": request.headers.get("User-Agent"),
        
        # Método HTTP usado (GET, POST, PUT, DELETE, etc.)
        "metodo_http": request.method,
        
        # Ruta/URL solicitada (ej: "/api/users")
        "ruta_solicitada": request.path,
        
        # Parámetros de la URL (ej: en /api/users?id=5, sería {"id": "5"})
        "parametros_url": request.args.to_dict(),
        
        # Datos enviados en formularios HTML
        "datos_formulario": request.form.to_dict(),
        
        # Datos enviados en formato JSON
        "datos_json": request.get_json(silent=True),
        
        # Todas las cabeceras HTTP de la petición
        "cabeceras_http": dict(request.headers),
        
        # Información geográfica del IP
        "ubicacion_geografica": obtener_geolocalizacion(ip_cliente)
    }
    
    # Guardamos toda esta información en nuestro archivo de registro
    guardar_registro(datos_registro)


# DEFINICIÓN DE RUTAS (ENDPOINTS) DEL API
# ----------------------------------------
@app.route("/api/", defaults={"ruta": ""})
@app.route("/api/<path:ruta>")
def capturar_todas_las_rutas(ruta):
    """
    Esta función captura TODAS las peticiones que empiecen con /api/
    
    El decorador @app.route define qué URLs manejará esta función.
    <path:ruta> significa que acepta cualquier texto después de /api/
    
    Parámetros:
        ruta (str): La ruta que el usuario intentó acceder
    
    Retorna:
        tuple: Una respuesta JSON con error 404 (No encontrado)
    """
    # Respondemos con un error 404 (Not Found) para cualquier ruta
    # Esto simula una API que no tiene ese endpoint
    return jsonify({"error": "Recurso no encontrado"}), 404


# PUNTO DE ENTRADA DEL PROGRAMA
# ------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("HONEYPOT API CON GEOLOCALIZACIÓN")
    print("=" * 70)
    print()
    print("Configuración:")
    print(f"  - Puerto: 443 (HTTPS)")
    print(f"  - Host: 0.0.0.0 (todas las interfaces de red)")
    print(f"  - Certificado SSL: cert.pem")
    print(f"  - Clave privada: key.pem")
    print(f"  - Archivo de registro: {ARCHIVO_REGISTRO}")
    print()
    print("IMPORTANTE:")
    print("  - Debes ejecutar este script con 'sudo' para usar el puerto 443")
    print("  - Asegúrate de tener los archivos cert.pem y key.pem")
    print()
    print("El servidor está escuchando...")
    print("Presiona Ctrl+C para detener")
    print("=" * 70)
    print()
    
    # Iniciamos el servidor Flask
    # host="0.0.0.0": acepta conexiones desde cualquier dirección IP
    # port=443: puerto estándar para HTTPS
    # ssl_context: archivos de certificado para conexiones seguras (HTTPS)
    app.run(
        host="0.0.0.0",
        port=443,
        ssl_context=("cert.pem", "key.pem")
    )
