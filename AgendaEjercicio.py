"""
-Permita registrar a los participantes de los eventos de agosto pidiendo: documento, nombre, edad y cargo.
-Permita registrar los eventos  pidiendo: nombre del evento, locación y día del mes
-Permita quitar del registro a los participantes .
-Permita eliminar y/o modificar eventos.

Para participar los empleados deben cancelar un aporte de 50.000 COP. Por lo tanto el programa también debe:

-Saber cuantos empleados no han cancelado aún el aporte y cuanto dinero suma la deuda.
-Saber cuales empleados (listarlos) no han cancelado.
-No permitir quitar del registro a participantes que ya hayan pagado, pues no se aceptan devoluciones
-Marcar eventos ya realizados.
-No permitir eliminar o modificar eventos ya realizados.

la lista de empleados debe tener otro parametro ---> pago
"""
def Pago(nombre, pago, listaPersonas):
    bandera = False
    for i in listaPersonas:
        if list(i.keys())[1] == nombre:
            list(i.values())[4] = pago
            bandera = True
        if not bandera:
            print("No se ha ingresado el nombre de la persona")
            
def MostrarRegistrado(listaPersonas):
    print("|----------|----------|----------|----------|")
    print("|----IDE---|--Nombre--|---Edad---|--Cargo---|")
    print("|----------|----------|----------|----------|")
    for i in listaPersonas:
        print(f"|{list(i.values())[0]:^10}|{list(i.values())[1]:^10}|{list(i.values())[2]:^10}|{list(i.values())[3]:^10}|")

def MostrarEvento(listaEvento):
    print("|----------|----------|----------|")
    print("|--Nombre--|--Lugar---|--Fecha---|")
    print("|----------|----------|----------|")
    for i in listaEvento:
        print(f"|{list(i.values())[0]:^10}|{list(i.values())[1]:^10}|{list(i.values())[2]:^10}|")
        
def unir(nombre, evento, listaEvento, listaPersonas):
    listaEvento = []


def añadir(documento, nombre, edad, cargo, listaPersonas, pago = False):
    info = {"documento":documento, "nombre":nombre, "edad":edad, "cargo":cargo, "Pago":pago}
    listaPersonas.append(info)

def Evento(nombreEvento, locacion, dia, listaEvento, estado = True):
    info = {"Nombre_Evento":nombreEvento, "Lugar":locacion, "Fecha":dia}
    listaEvento.append(info)

def Eliminar(nombre, listaPersonas):
    bandera = False
    for i in listaPersonas:
        if list(i.values())[1] == nombre:
            listaPersonas.remove(i)
            bandera = True
        if not bandera:
            print("No se ha encontrado el asistente al evento")
def Modificar(nombreEvento, listaEvento, NuevoNombre = False, Lugar = False, Fecha = False):
    for i in listaEvento:
        if i['Nombre_Evento'] == nombreEvento:
            if NuevoNombre:
                i['Nombre_Evento'] = NuevoNombre
            elif Lugar:
                i['Lugar'] = Lugar
            elif Fecha:
                i['Fecha'] = Fecha
            
listaPersonas = []
listaEvento = []
comando = 1

while comando != 0:
    print("Bienvenido al sistema de manejo de eventos")
    comando = int(input("Digita \n 1: Para añadir un nuevo integrante \n 2: Para añadir un nuevo evento \n 3: Para Quitar un participante \n 4: Para Modificar un evento \n 0: Para Salir del Menú \n"))

    if comando == 1:
        ide = int(input("Digita la documentacion de la persona: "))
        nom = input("Digita el nombre del asistente: ")
        edad = int(input("Digita la edad del asistente: "))
        cargo = input("Digita el cargo del asistente: ")

        añadir(ide, nom, edad, cargo, listaPersonas)
        MostrarRegistrado(listaPersonas)
    
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

