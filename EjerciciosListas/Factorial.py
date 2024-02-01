"""
Desarrolla una función 
que calcule el factorial de cada número en una lista.
"""
def factorial(numero, prod = 1):
    num = numero - 1
    prod = prod * numero
    if num == 1:
        return prod
    else:
        factorial(num, prod)


"""
def factorial(numero, prod=1):
    if numero == 0 or numero == 1:
        print(prod)
    else:
        prod *= numero
        factorial(numero - 1, prod)

"""

def Listafactorial(lista):
    fact = []
    for i in lista:
        num = factorial(i)
        fact.append(num)
    print(fact)

lis = [2,2,3,4,6,7,8,9]

Listafactorial(lis)



