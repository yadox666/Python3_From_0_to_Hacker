import json  # Módulo para trabajar con archivos JSON

# Diccionario con información sobre puertos y protocolos
datos_ciberseguridad = {
    "puertos": [
        {"nombre": "HTTP", "puerto": 80, "protocolo": "TCP"},
        {"nombre": "HTTPS", "puerto": 443, "protocolo": "TCP"},
        {"nombre": "FTP", "puerto": 21, "protocolo": "TCP"},
        {"nombre": "SSH", "puerto": 22, "protocolo": "TCP"},
        {"nombre": "DNS", "puerto": 53, "protocolo": "UDP"},
        {"nombre": "SMTP", "puerto": 25, "protocolo": "TCP"},
        {"nombre": "POP3", "puerto": 110, "protocolo": "TCP"},
        {"nombre": "IMAP", "puerto": 143, "protocolo": "TCP"},
        {"nombre": "SNMP", "puerto": 161, "protocolo": "UDP"},
    ]
}

# Recorremos los puertos y mostramos su información
for servicio in datos_ciberseguridad["puertos"]:
    print("Nombre:", servicio["nombre"])
    print("Puerto:", servicio["puerto"])
    print("Protocolo:", servicio["protocolo"])
    print("---")

# Guardamos el diccionario como archivo JSON
with open("puertos_ciberseguridad.json", "w") as archivo_json:
    json.dump(datos_ciberseguridad, archivo_json, indent=4)

print("Datos guardados en puertos_ciberseguridad.json")
