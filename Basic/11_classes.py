### Classes ###

# Definición

class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía

print(MyEmptyPerson)

# Clase con constructor, funciones y popiedades privadas y públicas
class Person:
    def __init__(self, name, surname, alias="Sin alias") :
        self.full_name = f"{name}{surname} ({alias})" #propiedad publica
        self.__name = name #propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} esta caminando")


my_person = Person("Alionca", "Ignacio")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()


my_other_person = Person("Alionca", "Ignacio", "AlioncaDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)

