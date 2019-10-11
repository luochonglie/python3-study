import time
import functools


def time_this(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        begin = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__} took {end - begin} seconds.')
        return res

    return wrapper


@time_this
def main():
    print("Hello")


if __name__ == '__main__':
    main()
