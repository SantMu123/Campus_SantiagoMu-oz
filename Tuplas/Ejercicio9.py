"""
Comprobar si un elemento existe en una tupla.
"""

tupla = (1,2,3,4,5,6,7,8,9,1,2,3,4)
contador = 0

for i in tupla:
    if i == 1:
        contador += 1
        
    if contador >= 2:
        print("El numero 1 se repite dos veces o mas")
        break

        

        