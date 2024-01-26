import random

for i in range(1,101):
    numero = random.randint(1,6)
    if numero == 6:
        print("Ha salido un seis!!!")
        break
    else:
        print(numero)
