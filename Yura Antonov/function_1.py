# Напишите функцию, которая принимает список чисел и возвращает его копию,
# состоящую только из уникальных чисел.
# Пример работы функции:
# Передавая список [1, 4, 7, 4, 12, 1, 7] мы должны получить [1, 4, 7, 12]


def get_unique_numbers(numbers):

    unique_numbers = list(set(numbers))
    return unique_numbers


print(get_unique_numbers([1, 4, 7, 4, 12, 1, 7]))
