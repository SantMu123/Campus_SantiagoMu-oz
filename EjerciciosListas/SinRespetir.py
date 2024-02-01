"""
Se crea una funcion en donde se utiliza un bucle que itere sobre los elementos de la lista que se pasa como parametro,
dentro, utilizo una estructura condicional que que verfica si el numero no está en la lista nueva que se ha creado para
almacenar los numeros únicos, si no está, se utiliza el método "append" para añadirlo en la lista nueva, finalmente, se
retorna dicha lista nueva llamada "Nueva"
"""

def ListaSinRepetir(lista,Nueva):
    for i in lista:
        if i not in Nueva:
            Nueva.append(i)
    return Nueva
            
lista = [1,1,2,3,4,5,5,5,5,4,4,2,3,4,1,1,1]
Nueva = []
print(ListaSinRepetir(lista, Nueva))




lon = len(lista)
for i in range(lon-1):
    for j in range(lon-1):
        if i == j:
            continue
        else:
            if lista[j] == lista[i]:
                lista.remove(j)
            else:
                continue
            
print(lista)

