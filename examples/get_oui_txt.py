# Requiere tener instalada la librería requests: pip install requests

import requests
import json

# URL donde se encuentra el archivo original con los datos OUI
URL_OUI = "http://standards-oui.ieee.org/oui/oui.txt"

# Nombre del archivo de salida en formato JSON
ARCHIVO_SALIDA = "lista_oui.json"

# Función que descarga el archivo desde internet
def descargar_oui(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verifica que la descarga sea exitosa
        return respuesta.text
    except requests.RequestException as error:
        print("Error al descargar el archivo:", error)
        return None

# Función que extrae los datos importantes y los convierte a una lista de diccionarios
def analizar_oui(texto):
    datos = []
    lineas = texto.splitlines()

    for linea in lineas:
        if "(base 16)" in linea:
            partes = linea.split("(base 16)")
            oui = partes[0].strip().replace("-", ":")       # Convierte el OUI a formato XX:XX:XX
            fabricante = partes[1].strip()
            datos.append({"oui": oui, "organizacion": fabricante})

    return datos

# Función para guardar los datos como archivo JSON
def guardar_json(datos, nombre_archivo):
    try:
        with open(nombre_archivo, "w") as archivo:
            json.dump(datos, archivo, indent=4)
        print("Datos guardados en:", nombre_archivo)
    except IOError as error:
        print("Error al guardar el archivo:", error)

# Función principal que controla el flujo del programa
def main():
    contenido = descargar_oui(URL_OUI)
    if contenido is None:
        return  # Si hubo error al descargar, detenemos el programa

    datos_oui = analizar_oui(contenido)
    guardar_json(datos_oui, ARCHIVO_SALIDA)

# Ejecutamos el programa principal
if __name__ == "__main__":
    main()
