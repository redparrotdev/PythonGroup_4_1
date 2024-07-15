# Даны 2 списка с одинаковым количеством элементов
# keys = ["key1", "key2", "key3", "key4"]
# values = [145, 12.4, False, "Some Text"]
# Напишите код, который создаст словарь, содержащий элементы 1 - го списка в виде ключей,
# а элементы 2 - го в качестве значений для этих ключей.
# Пример вывода: {'key1': 145, 'key2': 12.4, 'key3': False, 'key4': 'Some Text'}
# * Запишите код, используя генератор (list comprehension)

keys = ["key1", "key2", "key3", "key4"]
values = [145, 12.4, False, "Some Text"]

my_dict = {k: v for k, v in zip(keys, values)}
print(my_dict)
