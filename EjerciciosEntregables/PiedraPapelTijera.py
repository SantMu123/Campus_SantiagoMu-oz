import random

decision = input("Selecciona (R) (P) (S): ")

aleatorio = random.randint(1,3)

if decision == "R":
    if aleatorio == 1:
        print("Ha habido empate")
    if aleatorio == 2:
        print("Ha sacado Papel, Derrota")
    if aleatorio == 3:
        print("Ha sacado Tijera, Victoria") 
elif decision == "P":
    if aleatorio == 1:
        print("Ha sacado Papel, Victoria")
    if aleatorio == 2:
        print("Ha habido empate")
    if aleatorio == 3:
        print("Ha sacado Tijera, Victoria")
else:
    if aleatorio == 1:
        print("Ha sacado Piedra, Derrota")
    if aleatorio == 2:
        print("Ha sacado Papel, Victoria")
    if aleatorio == 3:
        print("Ha habido empate")