# Дан следющий список имен
# names = [
#     "Victoria",
#     "Wade",
#     "Chanelle",
#     "Victoria",
#     "Evan",
#     "Tyrone"
#     "Neve",
#     "Peggy",
#     "Tyrone",
#     "Peggy",
# ]
# Напишите код, который уберет из списка повторяющиеся имена, а так же имена, количество символов в которых меньше 5.
# Пример вывода: ['Peggy', 'Tyrone', 'Victoria', 'Chanelle']

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
s = set(names)
names = [n for n in s if len(n) >= 5]
print(names)
