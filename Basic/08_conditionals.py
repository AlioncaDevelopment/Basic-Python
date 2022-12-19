## CONDICIONALES ##

my_condition = False
## IF
if my_condition:
    print('Se ejecuta la condicion IF')

my_condition = 5 * 5

if my_condition == 10:
    print('Se ejecuta el if')

# if, elif, else
if my_condition > 10 and my_condition < 20:
    print('es mayor de 10 y menor 20')
elif my_condition == 25:
    print('es igula a 25')
else:
    print('es meno o igula a 10')

print('la ejecucion continua')

# Condicional con ispección de valor

my_string = ""

if not my_string:
    print('Cadena de texto vacia')

if my_string == "HOLA QTAL":
    print('Estas dentro del if')
