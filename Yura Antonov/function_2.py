
# Даны 2 списка с одинаковым количеством элементов
# keys = ["key1", "key2", "key3", "key4"]
# values = [145, 12.4, False, "Some Text"]
# Напишите код, который создаст словарь, содержащий элементы 1-го списка в виде ключей, а элементы 2-го в качестве значений для этих ключей.
# Пример вывода: {'key1': 145, 'key2': 12.4, 'key3': False, 'key4': 'Some Text'}
# * Запишите код, используя генератор (list comprehension)

keys = ["key1", "key2", "key3", "key4"]
values = [145, 12.4, False, "Some Text"]


dictionary = {keys[i]: values[i] for i in range(len(keys))}

print(dictionary)


# Перепишите код любой из задач предыдущих ДЗ в виде функции, которая возвращает результат.


def create_dictionary(keys, values):

    dictionary = {keys[i]: values[i] for i in range(len(keys))}
    return dictionary


keys = ["key1", "key2", "key3", "key4"]
values = [145, 12.4, False, "Some Text"]
result = create_dictionary(keys, values)

print(result)