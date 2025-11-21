"""
ESCÁNER DE PUERTOS MULTIHILO - Script Educativo
================================================
Este script escanea puertos TCP de forma paralela usando múltiples hilos,
lo que hace el escaneo MUCHO más rápido que hacerlo secuencialmente.

¿QUÉ SON LOS HILOS (THREADS)?
Los hilos permiten ejecutar múltiples tareas al mismo tiempo (concurrentemente).
Es como tener varios trabajadores escaneando puertos diferentes simultáneamente
en lugar de uno solo haciendo todo el trabajo secuencialmente.

COMPARACIÓN DE VELOCIDAD:
- Escaneo secuencial (1 puerto a la vez): ~8 minutos para 1024 puertos
- Escaneo multihilo (100 puertos simultáneos): ~10 segundos para 1024 puertos

¿QUÉ APRENDERÁS?
- Uso de sockets para conexiones de red
- Programación concurrente con ThreadPoolExecutor
- Comprensión de diccionarios (dict comprehension)
- Función as_completed() para procesar resultados en tiempo real

ADVERTENCIA:
Escanear puertos sin autorización puede ser ilegal. Usa solo en tus sistemas.
"""

# Importamos las librerías necesarias
import socket  # Para crear conexiones de red
from concurrent.futures import ThreadPoolExecutor, as_completed  # Para programación paralela


# CONFIGURACIÓN DEL ESCANEO
# --------------------------
# Dirección IP del objetivo a escanear
objetivo = "127.0.0.1"  # 127.0.0.1 = localhost (tu propio equipo)
                        # También puedes usar: "192.168.1.1", "scanme.nmap.org", etc.

# Definimos el rango de puertos a escanear
rango_puertos = range(1, 1025)  # Puertos del 1 al 1024 (puertos "well-known")
                                # Puedes cambiar a range(1, 100) para pruebas rápidas


# FUNCIÓN DE ESCANEO DE PUERTO INDIVIDUAL
# ----------------------------------------
def escanear_puerto(puerto):
    """
    Intenta conectarse a un puerto específico para verificar si está abierto.
    
    Esta función se ejecutará en paralelo (múltiples veces simultáneamente).
    
    Parámetros:
        puerto (int): Número de puerto a escanear (1-65535)
    
    Retorna:
        tuple: (numero_puerto, estado) donde estado es "ABIERTO" o "CERRADO"
    """
    # Creamos un socket (conexión de red)
    # AF_INET = IPv4, SOCK_STREAM = TCP
    # 'with' asegura que el socket se cierre automáticamente al terminar
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Establecemos timeout de 0.5 segundos
        # Si no hay respuesta en 0.5s, consideramos que el puerto está cerrado/filtrado
        sock.settimeout(0.5)
        
        # connect_ex() intenta conectarse al puerto
        # Retorna 0 si la conexión fue exitosa (puerto abierto)
        # Retorna otro número (código de error) si falla (puerto cerrado)
        if sock.connect_ex((objetivo, puerto)) == 0:
            return puerto, "ABIERTO"   # El puerto aceptó la conexión
        return puerto, "CERRADO"       # El puerto rechazó la conexión o no respondió


# FUNCIÓN PRINCIPAL DE ESCANEO MULTIHILO
# ---------------------------------------
def escaneo_con_hilos():
    """
    Ejecuta el escaneo de puertos usando múltiples hilos en paralelo.
    
    ThreadPoolExecutor gestiona automáticamente un grupo de hilos,
    distribuyendo el trabajo entre ellos eficientemente.
    """
    print(f"Escaneando {objetivo} con múltiples hilos...")
    print(f"Rango de puertos: {rango_puertos.start}-{rango_puertos.stop-1}")
    print(f"Esto puede tardar unos segundos...\n")

    # Creamos un pool (grupo) de 100 hilos trabajadores
    # max_workers=100 significa que 100 puertos se escanearán simultáneamente
    with ThreadPoolExecutor(max_workers=100) as ejecutor:
        
        # submit() envía una tarea al pool de hilos
        # Esta línea usa "dict comprehension" para crear un diccionario:
        # - Clave: objeto Future (representa la tarea en ejecución)
        # - Valor: número de puerto asociado
        # Se crea una tarea por cada puerto en el rango
        tareas = {ejecutor.submit(escanear_puerto, puerto): puerto for puerto in rango_puertos}

        # as_completed() devuelve las tareas conforme van terminando
        # No esperamos a que todas terminen, procesamos resultados en tiempo real
        for tarea in as_completed(tareas):
            # result() obtiene el valor retornado por escanear_puerto()
            puerto, estado = tarea.result()
            
            # Solo mostramos los puertos abiertos (los cerrados no son interesantes)
            if estado == "ABIERTO":
                print(f"Puerto TCP {puerto}: {estado}")
    
    print("\nEscaneo completado.")


# PUNTO DE ENTRADA DEL PROGRAMA
# ------------------------------
if __name__ == "__main__":
    # Este bloque solo se ejecuta si ejecutas el script directamente
    escaneo_con_hilos()