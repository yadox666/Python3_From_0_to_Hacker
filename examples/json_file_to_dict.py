import json  # Módulo para trabajar con archivos JSON

# Abrimos el archivo JSON y cargamos su contenido en una variable tipo diccionario
with open("puertos_ciberseguridad.json", "r") as archivo_json:
    datos = json.load(archivo_json)

# Mostramos el contenido completo para ver cómo está estructurado
print("Contenido del archivo:")
print(datos)

print("\nListado de puertos y protocolos:")

# Recorremos la lista de puertos y mostramos sus datos
for servicio in datos["puertos"]:
    print(f"Nombre: {servicio['nombre']}, Puerto: {servicio['puerto']}, Protocolo: {servicio['protocolo']}")
