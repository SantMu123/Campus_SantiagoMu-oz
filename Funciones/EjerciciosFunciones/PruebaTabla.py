def imprimir_tabla(filas):
    # Imprime el encabezado de la tabla
    print("| Columna 1 | Columna 2 | Columna 3 |")
    print("+------------+------------+------------+")

    # Imprime cada fila de la tabla
    for fila in filas:
        print(f"| {fila[0]:^10} | {fila[1]:^10} | {fila[2]:^10} |")

# Ejemplo de uso
mi_tabla = [
    ["Dato1", "Dato2", "Dato3"],
    ["Dato4", "Dato5", "Dato6"],
    ["Dato7", "Dato8", "Dato9"]
]

imprimir_tabla(mi_tabla)


"""
tabla = [[]]

for i in 

"""