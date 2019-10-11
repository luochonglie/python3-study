import requests
import concurrent.futures
from geek.decorator import time_consuming


def download_one(url):
    resp = requests.get(url)
    print(f'read {len(resp.content)} bytes from {url}')


@time_consuming
def download_all(sites):
    for site in sites:
        download_one(site)


@time_consuming
def download_all_thread(sites):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_one, sites)


@time_consuming
def download_all_process(sites):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(download_one, sites)


def main():
    sites = list(
        f'http://quanxue.cn/CT_NanHuaiJin/LunYu/LunYu{str(x).zfill(2)}.html'
        for x in range(2, 30))

    # download_all(sites)
    download_all_thread(sites)
    download_all_process(sites)


if __name__ == '__main__':
    main()
