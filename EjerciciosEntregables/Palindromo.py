palabra = input("ingrese una palabra: ")

if palabra == palabra[::-1]:
    print("Es palindromo")
else:
    print("No lo es")