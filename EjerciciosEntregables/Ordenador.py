"""
Ordenador de Lista: Escribe un script que ordene una lista de números 
ingresados, pero si un número es negativo, debe ser colocado al inicio.
"""

Lista = []
Positivo = True
while Positivo:
    i = eval(input("Ingrese un numero: "))
    Lista.append(i)
    if i < 0:
        Lista.insert(0,i)
        Positivo = False
print(Lista)