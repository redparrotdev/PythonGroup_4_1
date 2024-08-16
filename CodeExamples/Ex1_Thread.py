import threading
import datetime
import time

#class MyThread(threading.Thread):
#
#    def run(self):
#        pass

running = True


def show_time(interval):
    th = threading.current_thread()
    #global running
    while True:
        dt = datetime.datetime.now()
        print(f"Поток: {th.name} Время: {dt.strftime('%d %m %Y')}")
        time.sleep(interval)



th1 = threading.Thread(target=show_time,
                       args=[1],
                       daemon=True,
                       name="Thread_1")

th2 = threading.Thread(target=show_time,
                       args=[3],
                       daemon=True,
                       name="Thread2")

th1.start()
th2.start()

threads = threading.enumerate()
print(f"Активные потоки: {threads}")
time.sleep(10)

running = False

