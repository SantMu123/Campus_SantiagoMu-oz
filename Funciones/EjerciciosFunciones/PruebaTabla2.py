def añadirReserva(nombre, habitacion, duracion, Datos):
    # Crea una nueva fila para la reserva
    nueva_reserva = [nombre, habitacion, duracion]
    # Agrega la nueva fila a la lista de Datos
    Datos.append(nueva_reserva)

def imprimir_tabla(Datos):
    # Imprime el encabezado de la tabla
    print("| Columna 1 | Columna 2 | Columna 3 |")
    print("+------------+------------+------------+")

    # Imprime cada fila de la tabla
    for fila in Datos:
        print(f"| {fila[0]:^10} | {fila[1]:^10} | {fila[2]:^10} |")

def main():
    Datos = []

    while True:
        nombre = input("Digita el nombre: ")
        hab = input("Digita el tipo de habitacion: ")
        duracion = int(input("Digita la duracion de la estancia: "))
        añadirReserva(nombre, hab, duracion, Datos)

        comando = input("Desea salir, pulse '0', de lo contrario, presione cualquier tecla: ")
        if comando == '0':
            break

    imprimir_tabla(Datos)

if __name__ == "__main__":
    main()

