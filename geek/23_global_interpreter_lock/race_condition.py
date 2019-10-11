import threading

n = 0


def foo():
    global n
    n += 1


def run(i):
    threads = [threading.Thread(target=foo) for i in range(100)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(f'{i:03}: {n}')


def main():
    for i in range(1000):
        global n
        n = 0
        run(i)


if __name__ == '__main__':
    main()
