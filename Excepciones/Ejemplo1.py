try:
    entrada = input("por favor ingrese un numero: ")
    print(type(entrada))
    num = float(entrada)
    print("El numero contenido es: ", num)
except Exception: #se puede escpecificar para una excepcion
    print("Error de conversion de tipo de datos")
#util porque el programa no se detienem gestiona los errores
finally:
    #se ejecuta siempres, exista o no error
    print("El codigo continua aquí")