import json

datos = []
def cargaDatos():
    with open("veterinaria.json", "r") as file:
        respuesta = json.load(file)
        return respuesta

def guardarDatos(datos):
    with open("veterinaria.json", "w") as file:
        escritura = json.dumps(datos, indent = 4)
        file.write(escritura)
#tabla = cargaDatos()
#print(tabla)

def crearAnimal():
    try:
        animales = list(cargaDatos())
        tipo = input("Ingrese el tipo de animal: ")
        Npatas = input("Ingrese el numero de patas: ")
        Raza = input("Ingrese la raza del animal: ")
        animal = {"tipo": tipo, "nPatas": Npatas, "Raza": Raza}

        animales.append(animal)
        guardarDatos(animales)
    except Exception:
        print("Ocurre un error")

#crearAnimal()
#print(type(len(datos)))

def EliminarAnimal():
    try:
        animales = list(cargaDatos())
        for i in range(len(animales)):
            print(str(i), ". ", end = " ")
            print(animales[i])
        opc = int(input("ingrese el numero del animal a eliminar: "))
        animales.pop(opc)
        guardarDatos(animales)
        print("animal eliminado")
    except Exception:
        print("Ha ocurrido un problema")

 #EliminarAnimal()

def mostrarAnimal():
    try:
        animales = list(cargaDatos())
        for i in range(len(animales)):
            print(str(i),"->",animales[i]["tipo"])
        opc = int(input("Ingrese el número del animal a mostrar: "))
        print(animales[opc])
    except Exception:
        print("Ocurrió un error al mostrar animal!")

def mostrarTodosLosAnimales():
    try:
        animales = list(cargaDatos())
        for i in range(len(animales)):
            print(str(i),"->",animales[i])
    except Exception:
        print("Ocurrió un error al mostrar animal!")

def actualizarAnimal():
    try:
        indice = int(input("Digite el indice del elemento de la lista: "))
        comando = input("""
                        A: Desea modificar tipo
                        B: Desa modifcar numero patas
                        C: Desea modificar raza
                        """)
        if comando == "A":
            tipoNuevo = input("Digita el nuevo tipo: ")
            animales = list(cargaDatos())
            for i in range(len(animales)):
                if i == indice:
                    animales[i]['tipo'] = tipoNuevo
                    guardarDatos(animales)
                    print("Actualizacion exitosa")
        elif comando == "B":
            npatasNuevo = input("Digita el nuevo numero de patas: ")
            animales = list(cargaDatos())
            for i in range(len(animales)):
                if i == indice:
                    animales[i]['nPatas'] = npatasNuevo
                    guardarDatos(animales)
                    print("Actualizacion exitosa")
        elif comando == "C":
            razaNuevo = input("Digita la nueva raza: ")
            animales = list(cargaDatos())
            for i in range(len(animales)):
                if i == indice:
                    animales[i]['Raza'] = razaNuevo
                    guardarDatos(animales)
                    print("Actualizacion exitosa")
    except Exception:
        print("Ha ocurrido un error:")

actualizarAnimal()