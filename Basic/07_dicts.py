### Dictionaries ###

# Definición
"""
Estructura de datos para trabajar
con colecciones de datos almacenados
en pares de claves/valores.
Los diccionarios se ordenan
y son mutables soportar cambios
después de su creación, pero son
estrictos acerca de entradas
duplicadas. Todas las claves/valores
deben ser únicos
"""

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

#intro datos
my_other_dict = {"Nombre": "Alionca",
                 "Apellido": "Ignacio", "Edad": 36, 1: "Python"}

my_dict = {
    "Nombre": "Alionca",
    "Apellido": "Ignacio",
    "Edad": 36,
    "Lenguajes": {"Python", "Php", "Angular"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)

#longitud del object
print(len(my_other_dict))
print(len(my_dict))

## Búsqueda
print(my_dict[1])
print(my_dict["Nombre"])

# Buscar por la clave
print("Ignacio" in my_dict)
print("Apellido" in my_dict)

# Inserción
my_dict["Calle"] = "Calle AlioncaDev"
print("insert ", my_dict)

# Actualización
my_dict["Nombre"] = "Bárbara"
print(my_dict["Nombre"])


# Eliminación
del my_dict["Calle"]
print(my_dict)

## Otras operaciones

# Devuelve una lista de pares de valor clave en el diccionario.
print(my_dict.items())

# Devuelve una lista de las claves en el diccionario.
print(my_dict.keys())

# Devuelve una lista de todos los valores en el diccionario.
my_dict.values()

# Devuelve una lista de todos los valores en el diccionario.
print(my_dict.values())


my_list = ["Nombre", 1, "Piso"]

# Crea un nuevo diccionario de la lista dada de claves.
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

#Crea un nuevo diccionario con las teclas dadas y todos los valores establecidos en ninguno.
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))

"""
Crea un nuevo diccionario del diccionario dado.
El nuevo diccionario tendrá las mismas claves que el diccionario dado,
Pero todos los valores se establecerán en ninguno.
"""
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))

"""
Crea un nuevo diccionario del diccionario dado con todos los valores establecidos en "AlionCadev".
"""
my_new_dict = dict.fromkeys(my_dict, "AlioncaDev")
print((my_new_dict))

# Devuelve una lista de todos los valores en el diccionario.
my_values = my_new_dict.values()
print(type(my_values))

# Devuelve una lista de todos los valores en el diccionario
print(my_new_dict.values())

"""
Devuelve una lista de valores únicos en el diccionario 'my_new_dict'.
La lista se crea utilizando el método 'fromkeys' de la clase 'dict'
Para crear un nuevo diccionario a partir de los valores de 'my_new_dict', y luego
utilizando los métodos 'List' y 'Keys' para extraer los valores únicos.
"""
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))

# Devuelve una tupla de los pares de valor clave en el diccionario dado.
print(tuple(my_new_dict))

# Establece el valor de my_new_dict en el valor dado.
print(set(my_new_dict))