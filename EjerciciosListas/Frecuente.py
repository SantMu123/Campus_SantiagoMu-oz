def frecuente(lista):
    Nueva = []
    for i in lista:
        if i not in Nueva:
            Nueva.append(i)
    
    for j in Nueva:
        diccionario = {"Numero":j,
                       "Repetecion": 0}
    
    print(diccionario)
    
    
lista = [1,1,2,3,4,5,5,5,5,4,4,2,3,4,1,1,1]

frecuente(lista)