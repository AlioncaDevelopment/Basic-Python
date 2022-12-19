### Strings ###

# declaracion de variables
my_string = "Mi String"
my_other_string = 'Mi otro String'

# longitud de la variable
print(len(my_string))
print(len(my_other_string))
# concatenación variables
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Brais", "Moure", 35
"""
.format(varible1, variable2 ...)
coloca las variables en las posiciones
ordenadamente que se le indica
mediante {} en el texto
"""
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))

"""
% (varible1, variable2 ...)
coloca las variables en las posiciones
ordenadamente que se le indica
mediante %s para string y
%d para numbre en el texto
"""
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))

# concatenación y str(convierte age en string)
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
# concatenación
print(f"Mi nombre es {name} {surname} y mi edad es {age}")


# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)


# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize()) # pone la primera letra en mayúscula pero no cambia el valor
print(language.upper()) # pone el texto en minúscula pero no cambia el valor
print(language.lower().isupper()) # isupper() comprobar si el texto es ta en minús.
print(language.lower()) # pone el texto en mayúscula pero no cambia el valor
print(language.islower()) # comprobar si el texto es ta en mayús.
print(language.count("t")) # número de veces que se repite el carcter indicado
print(language.isnumeric()) # comprueba si es numero
print("1".isnumeric()) # comprueba si es numero
print(language.startswith("Py")) # comienza con() devuelve boolean
print(language.endswith("on")) # termina con() devuelve boolean
print("Py" == "py")  # No es lo mismo
print(language.swapcase()) # Cambia mayús. por minús. y vicebersa
print(language.title()) # Convierte el texto en formato titulo






