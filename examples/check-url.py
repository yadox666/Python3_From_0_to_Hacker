import requests
import argparse

# Configuramos los argumentos que el usuario puede pasarle al script
parser = argparse.ArgumentParser(description="Comprobar el estado HTTP de una URL.")
parser.add_argument("--url", type=str, help="La URL a comprobar.")
args = parser.parse_args()

# Aseguramos que la URL empiece con http:// o https://
def ensure_https(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        return "https://" + url
    return url

# Realiza la petición HTTP y devuelve el código de estado
def check_endpoint(url):
    try:
        response = requests.get(url, timeout=10)  # timeout evita que se quede colgado
        return response.status_code
    except requests.Timeout:
        return 0     # Si tarda demasiado
    except requests.RequestException:
        return 99    # Cualquier otro error

# Traducción simple de algunos códigos de estado comunes
def translate_status_code(code):
    translations = {
        0:  "Timeout",
        99: "Error",
        200: "OK",
        301: "Moved Permanently",
        302: "Found",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        500: "Internal Server Error",
        503: "Service Unavailable"
    }
    return translations.get(code, "Estado desconocido")

# Código principal del script
if args.url:
    url = ensure_https(args.url)  # Normalizamos la URL
    status_code = check_endpoint(url)
    status_text = translate_status_code(status_code)

    print(f"{url} - {status_code} ({status_text})")
else:
    print("Error: Debes especificar una URL con --url")
