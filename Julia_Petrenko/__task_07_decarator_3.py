# Напишите декоратор @not_empty_text, который будет проверять передаваемый аргумент text в функцию.
# В случае если text - пустая строка, заменить ее на строку "Hello".
#
# Напишите декоратор @to_upper, применяемый к любой функции, которая возвращает текст,
# который преобразует возвращаемый текст в верхний регистр.

def not_empty_text(func):
    def wrapper(text: str):
        if text == "":
            text = "Hello"
        # text = "Hello" if text == "" else text
        return func(text)
    return wrapper


def to_upper(func):
    def wrapper(text: str):
        return func(text.upper())
    return wrapper


@to_upper
@not_empty_text
def add_question(text: str):
    return text + "?"


print(add_question(""))
print(add_question("How is it going"))



