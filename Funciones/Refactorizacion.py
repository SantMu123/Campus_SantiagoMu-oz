cantidad = int(input())
cantidadInicial = cantidad

for billete in denominaciones:
    cantidadBilletes = cantidad // billete
    cantidad -= cantidadBilletes*billete
    billetes[billete] = cantidadBilletes