def repetidos(lista):
    diccionario = {}
    for i in lista:
        if i not in diccionario:
            diccionario[i] = 1
        else:
            diccionario[i] += 1

    diccionario_ordenado = dict(sorted(diccionario.items(), key=lambda item: item[1], reverse=True))
    print(diccionario_ordenado)


# Ejemplo de uso:
mi_lista = [1, 2, 3, 2, 4, 1, 5, 1]
repetidos(mi_lista)
print("*********************************")
lis = [1,1,1,2,2,2,4,4,4,5,5,6,6,8]
repetidos(lis)

