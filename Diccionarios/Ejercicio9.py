"""
Iterar a través de las claves y valores del diccionario.
"""

diccionario = {"santiago":23, "Paula":25, "Laura":45}
valores = list(diccionario.values())
for i,j in zip(diccionario,valores):
    print(f"La clave es: {i} y el valor es: {j}")
    
    