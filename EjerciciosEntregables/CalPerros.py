"""
https://www.zooplus.es/magazine/perros/adoptar-un-perro/ano-de-perro-en-humano

"""
tamaño = input("Digite G si El perro es grande, M si es Mediana o P si es Pequeño: ")
Perro = eval(input("Digite la edad del perro en años para la conversion: "))

Pequeño = [15,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,90,94,100,]
medio = [10,18,21,27,33,39,45,51,57,63,69,75,80,85,90,95,100]
Gran  = [8,14,18,22,31,40,49,58,67,76,85,94,100]

if tamaño == "G":
    edadHumano = Gran[Perro]
    print("La edad es: ", edadHumano)
elif tamaño == "M":
    edadHumano = medio[Perro]
    print("La edad es: ", edadHumano)
elif tamaño == "P":
    edadHumano = medio[Perro]
    print("La edad es: ", edadHumano)
else:
    print("Comando incorrecto")
        

"""
Pido al usuario el tamaño del perro y la edad, creo tres listas para cada tamaño del perro
que contiene la edad correspondiente en años de humano, luego, por medio de la estructura condicional
if, elif y else direccione según el tamaño del perro del usuario para luego aplicar el el año del perro
como el indice de la lista correspondiente, si no se selecciona ningún comando, sale el mensaje "comando
incorrecto"

"""
    
        

