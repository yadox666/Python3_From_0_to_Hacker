# Clase para representar una regla de firewall
class ReglaFirewall:
    def __init__(self, ip_origen, ip_destino, puerto, accion):
        """
        Inicializa una regla de firewall.
        :param ip_origen: IP de origen (ej. "192.168.1.10")
        :param ip_destino: IP de destino (ej. "10.0.0.5")
        :param puerto: Número de puerto (ej. 80)
        :param accion: "permitir" o "denegar"
        """
        self.ip_origen = ip_origen
        self.ip_destino = ip_destino
        self.puerto = puerto
        self.accion = accion.lower()  # Aseguramos que siempre esté en minúsculas

    def mostrar_regla(self):
        """Imprime la regla en formato legible."""
        print(f"Regla: {self.accion.upper()} tráfico de {self.ip_origen} hacia {self.ip_destino} en el puerto {self.puerto}")

    def esta_permitido(self, ip_origen, puerto):
        """
        Verifica si una conexión desde cierta IP y puerto está permitida por esta regla.
        :param ip_origen: IP de origen a comprobar
        :param puerto: Puerto a comprobar
        :return: True si está permitido, False si no
        """
        if self.ip_origen == ip_origen and self.puerto == puerto:
            return self.accion == "permitir"
        return False


# Crear objetos (reglas) de ejemplo
regla1 = ReglaFirewall("192.168.1.10", "10.0.0.5", 80, "permitir")
regla2 = ReglaFirewall("192.168.1.20", "10.0.0.5", 22, "denegar")

# Mostrar las reglas creadas
regla1.mostrar_regla()  # Salida: PERMITIR tráfico de 192.168.1.10 hacia 10.0.0.5 en el puerto 80
regla2.mostrar_regla()  # Salida: DENEGAR tráfico de 192.168.1.20 hacia 10.0.0.5 en el puerto 22

# Probar si ciertas conexiones están permitidas
print(regla1.esta_permitido("192.168.1.10", 80))  # True → la regla permite este tráfico
print(regla2.esta_permitido("192.168.1.20", 22))  # False → la regla explícitamente lo bloquea
