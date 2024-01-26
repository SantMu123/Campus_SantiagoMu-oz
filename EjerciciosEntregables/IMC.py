peso = eval(input("Ingrese su peso en kilogramos"))
altura = eval(input("Ingrese su altura en metros"))

imc = peso / altura**2

if imc >= 1 and imc <= 18.5:
    print("Tiene Bajo paso")
elif imc > 18.5 and imc <= 24.9:
    print("Tiene Peso Saludable")
elif imc > 24.9 and imc <= 29.9:
    print("Tiene Peso Saludable")
elif imc >= 30:
    print("Tiene Obesidad")
else:
    print("Peso o altura incorrectos")