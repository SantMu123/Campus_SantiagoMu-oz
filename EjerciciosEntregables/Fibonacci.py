n0 = 0
n1 = 1
cantidad = eval(input("Ingrese una cantidad: "))

print(n0)
print(n1)
for i in range(cantidad - 2):

    fib = n0 + n1
    print(fib)
    n1 = n0
    n0 = fib