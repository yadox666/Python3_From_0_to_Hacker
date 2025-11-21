
try:
	csv = open("ejemplo.csv","r")
except Exception as e:
	print("El fichero no se encontro")
	exit()

for linea in csv:
	if "nombre," in linea:
		continue
	linea = linea.rstrip()
	nombre = linea.split(",")[0]
	apellido = linea.split(",")[1]
	email = linea.split(",")[2]
	print(f"Mi nombre es {nombre} {apellido} y mi email es {email}")

csv.close()
