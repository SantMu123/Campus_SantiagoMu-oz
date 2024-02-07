import csv

def filtrar_por_edad_mayor(csv_file, edad_minima):
    # Lista para almacenar las filas filtradas
    filas_filtradas = []

    # Abrir el archivo CSV en modo lectura
    with open(csv_file, newline='') as archivo:
        lector_csv = csv.DictReader(archivo)
        
        # Iterar sobre cada fila del archivo CSV
        for fila in lector_csv:
            # Convertir el valor de la edad a entero
            edad = int(fila['Edad'])
            
            # Comprobar si la edad es mayor que la edad mínima especificada
            if edad > edad_minima:
                filas_filtradas.append(fila)

    return filas_filtradas

# Nombre del archivo CSV
archivo_csv = "C://Users//user//Desktop//datosCSV.csv"

# Edad mínima para filtrar
edad_minima = 30

# Filtrar las filas del archivo CSV por edad mayor que la edad mínima
resultado_filtrado = filtrar_por_edad_mayor(archivo_csv, edad_minima)

# Mostrar las filas filtradas
print("Filas con edad mayor que", edad_minima)
for fila in resultado_filtrado:
    print(fila)
