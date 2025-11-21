"""
WEB CRAWLER (ARAÑA WEB) - Script Educativo
===========================================
Este programa explora un sitio web siguiendo enlaces automáticamente,
similar a cómo funcionan los buscadores como Google para indexar páginas.

¿QUÉ ES UN WEB CRAWLER?
Un web crawler (también llamado spider o araña) es un programa que navega
automáticamente por sitios web, siguiendo los enlaces de una página a otra.

¿CÓMO FUNCIONA?
1. Empieza en una URL inicial
2. Descarga la página y extrae todos los enlaces
3. Visita cada enlace encontrado
4. Repite el proceso recursivamente hasta cierta profundidad

¿PARA QUÉ SIRVE?
- Buscadores web (Google, Bing) usan crawlers para indexar internet
- Herramientas SEO para analizar sitios web
- Detectar enlaces rotos
- Recopilar datos (web scraping)
- Mapear la estructura de un sitio

¿QUÉ APRENDERÁS?
- Uso de BeautifulSoup para parsear HTML
- Funciones recursivas
- Uso de set() para evitar duplicados
- Manejo de URLs relativas vs absolutas con urljoin()
- Concepto de profundidad en exploración de grafos

REQUISITOS:
    pip install requests beautifulsoup4

ADVERTENCIA:
Usar crawlers de forma irresponsable puede sobrecargar servidores.
Respeta el archivo robots.txt y los términos de servicio del sitio.
"""

# Importamos las librerías necesarias
import requests              # Para hacer peticiones HTTP
from bs4 import BeautifulSoup  # Para analizar y extraer datos de HTML
from urllib.parse import urljoin  # Para manejar URLs relativas y absolutas


# FUNCIÓN PRINCIPAL DEL CRAWLER
# ------------------------------
def simple_spider(start_url, max_depth=2):
    """
    Explora un sitio web siguiendo enlaces hasta una profundidad máxima.
    
    Esta función implementa un crawler simple que:
    - Visita cada página una sola vez (evita bucles infinitos)
    - Limita la exploración a cierta profundidad (evita explorar infinitamente)
    - Extrae y sigue todos los enlaces encontrados
    
    Parámetros:
        start_url (str): URL inicial desde donde empezar a explorar
        max_depth (int): Profundidad máxima de exploración
                        0 = solo la página inicial
                        1 = página inicial + enlaces directos
                        2 = dos niveles de enlaces, etc.
    
    EJEMPLO DE PROFUNDIDAD:
        Página A (depth=0)
        ├── Página B (depth=1)
        │   ├── Página D (depth=2)
        │   └── Página E (depth=2)
        └── Página C (depth=1)
    """
    # set() es una estructura de datos que NO permite duplicados
    # Usamos un set para guardar las URLs ya visitadas
    # Esto es MUY importante para evitar visitar la misma página múltiples veces
    visited = set()
    
    print(f"Iniciando crawler desde: {start_url}")
    print(f"Profundidad máxima: {max_depth}")
    print("-" * 70)

    # FUNCIÓN RECURSIVA INTERNA
    # --------------------------
    def crawl(url, depth):
        """
        Función recursiva que explora una URL y sigue sus enlaces.
        
        La recursividad permite explorar el sitio como un árbol:
        cada página llama a crawl() para sus enlaces hijos.
        
        Parámetros:
            url (str): URL a explorar
            depth (int): Profundidad actual en el árbol de exploración
        """
        
        # CONDICIÓN DE PARADA 1: Profundidad máxima alcanzada
        # Si llegamos más allá de la profundidad permitida, detenemos
        if depth > max_depth:
            return
        
        # CONDICIÓN DE PARADA 2: URL ya visitada
        # Si ya visitamos esta URL, la ignoramos para evitar bucles infinitos
        if url in visited:
            return

        # Mostramos la URL que estamos explorando con su profundidad
        indent = "  " * depth  # Sangría visual para mostrar la profundidad
        print(f"{indent}[Nivel {depth}] Explorando: {url}")
        
        # Añadimos la URL al conjunto de visitadas
        visited.add(url)

        # PASO 1: DESCARGAR LA PÁGINA
        # ----------------------------
        try:
            # Descargamos el contenido HTML de la página
            response = requests.get(url, timeout=5)  # timeout evita esperas infinitas
            
            # raise_for_status() lanza excepción si hay error HTTP (404, 500, etc.)
            response.raise_for_status()
            
        except requests.RequestException as e:
            # Si hay cualquier error (conexión, timeout, 404, etc.)
            print(f"{indent}  ⚠️ Error al acceder: {e}")
            return  # Detenemos la exploración de esta rama

        # PASO 2: PARSEAR EL HTML
        # ------------------------
        # BeautifulSoup convierte el HTML en un objeto navegable
        # 'html.parser' es el parser que usamos (viene incluido con Python)
        soup = BeautifulSoup(response.text, 'html.parser')

        # PASO 3: EXTRAER TODOS LOS ENLACES
        # ----------------------------------
        # find_all("a", href=True) encuentra todas las etiquetas <a> que tengan atributo href
        # href=True asegura que solo obtengamos enlaces con href válido
        enlaces_encontrados = 0
        
        for link in soup.find_all("a", href=True):
            # link["href"] contiene la URL del enlace
            # Puede ser relativa ("/about") o absoluta ("https://example.com/about")
            
            # urljoin() convierte URLs relativas en absolutas
            # Ejemplos:
            #   urljoin("https://example.com/page", "/about") → "https://example.com/about"
            #   urljoin("https://example.com/page", "contact") → "https://example.com/contact"
            #   urljoin("https://example.com/page", "https://other.com") → "https://other.com"
            full_url = urljoin(url, link["href"])
            
            enlaces_encontrados += 1
            
            # RECURSIÓN: Llamamos a crawl() para explorar este enlace
            # depth + 1 significa que bajamos un nivel en el árbol
            crawl(full_url, depth + 1)
        
        print(f"{indent}  → {enlaces_encontrados} enlaces encontrados")

    # INICIAR EL CRAWLING
    # --------------------
    # Llamamos a crawl() con la URL inicial y profundidad 0
    crawl(start_url, depth=0)
    
    # Resumen final
    print("-" * 70)
    print(f"Crawling completado. Total de páginas visitadas: {len(visited)}")


# PUNTO DE ENTRADA DEL PROGRAMA
# ------------------------------
if __name__ == "__main__":
    # URL inicial desde donde empezar a explorar
    # Puedes cambiar esta URL por cualquier sitio web que quieras explorar
    start_url = "https://example.com"
    
    # Profundidad máxima de exploración
    # CUIDADO: profundidades altas (3+) pueden visitar MUCHAS páginas
    # Empieza con 1 o 2 para pruebas
    max_depth = 2
    
    print("=" * 70)
    print("WEB CRAWLER SIMPLE")
    print("=" * 70)
    print()
    
    # Ejecutamos el spider
    simple_spider(start_url, max_depth=max_depth)

# CONSIDERACIONES IMPORTANTES:
# -----------------------------
# 1. RESPETA robots.txt: Los sitios indican qué pueden explorar los bots
# 2. AÑADE DELAYS: No hagas peticiones demasiado rápido (usa time.sleep())
# 3. RESPETA TOS: Lee los términos de servicio del sitio
# 4. IDENTIFÍCATE: Usa un User-Agent apropiado
# 5. LIMITA PROFUNDIDAD: Crawlers sin límite pueden tardar eternamente
#
# MEJORAS POSIBLES:
# - Filtrar por dominio (solo explorar el mismo sitio)
# - Guardar URLs en archivo o base de datos
# - Extraer y guardar contenido de las páginas
# - Añadir delays entre peticiones (time.sleep())
# - Implementar cola con threading para paralelizar
