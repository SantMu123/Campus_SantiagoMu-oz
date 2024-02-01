def trozos(lista, limite):
    Nueva = []
    lon = len(lista)
    partes = lon//limite
    for i in range(partes-1):
        for j in range(limite-1):
            Nueva.append(lista[j])
            lista.remove(lista[j])
            
        
        print(Nueva, end = ",")


lis = [1,2,3,4,6,7,8,9]
trozos(lis,2)


    