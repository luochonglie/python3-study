import asyncio
import sys


async def worker_1():
    print("worker_1 start")
    await asyncio.sleep(1)
    print("worker_1 end")


async def worker_2():
    print("worker_2 start")
    await asyncio.sleep(2)
    print("worker_2 end")


async def worker(name, sleep_time):
    print(f"{name} start")
    await asyncio.sleep(sleep_time)
    print(f'{name} end')


async def main_1():
    print("main_1 await worker sync")
    print("before await")
    await worker_1()
    print("awaited worker_1")
    await worker_2()
    print("awaited worker_2")
    print("finished")


async def main_2():
    print("main_2 await worker async")
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    print("before await")
    await task1
    print("awaited worker_1")
    await task2
    print("awaited worker_2")
    print("finished")


async def main_3(num=10, sleep_time=1):
    print(f"main_3 await [{num}] workers async")
    tasks = [asyncio.create_task(worker(f'worker_{i}', sleep_time)) for i in range(num)]
    print("before await")
    for i, task in enumerate(tasks):
        await task
        print(f"awaited worker_{i}")


async def main():
    main_3(10)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        asyncio.run(eval(sys.argv[1])())
    else:
        asyncio.run(main())
