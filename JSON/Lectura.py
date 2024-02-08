from io import open

ficheros = open("fichero.txt", "r")
texto = ficheros.read()
ficheros.close()
print(texto)