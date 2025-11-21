"""
WEB SCRAPING CON EXPRESIONES REGULARES - Script Educativo
==========================================================
Este script descarga el HTML de una página web y extrae información
específica usando expresiones regulares (regex).

¿QUÉ ES WEB SCRAPING?
Web scraping es el proceso de extraer datos de sitios web de forma automática.
Es útil para recopilar información, analizar datos o automatizar tareas.

¿QUÉ SON LAS EXPRESIONES REGULARES (REGEX)?
Son patrones de búsqueda de texto muy potentes que permiten encontrar
y extraer información específica de cadenas de texto.

¿QUÉ APRENDERÁS?
- Cómo descargar contenido HTML con requests
- Uso básico de expresiones regulares con re
- Procesamiento de argumentos con sys.argv
- Manejo de errores de red con try/except
- Uso de set() para eliminar duplicados
- Uso de sorted() para ordenar resultados

REQUISITOS:
    pip install requests

EJEMPLO DE USO:
    python scrap.py http://www.ewhois.com/ebay.com/

NOTA IMPORTANTE:
Algunos sitios web prohíben el scraping en sus términos de servicio.
Verifica siempre los términos de uso y el archivo robots.txt del sitio.
"""

# Importamos las librerías necesarias
import sys       # Para acceder a los argumentos de línea de comandos
import re        # Para usar expresiones regulares (regex)
import requests  # Para hacer peticiones HTTP y descargar páginas web


def main():
    """
    Función principal que coordina todo el proceso de scraping.
    """
    
    # PASO 1: VALIDAR ARGUMENTOS
    # ---------------------------
    # Verificamos que el usuario proporcionó una URL
    # sys.argv[0] = nombre del script
    # sys.argv[1] = primer argumento (la URL)
    if len(sys.argv) < 2:
        print("Uso: python scrap.py <URL>")
        print("\nEjemplo:")
        print("  python scrap.py http://www.ewhois.com/ebay.com/")
        return  # Termina la función si no hay argumentos suficientes

    # Obtenemos la URL desde los argumentos
    site = sys.argv[1]
    print(f"Descargando contenido de: {site}\n")

    # PASO 2: DESCARGAR EL CONTENIDO HTML
    # ------------------------------------
    # Usamos try/except para manejar errores de red
    try:
        # requests.get() hace una petición HTTP GET al sitio
        # Es como abrir la página en un navegador, pero obteniendo el HTML crudo
        response = requests.get(site)
        
        # response.text contiene el HTML de la página como texto
        html = response.text
        
    except requests.RequestException as e:
        # RequestException captura todos los errores de requests:
        # - Conexión fallida
        # - Timeout
        # - URL inválida, etc.
        print(f"Error al acceder al sitio: {e}")
        return  # Termina la función si hay error

    # PASO 3: EXTRAER INFORMACIÓN CON EXPRESIONES REGULARES
    # ------------------------------------------------------
    # re.findall() busca TODAS las coincidencias del patrón en el HTML
    # y retorna una lista con los resultados
    
    # Desglose del patrón regex: r"<div>([a-z0-9.\-]+?)\s"
    # <div>           = literal, busca la etiqueta <div>
    # (...)           = grupo de captura (lo que queremos extraer)
    # [a-z0-9.\-]     = caracteres permitidos: letras, números, punto, guión
    # +?              = uno o más caracteres (modo no-codicioso)
    # \s              = espacio en blanco (espacio, tab, salto de línea)
    #
    # re.IGNORECASE   = hace que la búsqueda no distinga mayúsculas/minúsculas
    resultados = re.findall(r"<div>([a-z0-9.\-]+?)\s", html, re.IGNORECASE)
    
    print(f"Se encontraron {len(resultados)} coincidencias (con duplicados)\n")

    # PASO 4: PROCESAR Y MOSTRAR RESULTADOS
    # --------------------------------------
    # set() elimina duplicados de la lista
    # sorted() ordena alfabéticamente
    # El resultado es una lista ordenada sin elementos repetidos
    resultados_unicos = sorted(set(resultados))
    
    print(f"Resultados únicos y ordenados ({len(resultados_unicos)} items):")
    print("-" * 50)
    
    # Iteramos sobre cada resultado único y lo imprimimos
    for item in resultados_unicos:
        print(item)


# PUNTO DE ENTRADA DEL PROGRAMA
# ------------------------------
if __name__ == "__main__":
    # Este bloque solo se ejecuta si el script se ejecuta directamente
    # (no cuando se importa como módulo)
    main()

# EJEMPLOS DE EXPRESIONES REGULARES ÚTILES:
# ------------------------------------------
# Emails:       r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# URLs:         r"https?://[a-zA-Z0-9./-]+"
# IPs:          r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
# Teléfonos:    r"\d{3}-\d{3}-\d{4}"
# 
# Para probar y aprender regex, visita: https://regex101.com/
