cantidad = eval(input("Ingrese la cantidad de unidades que va a llevar: "))
CostoUnidad = 5000

if cantidad > 12*3:
    costo = CostoUnidad * cantidad * 0.85
    docenas = cantidad // 12 
    print("El monto del descuento es: ", 15, "%")
    if docenas >= 4:
        cant = cantidad - 48 
        adicionales = cant // 12
        cantidad = cantidad + adicionales
    print("El monto de las unidades obsequiadas es: ", adicionales)
else:
    costo = CostoUnidad * cantidad * 0.9
    print("El monto del descuento es: ", 10, "%")
    print("El monto de las unidades obsequiadas es cero")

print("La cantida es: ", cantidad)
print("El costo a pagar es: ", costo)




