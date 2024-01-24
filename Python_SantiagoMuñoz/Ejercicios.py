
"""
Verificación de Edad:
1. Pregunta a una persona su edad y utiliza una declaración if para determinar si es mayor de 18 años y puede votar.
"""

edad = eval(input("Ingresa tu edad: "))
if edad >= 18:
    print("Es mayor de edad, puede votar")
else:
    print("No es mayor de edad, no puede votar")


calificacion = eval(input("ingresa calificacion: "))
if calificacion >= 80 and calificacion <= 100:
    print("A")
elif calificacion >= 70 and calificacion < 80:
    print("B")
elif calificacion >= 60 and calificacion < 70:
    print("C")
elif calificacion >= 50 and calificacion < 60:
    print("D")
else:
    print("reprueba")

"""
Decisión de Comida:
3. Permítele a alguien elegir un tipo de comida y utiliza condicionales if para recomendar un restaurante según la elección (por ejemplo, comida italiana, mexicana o china).
"""

comida = input("Ingrese el tipo de comida: ")
if comida == "pasta":
    print("Ve a un restaurante italiano")
elif comida == "tacos":
    print("ve a un restaurante mexicano")


"""
Verificación de Contraseña:
4. Solicita una contraseña y utiliza una declaración if para verificar si coincide con una contraseña predefinida antes de permitir el acceso.
"""

contraseña = input("ingresa una contraseña: ")
con = "1234"

if con == contraseña:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

"""
Verificación de Palíndromo:
5. Pide a alguien que ingrese una palabra y utiliza condicionales para determinar si es un palíndromo, es decir, si se lee igual de izquierda a derecha y de derecha a izquierda.
"""


palabra = input("ingresa una palabra para saber si es un palíndromo")

if palabra == palabra[::-1]:
    print("la palabra es palíndromo") 
else:
    print("no es")