# Requisitos:
# - Tener Nmap instalado en el sistema
# - Instalar el módulo de Python: pip install python-nmap

import nmap  # Librería para controlar Nmap desde Python
import json  # Para guardar resultados como archivo JSON

# Crear el escáner de puertos
scanner = nmap.PortScanner()

# Definir el objetivo y el rango de puertos
objetivo = "127.0.0.1"      # Dirección IP del equipo a escanear (localhost en este caso)
puertos = "1-1024"          # Rango de puertos a revisar

print(f"Escaneando {objetivo} en puertos {puertos}...")
scanner.scan(hosts=objetivo, ports=puertos)  # Ejecuta el escaneo

# Diccionario donde guardaremos los resultados
resultado_escaneo = {}

# Recorremos todos los hosts encontrados (en este caso, solo uno)
for host in scanner.all_hosts():
    resultado_escaneo[host] = {
        "estado": scanner[host].state(),  # online/offline
        "protocolos": {}
    }

    for protocolo in scanner[host].all_protocols():
        resultado_escaneo[host]["protocolos"][protocolo] = {}

        for puerto in scanner[host][protocolo].keys():
            info = scanner[host][protocolo][puerto]
            resultado_escaneo[host]["protocolos"][protocolo][puerto] = {
                "estado": info["state"],
                "nombre": info.get("name"),
                "producto": info.get("product"),
                "version": info.get("version")
            }

# Guardamos los datos en un archivo JSON
archivo_salida = "resultados_escaneo.json"
with open(archivo_salida, "w") as archivo:
    json.dump(resultado_escaneo, archivo, indent=4)

print(f"Resultados guardados en: {archivo_salida}")
