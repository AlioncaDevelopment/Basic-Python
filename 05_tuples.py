### Tuples ###

# Definición

#Declaracion de variables
my_tuple = tuple();
my_tuple2 = ();

#añadimos datos
my_tuple = (36, 1.70, 'Alionca', 'Ignacio', 'Alionca')
my_tuple2 = (36, 60, 30)

#pintamos contenido
print(my_tuple2)
print(my_tuple)

#mostrar el tipo de variable
print(type(my_tuple))

# Acceso a elementos y búsqueda
print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

#
print(my_tuple.count("Alionca"))
#
print(my_tuple.index("Ignacio"))
print(my_tuple.index("Alionca"))

# my_tuple[1] = 1.80 'tuple' El objeto no admite la asignación de elementos

#Concatenacion
Concat_tuple = my_tuple + my_tuple2
print(Concat_tuple)

#subTuple
print(Concat_tuple[3:6])

# Tupla mutable con conversión a lista

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "MoureDev"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Eliminación

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined





