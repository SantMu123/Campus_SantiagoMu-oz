"""
Implementa una función que ordene una lista de tuplas 
basándose en el segundo elemento de cada tupla.
"""
def ordenar(listas):
    lon = len(listas)
    for i in range(lon-1):
        for j in range(lon-i-1):
            if listas[j][1] < listas[j+1][1]:
                listas[j],listas[j+1] = listas[j+1],listas[j]
    print(listas)

lista_de_tuplas = [
    (20, 10),
    (40, 20),
    (10, 30),
    (4, 40)
]
        
ordenar(lista_de_tuplas)