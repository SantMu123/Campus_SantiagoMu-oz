"""
Desarrolla una función que simule un sistema de monitoreo para un refrigerador. Esta función debe recibir la temperatura actual del refrigerador y retornar un 
mensaje de alerta si la temperatura es menor a 2°C (riesgo de congelación) o mayor a 4°C (riesgo de descomposición).
"""

def alerta(temperatura):
    if temperatura <=2:
        return "Alerta"
    elif temperatura >=4:
        return "Riesgo de descomposicion"
    else: 
        "No es una temperatura"
        
temp = eval(input("ingrese la temperatura de su refregirador: "))

print(alerta(temp))