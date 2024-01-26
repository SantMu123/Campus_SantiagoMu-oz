palabra = input("Digite la palabra: ")
contador = 0

for i in palabra:
    contador += 1
    
if contador > 1 and contador <= 5:
    print("La palabra es corta")
elif contador > 5 and contador <= 10:
    print("La palabra es media")
elif contador > 10:
    print("La palabra es larga")
else:
    print("No ha ingresado palabra")