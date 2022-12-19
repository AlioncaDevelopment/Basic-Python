## VARIABLES ##

my_string = "My String variable"
print(my_string)

my_int = 36
print(my_int)

#convertir una variable int en string
my_int_to_string = str(my_int)
print(my_int_to_string)
print(type(my_int_to_string))

my_boolean = True
print(my_boolean)

# concatenación de variables en un print
print(my_string, my_int, my_int_to_string, my_boolean)
print("Este es el valor de: ", my_boolean)

# Algunas funciones del sistema
print(len(my_int_to_string)) #pinta la longitud

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Bárbara", "Ignacio", "Alionca", 36
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)


#Input
name = input('¿Cual es tu nombre?')
age = input('¿Cuantos años tienes?')
print(name)
print(age)

#Cambiamos su tipo
name = 36
age = "Alionca"

#forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print(type(address))






