"""
Comprobar si una clave existe en el diccionario.
"""

diccionario = {"santiago":23, "Paula":25, "Laura":45}

if "santiago" in list(diccionario.keys()):
    print("La clave está")
else:
    print("No está")