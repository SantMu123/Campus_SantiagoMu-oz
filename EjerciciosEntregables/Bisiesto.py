año = eval(input("Ingrese el año: "))

if (año % 400 == 0 or (año % 4 == 0 and año % 100 != 0)):
    print("año es bisiesto")
else:
    print("No es bisiesto") 