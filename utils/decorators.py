import time
import functools


def time_counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'------- [{func.__name__}] begin -------')
        begin = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__} took {(end - begin) * 1000} ms.')
        print(f'------- [{func.__name__}] end -------')
        return result

    return wrapper
