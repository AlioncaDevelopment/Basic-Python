## FUNCTIONS ##

## Definicion
def my_function():
    print("Esto es una funcion")

# llamada a la funcion
my_function()

# Función con parámetros de entrada/argumentos
def sum_two_values(value1: int, value2: int):
    print(value1 + value2)

sum_two_values(5, 10)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)


# Función con parámetros de entrada/argumentos y retorno
def sum_two_values_with_return(value1: int, value2: int):
    resul = value1 + value2
    return resul

my_result = sum_two_values_with_return(10, 5)
print(my_result)

# Resultado none ya que no devuelve nada la funcion
my_result = sum_two_values(1.4, 5.2)
print(my_result)


# Función con parámetros de entrada/argumentos por clave
def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Alionca", name="Dev")


# Función con parámetros de entrada/argumentos por defecto
def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Alionca", "Ignacio")
print_name_with_default("Alionca", "Ignacio", "AlioncaDev")


# Función con parámetros de entrada/argumentos arbitrarios
def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "AlioncaDev")
print_upper_texts("Hola")






