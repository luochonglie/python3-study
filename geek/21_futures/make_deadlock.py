import concurrent.futures
import time


def wait_on_b():
    time.sleep(5)
    print(b.result())
    return 'retch_b'


def wait_on_a():
    time.sleep(5)
    print(a.result())
    return print(__name__)


executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
a = executor.submit(wait_on_b)
b = executor.submit(wait_on_a)
