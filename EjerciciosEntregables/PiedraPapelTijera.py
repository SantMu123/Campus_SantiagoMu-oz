n0 = 0
n1 = 1

cantidad = eval(input("Ingrese la cantidad de numeros: "))

for i in range(cantidad):
    print(n0)
    print(n1)

    n1 = n0
    n0 = fib
    fib = n0 + n1