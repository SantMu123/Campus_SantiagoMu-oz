def fuera(x):
    def dentro(y):
        suma = x + y
        return suma
    return dentro


prueba = fuera(5)
prueba2 = prueba(10)
#print(prueba2)
#print(prueba(500))
print(fuera(20)(10))



