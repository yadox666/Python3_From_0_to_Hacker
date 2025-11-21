"""
CLASES EN PYTHON - Script Educativo
====================================
Este script enseña los conceptos fundamentales de Programación Orientada
a Objetos (POO) usando como ejemplo una clase para reglas de firewall.

¿QUÉ ES UNA CLASE?
Una clase es un "molde" o "plantilla" para crear objetos. Define:
- ATRIBUTOS: características o propiedades (datos)
- MÉTODOS: acciones o comportamientos (funciones)

¿QUÉ ES UN OBJETO?
Un objeto es una INSTANCIA de una clase (un caso específico creado a partir del molde).
Ejemplo: Si "Coche" es la clase, "mi_coche_rojo" sería un objeto.

¿POR QUÉ USAR CLASES?
- Organizar código de forma lógica
- Reutilizar código (crear múltiples objetos del mismo tipo)
- Modelar entidades del mundo real
- Encapsular datos y funcionalidad

CONCEPTOS CLAVE QUE APRENDERÁS:
1. Definición de clases con 'class'
2. Método constructor __init__()
3. El parámetro 'self'
4. Atributos de instancia
5. Métodos de instancia
6. Crear objetos (instanciar)
7. Llamar métodos de objetos
"""

# ============================================================================
# DEFINICIÓN DE LA CLASE
# ============================================================================

# La palabra clave 'class' define una nueva clase
# Por convención, los nombres de clases usan CamelCase (primera letra mayúscula)
class ReglaFirewall:
    """
    Clase que representa una regla de firewall.
    
    Esta clase modela una regla que controla el tráfico de red,
    permitiendo o denegando conexiones según IP de origen, destino y puerto.
    
    Atributos:
        ip_origen (str): Dirección IP desde donde se origina la conexión
        ip_destino (str): Dirección IP de destino
        puerto (int): Número de puerto (1-65535)
        accion (str): "permitir" o "denegar"
    """
    
    # MÉTODO CONSTRUCTOR: __init__()
    # ------------------------------
    # Este es un método especial que se ejecuta automáticamente al crear un objeto
    # Se usa para INICIALIZAR los atributos del objeto
    
    def __init__(self, ip_origen, ip_destino, puerto, accion):
        """
        Constructor: inicializa una nueva regla de firewall.
        
        IMPORTANTE: El primer parámetro de TODOS los métodos es 'self'
        'self' representa el objeto que se está creando/manipulando
        
        Parámetros:
            self: referencia automática al objeto (NO lo pasas al llamar)
            ip_origen: IP de origen (ej: "192.168.1.10")
            ip_destino: IP de destino (ej: "10.0.0.5")
            puerto: Número de puerto (ej: 80 para HTTP, 22 para SSH)
            accion: "permitir" o "denegar"
        """
        # self.nombre_atributo = valor
        # Esto crea ATRIBUTOS DE INSTANCIA (variables que pertenecen al objeto)
        
        self.ip_origen = ip_origen      # Guardamos la IP de origen
        self.ip_destino = ip_destino    # Guardamos la IP de destino
        self.puerto = puerto            # Guardamos el puerto
        
        # lower() convierte a minúsculas para evitar problemas de comparación
        # "Permitir", "PERMITIR", "permitir" → todos se vuelven "permitir"
        self.accion = accion.lower()

    # MÉTODO DE INSTANCIA 1
    # ---------------------
    # Los métodos son funciones que pertenecen a la clase
    # Siempre reciben 'self' como primer parámetro
    
    def mostrar_regla(self):
        """
        Imprime la regla de firewall en formato legible.
        
        Este método no recibe parámetros (excepto self) y no retorna nada,
        solo imprime información en la consola.
        """
        # Accedemos a los atributos del objeto usando self.nombre_atributo
        # upper() convierte la acción a mayúsculas para mejor visualización
        print(f"Regla: {self.accion.upper()} tráfico de {self.ip_origen} "
              f"hacia {self.ip_destino} en el puerto {self.puerto}")

    # MÉTODO DE INSTANCIA 2
    # ---------------------
    # Este método recibe parámetros adicionales y retorna un valor
    
    def esta_permitido(self, ip_origen, puerto):
        """
        Verifica si una conexión está permitida por esta regla.
        
        Este método compara la IP y puerto dados con los de la regla,
        y determina si la acción es "permitir" o "denegar".
        
        Parámetros:
            self: el objeto actual (automático)
            ip_origen: IP de origen a verificar
            puerto: Puerto a verificar
        
        Retorna:
            bool: True si está permitido, False si está denegado
        
        Ejemplo:
            regla.esta_permitido("192.168.1.10", 80) → True o False
        """
        # Comparamos los parámetros recibidos con los atributos del objeto
        if self.ip_origen == ip_origen and self.puerto == puerto:
            # Si coinciden, retornamos True si la acción es "permitir"
            return self.accion == "permitir"
        
        # Si no coinciden, esta regla no aplica (retornamos False)
        return False


# ============================================================================
# USO DE LA CLASE: CREAR OBJETOS (INSTANCIAS)
# ============================================================================

print("=" * 70)
print("DEMOSTRACIÓN DE CLASES EN PYTHON")
print("=" * 70)
print()

# CREAR OBJETOS (INSTANCIAR LA CLASE)
# ------------------------------------
# Sintaxis: nombre_objeto = NombreClase(argumentos)
# Los argumentos se pasan al método __init__()
# NOTA: NO pasamos 'self', Python lo hace automáticamente

print("1. CREANDO OBJETOS (INSTANCIAS DE LA CLASE)")
print("-" * 70)

# Creamos el primer objeto: una regla que PERMITE tráfico
# regla1 es una INSTANCIA de la clase ReglaFirewall
regla1 = ReglaFirewall("192.168.1.10", "10.0.0.5", 80, "permitir")
print("✓ Creado objeto 'regla1': PERMITE tráfico HTTP (puerto 80)")

# Creamos el segundo objeto: una regla que DENIEGA tráfico
# regla2 es otra INSTANCIA de la misma clase, pero con valores diferentes
regla2 = ReglaFirewall("192.168.1.20", "10.0.0.5", 22, "denegar")
print("✓ Creado objeto 'regla2': DENIEGA tráfico SSH (puerto 22)")

print()


# ACCEDER A ATRIBUTOS DE LOS OBJETOS
# -----------------------------------
print("2. ACCEDIENDO A ATRIBUTOS DE LOS OBJETOS")
print("-" * 70)

# Podemos leer los atributos usando: objeto.atributo
print(f"IP origen de regla1: {regla1.ip_origen}")
print(f"Puerto de regla1: {regla1.puerto}")
print(f"Acción de regla1: {regla1.accion}")
print()
print(f"IP origen de regla2: {regla2.ip_origen}")
print(f"Puerto de regla2: {regla2.puerto}")
print(f"Acción de regla2: {regla2.accion}")

print()


# LLAMAR MÉTODOS DE LOS OBJETOS
# ------------------------------
print("3. LLAMANDO MÉTODOS DE LOS OBJETOS")
print("-" * 70)

# Sintaxis: objeto.metodo(argumentos)
# NOTA: NO pasamos 'self', Python lo hace automáticamente

# Llamamos al método mostrar_regla() de cada objeto
regla1.mostrar_regla()  
# Internamente ejecuta: mostrar_regla(regla1)
# Por eso dentro del método podemos usar self.ip_origen, etc.

regla2.mostrar_regla()

print()


# USAR MÉTODOS QUE RETORNAN VALORES
# ----------------------------------
print("4. USANDO MÉTODOS QUE RETORNAN VALORES")
print("-" * 70)

# Probamos si ciertas conexiones están permitidas
# Estos métodos retornan True o False

resultado1 = regla1.esta_permitido("192.168.1.10", 80)
print(f"¿Regla1 permite 192.168.1.10:80? {resultado1}")
# True porque la regla1 tiene acción="permitir" para esa IP y puerto

resultado2 = regla2.esta_permitido("192.168.1.20", 22)
print(f"¿Regla2 permite 192.168.1.20:22? {resultado2}")
# False porque la regla2 tiene acción="denegar" para esa IP y puerto

# Probemos una IP diferente
resultado3 = regla1.esta_permitido("192.168.1.99", 80)
print(f"¿Regla1 permite 192.168.1.99:80? {resultado3}")
# False porque la IP no coincide con la de la regla

print()


# MÚLTIPLES OBJETOS INDEPENDIENTES
# ---------------------------------
print("5. CADA OBJETO ES INDEPENDIENTE")
print("-" * 70)

# Podemos crear muchos objetos de la misma clase
# Cada uno tiene sus propios atributos (valores independientes)
regla3 = ReglaFirewall("10.0.0.1", "172.16.0.1", 443, "permitir")
regla4 = ReglaFirewall("10.0.0.2", "172.16.0.1", 3306, "denegar")

print("Se crearon 4 objetos ReglaFirewall en total:")
regla1.mostrar_regla()
regla2.mostrar_regla()
regla3.mostrar_regla()
regla4.mostrar_regla()

print()
print("=" * 70)
print("FIN DE LA DEMOSTRACIÓN")
print("=" * 70)

# RESUMEN DE CONCEPTOS:
# ======================
# 
# 1. CLASE: Plantilla para crear objetos (definida con 'class')
# 2. OBJETO: Instancia específica de una clase
# 3. __init__(): Método constructor que inicializa el objeto
# 4. self: Referencia al objeto actual (primer parámetro de métodos)
# 5. ATRIBUTOS: Variables que pertenecen al objeto (self.nombre)
# 6. MÉTODOS: Funciones que pertenecen a la clase
# 7. INSTANCIAR: Crear un objeto (objeto = Clase(argumentos))
# 8. LLAMAR MÉTODO: objeto.metodo(argumentos)
# 9. ACCEDER ATRIBUTO: objeto.atributo
#
# ANALOGÍA:
# ---------
# Clase = Receta de galletas (las instrucciones)
# Objeto = Galleta específica (resultado de seguir la receta)
# Atributos = Características (sabor, tamaño, color)
# Métodos = Acciones (hornear, decorar, comer)
