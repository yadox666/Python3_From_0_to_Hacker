"""
ESCÁNER DE PUERTOS SIMPLE - Script Educativo
=============================================
Este script escanea puertos TCP de forma secuencial (uno tras otro)
para detectar cuáles están abiertos en un equipo.

¿QUÉ ES UN SOCKET?
Un socket es el "punto final" de una conexión de red. Es como un enchufe:
permite que dos programas se comuniquen a través de la red.

¿QUÉ ES UN PUERTO?
Los puertos son números del 1 al 65535 que identifican servicios específicos:
- Puerto 80: Servidor web HTTP
- Puerto 443: Servidor web HTTPS
- Puerto 22: SSH (conexión remota)
- Puerto 3306: MySQL (base de datos)

¿QUÉ APRENDERÁS?
- Uso básico de sockets en Python
- Cómo detectar si un puerto está abierto o cerrado
- Diferencia entre escaneo secuencial y paralelo
- Uso de connect_ex() para probar conexiones

NOTA: Este script es LENTO porque escanea un puerto a la vez.
Para escaneos más rápidos, usa socket_scanner_multithreaded.py

ADVERTENCIA:
Escanear puertos sin autorización puede ser ilegal. Usa solo en tus sistemas.
"""

# Importamos el módulo socket
import socket  # Módulo para trabajar con conexiones de red (viene incluido con Python)


# CONFIGURACIÓN DEL ESCANEO
# --------------------------
# Dirección IP del equipo a escanear
objetivo = "127.0.0.1"  # 127.0.0.1 = localhost (tu propio equipo)
                        # También puedes usar: "192.168.1.1", "scanme.nmap.org", etc.

# Definimos el rango de puertos a escanear
puertos = range(1, 1025)  # Del 1 al 1024 (puertos "well-known" o comunes)
                          # Puedes cambiar a range(1, 100) para pruebas más rápidas

# Variable de depuración: muestra también los puertos cerrados
debug = False  # Cambia a True si quieres ver TODOS los puertos (abiertos y cerrados)


# FUNCIÓN DE ESCANEO
# -------------------
def escanear_puertos(host, rango_puertos):
    """
    Escanea un rango de puertos en un host para detectar cuáles están abiertos.
    
    Este escaneo es SECUENCIAL: prueba un puerto, espera resultado, prueba el siguiente.
    Por eso es lento (puede tardar varios minutos para 1024 puertos).
    
    Parámetros:
        host (str): Dirección IP o nombre del host a escanear
        rango_puertos (range): Rango de puertos a verificar
    """
    print(f"Escaneando {host}...")
    print(f"Rango de puertos: {rango_puertos.start}-{rango_puertos.stop-1}")
    print(f"Esto puede tardar varios minutos (escaneo secuencial)...\n")

    # Iteramos sobre cada puerto del rango
    for puerto in rango_puertos:
        # PASO 1: Crear un socket
        # AF_INET = familia de direcciones IPv4
        # SOCK_STREAM = tipo de socket TCP (conexión orientada, confiable)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # PASO 2: Establecer timeout (tiempo máximo de espera)
        # Si no hay respuesta en 1 segundo, consideramos el puerto cerrado/filtrado
        s.settimeout(1)

        # PASO 3: Intentar conectarnos al puerto
        # connect_ex() es similar a connect() pero retorna un código de error
        # en lugar de lanzar una excepción
        # Retorna 0 si la conexión fue exitosa (puerto abierto)
        # Retorna otro número (código de error) si falla (puerto cerrado/filtrado)
        resultado = s.connect_ex((host, puerto))

        # PASO 4: Interpretar el resultado
        if resultado == 0:
            # Si resultado es 0, el puerto aceptó la conexión = está ABIERTO
            print(f"Puerto {puerto}: ABIERTO")
        elif debug:
            # Si debug está activado, mostramos también los puertos cerrados
            # Esto genera MUCHA salida, por eso está desactivado por defecto
            print(f"Puerto {puerto}: CERRADO")

        # PASO 5: Cerrar el socket para liberar recursos del sistema
        # Es importante cerrar cada socket después de usarlo
        s.close()
    
    print("\nEscaneo completado.")


# PUNTO DE ENTRADA DEL PROGRAMA
# ------------------------------
# Ejecutamos la función de escaneo con los parámetros configurados
escanear_puertos(objetivo, puertos)

# DIFERENCIA CON socket_scanner_multithreaded.py:
# ------------------------------------------------
# Este script:  Escanea 1 puerto → espera → escanea siguiente puerto
#               Tiempo: ~8-10 minutos para 1024 puertos
#
# Multihilo:    Escanea 100 puertos simultáneamente
#               Tiempo: ~10 segundos para 1024 puertos
#
# Usa este script para aprender los conceptos básicos.
# Usa el multihilo para escaneos reales (es 50x más rápido).
