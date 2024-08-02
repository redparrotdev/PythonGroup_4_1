# Тема 10-11 ООП. Классы

## Классы

### Задача 1

Создайте класс `User`. Класс должен содержать 2 атрибута: `age` - приватный и `name` - публичный. Значения для каждого атрибута должны передаваться в конструктор. Для атрибута age организовать `getter` и `setter` (должен позволять установить только положительный возраст). В класс добавить метод `is_adult()`, возвращающий `True`, если пользователь совершеннолетний. Пример работы программы:

```python
class User:
    ...


user1 = User("Roman", 25)
user2 = User("Irina", 17)

user2.age = -14  # Ничего не меняет

print(user1.age)  # 25
print(user2.age)  # 17

print(user1.is_adult())  # True
print(user2.is_adult())  # False
```

### Задача 2

Есть 2 следующих класса:
```python
class Page:

    def __init__(self, text: str):
        self.__text = text

    @property
    def content(self):
        return self.text
    

class Book:

    def __init__(self, content: list[str]):
        self.__content = content
        self.pages = len(content)

    def read(self):
        return "\n".join(self.__content)
    
    def get_page(self, page_num: int):
        if (0 <= abs(int) <= self.pages):
            return self.__content[page_num]
```

Добавте возможность создания объектов классов на основе данных друг друга: из `Page` можно создать `Book` и обратно. Используйте `classmethod` или `staticmethod` (на ваше усмотрение). Пример работы программы:
```python
class Page:
    ...


class Book:
    ...


page1 = Page("Single page")
book1 = Book(["This book", "about programing", "and other stuff"])

page2 = Page.from_book(book1)
book2 = Book.from_page(page1)
```

### Задача 3

Реализуйте класс `HistoryList` - класс, который добавляет историю добавления и удаления данных из списка. Класс должен позволять добавлять, удалять (по индексу) и получать значение (по индексу) в списке. Для получение всего списка реализуйте свойсто `data`, которое будет возвращать содержимое списка в виде кортежа. Доступ к основному списку класса должен быть ограничен. Для получения истории реализуйте следующие методы: `addition_history()` - возвращает кортеж всех добавленных значений, `deletion_history` - возвращает кортеж всех удаленных значений и `get_history` - возвращает словарь со всей историей вида `{"add": (), "del": ()}`. Пример работы программы:
```python
class HistoryList:
    ...


my_list = HistoryList()

my_list.add_value(10)
my_list.add_value(20)

print(my_list.addition_history())  # (10, 20)

my_list.del_value(20)

print(my_list.deletion_history())  # (20)

print(my_list.get_value(0))  # 10

print(my_list.get_history())  # {"add": (10, 20), "del": (20)}
```


## Наследование, Полиморфизм

### Задача 1

Есть следующие классы:
```python
class Animal:

    def speek(self):
        return "No sound"


class Cat(Animal):
    ...


class Dog(Animal):
    ...


class Parrot(Animal):
    ...
```

Для каждого дочернего класса перезапишите метод `speek()`, чтобы он возвращал подходящий по имени класса звук животного.


### Задача 2

Есть следующий класс:
```python
class Color:

    def __init__(self, r: int, g: int, b:int):
        self.r = r
        self.g = g
        self.b = b
```

Добавьте для этого класса возможность сложения и вычитания с другим цветом (воспользуйтесь встроенными методами). Так же добавьте строковое представление для класса вида `"R: 213,G: 175,B: 54"`. Учтите, что значение для каждого цвета не может быть больше `255` и меньше `0`. Пример работы программы:
```python
class Color:
    ...
        

color1 = Color(10, 10, 10)
color2 = Color(20, 20, 20)

color3 = color1 + color2 
print(color3)  # "R: 30,G: 30,B: 30"

print(color3 - Color(15, 15, 20))  # "R: 15,G: 15,B: 10"
```

\* дополнительно добавить возможность получения цвета по индексу (0-2).
```python
color = Color(150, 200, 200)

print(color[1])  # 200
```
\*\* дополнительно добавить возможность сравнения цветов на равенство и не равенство

### Задача 3

Есть следующий базовый класс `Logger` и класс, который использует этот класс:
```python
class Logger:

    def log(self, msg: str):
        ...


class SomeDataClass:

    def __init__(self, logger: Logger):
        self.__logger = logger

    def some_data_process(self, data: str):
        print("Starting processing")
        print(f"Processing {data}")
        print("Data process finished")

        # Performing logging
        print("Logging data")
        self.__logger.log(f"[LOG] Data <{data}> processed!")
```

Реализуйте 2 дочерних класса: `ConsoleLogger` (выводит получаемое сообщение в консоль) и `FileLogger` (сохраняет сообщение в файл). Класс `FileLogger` в качестве аргумента конструктора принимает путь к файлу. Пример работы программы: 
```python
console_logger = ConsoleLogger()
file_logger = FileLogger("log.txt")
c1 = SomeDataClass(console_logger)
c2 = SomeDataClass(file_logger)

# Выведет в консоль [LOG] Data <Data for class 1> processed!
c1.some_data_process("Data for class 1")

# Создаст файл log.txt и запишет в него строчку
# [LOG] Data <Data for class 2> processed!
c2.some_data_process("Data for class 2")
```
