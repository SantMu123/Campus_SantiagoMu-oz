"""
Sistema de Gestión de Reservas para un Hotel
Objetivo: Desarrollar un sistema básico de gestión de reservas para un hotel que permita añadir y cancelar reservas, verificar disponibilidad 
de habitaciones, y calcular el costo total de la estancia basado en la duración y el tipo de habitación. El hotel cuenta con diferentes tipos de habitaciones 
(simple, doble, suite) con distintas tarifas.

Requerimientos:
Añadir Reserva: La función debe permitir añadir una reserva indicando el nombre del cliente, el tipo de habitación (simple, doble, suite), y la duración 
de la estancia en días. Cada tipo de habitación tiene un costo por noche (por ejemplo, simple: $100, doble: $150, suite: $200).

Cancelar Reserva: La función debe permitir cancelar una reserva existente mediante el nombre del cliente.
Verificar Disponibilidad: Antes de añadir una reserva, se debe verificar si hay disponibilidad para el tipo de habitación solicitado. 
El hotel tiene una cantidad limitada de habitaciones de cada tipo (por ejemplo, 10 simples, 5 dobles, 3 suites).

Calcular Costo Total: Al finalizar la estancia, se debe calcular el costo total basado en el tipo de habitación y la duración de la estancia.

Reporte de Ocupación: Una función que muestre la ocupación actual del hotel, incluyendo el número de habitaciones ocupadas y 
disponibles por cada tipo.
"""
def actualizacion(habitacion, Habitaciones):
    if habitacion == "simple":
        Habitaciones[0] -= 1
        if Habitaciones == 0:
            print("No hay más cupo para habitaciones simples") 
    elif habitacion == "doble":
        Habitaciones[1] -= 1
        if Habitaciones == 0:
            print("No hay más cupo para habitaciones dobles") 
    if habitacion == "suite":
        Habitaciones[2] -= 1
        if Habitaciones == 0:
            print("No hay más cupo para habitaciones suite") 

def costoTotal(habitacion, duracion):
    costoDia = 100
    if habitacion == "simple":
        return costoDia * duracion
    elif habitacion == "doble":
        return costoDia*1.5* duracion
    if habitacion == "suite":
        return costoDia*2* duracion

def añadirReserva(nombre,habitacion,duracion,Datos):
    
    nuevaReserva = [nombre, habitacion, duracion]
    Datos.append(nuevaReserva)
    
def cancelarReserva(nombre, Datos):
    for fila in Datos:
        if nombre == fila[0]:
            Datos.remove(fila)
            print("Eliminacion completada!!!")
            break
        else: 
            print("No se ha encontrado nombre")
            
def imprimir_tabla(Datos):
    
    print("| Nombre | Habitacion | Duracion |")
    print("+------------+------------+------------+")

    for fila in Datos:
        print(f"| {fila[0]:^10} | {fila[1]:^10} | {fila[2]:^10} |")
        
def imprimir_tabla_habitaciones(Habitaciones):
    
    print("| Simples | Dobles | Suits |")
    print("+---------+--------+-------+")

    for fila in Habitaciones:
        print(f"| {fila[0]:^10} | {fila[1]:^10} | {fila[2]:^10} |")
    
comando = 1
contador = 0
Datos = []
Habitaciones = []

Habitaciones.append([10,5,3])

while comando != 0:
    nombre = input("Digita el nombre: ")
    hab = input("Digita el tipo de habitacion: ")
    duracion = eval(input("Digita la duracion de la estancia: "))
    añadirReserva(nombre, hab, duracion, Datos)
    actualizacion(hab, Habitaciones)
    comando = eval(input("Desa salir, pulse 0, si desea eliminar registro pulse 1, desea mirar las habitaciones disponibles pulse 2, digite 3 si quiere saber el costo de su estadia"))
    if comando == 1:
        nombre = input("Digita el nombre: ")
        cancelarReserva(nombre, Datos)
    elif comando == 2:
        imprimir_tabla_habitaciones(Habitaciones)
    elif comando == 3:
        hab = input("Digita el tipo de habitacion: ")
        duracion = eval(input("Digita la duracion de la estancia: "))
        costo = costoTotal(hab, duracion)
        print("El costo total de su estadia es: ", costo)
        

imprimir_tabla(Datos)