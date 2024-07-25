# Напишите функцию find_a_bug(text: str, callback),
# которая будет принимать строку вида "Done_Task1, Done_Task2, Bug_Task3, Done_Task4, Bug_Task5".
# Функци должна разобрать строку на комоненты, разделенные запятой.
# Для каждой строки, содержащей слово bug (в любом регистре), вызвать функцию callback и передать туда эту строчку.
# Функция callback(text) должна вывести в консоль текст вида Фиксим баг <Bug_Task3>.

def find_bug(text: str, bag_callback):
    # print(text.split(","))
    [bug_callback(n.strip()) for n in text.split(",") if n.lower().find("bug") > -1]


def bug_callback(text):
    print(f"Fix the bug <{text}>")


find_bug("Done_Task1, Done_Task2, Bug_Task3, Done_Task4, Bug_Task5", bug_callback)

