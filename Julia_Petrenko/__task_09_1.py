# Напишите программу для подготовки папки и python-файлов для ваших домашних заданий.
#
# Функции программы:
#
#     Мы можете ввести путь, по которому будет создана структура
#     Вы можете ввести название для основной папки
#     Вы можете указать, сколько python-файлов будет созданов внутри папки
#     Вы можете дополнительно указать, какое общее название будуте иметь эти файлы или использовать значение по умолчанию
#     (прим. Task_<n> or solution_<n>)

import os

target_path = input("Enter target path where you will create new folder <for example, D:\\Academy_Shag\\Python>: ")
new_folder = input("Enter name for new folder: ")  # my_path = "Julia Petrenko"
file_count = int(input("How much files do you want to create: "))  # __task_09
file_name_pattern = input("Enter file name pattern: ")

new_path = os.path.join(target_path, new_folder)

if not os.path.exists(new_path):
    os.mkdir(new_path)

n = 1
while n <= file_count:
    file_name = file_name_pattern + "_" + str(n) + ".py"
    open(os.path.join(new_path, file_name), "w").close()
    n += 1






