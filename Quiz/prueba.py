lista = [{"hola":(1,300)},{"dos":(2,400)}]

for i in lista:
    print(list(i.keys())[0])
    print(list(i.values())[0][0])
    print("-----")

