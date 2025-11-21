"""
LEER ARCHIVO JSON Y CONVERTIRLO A DICCIONARIO - Script Educativo
=================================================================
Este script demuestra cómo leer un archivo JSON y convertirlo en
un diccionario de Python para poder trabajar con los datos.

¿QUÉ ES JSON?
JSON (JavaScript Object Notation) es un formato estándar para almacenar
y transportar datos. Es muy parecido a los diccionarios de Python.

¿POR QUÉ USAR JSON?
- Formato legible tanto para humanos como para máquinas
- Estándar universal usado en APIs, bases de datos, configuraciones
- Fácil de convertir entre JSON y estructuras de Python

¿QUÉ APRENDERÁS?
- Cómo leer archivos JSON con json.load()
- Conversión automática JSON → diccionario Python
- Acceso a datos anidados (diccionarios dentro de listas)
- Uso de with para manejo seguro de archivos
- Iteración sobre listas dentro de diccionarios

ESTRUCTURA DEL ARCHIVO JSON ESPERADO:
{
    "puertos": [
        {
            "nombre": "HTTP",
            "puerto": 80,
            "protocolo": "TCP"
        },
        {
            "nombre": "HTTPS",
            "puerto": 443,
            "protocolo": "TCP"
        }
    ]
}
"""

# Importamos el módulo json
# Este módulo viene incluido con Python (no necesitas instalarlo)
import json

# PASO 1: ABRIR Y CARGAR EL ARCHIVO JSON
# ---------------------------------------
# Usamos 'with' que maneja automáticamente el cierre del archivo
# Esto es una BUENA PRÁCTICA porque garantiza que el archivo se cierre
# incluso si hay un error

# open() abre el archivo
# "puertos_ciberseguridad.json" = nombre del archivo a leer
# "r" = modo lectura (read)
# "as archivo_json" = le damos un nombre al objeto archivo
with open("puertos_ciberseguridad.json", "r") as archivo_json:
    # json.load() lee el archivo JSON y lo convierte automáticamente
    # en un diccionario de Python (o lista, según la estructura del JSON)
    # 
    # CONVERSIÓN AUTOMÁTICA:
    # JSON object {} → diccionario Python {}
    # JSON array [] → lista Python []
    # JSON string → str
    # JSON number → int o float
    # JSON true/false → True/False
    # JSON null → None
    datos = json.load(archivo_json)
# Al salir del bloque 'with', el archivo se cierra automáticamente

# PASO 2: MOSTRAR EL CONTENIDO COMPLETO
# --------------------------------------
# Imprimimos el diccionario completo para ver su estructura
print("Contenido del archivo:")
print(datos)
# Esto muestra TODO el diccionario tal como fue convertido desde JSON

# Separador visual para mejor legibilidad
print("\nListado de puertos y protocolos:")

# PASO 3: RECORRER Y PROCESAR LOS DATOS
# --------------------------------------
# datos["puertos"] accede a la clave "puertos" del diccionario
# Esta clave contiene una LISTA de diccionarios
# Cada diccionario representa un servicio con nombre, puerto y protocolo

# Iteramos sobre cada elemento de la lista
for servicio in datos["puertos"]:
    # En cada iteración, 'servicio' es un diccionario con las claves:
    # - 'nombre': nombre del servicio (ej: "HTTP")
    # - 'puerto': número de puerto (ej: 80)
    # - 'protocolo': tipo de protocolo (ej: "TCP")
    
    # Accedemos a cada valor usando servicio['clave']
    # Usamos f-string para formatear la salida
    print(f"Nombre: {servicio['nombre']}, Puerto: {servicio['puerto']}, Protocolo: {servicio['protocolo']}")

# EXPLICACIÓN DE LA ESTRUCTURA DE DATOS:
# =======================================
# 
# datos (diccionario)
#   └── "puertos" (lista)
#         ├── [0] (diccionario)
#         │     ├── "nombre": "HTTP"
#         │     ├── "puerto": 80
#         │     └── "protocolo": "TCP"
#         ├── [1] (diccionario)
#         │     ├── "nombre": "HTTPS"
#         │     ├── "puerto": 443
#         │     └── "protocolo": "TCP"
#         └── ...
#
# FORMAS DE ACCEDER A LOS DATOS:
# - datos["puertos"]           → Lista completa de servicios
# - datos["puertos"][0]        → Primer servicio (diccionario)
# - datos["puertos"][0]["nombre"] → Nombre del primer servicio
# - len(datos["puertos"])      → Cantidad de servicios
