class Animal:

    def speek(self):
        return "No sound"

# Для каждого дочернего класса перезапишите метод speek(), чтобы он возвращал подходящий по имени класса звук животного.

class Cat(Animal):
    def speek(self):
        return "Meow"


class Dog(Animal):
    def speek(self):
        return "Woof"


class Parrot(Animal):
    def speek(self):
        return "Good bird"


cat = Cat()
print(cat.speek())

dog = Dog()
print(dog.speek())

parrot = Parrot()
print(parrot.speek())

