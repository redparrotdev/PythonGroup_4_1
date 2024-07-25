# Напишите декорато @call_twice, который будет применим к любой функции и будет вызывать ее дважды.
def call_twice(inter_func):
    def wrapper():
        inter_func()
        inter_func()

    return wrapper


@call_twice
def hello():
    print("Hello")

# f = call_twice(hello)
# f()


hello()




