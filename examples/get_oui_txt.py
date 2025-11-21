"""
DESCARGADOR Y PROCESADOR DE DATOS OUI - Script Educativo
=========================================================
Este script descarga la base de datos oficial de IEEE que contiene información
sobre fabricantes de dispositivos de red basándose en sus direcciones MAC.

¿QUÉ ES UN OUI (Organizationally Unique Identifier)?
Es un código de 24 bits (3 bytes) que identifica al fabricante de un dispositivo.
Los primeros 3 bytes de cualquier dirección MAC indican quién fabricó el dispositivo.

Ejemplo de dirección MAC: A4:C3:F0:12:34:56
- A4:C3:F0 = OUI (identifica al fabricante, ej: Apple Inc.)
- 12:34:56 = Identificador único del dispositivo

¿PARA QUÉ SIRVE ESTO?
Este script es útil para:
- Identificar fabricantes de dispositivos en una red
- Análisis de seguridad de redes
- Inventario de dispositivos
- Detección de dispositivos no autorizados

¿QUÉ APRENDERÁS?
- Descargar archivos grandes desde internet
- Procesar archivos de texto línea por línea
- Transformar datos de un formato a otro (TXT a JSON)
- Manipulación de strings: split(), strip(), replace()
- Guardar datos estructurados en JSON

REQUISITOS:
    pip install requests

RESULTADO:
Genera un archivo JSON con ~30,000 fabricantes y sus códigos OUI.
"""

# Importamos las librerías necesarias
import requests  # Para descargar archivos desde internet
import json      # Para guardar los datos en formato JSON


# CONFIGURACIÓN
# -------------
# URL oficial de IEEE donde se encuentra la base de datos actualizada de OUI
# Este archivo contiene información de todos los fabricantes registrados
URL_OUI = "http://standards-oui.ieee.org/oui/oui.txt"

# Nombre del archivo de salida donde guardaremos los datos procesados
ARCHIVO_SALIDA = "lista_oui.json"


# FUNCIÓN 1: DESCARGAR ARCHIVO OUI
# ---------------------------------
def descargar_oui(url):
    """
    Descarga el archivo de texto OUI desde la URL de IEEE.
    
    El archivo original es un .txt de varios MB con formato:
    XX-XX-XX   (base 16)		Nombre del Fabricante
    
    Parámetros:
        url (str): URL del archivo a descargar
    
    Retorna:
        str: Contenido del archivo como texto, o None si hay error
    """
    print(f"Descargando base de datos OUI desde IEEE...")
    print(f"URL: {url}")
    print("Esto puede tardar unos segundos...\n")
    
    try:
        # requests.get() descarga el contenido de la URL
        respuesta = requests.get(url)
        
        # raise_for_status() lanza una excepción si hubo error HTTP
        # (códigos 4xx o 5xx como 404 Not Found, 500 Internal Server Error)
        respuesta.raise_for_status()
        
        print("✓ Descarga completada exitosamente\n")
        
        # respuesta.text contiene el archivo completo como string
        return respuesta.text
        
    except requests.RequestException as error:
        # RequestException captura todos los errores de requests
        print("Error al descargar el archivo:", error)
        return None


# FUNCIÓN 2: ANALIZAR Y EXTRAER DATOS
# ------------------------------------
def analizar_oui(texto):
    """
    Procesa el archivo de texto OUI y extrae los datos importantes.
    
    El archivo original tiene este formato:
        A4-C3-F0   (base 16)		Apple, Inc.
        00-1B-63   (base 16)		Apple, Inc.
    
    Lo convertimos a:
        {"oui": "A4:C3:F0", "organizacion": "Apple, Inc."}
    
    Parámetros:
        texto (str): Contenido completo del archivo OUI
    
    Retorna:
        list: Lista de diccionarios con OUI y fabricante
    """
    print("Procesando datos...")
    
    # Lista vacía donde guardaremos los diccionarios
    datos = []
    
    # splitlines() divide el texto en líneas (separa por \n)
    # Retorna una lista donde cada elemento es una línea del archivo
    lineas = texto.splitlines()
    
    # Iteramos sobre cada línea del archivo
    for linea in lineas:
        # Solo nos interesan las líneas que contienen "(base 16)"
        # Estas líneas tienen el formato: OUI (base 16) Fabricante
        if "(base 16)" in linea:
            # split() divide la línea usando "(base 16)" como separador
            # partes[0] = la parte antes de "(base 16)" (el OUI)
            # partes[1] = la parte después de "(base 16)" (el fabricante)
            partes = linea.split("(base 16)")
            
            # Procesamos el OUI:
            # strip() elimina espacios al inicio y final
            # replace("-", ":") cambia guiones por dos puntos
            # Ejemplo: "A4-C3-F0   " → "A4:C3:F0"
            oui = partes[0].strip().replace("-", ":")
            
            # Procesamos el nombre del fabricante:
            # strip() elimina espacios extras
            # Ejemplo: "   Apple, Inc.  " → "Apple, Inc."
            fabricante = partes[1].strip()
            
            # Creamos un diccionario con los datos y lo añadimos a la lista
            datos.append({"oui": oui, "organizacion": fabricante})
    
    print(f"✓ Se procesaron {len(datos)} registros OUI\n")
    return datos


# FUNCIÓN 3: GUARDAR EN FORMATO JSON
# -----------------------------------
def guardar_json(datos, nombre_archivo):
    """
    Guarda la lista de datos en un archivo JSON.
    
    JSON es un formato estándar para intercambio de datos,
    fácil de leer tanto para humanos como para programas.
    
    Parámetros:
        datos (list): Lista de diccionarios a guardar
        nombre_archivo (str): Nombre del archivo de salida
    """
    print(f"Guardando datos en formato JSON...")
    
    try:
        # Abrimos el archivo en modo escritura ("w" = write)
        with open(nombre_archivo, "w") as archivo:
            # json.dump() convierte los datos Python a formato JSON
            # indent=4 hace que el archivo sea legible (con sangría)
            json.dump(datos, archivo, indent=4)
        
        print(f"✓ Datos guardados exitosamente en: {nombre_archivo}")
        print(f"✓ El archivo tiene {len(datos)} fabricantes registrados")
        
    except IOError as error:
        # IOError se lanza si hay problemas al escribir el archivo
        # (disco lleno, sin permisos, etc.)
        print("Error al guardar el archivo:", error)


# FUNCIÓN PRINCIPAL
# -----------------
def main():
    """
    Función principal que coordina todo el proceso:
    1. Descargar el archivo OUI
    2. Analizar y extraer los datos
    3. Guardar en formato JSON
    """
    print("=" * 70)
    print("DESCARGADOR Y PROCESADOR DE BASE DE DATOS OUI")
    print("=" * 70)
    print()
    
    # PASO 1: Descargar el archivo
    contenido = descargar_oui(URL_OUI)
    if contenido is None:
        print("\n❌ El proceso se detuvo debido a un error en la descarga.")
        return  # Si hubo error al descargar, detenemos el programa

    # PASO 2: Analizar y extraer datos
    datos_oui = analizar_oui(contenido)
    
    # PASO 3: Guardar en JSON
    guardar_json(datos_oui, ARCHIVO_SALIDA)
    
    print()
    print("=" * 70)
    print("PROCESO COMPLETADO")
    print("=" * 70)


# PUNTO DE ENTRADA DEL PROGRAMA
# ------------------------------
if __name__ == "__main__":
    # Este bloque solo se ejecuta si el script se ejecuta directamente
    main()

# EJEMPLO DEL ARCHIVO JSON GENERADO:
# -----------------------------------
# [
#     {
#         "oui": "A4:C3:F0",
#         "organizacion": "Apple, Inc."
#     },
#     {
#         "oui": "00:1B:63",
#         "organizacion": "Apple, Inc."
#     },
#     {
#         "oui": "B8:27:EB",
#         "organizacion": "Raspberry Pi Foundation"
#     }
# ]
