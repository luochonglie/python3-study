import asyncio
import aiohttp
import core.time_this as decorator


async def load_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(f'Read {resp.content_length} from {url}')


@decorator.time_this
async def load_all(sites):
    tasks = [asyncio.create_task(load_one(site)) for site in sites]
    await asyncio.gather(*tasks)


def main():
    sites = list(
        f'http://quanxue.cn/CT_NanHuaiJin/LunYu/LunYu{str(x).zfill(2)}.html'
        for x in range(2, 30))

    asyncio.run(load_all(sites))


if __name__ == '__main__':
    main()
