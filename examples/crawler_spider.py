# Este programa explora un sitio web y sigue enlaces hasta una cierta profundidad.
# Ideal para aprender cómo funciona un "web crawler" simple.

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Función principal del "spider" (rastreador)
def simple_spider(start_url, max_depth=2):
    visited = set()  # Conjunto para guardar URLs visitadas y no repetir

    # Función interna recursiva para explorar las páginas
    def crawl(url, depth):
        if depth > max_depth:
            return  # Si se alcanza la profundidad máxima, detenemos la exploración
        if url in visited:
            return  # Si ya visitamos esta URL, la ignoramos

        print(f"Explorando: {url}")
        visited.add(url)  # Marcamos la URL como visitada

        try:
            response = requests.get(url)
            response.raise_for_status()  # Verifica que la respuesta sea exitosa (código 200)
        except requests.RequestException as e:
            print(f"No se pudo acceder a {url}: {e}")
            return

        # Usamos BeautifulSoup para analizar el contenido HTML de la página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscamos todos los enlaces (<a href="...">)
        for link in soup.find_all("a", href=True):
            full_url = urljoin(url, link["href"])  # Completamos la URL si es relativa
            crawl(full_url, depth + 1)  # Llamamos recursivamente para seguir ese enlace

    # Iniciamos el rastreo desde la URL proporcionada
    crawl(start_url, depth=0)

# Ejecución principal: define el sitio y empieza a explorar
if __name__ == "__main__":
    # Puedes cambiar esta URL por otra para probar
    start_url = "https://example.com"
    simple_spider(start_url, max_depth=2)
