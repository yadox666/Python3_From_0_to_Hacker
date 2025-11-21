"""
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
- Cómo abrir y leer archivos
- Manejo de excepciones con try/except
- Procesamiento de texto línea por línea
- Uso de split() para separar datos
- Uso de rstrip() para limpiar saltos de línea

REQUISITO:
Debe existir un archivo "ejemplo.csv" en la misma carpeta
"""

# PASO 1: ABRIR EL ARCHIVO CSV
# -----------------------------
# Usamos try/except para manejar errores si el archivo no existe
try:
	# open() abre el archivo
	# "ejemplo.csv" = nombre del archivo
	# "r" = modo lectura (read)
	csv = open("ejemplo.csv","r")
except Exception as e:
	# Si hay cualquier error (archivo no existe, sin permisos, etc.)
	print("El fichero no se encontro")
	exit()  # Termina el programa

# PASO 2: PROCESAR CADA LÍNEA DEL ARCHIVO
# ----------------------------------------
# El bucle for itera sobre cada línea del archivo
for linea in csv:
	# Saltamos la primera línea si contiene los encabezados (nombre, apellido, email)
	if "nombre," in linea:
		continue  # continue salta a la siguiente iteración del bucle
	
	# rstrip() elimina espacios en blanco y saltos de línea al final
	# Ejemplo: "Juan,García,juan@email.com\n" → "Juan,García,juan@email.com"
	linea = linea.rstrip()
	
	# split(",") divide la línea usando la coma como separador
	# Retorna una lista: ["Juan", "García", "juan@email.com"]
	nombre = linea.split(",")[0]     # Primer elemento (índice 0)
	apellido = linea.split(",")[1]   # Segundo elemento (índice 1)
	email = linea.split(",")[2]      # Tercer elemento (índice 2)
	
	# Imprimimos la información formateada usando f-strings
	print(f"Mi nombre es {nombre} {apellido} y mi email es {email}")

# PASO 3: CERRAR EL ARCHIVO
# --------------------------
# Es importante cerrar el archivo cuando terminamos de usarlo
# Esto libera recursos del sistema
csv.close()
