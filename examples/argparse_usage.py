"""
ARGPARSE BÁSICO - Script Educativo
===================================
Este script introduce los conceptos básicos de argparse para crear programas
que aceptan argumentos desde la línea de comandos.

¿QUÉ ES ARGPARSE?
argparse es una librería estándar de Python que permite que tus programas
reciban información desde la línea de comandos, igual que comandos del sistema
como 'ls -la' o 'grep -i texto'.

¿POR QUÉ USAR ARGPARSE?
- Hace que tus programas sean más flexibles
- Permite reutilizar el mismo código con diferentes valores
- Genera ayuda automática con --help
- Valida automáticamente los datos de entrada

EJEMPLO DE USO:
    python argparse_usage.py --nombre Ana --edad 30

PARA VER LA AYUDA:
    python argparse_usage.py --help
"""

# Importamos la librería argparse
# Esta librería viene incluida con Python (no necesitas instalarla)
import argparse


# PASO 1: CREAR EL PARSER
# ------------------------
# El parser (analizador) es el objeto que se encargará de leer
# y procesar los argumentos que el usuario escriba en la terminal

parser = argparse.ArgumentParser(
    description="Ejemplo básico de argparse: solicita nombre y edad del usuario.",
    epilog="Ejemplo: python argparse_usage.py --nombre Ana --edad 30"
)

# PASO 2: DEFINIR LOS ARGUMENTOS
# -------------------------------
# Ahora le decimos al parser qué argumentos esperamos recibir

# Argumento 1: --nombre
# El usuario DEBE proporcionar su nombre (required=True)
parser.add_argument(
    "--nombre",
    required=True,  # Este argumento es obligatorio
    help="Tu nombre completo"
)

# Argumento 2: --edad
# Este argumento espera un número entero (type=int)
# Python validará automáticamente que sea un número
parser.add_argument(
    "--edad",
    type=int,  # Solo acepta números enteros
    help="Tu edad en años (debe ser un número entero)"
)


# PASO 3: PROCESAR LOS ARGUMENTOS
# --------------------------------
# parse_args() lee lo que el usuario escribió en la terminal
# y lo convierte en un objeto con los valores
args = parser.parse_args()


# PASO 4: USAR LOS ARGUMENTOS
# ----------------------------
# Ahora podemos acceder a los valores con args.nombre_argumento

print("=" * 50)
print("INFORMACIÓN RECIBIDA")
print("=" * 50)
print()

# Mostramos el mensaje personalizado
if args.edad is not None:
    print(f"Hola {args.nombre}, tienes {args.edad} años.")
    
    # Agregamos algo de lógica adicional para hacer el ejemplo más interesante
    if args.edad < 18:
        print("Eres menor de edad.")
    elif args.edad < 65:
        print("Eres adulto.")
    else:
        print("Eres adulto mayor.")
else:
    # Si el usuario no proporcionó la edad
    print(f"Hola {args.nombre}.")

print()
print("=" * 50)


# EJEMPLOS DE CÓMO EJECUTAR ESTE SCRIPT:
# ---------------------------------------
# 
# Ejemplo 1 - Con nombre y edad:
#   python argparse_usage.py --nombre Ana --edad 30
#   Salida: Hola Ana, tienes 30 años.
#
# Ejemplo 2 - Solo con nombre:
#   python argparse_usage.py --nombre Juan
#   Salida: Hola Juan.
#
# Ejemplo 3 - Ver la ayuda:
#   python argparse_usage.py --help
#   Muestra toda la documentación del script
#
# Ejemplo 4 - Error si falta el nombre:
#   python argparse_usage.py --edad 25
#   Error: el argumento --nombre es obligatorio
#
# Ejemplo 5 - Error si la edad no es un número:
#   python argparse_usage.py --nombre Pedro --edad abc
#   Error: el argumento --edad debe ser un entero