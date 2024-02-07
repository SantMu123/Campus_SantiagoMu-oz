import csv

def mostrar_contenido_csv(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                print(fila)
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Nombre del archivo CSV que deseas leer
nombre_archivo = "C://Users//user//Desktop//datosCSV.csv"

# Llama a la función para mostrar el contenido del archivo CSV
mostrar_contenido_csv(nombre_archivo)
