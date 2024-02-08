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
"""
def Pago(nombre, pago, listaPersonas):
    bandera = False
    for i in listaPersonas:
        if list(i.keys())[1] == nombre:
            list(i.values())[4] = pago
            bandera = True
        if not bandera:
            print("No se ha ingresado el nombre de la persona")

def unir(nombre, evento, listaEvento, listaPersonas):
    listaEvento = []


def añadir(documento, nombre, edad, cargo, listaPersonas, pago = False):
    info = {"documento":documento, "nombre":nombre, "edad":edad, "cargo":cargo, "Pago":pago}
    listaPersonas.append(info)

def Evento(nombreEvento, locacion, dia, listaEvento, estado):
    info = {"Nombre_Evento":nombreEvento, "Lugar":locacion, "Fecha":dia}
    listaEvento.append(info)

def Eliminar(nombre, listaPersonas):
    bandera = False
    for i in listaPersonas:
        if list(i.keys())[1] == nombre:
            listaPersonas.remove(i)
            bandera = True
        if not bandera:
            print("No se ha encontrado el asistente al evento")
def Modificar(nombreEvento, listaEvento, NuevoNombre = False, Lugar = False, Fecha = False):
    for i in listaEvento:
        if list(i.keys())[0] == nombreEvento:
            if NuevoNombre:
                list(i.keys())[0] = NuevoNombre
            elif Lugar:
                list(i.keys())[1] = NuevoNombre
            elif Fecha:
                list(i.keys())[2] = NuevoNombre
            
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
    
    elif comando == 2:
        evento = input("Digita el nombre del evento: ")
        lugar = input("Digita el lugar del evento: ")
        fecha = input("Digita el día: ")

        Evento(evento, lugar, fecha, listaEvento)

    elif comando == 3:
        nombre = input("Digita el nombre de la persona que quieres eliminar de la lista asistentes: ")
        Eliminar(nombre, listaPersonas)

    elif comando == 4:
        nombreEve = input("Ingresa el nombre del evento que quieres modificar: ")
        opcion = input("Digita \n A: Si quieres modificar el nombre del evento \n B: Si quieres modificar Lugar \n C: Si quieres modificar fecha")
        if opcion == "A":
            nombreNuevo = input("Ingresa el nuevo nombre del evento: ")
            Modificar(nombreEve, listaEvento, NuevoNombre=nombreNuevo)
        elif opcion == "B":
            lugarNuevo = input("Ingresa nuevo Lugar: ")
            Modificar(nombreEve, listaEvento, Lugar = lugarNuevo, Fecha = False)
        elif opcion == "C":
            fechaNueva = input("Digita la nueva fecha del evento: ")
            Modificar(nombreEve, listaEvento, Fecha = fechaNueva)

