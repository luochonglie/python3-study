import time
import concurrent.futures
import core.time_this as timetools


def cpu_bound(number):
    print(sum(i * i for i in range(number)))


@timetools.time_this
def sync_calculate_sums(numbers):
    for number in numbers:
        cpu_bound(number)


@timetools.time_this
def multi_proc_calculate_sums(numbers):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(cpu_bound, numbers)


@timetools.time_this
def multi_thread_calculate_sums(numbers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(cpu_bound, numbers)


def main():
    numbers = [10000000 + x for x in range(20)]
    sync_calculate_sums(numbers)
    multi_proc_calculate_sums(numbers)
    multi_thread_calculate_sums(numbers)


if __name__ == '__main__':
    main()
