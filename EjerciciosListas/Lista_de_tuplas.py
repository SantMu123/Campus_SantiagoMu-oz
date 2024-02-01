
def listaTuplas(lista1, lista2):
    NuevaLista = []
    for i,j in zip(lista1,lista2):
        lis = [i,j]
        tupla = tuple(lis)
        NuevaLista.append(tupla)
    
        
    print(NuevaLista)
    
lista1 = [1,2,3,4,5,6,7]
lista2 = [4,5,6,7,8,9,8]

listaTuplas(lista1, lista2) 

       