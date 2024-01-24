"""
Organiza run programa que le pregunte al usarui el nombre, numeros de horas trabajadas
el costo por hora y debe mostrar:

Al señor se le debe tanto
"""

nombre = input("Ingrese su nombre: ")
horas = eval(input("Ingrese las horas trabajadas: "))
costoPorHora = eval(input("Cual es el costo por hora: "))

total = horas * costoPorHora

print("Al señor " + nombre + " que trabajó ", horas, "horas" + " Se le debe pagar: ", total, " pesos")