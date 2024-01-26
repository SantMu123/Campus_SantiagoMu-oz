palabra = input("Ingrese una palabra: ")
contadorVocal = 0
contadorConso = 0
for letra in palabra:
    if letra == "a":
        contadorVocal += 1
    elif letra == "e":
        contadorVocal += 1
    elif letra == "i":
        contadorVocal += 1
    elif letra == "o":
        contadorVocal += 1
    elif letra == "u":
        contadorVocal += 1
    elif letra == " ":
        continue
    else:
        contadorConso += 1

print("La cantidad de vocales es: ", contadorVocal)
print("La cantidad de vocales es: ", contadorConso)