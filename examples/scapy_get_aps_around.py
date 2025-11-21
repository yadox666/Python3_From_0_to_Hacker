"""
ESCÁNER DE REDES WI-FI - Script Educativo
==========================================
Este script escanea redes Wi-Fi cercanas y muestra información sobre ellas.

¿QUÉ ES UN ESCÁNER DE REDES WI-FI?
Es un programa que detecta todas las redes Wi-Fi en el área, capturando
los paquetes "beacon" que los routers envían para anunciar su presencia.

¿QUÉ SON LOS BEACON FRAMES?
Son paquetes que los puntos de acceso (routers) envían constantemente
para anunciar su red. Contienen información como el SSID (nombre) y MAC.

¿QUÉ APRENDERÁS?
- Cómo capturar paquetes de red con Scapy
- Qué son las direcciones MAC y el OUI
- Diferencia entre SSID y BSSID
- Cómo identificar fabricantes de dispositivos
- Procesamiento de archivos JSON grandes
- Uso de sniff() para captura de paquetes en tiempo real

REQUISITOS:
1. Instalar Scapy: pip install scapy
2. Permisos de administrador: sudo python scapy_get_aps_around.py
3. Tener la suite instalada de aircrack-ng: sudo apt install aircrack-ng
4. Tarjeta Wi-Fi en modo monitor (airmon-ng start wlan0)
5. Ejecutar el script como root (sudo)
6. Tener la OUI list actualizada con el nombre `oui_list.json`
7. Archivo 'oui_list.json' en la misma carpeta

EJEMPLO DE USO:
    sudo python scapy_get_aps_around.py

NOTA IMPORTANTE:
El escaneo de redes Wi-Fi puede ser considerado intrusivo en algunos lugares.
Usa este script solo con fines educativos y en tus propias redes o con permiso.
"""

# Importamos las librerías necesarias
from scapy.all import *  # Librería para manipular paquetes de red
import json  # Librería para trabajar con archivos JSON
from scapy.layers.dot11 import Dot11, Dot11Beacon  # Clases específicas para Wi-Fi

# CONFIGURACIÓN DEL SCRIPT
# ------------------------
# Ruta al archivo JSON que contiene información de fabricantes de dispositivos
ARCHIVO_OUI = "oui_list.json"

# Nombre de la interfaz de red Wi-Fi en modo monitor
# Ejemplos comunes: "wlan0mon", "en0" (Mac), "wlan1mon"
INTERFAZ_WIFI = "wlan0mon"


def cargar_datos_fabricantes():
    """
    Esta función carga el archivo JSON con información de fabricantes.
    
    OUI (Organizationally Unique Identifier) son los primeros 3 bytes
    de una dirección MAC que identifican al fabricante del dispositivo.
    
    Retorna:
        dict: Un diccionario donde la clave es el OUI y el valor es el fabricante
        {} (vacío): Si hay algún error al cargar el archivo
    """
    try:
        # Abrimos el archivo JSON en modo lectura
        with open(ARCHIVO_OUI, "r") as archivo:
            # Cargamos los datos JSON
            datos_oui = json.load(archivo)
            
            # Convertimos la lista en un diccionario para búsquedas más rápidas
            # Ejemplo: {"00AA00": "Fabricante XYZ", "11BB11": "Fabricante ABC"}
            diccionario_fabricantes = {}
            for entrada in datos_oui:
                oui = entrada["oui"]
                organizacion = entrada["organization"]
                diccionario_fabricantes[oui] = organizacion
            
            return diccionario_fabricantes
            
    except IOError:
        # Error si no se puede abrir el archivo
        print(f"Error: No se pudo abrir el archivo {ARCHIVO_OUI}")
        return {}
    except json.JSONDecodeError:
        # Error si el archivo JSON está mal formado
        print(f"Error: El archivo {ARCHIVO_OUI} no es un JSON válido")
        return {}


def extraer_oui_de_bssid(bssid):
    """
    Extrae el OUI (identificador del fabricante) de una dirección MAC.
    
    Una dirección MAC tiene el formato: AA:BB:CC:DD:EE:FF
    El OUI son los primeros 3 pares: AA:BB:CC
    
    Parámetros:
        bssid (str): Dirección MAC del punto de acceso (ej: "A4:B2:C3:D4:E5:F6")
    
    Retorna:
        str: Los primeros 3 octetos en mayúsculas sin separadores (ej: "A4B2C3")
    """
    # Dividimos la MAC por los dos puntos y tomamos los primeros 3 elementos
    primeros_tres_octetos = bssid.split(":")[:3]
    
    # Unimos los octetos sin separadores y lo convertimos a mayúsculas
    oui = "".join(primeros_tres_octetos).upper()
    
    return oui


def procesar_paquete(paquete, diccionario_fabricantes):
    """
    Esta función procesa cada paquete Wi-Fi capturado.
    
    Los routers Wi-Fi envían constantemente paquetes llamados "beacons"
    que anuncian su presencia. Esta función lee esos paquetes.
    
    Parámetros:
        paquete: El paquete de red capturado
        diccionario_fabricantes: Diccionario con información de fabricantes
    """
    # Verificamos si el paquete es un "beacon" (anuncio de red Wi-Fi)
    if paquete.haslayer(Dot11Beacon):
        
        # Extraemos el BSSID (dirección MAC del punto de acceso)
        bssid = paquete[Dot11].addr2
        
        # Extraemos el SSID (nombre de la red Wi-Fi)
        # Si el nombre está oculto, mostramos "SSID Oculto"
        if paquete[Dot11Elt].info:
            ssid = paquete[Dot11Elt].info.decode()
        else:
            ssid = "SSID Oculto"
        
        # Obtenemos el OUI del BSSID
        oui = extraer_oui_de_bssid(bssid)
        
        # Buscamos el fabricante en nuestro diccionario
        # Si no lo encontramos, mostramos "Desconocido"
        fabricante = diccionario_fabricantes.get(oui, "Desconocido")
        
        # Mostramos la información de la red Wi-Fi encontrada
        print(f"Nombre Red: {ssid}")
        print(f"Dirección MAC: {bssid}")
        print(f"Fabricante: {fabricante}")
        print("-" * 60)


def main():
    """
    Función principal del programa.
    
    Esta función coordina todo el proceso:
    1. Carga los datos de fabricantes
    2. Inicia el escaneo de redes Wi-Fi
    3. Procesa cada paquete capturado
    """
    print("=" * 60)
    print("ESCÁNER DE REDES WI-FI")
    print("=" * 60)
    print()
    
    # Cargamos el diccionario de fabricantes
    diccionario_fabricantes = cargar_datos_fabricantes()
    
    # Verificamos si se cargaron correctamente los datos
    if not diccionario_fabricantes:
        print("Error: No se pudieron cargar los datos de fabricantes.")
        print(f"Asegúrate de que el archivo '{ARCHIVO_OUI}' existe.")
        return
    
    print(f"✓ Datos de fabricantes cargados correctamente")
    print(f"✓ Interfaz Wi-Fi: {INTERFAZ_WIFI}")
    print()
    print("Iniciando escaneo de redes Wi-Fi...")
    print("(Presiona Ctrl+C para detener)")
    print("-" * 60)
    
    try:
        # Iniciamos la captura de paquetes Wi-Fi
        # iface: interfaz de red a usar
        # prn: función que procesa cada paquete
        # store: 0 significa que no guardamos los paquetes en memoria
        sniff(
            iface=INTERFAZ_WIFI,
            prn=lambda pkt: procesar_paquete(pkt, diccionario_fabricantes),
            store=0
        )
    except KeyboardInterrupt:
        # El usuario presionó Ctrl+C
        print("\n\nEscaneo detenido por el usuario.")
    except Exception as error:
        # Otro tipo de error
        print(f"\nError durante el escaneo: {error}")
        print("\nVerifica que:")
        print("1. Estés ejecutando el script con permisos de administrador (sudo)")
        print(f"2. La interfaz '{INTERFAZ_WIFI}' exista y esté en modo monitor")


# Este bloque solo se ejecuta si el script se ejecuta directamente
# (no cuando se importa como módulo)
if __name__ == "__main__":
    main()
