import threading
import random
import time


value = 0
lock_object = threading.RLock()


def increment(amount):
    global value
    th = threading.current_thread()
    for j in range(5):
        print(f"Поток {th.name} ожидает блокировку")
        with lock_object:
            print(f"Поток {th.name} поставил блокировку")
            print(f"Поток {th.name} увиличивает на {amount}")
            value += amount
            print(f"Value: {value}")
            time.sleep(0.3)
            print(f"Поток {th.name} снял блокировку")


threads = []

for i in range(4):
    th = threading.Thread(target=increment,
                          args=[i + 1],
                          name=f"Thread_{i + 1}")

    threads.append(th)


for t in threads: t.start()

input()
lock_object.release()
