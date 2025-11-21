# Uso: python scrap.py http://www.ewhois.com/ebay.com/
# Este script extrae cadenas de texto específicas de un sitio web usando expresiones regulares.

import sys
import re
import requests

def main():
    if len(sys.argv) < 2:
        print("Uso: python scrap.py <URL>")
        return

    site = sys.argv[1]
    try:
        response = requests.get(site)
        html = response.text
    except requests.RequestException as e:
        print(f"Error al acceder al sitio: {e}")
        return

    # Buscar patrones tipo dominio dentro de <div> como "ejemplo.com"
    resultados = re.findall(r"<div>([a-z0-9.\-]+?)\s", html, re.IGNORECASE)

    for item in sorted(set(resultados)):
        print(item)

if __name__ == "__main__":
    main()
