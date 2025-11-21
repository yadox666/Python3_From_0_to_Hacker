import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

# Dirección del objetivo (localhost en este caso)
objetivo = "127.0.0.1"

# Rango de puertos a escanear (puedes reducirlo para pruebas)
rango_puertos = range(1, 1025)  # Puertos comunes: 1 al 1024

# Función que intenta conectarse a un puerto
def escanear_puerto(puerto):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)  # Tiempo máximo de espera
        if sock.connect_ex((objetivo, puerto)) == 0:
            return puerto, "ABIERTO"
        return puerto, "CERRADO"

# Ejecutamos el escaneo en paralelo usando hilos
def escaneo_con_hilos():
    print(f"Escaneando {objetivo} con múltiples hilos...")

    # Creamos un "pool" de 100 hilos
    with ThreadPoolExecutor(max_workers=100) as ejecutor:
        # Enviamos tareas al pool: un hilo por puerto
        tareas = {ejecutor.submit(escanear_puerto, puerto): puerto for puerto in rango_puertos}

        # Imprimimos los resultados a medida que terminan
        for tarea in as_completed(tareas):
            puerto, estado = tarea.result()
            if estado == "ABIERTO":
                print(f"Puerto TCP {puerto}: {estado}")

# Llamamos a la función principal
if __name__ == "__main__":
    escaneo_con_hilos()