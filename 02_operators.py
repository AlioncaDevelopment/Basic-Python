### Operadores Aritméticos ###

# Operaciones con enteros
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 // 4)

#Operaciones con cadenas
print('Hola' + 'Python' + 'Qtal?')
print("Hola" + str(5))

#Operaciones mixtas
print("Hola" * 5)
print("Hola" * (2**3))

my_float = 2.5 * 2
#int() convierte un numero deciamal en entero
print("Hola" * int(my_float))


### Operadores Comparativos ###

# Operaciones con enteros
print(3 > 4) # mayor que
print(3 < 4) # menor que
print(3 >= 4) # mayor o igual que
print(4 <= 4) # menor o igual que
print(3 == 4) # igual que
print(3 != 4) # distinto de

# Operaciones con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Lógicos ###


# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "Hola" > "Python") # and '&' debe cumplir ambas condiciones
print(3 > 4 or "Hola" > "Python") # or '|' debe cumpli una de las dos condiciones
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
"""
Or debe cumplir una de las dos
y si es la segunda debe cumplir
ambas por el and englobado entre ()
"""
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4)) # not '!' niega la condicion
