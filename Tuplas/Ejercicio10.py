"""
Crear una tupla con números y encontrar el mínimo y máximo.
"""
import random

tupla = (1,2,3,4,9,7,8,3,5,4,6)
num1 = tupla[random.randint(0,9)]
num2 = tupla[random.randint(0,9)]
may = max(tupla)
min = min(tupla)
"""
for i in tupla:
    if i < num1:
        min = i
    else:
        min = num1
    
    if i > num2:
        may = i
    else:
        may = num2
"""  

print("el minimo es: ", min, " el maximo es: ", may)

        
