import argparse

parser = argparse.ArgumentParser(description="Ejemplo básico de argparse.")
parser.add_argument("--nombre", required=True, help="Tu nombre")
parser.add_argument("--edad", type=int, help="Tu edad")

args = parser.parse_args()
print(f"Hola {args.nombre}, tienes {args.edad} años.")

# python3 argparse_usage.py --nombre Ana --edad 30
# Salida:
# Hola Ana, tienes 30 años.