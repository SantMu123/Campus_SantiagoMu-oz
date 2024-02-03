# Creación de conjuntos
conjunto_vacio = set()
otro_conjunto = set([1, 2, 3, 4, 5])

# Agregar elementos
mi_conjunto = {1, 2, 3}
mi_conjunto.add(4)

# Eliminar elementos
mi_conjunto.remove(2)
mi_conjunto.discard(3)
elemento_eliminado = mi_conjunto.pop()

# Operaciones de conjunto
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

union_set = conjunto1.union(conjunto2)  # O usando el operador |
interseccion_set = conjunto1.intersection(conjunto2)  # O usando el operador &
diferencia_set = conjunto1.difference(conjunto2)  # O usando el operador -
diferencia_simetrica_set = conjunto1.symmetric_difference(conjunto2)  # O usando el operador ^

# Eliminar todos los elementos del conjunto
#mi_conjunto.clear()

