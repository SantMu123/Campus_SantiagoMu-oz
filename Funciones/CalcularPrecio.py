def CalcularPrecio(nombre, cantProd, precio = 3000):
    print(f"Hola {nombre}, tienes que pagar {precio * cantProd} por llevar {cantProd} productos")


print("Bienvenido a su sistema")
nombre = input("Digita tu nombre: ")
yogurt = 3000
Queso = 4000
Galletas = 2000
print(f"Existen los siguientes productos: \n yogurt = {yogurt} - Queso = {Queso}, Galletas = {Galletas}")
Producto = input("Escriba el producto: ")
Cantidad = eval(input("Digita la cantidad de productos que vas a llevar: "))

if Producto == "yogurt":
    precio = 3000
    CalcularPrecio(nombre, Cantidad, precio)
elif Producto == "Queso":
    precio = 4000
    CalcularPrecio(nombre, Cantidad, precio)
elif Producto == "Galletas":
    precio = 2000
    CalcularPrecio(nombre, Cantidad, precio)



