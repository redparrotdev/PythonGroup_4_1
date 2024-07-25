# Напишите декоратор not_negative, который будет преобразовывать значение функции в положительное,
# если функция вернет отрицательное.

def not_negative(inter_func):
    def wrapper():
        res = inter_func()
        if res < 0:
            res *= -1
        return res

    return wrapper


@not_negative
def get_a_number():
    return -10


# f = not_negative(get_a_number)
# f()
print(get_a_number())


@not_negative
def get_a_number2():
    return 45


print(get_a_number2())


