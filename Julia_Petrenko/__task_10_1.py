# Создайте класс User. Класс должен содержать 2 атрибута: age - приватный и name - публичный.
# Значения для каждого атрибута должны передаваться в конструктор.
# Для атрибута age организовать getter и setter (должен позволять установить только положительный возраст).
# В класс добавить метод is_adult(), возвращающий True, если пользователь совершеннолетний. Пример работы программы:

class User:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print(f"Age - {age} is not valid. Age have to be > 0.")

    def is_adult(self):
        adult = False
        if self.__age > 17:
            adult = True
        return adult


User1 = User("Roman", 25)
User2 = User("Stephen", 15)

print(User1.is_adult())
print(User2.is_adult())


