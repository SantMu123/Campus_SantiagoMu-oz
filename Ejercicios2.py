"""
horas = eval(input("Ingrese la cantidad de horas: "))

if horas <= 10:
    sueldo = 5 * horas
elif horas > 10 & horas <= 20:
    sueldo = 10 * horas
elif horas >= 20:
    sueldo = 15 * horas

print("Su sueldo es: ", sueldo) 

"""

num1 = eval(input("Ingrese el primer numero: "))
num2 = eval(input("Ingrese el primer numero: "))
num3 = eval(input("Ingrese el primer numero: "))

promedio = (num1 + num2 + num3) / 3

if promedio >= 3:
    print("El estudiante aprobó")
else:
    print("El estudiante No aprobó")


