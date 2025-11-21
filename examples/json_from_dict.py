"""
CONVERTIR DICCIONARIO A ARCHIVO JSON - Script Educativo
========================================================
Este script demuestra cómo convertir un diccionario de Python en un
archivo JSON para guardar datos de forma permanente.

¿QUÉ ES JSON?
JSON (JavaScript Object Notation) es un formato de texto para almacenar datos.
Es el formato estándar para intercambiar información entre aplicaciones.

¿CUÁNDO CONVERTIR DICCIONARIO A JSON?
- Guardar configuraciones de un programa
- Almacenar datos de forma estructurada
- Compartir datos entre diferentes lenguajes de programación
- Crear archivos de respaldo de datos
- Exportar datos para APIs

¿QUÉ APRENDERÁS?
- Cómo crear diccionarios anidados (con listas y diccionarios dentro)
- Cómo iterar sobre estructuras de datos complejas
- Cómo convertir diccionarios Python a JSON con json.dump()
- El parámetro indent para hacer JSON legible
- Uso de with para escritura segura de archivos

PROCESO:
Diccionario Python → json.dump() → Archivo JSON
"""

# Importamos el módulo json
# Este módulo viene incluido con Python (no necesitas instalarlo)
import json

# PASO 1: CREAR LA ESTRUCTURA DE DATOS EN PYTHON
# -----------------------------------------------
# Creamos un diccionario con información sobre puertos de red comunes
# Este es un diccionario ANIDADO: contiene listas y diccionarios dentro

datos_ciberseguridad = {
    # La clave "puertos" contiene una LISTA de diccionarios
    "puertos": [
        # Cada elemento de la lista es un DICCIONARIO con 3 claves
        {"nombre": "HTTP", "puerto": 80, "protocolo": "TCP"},     # Navegación web
        {"nombre": "HTTPS", "puerto": 443, "protocolo": "TCP"},   # Navegación web segura
        {"nombre": "FTP", "puerto": 21, "protocolo": "TCP"},      # Transferencia de archivos
        {"nombre": "SSH", "puerto": 22, "protocolo": "TCP"},      # Acceso remoto seguro
        {"nombre": "DNS", "puerto": 53, "protocolo": "UDP"},      # Resolución de nombres
        {"nombre": "SMTP", "puerto": 25, "protocolo": "TCP"},     # Envío de correo
        {"nombre": "POP3", "puerto": 110, "protocolo": "TCP"},    # Recepción de correo
        {"nombre": "IMAP", "puerto": 143, "protocolo": "TCP"},    # Acceso a correo
        {"nombre": "SNMP", "puerto": 161, "protocolo": "UDP"},    # Gestión de red
    ]
}

# ESTRUCTURA DEL DICCIONARIO:
# datos_ciberseguridad (diccionario)
#   └── "puertos" (lista)
#         ├── [0] {"nombre": "HTTP", "puerto": 80, "protocolo": "TCP"}
#         ├── [1] {"nombre": "HTTPS", "puerto": 443, "protocolo": "TCP"}
#         └── ...

# PASO 2: MOSTRAR LOS DATOS ANTES DE GUARDAR
# -------------------------------------------
# Recorremos la lista de puertos para ver qué vamos a guardar

print("=" * 60)
print("INFORMACIÓN DE PUERTOS Y PROTOCOLOS")
print("=" * 60)
print()

# datos_ciberseguridad["puertos"] accede a la lista dentro del diccionario
# El bucle for itera sobre cada diccionario dentro de la lista
for servicio in datos_ciberseguridad["puertos"]:
    # En cada iteración, 'servicio' es un diccionario con 3 claves
    # Accedemos a cada valor usando servicio["clave"]
    print("Nombre:", servicio["nombre"])
    print("Puerto:", servicio["puerto"])
    print("Protocolo:", servicio["protocolo"])
    print("---")  # Separador visual

print()

# PASO 3: GUARDAR EL DICCIONARIO COMO ARCHIVO JSON
# -------------------------------------------------
# Usamos 'with' que garantiza que el archivo se cierre correctamente

# open() abre/crea el archivo
# "puertos_ciberseguridad.json" = nombre del archivo a crear
# "w" = modo escritura (write) - crea el archivo o lo sobrescribe si existe
# "as archivo_json" = nombre que le damos al objeto archivo
with open("puertos_ciberseguridad.json", "w") as archivo_json:
    # json.dump() convierte el diccionario Python a formato JSON
    # y lo escribe directamente en el archivo
    # 
    # Parámetros:
    # - datos_ciberseguridad: el diccionario a convertir
    # - archivo_json: dónde escribir el resultado
    # - indent=4: añade sangría de 4 espacios para que sea legible
    #
    # CONVERSIÓN AUTOMÁTICA:
    # diccionario Python {} → JSON object {}
    # lista Python [] → JSON array []
    # str → JSON string
    # int/float → JSON number
    # True/False → JSON true/false
    # None → JSON null
    json.dump(datos_ciberseguridad, archivo_json, indent=4)
# Al salir del bloque 'with', el archivo se cierra y guarda automáticamente

print("✓ Datos guardados en puertos_ciberseguridad.json")
print()

# RESULTADO: El archivo JSON creado tendrá este formato:
# {
#     "puertos": [
#         {
#             "nombre": "HTTP",
#             "puerto": 80,
#             "protocolo": "TCP"
#         },
#         {
#             "nombre": "HTTPS",
#             "puerto": 443,
#             "protocolo": "TCP"
#         },
#         ...
#     ]
# }

# DIFERENCIA ENTRE json.dump() y json.dumps():
# =============================================
# json.dump()  → Escribe directamente a un ARCHIVO
#                dump(datos, archivo)
#
# json.dumps() → Convierte a un STRING
#                texto_json = dumps(datos)
#                print(texto_json)
#
# PARÁMETROS ÚTILES DE json.dump():
# ==================================
# indent=4         → Añade sangría (hace el JSON legible)
# sort_keys=True   → Ordena las claves alfabéticamente
# ensure_ascii=False → Permite caracteres especiales (ñ, á, etc.)
#
# Ejemplo con más parámetros:
# json.dump(datos, archivo, indent=4, sort_keys=True, ensure_ascii=False)
