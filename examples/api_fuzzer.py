"""
API FUZZER (DESCUBRIDOR DE ENDPOINTS) - Script Educativo
=========================================================
Este script realiza "fuzzing" en una API: prueba muchas rutas posibles
para descubrir endpoints que existen pero no están documentados.

¿QUÉ ES FUZZING?
Fuzzing es una técnica de testing de seguridad que consiste en enviar
múltiples peticiones con diferentes valores para descubrir:
- Rutas ocultas o no documentadas
- Endpoints de administración expuestos
- Configuraciones incorrectas
- Vulnerabilidades potenciales

¿CÓMO FUNCIONA?
1. Lee un diccionario con miles de rutas comunes (login, admin, api, etc.)
2. Prueba cada ruta con diferentes métodos HTTP (GET, POST, etc.)
3. Identifica qué rutas existen (responden con códigos 2xx o 3xx)
4. Muestra solo las rutas que funcionan

¿PARA QUÉ SIRVE?
- Pentesting: encontrar vectores de ataque
- Auditorías de seguridad: detectar endpoints expuestos
- Testing: verificar que rutas privadas no sean accesibles
- Mapeo de APIs: descubrir funcionalidad oculta

¿QUÉ APRENDERÁS?
- Técnicas de fuzzing/bruteforce
- Diferencia entre métodos HTTP
- Cómo leer archivos de diccionario
- Interpretación de códigos de estado HTTP
- Testing automatizado de APIs

REQUISITOS:
    pip install requests

ADVERTENCIA:
El fuzzing puede generar MUCHAS peticiones y sobrecargar servidores.
Solo usa este script en:
- Tus propios sistemas
- Entornos de testing con permiso explícito
- Programas de bug bounty autorizados

NUNCA lo uses en sistemas de terceros sin autorización (es ILEGAL).
"""

# Importamos la librería necesaria
import requests  # Para hacer peticiones HTTP

# Desactivamos las advertencias de SSL para certificados autofirmados
# Esto es necesario porque muchos entornos de desarrollo usan certificados no válidos
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# CONFIGURACIÓN DEL FUZZER
# -------------------------

# URL base de la API que vamos a analizar
url_base = "https://127.0.0.1/api"  # Cambia esto por la URL de tu objetivo

# Archivo con el diccionario de rutas posibles
# Este archivo debe contener una ruta por línea
# Ejemplo de contenido:
#   login
#   admin
#   users
#   api/v1
#   config
archivo_diccionario = "endpoints.txt"

# Lista de métodos HTTP que queremos probar
# GET: para obtener información
# POST: para enviar información
# Podrías añadir: PUT, DELETE, PATCH, HEAD, OPTIONS
metodos = ["GET", "POST"]


# PASO 1: CARGAR EL DICCIONARIO DE RUTAS
# ---------------------------------------
print("=" * 70)
print("API FUZZER - DESCUBRIDOR DE ENDPOINTS")
print("=" * 70)
print()
print(f"Configuración:")
print(f"  - URL base: {url_base}")
print(f"  - Diccionario: {archivo_diccionario}")
print(f"  - Métodos HTTP: {', '.join(metodos)}")
print()

# Abrimos el archivo de diccionario y leemos todas las rutas
with open(archivo_diccionario, "r") as archivo:
    # List comprehension que:
    # 1. Lee cada línea del archivo
    # 2. Elimina espacios con strip()
    # 3. Ignora líneas vacías con "if linea.strip()"
    rutas = [linea.strip() for linea in archivo if linea.strip()]

print(f"Se cargaron {len(rutas)} rutas del diccionario")
print()
print("Iniciando fuzzing... (esto puede tardar)")
print("-" * 70)

# Contadores para estadísticas
rutas_encontradas = 0
total_peticiones = 0


# PASO 2: PROBAR CADA RUTA CON CADA MÉTODO
# -----------------------------------------
# Bucle anidado: por cada ruta, probamos todos los métodos
for ruta in rutas:
    for metodo in metodos:
        # Construimos la URL completa
        # Ejemplo: https://127.0.0.1/api/login
        url_completa = f"{url_base}/{ruta}"
        
        total_peticiones += 1

        try:
            # Enviamos la petición HTTP según el método
            if metodo == "GET":
                # GET: solicita información del servidor
                # verify=False: ignora errores de certificado SSL
                # timeout=5: espera máximo 5 segundos
                respuesta = requests.get(url_completa, verify=False, timeout=5)
                
            elif metodo == "POST":
                # POST: envía información al servidor
                respuesta = requests.post(url_completa, verify=False, timeout=5)

            # ANÁLISIS DE LA RESPUESTA
            # -------------------------
            # Códigos HTTP:
            # 1xx = Informativos
            # 2xx = Éxito (200 OK, 201 Created, etc.)
            # 3xx = Redirección (301, 302, etc.)
            # 4xx = Error del cliente (404 Not Found, 403 Forbidden)
            # 5xx = Error del servidor (500, 503, etc.)
            
            # Solo nos interesan las respuestas exitosas o redirecciones (< 400)
            # Estas indican que la ruta EXISTE
            if respuesta.status_code < 400:
                rutas_encontradas += 1
                
                # Mostramos la ruta encontrada
                print(f"✓ [{metodo}] {url_completa} - Código: {respuesta.status_code}")
                
                # Análisis adicional según el código
                if respuesta.status_code == 200:
                    # 200 OK: La ruta existe y funciona correctamente
                    print(f"    → Endpoint funcional encontrado")
                    
                elif respuesta.status_code in [301, 302, 307, 308]:
                    # 3xx: Redirección
                    print(f"    → Redirige a otra ubicación")
                    
                elif respuesta.status_code == 401:
                    # 401 Unauthorized: Requiere autenticación
                    # Aunque es 4xx, indica que la ruta existe
                    print(f"    → Requiere autenticación (ruta protegida)")
                    
                elif respuesta.status_code == 403:
                    # 403 Forbidden: Sin permisos
                    print(f"    → Acceso prohibido (pero la ruta existe)")

        except requests.Timeout:
            # La petición tardó demasiado
            # Podría indicar un problema o un sistema de defensa (rate limiting)
            pass  # Ignoramos timeouts para no saturar la salida
            
        except requests.RequestException as error:
            # Cualquier otro error de conexión
            # Esto es normal cuando probamos muchas rutas que no existen
            pass  # Ignoramos errores comunes para mantener la salida limpia


# PASO 3: MOSTRAR ESTADÍSTICAS FINALES
# -------------------------------------
print("-" * 70)
print()
print("FUZZING COMPLETADO")
print("=" * 70)
print(f"Estadísticas:")
print(f"  - Total de peticiones realizadas: {total_peticiones}")
print(f"  - Rutas/endpoints encontrados: {rutas_encontradas}")
print(f"  - Tasa de éxito: {(rutas_encontradas/total_peticiones*100):.2f}%")
print()

if rutas_encontradas > 0:
    print("✓ Se encontraron endpoints accesibles")
    print("  Revisa la lista anterior para identificar posibles vulnerabilidades")
else:
    print("⚠️ No se encontraron endpoints accesibles")
    print("  Posibles razones:")
    print("  - La API no existe en esa URL")
    print("  - El diccionario no contiene las rutas correctas")
    print("  - Hay un firewall o sistema de protección bloqueando")

print()

# MEJORAS POSIBLES:
# -----------------
# 1. Añadir más métodos HTTP (PUT, DELETE, PATCH, OPTIONS, HEAD)
# 2. Enviar datos en el cuerpo (JSON, formularios)
# 3. Probar diferentes cabeceras HTTP
# 4. Añadir delays entre peticiones (time.sleep()) para no saturar
# 5. Guardar resultados en un archivo
# 6. Usar threading para ir más rápido
# 7. Detectar falsos positivos (páginas de error personalizadas)
# 8. Añadir autenticación (tokens, cookies)
#
# HERRAMIENTAS PROFESIONALES:
# - ffuf: fuzzer rápido y potente en Go
# - gobuster: descubridor de directorios
# - dirb/dirbuster: fuzzing de directorios web
# - wfuzz: fuzzer web avanzado
