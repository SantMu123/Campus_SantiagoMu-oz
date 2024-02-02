"""
Contar cuántas veces aparece un elemento en una tupla.
"""
tupla = (1,2,3,4,5,6,7,8,9,1,1,1,2,2,2,3,3,3,5,5,5,8,8,8)
contador = 0
lon = len(tupla)
for i in tupla:
    if i == 5:
        contador += 1
    
print("El numero 5 se repite: ", contador, " veces")




