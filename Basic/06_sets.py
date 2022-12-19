### Sets ###

# Definición
my_set = set()
my_other_set = {}

print(type(my_set))
# Inicialmente es un diccionario
print(type(my_other_set))

my_other_set = {"Alionca", "Ignacio", 35, 'Rojo'}
print(type(my_other_set))

#longitud del object
print(len(my_other_set))

# Inserción de un dato nuevo
my_other_set.add("AlioncaDev")
# Un set no es una estructura ordenada
print(my_other_set)
# Un set no admite repetidos
my_other_set.add("AlioncaDev")
print(my_other_set)

# Búsqueda
print("Buscar ")
print("Alionca" in my_other_set)
# busca el termino completo
print("Ali" in my_other_set)

# Eliminación
my_other_set.remove("Rojo")
print(my_other_set)

# Elimina todos los elementos del conjunto my_other_set.
my_other_set.clear()
print(len(my_other_set))


# Elimine el objeto establecido almacenado en la variable 'my_other_set'.
del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación
my_set = {"Ignacio", "Alionca", 35}
print('SET', type(my_set))
my_list = list(my_set)
print('LIST', type(my_list))
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

## Otras operaciones
# Cree un nuevo conjunto combinando los elementos de dos conjuntos existentes.
my_new_set = my_set.union(my_other_set)

"""
Crea un nuevo conjunto combinando los elementos de my_new_set, my_set y {"javascript", "c#"}
@return {Set} Un nuevo conjunto que contiene los elementos combinados de los dos conjuntos.
"""
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))

"""
Devuelve un nuevo conjunto que contiene
los elementos presentes en my_new_set
que no están presentes en my_set.
"""
print(my_new_set.difference(my_set))





