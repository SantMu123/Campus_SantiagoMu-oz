valor = eval(input("Ingrese el valor: "))

if valor >= 1 and valor <= 500:
    impuesto = 1.15
    print("El valor a pagar por impuestos es: ",valor*0.15, "en total es: ", valor * impuesto)
elif valor > 500 and valor <= 1000:
    impuesto = 1.30
    print("El valor a pagar por impuestos es: ",valor*0.30, "en total es: ", valor * impuesto)
elif valor > 1000 and valor <= 1500:
    impuesto = 1.45
    print("El valor a pagar por impuestos es: ",valor*0.45, "en total es: ", valor * impuesto)
elif valor > 1500 and valor <= 2000:
    impuesto = 1.55
    print("El valor a pagar por impuestos es: ",valor*0.55, "en total es: ", valor * impuesto)
elif valor > 2000:
    impuesto = 1.65
    print("El valor a pagar por impuestos es: ",valor*0.65, "en total es: ", valor * impuesto)
else:
    print("Valor no valido")