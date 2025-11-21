"""
ESCÁNER DE PUERTOS CON NMAP - Script Educativo
===============================================
Este script utiliza Nmap para escanear puertos de un equipo y detectar
servicios que están escuchando en esos puertos.

¿QUÉ ES NMAP?
Nmap es una herramienta de seguridad que permite descubrir hosts y servicios
en una red. Es usado por administradores de sistemas y especialistas en seguridad.

¿QUÉ SON LOS PUERTOS?
Los puertos son "puertas" numéricas donde los servicios escuchan conexiones:
- Puerto 80: HTTP (páginas web)
- Puerto 443: HTTPS (páginas web seguras)
- Puerto 22: SSH (conexión remota segura)
- Puerto 3306: MySQL (base de datos)

¿QUÉ APRENDERÁS?
- Cómo usar python-nmap para escanear puertos
- Estructuras de datos anidadas (diccionarios dentro de diccionarios)
- Cómo guardar resultados en formato JSON
- Iteración sobre múltiples niveles de datos

REQUISITOS:
- Tener Nmap instalado en el sistema (sudo apt install nmap / brew install nmap)
- Instalar el módulo de Python: pip install python-nmap

ADVERTENCIA:
Escanear puertos sin permiso puede ser ilegal. Usa solo en tus propios sistemas
o con autorización explícita.
"""

# Importamos las librerías necesarias
import nmap  # Librería para controlar Nmap desde Python
import json  # Para guardar resultados como archivo JSON


# PASO 1: CREAR EL ESCÁNER
# -------------------------
# PortScanner() es el objeto que nos permite realizar escaneos
scanner = nmap.PortScanner()


# PASO 2: CONFIGURAR EL ESCANEO
# ------------------------------
# Definimos qué queremos escanear y qué puertos queremos revisar

objetivo = "127.0.0.1"      # Dirección IP del equipo a escanear
                            # 127.0.0.1 = localhost (tu propio equipo)
                            # También puedes usar: "192.168.1.1", "scanme.nmap.org", etc.

puertos = "1-1024"          # Rango de puertos a revisar
                            # 1-1024 son los puertos "well-known" (más comunes)
                            # También puedes usar: "22,80,443" o "1-65535"


# PASO 3: EJECUTAR EL ESCANEO
# ----------------------------
print(f"Escaneando {objetivo} en puertos {puertos}...")

# scan() ejecuta el escaneo de puertos
# hosts: el objetivo a escanear (puede ser múltiples IPs)
# ports: el rango de puertos a verificar
scanner.scan(hosts=objetivo, ports=puertos)


# PASO 4: PROCESAR Y ESTRUCTURAR LOS RESULTADOS
# ----------------------------------------------
# Creamos un diccionario vacío donde guardaremos toda la información
resultado_escaneo = {}

# all_hosts() devuelve una lista con todas las IPs escaneadas
# En este caso será solo una: ["127.0.0.1"]
for host in scanner.all_hosts():
    # Para cada host, creamos un diccionario con su estado y protocolos
    resultado_escaneo[host] = {
        "estado": scanner[host].state(),  # Estado del host: "up" (online) o "down" (offline)
        "protocolos": {}                  # Diccionario para guardar info de cada protocolo
    }

    # all_protocols() devuelve los protocolos encontrados (tcp, udp, etc.)
    # Normalmente será ["tcp"]
    for protocolo in scanner[host].all_protocols():
        # Creamos un diccionario para este protocolo
        resultado_escaneo[host]["protocolos"][protocolo] = {}

        # Iteramos sobre cada puerto encontrado en este protocolo
        # keys() devuelve los números de puerto: [22, 80, 443, ...]
        for puerto in scanner[host][protocolo].keys():
            # Obtenemos toda la información de este puerto
            info = scanner[host][protocolo][puerto]
            
            # Guardamos la información relevante del puerto
            resultado_escaneo[host]["protocolos"][protocolo][puerto] = {
                "estado": info["state"],           # "open", "closed", "filtered"
                "nombre": info.get("name"),        # Nombre del servicio: "http", "ssh", etc.
                "producto": info.get("product"),   # Software: "Apache", "OpenSSH", etc.
                "version": info.get("version")     # Versión del software: "2.4", "7.9", etc.
            }
            # Nota: usamos .get() en lugar de [] para evitar errores si no existe la clave


# PASO 5: GUARDAR LOS RESULTADOS EN UN ARCHIVO JSON
# --------------------------------------------------
archivo_salida = "resultados_escaneo.json"

# Abrimos el archivo en modo escritura ("w" = write)
with open(archivo_salida, "w") as archivo:
    # json.dump() convierte el diccionario Python a formato JSON y lo guarda
    # indent=4 hace que el JSON sea legible (con sangría de 4 espacios)
    json.dump(resultado_escaneo, archivo, indent=4)

print(f"Resultados guardados en: {archivo_salida}")

# ESTRUCTURA DEL ARCHIVO JSON RESULTANTE:
# {
#     "127.0.0.1": {
#         "estado": "up",
#         "protocolos": {
#             "tcp": {
#                 "22": {
#                     "estado": "open",
#                     "nombre": "ssh",
#                     "producto": "OpenSSH",
#                     "version": "8.2"
#                 },
#                 "80": {
#                     "estado": "open",
#                     "nombre": "http",
#                     "producto": "Apache",
#                     "version": "2.4"
#                 }
#             }
#         }
#     }
# }
