
def MostrarRegistrado(listaPersonas):
    print("|----------|----------|----------|----------|")
    print("|----IDE---|--Nombre--|---Edad---|--Cargo---|")
    print("|----------|----------|----------|----------|")
    for i in listaPersonas:
        print(f"|{list(i.values())[0]:^10}|{list(i.values())[1]:^10}|{list(i.values())[2]:^10}|{list(i.values())[3]:^10}|")

def MostrarEvento(listaEvento):
    for i in listaEvento:
        if i[1]:
            print("|----------|----------|----------|")
            print("|--Nombre--|--Lugar---|--Fecha---|")
            print("|----------|----------|----------|")
            for i in listaEvento:
                print(f"|{i[0]['Nombre_Evento']:^10}|{i[0]['Lugar']:^10}|{i[0]['Fecha']:^10}|")
        else:
            print("El evento ya se ha hecho")

def unir(nombreEvento, nombrePersona, ListaPersonas, ListaEvento, listaEventoConjunto):
    for evento,participante in zip(ListaEvento,ListaPersonas):
        if evento[0]["Nombre_Evento"] == nombreEvento and participante['nombre'] == nombrePersona:
            info = (evento, participante)
            listaEventoConjunto.append(info)
    
def MostrarEventoAsistentes(listaEventoConjunto):
    for evento,asistentes in listaEventoConjunto:
        print(f"Nombre Evento:{evento[0]['Nombre_Evento']:^10}")
        print(f"Fecha Evento:{evento[0]['Lugar']:^10}")
        print(f"Lugar Evento:{evento[0]['Fecha']:^10}")
        print("-------------------------------------------------")
        print(f"{"Evento Activo" if evento[0][1] else "Evento No Activo"}")
        print("|----------|----------|----------|")
        print("|-Asistente|--Cargo---|---Pago---|")
        print("|----------|----------|----------|")
        print(f"|{asistentes[1]['nombre']:^10}|{asistentes[3]['Cargo']:^10}|{evento[4]['Pago']:^10}|")
        print("-------------------------------------------------")


def añadir(documento, nombre, edad, cargo, pago, listaPersonas):
    info = {"documento":documento, "nombre":nombre, "edad":edad, "cargo":cargo, "Pago":pago}
    listaPersonas.append(info)

def Evento(nombreEvento, locacion, diaEvento, diaActual, listaEvento):
    if diaActual < diaEvento:
        estado = True
    else:
        estado = False
    info = ({"Nombre_Evento":nombreEvento, "Lugar":locacion, "Fecha":diaEvento, "Dia Actual":diaActual},estado)
    listaEvento.append(info)

def Eliminar(nombre, listaPersonas):
    bandera = False
    for i in listaPersonas:
        if list(i.values())[1] == nombre:
            listaPersonas.remove(i)
            bandera = True
        if not bandera:
            print("No se ha encontrado el asistente al evento")

def Modificar(nombreEvento, listaEvento, NuevoNombre=False, Lugar=False, Fecha=False):
    for evento, estado in listaEvento:
        if evento['Nombre_Evento'] == nombreEvento and not estado:
            if NuevoNombre:
                evento['Nombre_Evento'] = NuevoNombre
            elif Lugar:
                evento['Lugar'] = Lugar
            elif Fecha:
                evento['Fecha'] = Fecha
            return True
    return False
            
listaPersonas = []
listaEvento = []
listaEventoConjunto = []
comando = 1

while comando != 0:
    print("Bienvenido al sistema de manejo de eventos")
    print("Crea un evento!!!")
    nombre = input("Ingresa el nombre del Evento: ")
    Lugar = input("Ingresa el nombre del lugar: ")
    Fecha = int(input("Ingresa la fecha de realización: "))
    FechaActual = int(input("Digita la fecha Actual: "))
    
    Evento(nombre, Lugar, Fecha, FechaActual, listaEvento)
    comando = int(input("Digita \n 1: Para añadir integrante a un evento \n 2: Para añadir un nuevo evento \n 3: Para Quitar un participante \n 4: Para Modificar un evento \n 0: Para Salir del Menú \n"))

    if comando == 1:
        ide = int(input("Digita la documentacion de la persona: "))
        nom = input("Digita el nombre del asistente: ")
        edad = int(input("Digita la edad del asistente: "))
        cargo = input("Digita el cargo del asistente: ")
        pago = int(input("Digita el aporte del asistente"))
        añadir(ide, nom, edad, cargo, pago, listaPersonas)
        MostrarRegistrado(listaPersonas)
        print("Tenemos los siguientes eventos Activos, a cual de ellos deseas añadir el nuevo asistente: ")
        MostrarEvento(listaEvento)
        
        event = input("Digita nombre de evento: ")
        unir(event, nom, listaPersonas, listaEvento, listaEventoConjunto)
        
        print("**********************Evento Actualizado*************************")
        MostrarEventoAsistentes(listaEventoConjunto)
        
    elif comando == 2:
        evento = input("Digita el nombre del evento: ")
        lugar = input("Digita el lugar del evento: ")
        fecha = int(input("Digita el día: "))

        Evento(evento, lugar, fecha, listaEvento)
        MostrarEvento(listaEvento)

    elif comando == 3:
        nombre = input("Digita el nombre de la persona que quieres eliminar de la lista asistentes: ")
        Eliminar(nombre, listaPersonas)
        MostrarRegistrado(listaPersonas)

    elif comando == 4:
        nombreEve = input("Ingresa el nombre del evento que quieres modificar: ")
        opcion = input("Digita \n A: Si quieres modificar el nombre del evento \n B: Si quieres modificar Lugar \n C: Si quieres modificar fecha \n")
        if opcion == "A":
            nombreNuevo = input("Ingresa el nuevo nombre del evento: ")
            Modificar(nombreEve, listaEvento, NuevoNombre=nombreNuevo)
            MostrarEvento(listaEvento)
        elif opcion == "B":
            lugarNuevo = input("Ingresa nuevo Lugar: ")
            Modificar(nombreEve, listaEvento, Lugar = lugarNuevo)
            MostrarEvento(listaEvento)
        elif opcion == "C":
            fechaNueva = input("Digita el nuevo dia del evento: ")
            Modificar(nombreEve, listaEvento, Fecha = fechaNueva)
            MostrarEvento(listaEvento)
    
    """
    if Modificar(nombre_evento_modificar, lista_eventos, NuevoNombre=nuevo_nombre, Lugar=nuevo_lugar, Fecha=nueva_fecha):
        print("Evento modificado con éxito.")
    else:
        print("No se pudo modificar el evento. El evento no existe o ya se realizó.")
    """

    #break es una estructura de ramificacion