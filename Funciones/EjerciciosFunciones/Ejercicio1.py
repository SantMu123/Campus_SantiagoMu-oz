"""
Calculadora de Propina
Crea una función que calcule cuánto de propina dejar en un restaurante basado en la calidad del servicio. 
La función debe aceptar el monto de la cuenta y la calidad del servicio (buena, aceptable, mala) y retornar el monto de la propina.
"""

def propina(cuenta, calidad):
    if calidad == "buena":
        return cuenta*0.15
    elif calidad == "aceptable":
        return cuenta*0.10
    elif calidad == "mala":
        return cuenta*0.05
    else:
        return cuenta
    
print("Hola usuario")
cue = eval(input("Ingresa la cuenta: "))
servicio = input("Ingresa la calidad del servicio: ")

total_Propina = propina(cue, servicio)
print("el total a propina a dejar es: ", total_Propina)