# Есть следующий код:
#
# file_name = input("Имя файла: ") + ".txt"
#
# file_data = []
#
# print("[Начало записи]")
# while True:
#     line = input(">>> ")
#
#     if (line.strip().lower()) == "#end":
#         break
#
#     file_data.append(line)
#
# print("[Запись завершена]")
#
# with open(file_name, "w") as file:
#     text = "\n".join(file_data)
#     file.write(text)
#
# print(f"[Сохранено в файл {file_name}]")
#
# Создайте поток, который будет раз в 5(или другое значение) секунд записывать данные из списка file_data в файл,
# к названию которого добавлено "_autosave".В конце работы программы удалить файл резервной копии.
#
# *Учтите, что программа может завершится преждевременно, в таком должен быть создан файл с указанным именем
# и в него должны быть записаны данные из резервного файла.Резервный файл удалить

import threading as thr
import time
import os
import shutil

file_name_short = input("Имя файла: ")
file_name = (file_name_short + ".txt")
file_name_autosave = (file_name_short + "_autosave.txt")

file_data = []


def autosave(interval):
    global file_data
    while True:
        with open(file_name_autosave, "w") as file_as:
            text_as = "\n".join(file_data)
            file_as.write(text_as)
            print(file_data)
        time.sleep(interval)


thr_autosave = thr.Thread(target=autosave, args=(5, ), daemon=True)
thr_autosave.start()

print("[Начало записи]")
while True:
    line = input(">>> ")

    if (line.strip().lower()) == "#end":
         break

    file_data.append(line)

print("[Запись завершена]")

if os.path.isfile(file_name):
    os.remove(file_name)
os.rename(file_name_autosave, file_name)

# try:
#     file = open(file_name, "w")
#     text = "\n".join(file_data)
#     file.write(text)
# except:
# os.rename(file_name_autosave, file_name)
# finally:
#     file_name.close()
#     os.remove(file_name_autosave)

print(f"[Сохранено в файл {file_name}]")