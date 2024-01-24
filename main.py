# Написать программу, которая считывает список из 10 URL-адресов и одновременно загружает данные с каждого адреса.
# После загрузки данных нужно записать их в отдельные файлы.
# Используйте потоки.
import threading
import time
import requests

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

threads = []  # список для наших потоков
start_time = time.time()


def download(_url):
    response = requests.get(_url)
    file_name = 'threading_' + _url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(response.text)
   

for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print(f"Downloaded  in {time.time() - start_time:2f} seconds")