"""
nombre de usuario, hola ... bienvenido
area de un cuadrado, dentro de la funcion solamente debvolver el area
"""

def areaCuadrado(lado):
    return lado * lado

lado = eval(input("ingresa el lado del cuadrado: "))

area = areaCuadrado(lado)

print("El area del cuadrado es: ", area)


def Saludo(nombre):
    print(f"Hola, {nombre}")

Saludo("Santiago")