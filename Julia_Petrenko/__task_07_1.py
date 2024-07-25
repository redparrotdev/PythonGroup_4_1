# Напишите функцию, которая будет принимать число в качестве аргумента и увеличивать его значение в 2 раза.
# Если число отрицательное, заменить его на положительное.
# Пример работы функции: При передаче функцию числа 4 обратно мы получим 8. При передаче функции числа -5 мы получим 10
def mult_two(a):
    if a[0] == "-":
        a = a[1:]
    if a.count(".") < 2 and a.replace(".", "").isdigit():
        return float(a) * 2
    else:
        print(f"Check you enter of number. You enter {a}")
    return


a = input("Enter number for multiplication: ")
print(mult_two(a))
