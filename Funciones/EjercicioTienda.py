
def CalcularPrecio(precioOriginal, porcentajeDescuento):
    descuento = precioOriginal - precioOriginal*porcentajeDescuento
    return descuento

def calculoImpuesto(precioConDescuento, porcentajeDescuento):
    IVA = precioConDescuento * porcentajeDescuento
    return precioConDescuento + IVA

def total():
    precioTotal = float(input("Precio producto"))
    descuento = float(input("Descuento"))
    impuesto = float(input("IVA"))

    precioDescuento = CalcularPrecio(precioTotal, descuento)
    precioDescuentoConImpuesto = calculoImpuesto(precioDescuento, impuesto)

    print("Bienvenido su precio inicial fue: ", precioTotal)
    print("Bienvenido su precio inicial con descuento fue: ", precioDescuento)
    print("Bienvenido su precio descuento con impuesto es: ", precioDescuentoConImpuesto)

#algoritmo

total()