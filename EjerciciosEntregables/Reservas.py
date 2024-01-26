edad = eval(input("ingrese su edad: "))
membresia = input("ingrese su membresi: ")
precio = 30000

if edad >= 18 and edad < 25 and membresia == "Oro":
    descuento = precio * 0.50
    precioNeto = precio * descuento
    print("El precio es: ", precioNeto)
elif edad >= 25 and edad < 50 and membresia == "Oro":
    descuento = precio * 0.55
    precioNeto = precio * descuento
    print("El precio es: ", precioNeto) 
elif edad >= 50 and edad < 75 and membresia == "Oro":
    descuento = precio * 0.65
    precioNeto = precio * descuento
    print("El precio es: ", precioNeto) 
elif edad >= 18 and edad < 25 and membresia == "Plata":
    descuento = precio * 0.30
    precioNeto = precio * descuento
    print("El precio es: ", precioNeto) 
elif edad >= 25 and edad < 50 and membresia == "Plata":
    descuento = precio * 0.35
    precioNeto = precio * descuento
    print("El precio es: ", precioNeto) 
elif edad >= 50 and edad < 75 and membresia == "Plata":
    descuento = precio * 0.45
    precioNeto = precio * descuento
    print("El precio es: ", precioNeto) 
elif edad >= 18 and edad < 25 and membresia == "Bronce":
    descuento = precio * 0.15
    precioNeto = precio * descuento
    print("El precio es: ", precioNeto) 
elif edad >= 25 and edad < 50 and membresia == "Bronce":
    descuento = precio * 0.25
    precioNeto = precio * descuento
    print("El precio es: ", precioNeto)
elif edad >= 50 and edad < 75 and membresia == "Bronce":
    descuento = precio * 0.30
    precioNeto = precio * descuento
    print("El precio es: ", precioNeto) 
else:
    print("Edad o membresia incorrecta") 