comando = input("si desea Celsius --> Fahrenheit, marque A, si es vicerverza marque B")
valor = eval(input("ingrese la temperatura a convertir"))

if comando == "A":
    fah = (valor * 9/5) + 32
    print("La conversion es: ", fah)
elif comando == "B":
    cel = (valor - 32) * 5/9
    print("La conversion es: ", cel)
else:
    print("Comando incorrecto")