import random 

ale = random.randint(1,100)
bandera = True
print(ale)

while bandera:
    num = eval(input("Ingrese el numero: "))
    if num > ale:
        print("El numero está por encima")
    elif num < ale:
        print("El numero es menor")
    else:
        print("Adivinista el numero: ", ale)
        bandera = False 

