import asyncio


async def worker_1():
    print("worker_1 start")
    await asyncio.sleep(1)
    print("worker_1 end")


async def worker_2():
    print("worker_2 start")
    await asyncio.sleep(1)
    print("worker_2 end")


async def worker(name, sleep_time):
    print(f"{name} start")
    await asyncio.sleep(sleep_time)
    print(f'{name} end')


async def main():
    tasks = [asyncio.create_task(worker(f'worker_{i}', 1)) for i in range(1000)]
    print("before await")
    for i, task in enumerate(tasks):
        await task
        print(f"awaited worker_{i}")


if __name__ == "__main__":
    asyncio.run(main())
