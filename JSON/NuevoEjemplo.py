from io import open

texto = "Una linea con texto \n otra linea"
ficheros = open("fichero.txt", "w")
ficheros.write(texto)
ficheros.close()
