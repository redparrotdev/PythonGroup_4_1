# Программа для проверки наличия товара на складе.
# Программа на вход получает из консоли строку с нужными товарами в следующем виде:
# молоко, ХлеБ, КолбаСА, ЯЙцА.
# Затем в консоль вводится строка с товарами, которые есть на складе:
# ХЛЕБ, яйца, колбаСа.
# Программа должна проверить наличие товара на скалде и вывести информацию в консоль (формат вывода произвольный).
#
# Пример вывода:
# Нужно: молоко, ХлеБ, КолбаСА, ЯЙцА
# Склад: ХЛЕБ, яйца, колбаСа
# <Молоко> на складе: [Нет]
# <Хлеб> на складе: [Да]
# <Колбаса> на складе: [Да]
# <Яйца> на складе: [Да]

listNeed = input("Enter a list of needed products separated by commas: ").split(",")
setNeed = set(i.strip().lower() for i in listNeed)

listStore = input("Enter a list of products on the store separated by commas: ").split(",")
setStore = set(i.strip().lower() for i in listStore)

d = {i.strip().capitalize(): "Yes" if i.lower() in setStore else "No" for i in setNeed}

for k, v in d.items():
    print(f"<{k}> on the store: [{v}]")

