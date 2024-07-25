def call_once(func):
    n = 0
    res = 0

    def wrapper(a, b):
        nonlocal n, res
        if n == 0:
            res = func(a, b)
            n += 1
        else:
            n += 1

        print(f"n = {n}, summ = {res}")

    return wrapper


@call_once
def summ(a, b):
    return a + b


summ(1, 5)
summ(2, 6)
summ(3, 7)
summ(4, 8)


