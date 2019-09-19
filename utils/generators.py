def fibonacci(k):
    if k < 1:
        return

    times = 1
    a, b = 1, 1
    while times <= k:
        if times == 1:
            yield a
        elif times == 2:
            yield b
        else:
            a, b = b, a+b
            yield b
        times += 1


def main():
    pass


if __name__ == '__main__':
    print(list(fibonacci(10)))
