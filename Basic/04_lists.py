### Lists ###

# Definición de list
my_list = list()
my_other_list = []

# longitud del object
print(len(my_list))

#intro datos a la lista
my_list = [35, 24, 62, 52, 30, 30, 17]
my_other_list = [35, 1.77, "Alionca", "Ignacio"]

print(my_list)
#longitud de la lista
print(len(my_list))

# tipo de variable
print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[1])
# busca desde el final de la lista -numb
print(my_other_list[-1])
print(my_other_list[-4])

#Cuenta las veces que se repite el dato introducido '30'
print(my_list.count(30))
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError
"""
devuelve la primera
aparición / índice
del elemento en la
lista dada como
argumento de la función.
"""
print(my_other_list.index("Alionca"))

"""
Desempaquete los elementos de
my_other_list en el
variables age, height,
name y surname.
"""
age, height, name, surname = my_other_list
print(name)

"""
Desempaqué los elementos de my_other_list en variables.
Parámetros:
my_other_list(Lista): una lista de elementos que se deben desempaquetar.
Devoluciones:
name (str): El tercer elemento de my_other_list.
height (str): El segundo elemento de my_other_list.
age (str): El primer elemento de my_other_list.
surname (str): El cuarto elemento de my_other_list.
"""
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación
print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

my_other_list.append("MoureDev")
print(my_other_list)

# Inserta la cadena "ROJO" en el índice 1 de la lista my_other_list.
my_other_list.insert(1, "Rojo")
print(my_other_list)

# Establece el valor del segundo elemento de la matriz my_other_list en "Azul"
my_other_list[1] = "Azul"
print(my_other_list)

# Elimina el elemento "Azul" de la lista my_other_list.
my_other_list.remove("Azul")
print(my_other_list)

# Elimina el elemento 30 de la lista my_list.
my_list.remove(30)
print(my_list)

# Elimina y devuelve el último elemento de la lista 'my_list'.
print(my_list.pop())
print(my_list)


# Elimina y devuelve el elemento en el índice 2 de la lista 'my_list'.
my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

# Elimina el elemento en el índice 2 de la lista 'my_list'.
del my_list[2]
print(my_list)

## Operaciones con listas

# Crea una copia superficial de la lista my_list y la asigna a la variable my_new_list.
my_new_list = my_list.copy()

#Elimina todos los elementos de la lista 'my_list'.
my_list.clear()
print(my_list)
print(my_new_list)

# Invierte el orden de los elementos en la lista my_new_list.
my_new_list.reverse()
print(my_new_list)

# Ordene los elementos de la lista 'my_new_list' en orden ascendente.
my_new_list.sort()
print(my_new_list)

## Sublistas
# Devuelve una porción de la lista my_new_list desde el índice 1 hasta, pero no incluir, índice 3.
print(my_new_list[1:3])

## Cambio de tipo
my_list = "Hola Python"
print(my_list)
print(type(my_list))