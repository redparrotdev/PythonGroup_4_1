# Тема 5 Коллекции

1. Дан следющий список имен 
```python
names = [
    "Victoria",
    "Wade",
    "Chanelle",
    "Victoria",
    "Evan",
    "Tyrone"
    "Neve",
    "Peggy",
    "Tyrone", 
    "Peggy",
]
```
Напишите код, который уберет из списка повторяющиеся имена, а так же имена , количество символов которых меньше 5. Пример вывода:
```['Peggy', 'Tyrone', 'Victoria', 'Chanelle']```

2. Даны 2 списка с одинаковым количеством элементов
```python
keys = ["key1", "key2", "key3", "key4"]
values = [145, 12.4, False, "Some Text"]
```
Напишите код, который создаст словарь, содержащий элементы 1-го списка в виде ключей, а элементы 2-го в качестве значений для этих ключей. Пример вывода: ```{'key1': 145, 'key2': 12.4, 'key3': False, 'key4': 'Some Text'}```
\* Запишите код, используя генератор (**list comprehension**)

3. Пользователь может ввести в программу произвольный текст, например ```This is some text to test```. Напишите код, который посчитает количество каждой буквы в предложении (пробелы не учитывать) и составит на основе этого словарь. Пример вывода ```'T': 1, 'o': 2, 'm': 1, 'x': 1, 's': 4, 'e': 3, 'h': 1, 'i': 2, 't': 5}```.
\* Запишите код, используя генератор (**list comprehension**)

4. Программа для проверки наличия товара на складе. Программа на вход получает из консоли строку с нужными товарами в следующем виде: ```молоко, ХлеБ, КолбаСА, ЯЙцА```. Затем в консоль вводится строка с товарами, которые есть на складе: ```ХЛЕБ, яйца, колбаСа```. Программа должна проверить наличие товара на скалде и вывести информацию в консоль (формат вывода произвольный). Пример вывода:
```
Нужно: молоко, ХлеБ, КолбаСА, ЯЙцА
Склад: ХЛЕБ, яйца, колбаСа
<Молоко> на складе: [Нет]
<Хлеб> на складе: [Да]
<Колбаса> на складе: [Да]
<Яйца> на складе: [Да]
```
Примечание: программа должна уметь работать с любым регистром и не зависеть от пробелов: ```моЛОко ,хлеб, колбаСА```