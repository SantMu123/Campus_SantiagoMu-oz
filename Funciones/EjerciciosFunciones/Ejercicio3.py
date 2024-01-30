"""
Escribe una función que recomiende qué tipo de ropa vestir basado en la temperatura exterior actual. 
Por ejemplo, por encima de 25°C recomienda ropa ligera, entre 15°C y 25°C sugiere una camiseta y pantalón, etc.
"""

def recomienda(temperatura):
    if temperatura >= 25:
        return "Viste Ropa ligera"
    elif temperatura >= 15 and temperatura <= 25:
        return "Viste con camiseta y pantalon"
    elif temperatura < 15:
        return "Viste con Buso y bufanda"
    
temp = eval(input("Ingresa la temperatura del día: "))
print(recomienda(temp))