"""
VERIFICADOR DE ESTADO DE URLs - Script Educativo
=================================================
Este script verifica si una URL está disponible y devuelve su código
de estado HTTP.

¿QUÉ SON LOS CÓDIGOS DE ESTADO HTTP?
Son números de 3 dígitos que los servidores web devuelven para indicar
el resultado de una petición:
- 2xx = Éxito (200 OK)
- 3xx = Redirección (301 Moved, 302 Found)
- 4xx = Error del cliente (404 Not Found, 403 Forbidden)
- 5xx = Error del servidor (500 Internal Server Error)

¿PARA QUÉ SIRVE?
- Verificar si un sitio web está online
- Comprobar enlaces rotos
- Monitorizar la disponibilidad de servicios
- Testing de APIs y endpoints

¿QUÉ APRENDERÁS?
- Códigos de estado HTTP
- Manejo de timeouts en peticiones
- Normalización de URLs
- Uso de argparse para crear CLIs
- Manejo específico de excepciones

REQUISITOS:
    pip install requests

EJEMPLOS DE USO:
    python check-url.py --url https://www.google.com
    python check-url.py --url google.com
    python check-url.py --url http://httpstat.us/404
"""

# Importamos las librerías necesarias
import requests  # Para hacer peticiones HTTP
import argparse  # Para crear una interfaz de línea de comandos


# CONFIGURACIÓN DE ARGUMENTOS DE LÍNEA DE COMANDOS
# -------------------------------------------------
# Creamos el parser para procesar argumentos
parser = argparse.ArgumentParser(
    description="Comprobar el estado HTTP de una URL.",
    epilog="Ejemplo: python check-url.py --url https://www.google.com"
)

# Definimos el argumento --url
parser.add_argument(
    "--url",
    type=str,
    help="La URL a comprobar (ej: https://www.google.com o google.com)"
)

# Procesamos los argumentos proporcionados por el usuario
args = parser.parse_args()


# FUNCIÓN 1: NORMALIZAR URL
# --------------------------
def ensure_https(url):
    """
    Asegura que la URL tenga un protocolo (http:// o https://).
    
    Si el usuario escribe "google.com", lo convierte a "https://google.com"
    Si ya tiene protocolo, lo deja como está.
    
    Parámetros:
        url (str): URL que puede o no tener protocolo
    
    Retorna:
        str: URL con protocolo incluido
    
    Ejemplos:
        ensure_https("google.com") → "https://google.com"
        ensure_https("http://google.com") → "http://google.com"
        ensure_https("https://google.com") → "https://google.com"
    """
    # Verificamos si la URL NO empieza con http:// ni https://
    if not url.startswith("http://") and not url.startswith("https://"):
        # Si no tiene protocolo, añadimos https:// por defecto
        return "https://" + url
    
    # Si ya tiene protocolo, la retornamos sin cambios
    return url


# FUNCIÓN 2: VERIFICAR ENDPOINT
# ------------------------------
def check_endpoint(url):
    """
    Realiza una petición HTTP GET a la URL y devuelve el código de estado.
    
    Esta función intenta conectarse a la URL y obtener su código de respuesta.
    Maneja específicamente dos tipos de errores:
    - Timeout: cuando la conexión tarda demasiado
    - RequestException: cualquier otro error de red
    
    Parámetros:
        url (str): URL completa a verificar (con protocolo)
    
    Retorna:
        int: Código de estado HTTP, o valores especiales:
             - 0 si hay timeout
             - 99 si hay otro tipo de error
    """
    try:
        # requests.get() hace una petición HTTP GET a la URL
        # timeout=10 significa que esperamos máximo 10 segundos
        # Si tarda más, se lanza una excepción Timeout
        response = requests.get(url, timeout=10)
        
        # response.status_code contiene el código HTTP (200, 404, 500, etc.)
        return response.status_code
        
    except requests.Timeout:
        # Si la petición tarda más de 10 segundos
        # Retornamos 0 como código especial para timeout
        return 0
        
    except requests.RequestException:
        # RequestException captura todos los demás errores:
        # - Problemas de conexión
        # - DNS no resuelve
        # - URL inválida
        # - Certificado SSL inválido, etc.
        # Retornamos 99 como código especial para error general
        return 99


# FUNCIÓN 3: TRADUCIR CÓDIGOS DE ESTADO
# --------------------------------------
def translate_status_code(code):
    """
    Traduce un código de estado numérico a un mensaje descriptivo.
    
    Los códigos HTTP son números, pero es más útil ver qué significan.
    Esta función proporciona una descripción en español de los códigos
    más comunes.
    
    Parámetros:
        code (int): Código de estado HTTP
    
    Retorna:
        str: Descripción del código en español
    
    CATEGORÍAS DE CÓDIGOS HTTP:
        1xx - Informativos (raro verlos)
        2xx - Éxito
        3xx - Redirección
        4xx - Error del cliente (problema con la petición)
        5xx - Error del servidor (problema en el servidor)
    """
    # Diccionario con los códigos más comunes y su significado
    translations = {
        # Códigos especiales (no estándar HTTP)
        0:   "Timeout (tiempo de espera agotado)",
        99:  "Error de conexión",
        
        # Códigos 2xx - Éxito
        200: "OK (petición exitosa)",
        
        # Códigos 3xx - Redirección
        301: "Moved Permanently (movido permanentemente)",
        302: "Found (encontrado, redirección temporal)",
        
        # Códigos 4xx - Error del cliente
        400: "Bad Request (petición incorrecta)",
        401: "Unauthorized (no autorizado, falta autenticación)",
        403: "Forbidden (prohibido, sin permisos)",
        404: "Not Found (no encontrado)",
        
        # Códigos 5xx - Error del servidor
        500: "Internal Server Error (error interno del servidor)",
        503: "Service Unavailable (servicio no disponible)"
    }
    
    # get() busca el código en el diccionario
    # Si no lo encuentra, retorna "Estado desconocido"
    return translations.get(code, "Estado desconocido")


# CÓDIGO PRINCIPAL DEL SCRIPT
# ----------------------------
if args.url:
    # El usuario proporcionó una URL
    
    # PASO 1: Normalizar la URL (asegurar que tenga protocolo)
    url = ensure_https(args.url)
    
    # PASO 2: Verificar el endpoint (hacer la petición HTTP)
    print(f"Verificando: {url}")
    status_code = check_endpoint(url)
    
    # PASO 3: Traducir el código de estado a texto legible
    status_text = translate_status_code(status_code)
    
    # PASO 4: Mostrar el resultado
    print(f"\nResultado:")
    print(f"  URL: {url}")
    print(f"  Código: {status_code}")
    print(f"  Estado: {status_text}")
    
    # Indicador visual según el resultado
    if status_code == 200:
        print(f"  ✓ La URL está disponible")
    elif status_code in [301, 302]:
        print(f"  ↻ La URL redirige a otra ubicación")
    elif status_code >= 400 and status_code < 500:
        print(f"  ⚠️ Error en la petición")
    elif status_code >= 500:
        print(f"  ❌ Error en el servidor")
    else:
        print(f"  ⚠️ Problema de conexión")
        
else:
    # El usuario NO proporcionó una URL
    print("Error: Debes especificar una URL con --url")
    print("\nEjemplos de uso:")
    print("  python check-url.py --url https://www.google.com")
    print("  python check-url.py --url google.com")
    print("  python check-url.py --url http://httpstat.us/404")
    print("\nPara ver ayuda completa: python check-url.py --help")

# CÓDIGOS DE ESTADO HTTP MÁS COMUNES:
# ------------------------------------
# 200 OK - Todo correcto
# 301 Moved Permanently - Recurso movido permanentemente
# 302 Found - Redirección temporal
# 304 Not Modified - Recurso no modificado (caché)
# 400 Bad Request - Petición mal formada
# 401 Unauthorized - Requiere autenticación
# 403 Forbidden - Sin permisos para acceder
# 404 Not Found - Recurso no encontrado
# 500 Internal Server Error - Error en el servidor
# 502 Bad Gateway - Error en el gateway/proxy
# 503 Service Unavailable - Servicio temporalmente no disponible
