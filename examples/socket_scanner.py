import socket  # Módulo para trabajar con conexiones de red

# Dirección IP del equipo a escanear (localhost por defecto)
objetivo = "127.0.0.1"

# Rango de puertos a probar (puedes reducirlo para pruebas rápidas)
puertos = range(1, 1025)  # Del 1 al 1024 (puertos comunes)

# Mostrar puertos cerrados (útil para depurar)
debug = False

# Función que escanea los puertos del objetivo
def escanear_puertos(host, rango_puertos):
    print(f"Escaneando {host}...")

    for puerto in rango_puertos:
        # Creamos un socket tipo TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Máximo 1 segundo por intento

        # Intentamos conectarnos al puerto
        resultado = s.connect_ex((host, puerto))

        if resultado == 0:
            print(f"Puerto {puerto}: ABIERTO")
        elif debug:
            print(f"Puerto {puerto}: CERRADO")

        s.close()  # Cerramos el socket para liberar recursos

# Ejecutamos el escaneo
escanear_puertos(objetivo, puertos)
