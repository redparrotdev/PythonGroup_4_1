import threading
from threading import Thread, current_thread
import time


def write_data():
    th = current_thread()
    print(f"Начало записи потоком {th.name}")
    time.sleep(5)
    with open("file.txt", "w") as f:
        f.write("Some new file data")


th1 = Thread(target=write_data, name="WriteThread")

th1.start()

th1.join()

with open("file.txt", "r") as file:
    print(f"Данные из файла: {file.read()}")
