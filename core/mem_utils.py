import os
import psutil


def show_mem_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    mem = info.uss / 1024. / 1024
    print(f'{hint} memory used: {mem} MB.')
