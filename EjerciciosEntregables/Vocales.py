palabra = input("Ingrese una palabra: ")
contador = 0
for letra in palabra:
    if letra == "a":
        contador += 1
    elif letra == "e":
        contador += 1
    elif letra == "i":
        contador += 1
    elif letra == "o":
        contador += 1
    elif letra == "u":
        contador += 1
    else:
        continue

print("La cantidad de vocales es: ", contador)