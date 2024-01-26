num = eval(input("Ingrese un numero para saber si es primo"))
contador = 0

for i in (1,num+1):
    if num % i == 0:
        contador += 1
        
if contador > 2:
    print("El numero: ", num, "Es primo")
else:
    print("No es primo")
