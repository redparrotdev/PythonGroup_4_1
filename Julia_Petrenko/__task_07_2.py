# Напишите функцию, которая принимает список чисел и возвращает его копию,
# состоящую только из уникальных чисел.
# Пример работы функции: Передавая список [1, 4, 7, 4, 12, 1, 7] мы должны получить [1, 4, 7, 12]

def uniq_list(l):
    return list(set(l))


s_input = input("Enter list if number: ").split(",")
#1,4, 6, 7 , 3, 7 , 9,1,5,3

l = [int(i) for i in s_input]

new_list = uniq_list(l)

print(new_list)