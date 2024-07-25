# Перепишите код любой из задач предыдущих ДЗ в виде функции, которая возвращает результат.
#
# __task_05_3
# Пользователь может ввести в программу произвольный текст,
# например, This is some text to test.
# Напишите код, который посчитает количество каждой буквы в предложении (пробелы не учитывать)
# и составит на основе этого словарь.
# Пример вывода 'T': 1, 'o': 2, 'm': 1, 'x': 1, 's': 4, 'e': 3, 'h': 1, 'i': 2, 't': 5}.
# * Запишите код, используя генератор (list comprehension)

def count_letter(textInput):
    d = {i: textInput.count(i) for i in textInput if i.isalpha()}
    return d


textInput = input("Enter some text: ")
print(count_letter(textInput))



