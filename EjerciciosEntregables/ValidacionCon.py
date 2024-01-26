contraseña = input("Ingresa una contraseña: ")
bandera1 = False
bandera2 = False
bandera3 = False
bandera4 = False
 
contador = 0

for i in contraseña:
    contador += 1
    if i.isupper():
        bandera1 = True
    elif i.islower():
        bandera2 = True
    elif int(i) == True:
        bandera3 = True
    elif contador >= 8:
        bandera4 = True
        
if bandera1 and bandera2 and bandera3 and bandera4:
    print("La contraseña es correcta!!!")
    
