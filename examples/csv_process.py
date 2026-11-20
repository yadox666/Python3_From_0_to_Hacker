#!/usr/bin/env python3
"""
Author: Yago Hansen
Version: 1.0

PROCESADOR DE ARCHIVOS CSV - Script Educativo
==============================================
Este script lee un archivo CSV (valores separados por comas) y procesa
cada línea para extraer información de usuarios.

¿QUÉ ES UN ARCHIVO CSV?
CSV (Comma Separated Values) es un formato de archivo donde los datos
están separados por comas. Ejemplo:
    nombre,apellido,email
    Juan,García,juan@email.com
    Ana,Martínez,ana@email.com

¿QUÉ APRENDERÁS?
- Cómo abrir y leer archivos con "with"
- Manejo de excepciones con try/except
- Procesamiento de texto línea por línea
- Uso de split() para separar datos
- Uso de strip() para limpiar saltos de línea
- Desempaquetado de listas en varias variables

REQUISITO:
Debe existir un archivo "ejemplo.csv" en la misma carpeta
"""

ARCHIVO_CSV = "ejemplo.csv"

try:
    # "with" cierra el archivo automáticamente al terminar el bloque
    with open(ARCHIVO_CSV, "r", encoding="utf-8") as archivo:
        for numero_linea, linea in enumerate(archivo):
            # La primera línea contiene los encabezados (nombre, apellido, email)
            if numero_linea == 0:
                continue

            # strip() elimina el salto de línea final: "Juan,García,juan@email.com\n"
            linea = linea.strip()
            if not linea:
                continue  # Saltamos líneas vacías

            # split(",") devuelve una lista y la desempaquetamos en tres variables
            nombre, apellido, email = linea.split(",")

            print(f"Mi nombre es {nombre} {apellido} y mi email es {email}")

except FileNotFoundError:
    print(f"El fichero '{ARCHIVO_CSV}' no se encontró")
except ValueError:
    print("Alguna línea no tiene exactamente 3 columnas")

# NOTA: para CSV reales (con comas dentro de comillas, etc.) usa el módulo
# estándar "csv": import csv; csv.DictReader(archivo)
