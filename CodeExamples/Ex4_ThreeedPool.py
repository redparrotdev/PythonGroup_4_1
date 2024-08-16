import threading
from concurrent.futures import ThreadPoolExecutor
import time
import random


def write_to_file(data: list[str]):
    th = threading.current_thread()
    for l in data:
        print(l.format(th.name))
        time.sleep(random.random())


pool = ThreadPoolExecutor(max_workers=3,
                          thread_name_prefix="FileThread")

data_to_write = [
    "Line1 {0}",
    "Line2 {0}",
    "Line3 {0}",
    "Line4 {0}"
]

pool.submit(write_to_file, data=data_to_write)
pool.submit(write_to_file, data=data_to_write)
pool.submit(write_to_file, data=data_to_write)
pool.submit(write_to_file, data=data_to_write)
pool.submit(write_to_file, data=data_to_write)
pool.submit(write_to_file, data=data_to_write)
