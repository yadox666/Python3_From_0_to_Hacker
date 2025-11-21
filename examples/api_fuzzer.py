# Requiere: pip install requests

import requests

# URL base de la API que vamos a "fuzzear"
url_base = "https://127.0.0.1/api"  # Cambia esto por la URL real de tu API

# Archivo de texto con posibles rutas (una por línea, como: login, user, admin)
archivo_diccionario = "endpoints.txt"

# Métodos HTTP que queremos probar
metodos = ["GET", "POST"]

# Cargamos las posibles rutas desde el archivo
with open(archivo_diccionario, "r") as archivo:
    rutas = [linea.strip() for linea in archivo if linea.strip()]

# Probamos cada ruta con cada método
for ruta in rutas:
    for metodo in metodos:
        url_completa = f"{url_base}/{ruta}"

        try:
            # Enviamos la petición dependiendo del método
            if metodo == "GET":
                respuesta = requests.get(url_completa, verify=False)  # verify=False para ignorar SSL autofirmado
            elif metodo == "POST":
                respuesta = requests.post(url_completa, verify=False)

            # Mostramos solo si la ruta devuelve un código exitoso (< 400)
            if respuesta.status_code < 400:
                print(f"[{metodo}] {url_completa} - Código: {respuesta.status_code}")

        except requests.RequestException as error:
            print(f"Error con {metodo} {url_completa}: {error}")
