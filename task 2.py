import time
import requests
from multiprocessing import Process  # ,Pool

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


def download(_url):
    response = requests.get(_url)
    file_name = 'threading_' + _url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {_url} in {time.time() - start_time:2f} seconds")


processes = []  # список для наших процессов
start_time = time.time()


if __name__ == '__main__':  # обязательно для процессов!
    for url in urls:
        process = Process(target=download, args=(url, ))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    # for process in processes:
    #     # проверяем, выполняется ли поток в данный момент времени
    #     print(process.is_alive())