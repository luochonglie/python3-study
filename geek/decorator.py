import time
import functools


def time_consuming(func):
    @functools.wraps(func)
    def wraper(*args, **kwargs):
        begin = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        duration = (end - begin) * 1000
        print(f'{func.__name__} took {duration} ms.')
        return res

    return wraper


@time_consuming
def main():
    print("Hello")


if __name__ == '__main__':
    main()
