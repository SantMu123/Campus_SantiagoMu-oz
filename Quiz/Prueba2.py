"""
Añadir productos al inventario
Actualizar la cantidad de un producto existente
Eliminar producto
Calcular el valor total del inventario
"""

def NuevosProductos(nombre,cantidad,precio,ListaProductos):
    producto = {nombre:(cantidad,precio)}
    ListaProductos.append(producto)
    
def Actualizar(nombre,NuevaCantidad,ListaProductos):
    
    for i in ListaProductos:
        if nombre == list(i.keys())[0]:
            i[nombre][0] = NuevaCantidad
            
def eliminar(nombre, ListaProductos):
    for i in ListaProductos:
        if nombre == list(i.keys())[0]:
            ListaProductos.remove(i)
            
def mostrar(ListaProductos):
    print("|----------|----------|----------")
    print("|-Producto-|-Cantidad-|-Precio-|")
    print("|----------|----------|----------|")
    for i in ListaProductos:
        print(f"|{list(i.keys())[0]:^10}|{list(i.values())[0][0]:^10}|{list(i.values())[0][1]:^10}")
            
listaProductos = [{"Queso": (5,3000)}]
valorTotal = 0
TotalArticulos = 0
comando = 1

while comando != 0:
    print("**********************************")
    print("1: Añadir Productos \n 2: Actualizar la cantidad \n 3: Eliminar Producto \n 4: Calcular valor total inventario \n 0: Salir"  )
    comando = int(input("Digita el comando de acuerdo a tu necesidad: "))
    print("**********************************")
    
    if comando == 1:
        nom = input("Digita el nombre del producto: ")
        cant = int(input("Digita la cantidad: "))
        precio = int(input("Digita el precio: "))
        NuevosProductos(nom, cant, precio, listaProductos)
        mostrar(listaProductos)
    elif comando == 2:
        nom = input("Digita el nombre del producto: ")
        NuevaCant = int(input("Digita la cantidad: "))
        Actualizar(nom, NuevaCant, listaProductos)
        mostrar(listaProductos)
    elif comando == 3:
        nom = input("Digita el nombre del producto: ")
        eliminar(nom, listaProductos)
        mostrar(listaProductos)
    elif comando == 4:
        for i in listaProductos:
            valorTotal += list(i.values())[0][1]
            TotalArticulos += list(i.values())[0][0]
        print("El valor total del inventario es: ", valorTotal, "con un total de ", TotalArticulos, "Articulos")