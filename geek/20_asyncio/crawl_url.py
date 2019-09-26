import asyncio


async def crawl_page(url):
    print(f'crawling {url}')
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print(f'ok {url}')


async def main(url_list):
    tasks = [asyncio.create_task(crawl_page(url)) for url in url_list]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    urls = ['url_1', 'url_2', 'url_3', 'url_4']
    asyncio.run(main(urls))
