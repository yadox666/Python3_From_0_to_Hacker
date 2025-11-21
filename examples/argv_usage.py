"""
SYS.ARGV - Script Educativo
============================
Este script demuestra el uso básico de sys.argv para recibir argumentos
desde la línea de comandos.

¿QUÉ ES SYS.ARGV?
sys.argv es una lista que contiene todos los argumentos pasados al script:
- argv[0] = nombre del script
- argv[1], argv[2], ... = argumentos adicionales

EJEMPLO DE USO:
    python argv_usage.py uno dos tres
"""

# Importamos el módulo sys (system)
# Este módulo proporciona acceso a variables y funciones del sistema
import sys

# len(sys.argv) cuenta cuántos elementos hay en la lista de argumentos
# IMPORTANTE: El primer elemento (índice 0) es siempre el nombre del script
print("Número de argumentos:", len(sys.argv))

# sys.argv es una lista con todos los argumentos
# Todos los valores en sys.argv son strings (texto)
print("Lista de argumentos:", sys.argv)

# EJEMPLO DE EJECUCIÓN:
# python3 argv_usage.py uno dos tres
# 
# SALIDA ESPERADA:
# Número de argumentos: 4
# Lista de argumentos: ['argv_usage.py', 'uno', 'dos', 'tres']
#
# EXPLICACIÓN:
# - argv[0] = 'argv_usage.py' (nombre del script)
# - argv[1] = 'uno' (primer argumento)
# - argv[2] = 'dos' (segundo argumento)
# - argv[3] = 'tres' (tercer argumento)
