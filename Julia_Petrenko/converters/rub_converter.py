# Задача 1
# Создайте пакет с именем converters с 3 мя модулями внутри eur_converter.py, usd_converter.py, rub_converter.py.
# В каждом модуле определите функцию convert(amount: float), которая принимает сумму в BYN и возвращает сумму в валюте модуля.

# Задача 2
# Для предыдущего задания добавьте для каждого модуля входную точку в программу,
# в которой будет возможность передать аргументы для файла через командную строку.
#
# Пример работы:
# G:\IT ШАГ\py_modules>converters\usd_converter.py 10
# 3.125
from sys import argv


def converter(amount: float):
    return amount * 26.39


print(len(argv))
if __name__ == "__main__" and len(argv) > 1:
    print(converter(float(argv[1])))
    # print(argv[0], argv[1])






