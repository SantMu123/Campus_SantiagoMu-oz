"""
Acceder al valor de una clave específica en el diccionario.
"""

diccionario = {"santiago":23, "Paula":25, "Laura":45}

#nombre = list(diccionario.keys())
nombre = list(diccionario.keys())[list(diccionario.values()).index(23)]
print(nombre)

for i in diccionario:
    if diccionario[i] == 23:
        print("La clave es: ", i)