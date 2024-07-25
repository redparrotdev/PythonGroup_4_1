def repeat(func):
    def wrapper(num, name="Bob"):
        for i in range(num):
            func(name)
    return wrapper


@repeat
def say_hello_to(name="Bob"):
    print(f"Hello, {name}")


say_hello_to(4, "Kriss")
say_hello_to(4)

# say_hello_to = repeat(say_hello_to)
# say_hello_to(4, "Bill")
