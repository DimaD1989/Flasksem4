# Задание №3
#
# Написать программу, которая считывает список
# из 10 URL-адресов и одновременно загружает
# данные с каждого адреса.
#
# После загрузки данных нужно записать их
# в отдельные файлы.
#
# Используйте асинхронный подход.

import asyncio
import aiohttp
import time


urls = [
    'https://gb.ru/',
    'https://google.com',
    'https://yandex.ru',
    'https://python.org',
    'https://mail.ru',
    'https://stepik.org',
    'https://vk.com',
    'https://yahoo.com',
    'https://pikabu.ru',
    'https://codelessons.ru'
    ]


async def download(_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(_url) as response:
            text = await response.text()
            file_name = 'asyncio_' + _url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Downloaded {_url} in {time.time() - start_time:2f} seconds")


async def main():
    tasks = []
    for _url in urls:
        task = asyncio.ensure_future(download(_url))
        tasks.append(task)
    await asyncio.gather(*tasks)

start_time = time.time()

if __name__ == '__main__':  # обязательно для асинхронного подхода!
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

# import threading
# import time
# import requests
# import multiprocessing
#
# urls = [
#     'https://gb.ru/',
#     'https://google.com',
#     'https://yandex.ru',
#     'https://python.org',
#     'https://mail.ru',
#     'https://stepik.org',
#     'https://vk.com',
#     'https://yahoo.com',
#     'https://pikabu.ru',
#     'https://codelessons.ru'
# ]
#
# mult = []  # список для наших потоков
# start_time = time.time()
#
#
# def download(_url):
#     response = requests.get(_url)
#     file_name = 'mult_' + _url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
#     with open(file_name, 'w', encoding='utf-8') as f:
#         f.write(response.text)
#
# if __name__ == '__main__':
#
#     for url in urls:
#         thread = multiprocessing.Process(target=download, args=[url])
#         mult.append(thread)
#         thread.start()
#
#     for thread in mult:
#         thread.join()
#     print(f"Downloaded in {time.time() - start_time:2f} seconds")
#  import aiohttp
# import time
# import asyncio
#
# urls = [
#     'https://gb.ru/',
#     'https://google.com',
#     'https://yandex.ru',
#     'https://python.org',
#     'https://mail.ru',
#     'https://stepik.org',
#     'https://vk.com',
#     'https://yahoo.com',
#     'https://pikabu.ru',
#     'https://codelessons.ru'
#     ]
#
# threads = []  # список для наших потоков
# start_time = time.time()
#
#
# async def download(_url):
#     async with aiohttp.ClientSession() as aiohttp_session:
#         async with aiohttp_session.get(_url) as async_with:
#             text = await async_with.text()
#             file_name = 'async_' + _url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
#             with open(file_name, 'w', encoding='utf-8') as f:
#                 f.write(text)
#
#
# async def main():
#     task = []
#     for url in urls:
#         task.append(asyncio.create_task(download(url)))
#     await asyncio.gather(*task)
#
# if __name__ == "__main__":
#     asyncio.run(main())
# print(f"Downloaded in {time.time() - start_time:2f} seconds")
