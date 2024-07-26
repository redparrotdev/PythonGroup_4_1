def repeat(num):
    def wrapper(func):
        def inner(name="Bob"):
            for i in range(num):
                func(name)

        return inner

    return wrapper


@repeat(4)
def say_hello_to(name="Bob"):
    print(f"Hello, {name}")


say_hello_to("Kriss")

