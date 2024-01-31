def actualizacion(habitacion, Habitaciones):
    if habitacion == "simple" and Habitaciones[0][0] > 0:
        Habitaciones[0][0] -= 1
        if Habitaciones[0][0] == 0:
            print("No hay más cupo para habitaciones simples")
    elif habitacion == "doble" and Habitaciones[0][1] > 0:
        Habitaciones[0][1] -= 1
        if Habitaciones[0][1] == 0:
            print("No hay más cupo para habitaciones dobles")
    elif habitacion == "suite" and Habitaciones[0][2] > 0:
        Habitaciones[0][2] -= 1
        if Habitaciones[0][2] == 0:
            print("No hay más cupo para habitaciones suite")
    else:
        print("No hay más cupo para el tipo de habitación solicitado o la cantidad es 0")


def imprimir_tabla_habitaciones(Habitaciones):
    print("| Simples | Dobles | Suits |")
    print("+---------+--------+-------+")
    print(f"| {Habitaciones[0][0]:^10} | {Habitaciones[0][1]:^10} | {Habitaciones[0][2]:^10} |")

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


comando = 1
contador = 0
Datos = []
Habitaciones = []

Habitaciones.append([10, 5, 3])

while comando != 0:
    nombre = input("Digita el nombre: ")
    hab = input("Digita el tipo de habitacion: ")
    duracion = eval(input("Digita la duracion de la estancia: "))
    añadirReserva(nombre, hab, duracion, Datos)
    actualizacion(hab, Habitaciones) 
    imprimir_tabla_habitaciones(Habitaciones)

    comando = eval(input("Desa salir, pulse 0, si desea eliminar registro pulse 1, digite 2 si quiere saber el costo de su estadia, si desea ver los usuarios hospedados pulse 3, si quiere agregar otro usuario pulse 5: "))
                   
    if comando == 1:
        nombre = input("Digita el nombre: ")
        cancelarReserva(nombre, Datos)
    elif comando == 2:
        hab = input("Digita el tipo de habitacion: ")
        duracion = eval(input("Digita la duracion de la estancia: "))
        costo = costoTotal(hab, duracion)
        print("El costo total de su estadia es: ", costo)
    elif comando == 3:
        imprimir_tabla(Datos)
