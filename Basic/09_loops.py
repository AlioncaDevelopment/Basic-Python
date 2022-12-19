### LOOPS ###.

## WHILE

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # es opcional
    print('Es mayor a 10')

print("Continua la ejecucion")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print('se detiene la ejecucion')
        break
    print(my_condition)

print("Continua la ejecucion")

## FOR

my_list = [35, 24, 62, 52, 30, 30, 17]
for elem in my_list:
    print(elem)


my_tuple = (35, 1.77, "Alionca", "Dinorah", "Bárbara")
for elem in my_tuple:
    print(elem)

my_set = {"Alionca", "Dinorah", 35}
for elem in my_set:
    print(elem)

my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
for elem in my_dict:
    print(elem)
    if elem == "Edad":
        break
    else:
        print("El bluce for para diccionario ha finalizado")

print("La ejecución continúa")

for elem in my_dict:
    print(elem)
    if elem == "Edad":
        continue
    print("Se ejecuta")
else:
    print('El bucle for para dicionario ha finalizado')


