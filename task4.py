# Задание №4

# Создать программу, которая будет производить
# подсчёт количества слов в каждом файле в указанной
# директории и выводить результаты в консоль.

# Используйте потоки.

import threading
import time

from urllib3 import response
from yarl import _url

from task3 import urls, download

work_path = '../seminar_4'

threads = []  # список для наших потоков
start_time = time.time()


def parser_file(file_name):
    file_name = 'threading_' + _url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {_url} in {time.time() - start_time:2f} seconds")


for url in urls:
    thread = threading.Thread(target=download, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

for thread in threads:
     # проверяем, выполняется ли поток в данный момент времени
     print(thread.is_alive())

# # Создать программу, которая будет производить подсчет количества слов в каждом файле в
# # указанной директории и выводить результаты в консоль.
# # Используйте асинхронный подход.
#
# import asyncio
# import time
# import os
#
# threads = []  # список для наших потоков
# start_time = time.time()
#
#
# async def count_words(file_name):
#     with open(file_name, 'r', encoding='utf-8') as f:
#         text = f.read()
#         words = text.split()
#         return len(words)
#
# async def count_directory(directory):
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             file_name = os.path.join(root, file)
#             print(file_name, await count_words(file_name))
#
#
# if __name__ == '__main__':
#     asyncio.run(count_directory('c:/Users/shuri/PycharmProjects/pythonProject2/seminar4'))
#     print(f"Downloaded in {time.time() - start_time:2f} seconds")

# # Создать программу, которая будет производить подсчет количества слов в каждом файле в
# # указанной директории и выводить результаты в консоль.
# # Используйте процессы.
#
# import multiprocessing
# import time
# import os
#
# threads = []  # список для наших потоков
# start_time = time.time()
#
#
# def count_words(file_name):
#     with open(file_name, 'r', encoding='utf-8') as f:
#         text = f.read()
#         words = text.split()
#         return len(words)
#
# def count_directory(directory):
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             file_name = os.path.join(root, file)
#             tread = multiprocessing.Process(target=print, args=(file_name, count_words(file_name)))
#             threads.append(tread)
#             tread.start()
#
# if __name__ == '__main__':
#     count_directory('c:/Users/shuri/PycharmProjects/pythonProject2/seminar4')
#     for thread in threads:
#         thread.join()
#     print(f"Downloaded in {time.time() - start_time:2f} seconds")

# # Создать программу, которая будет производить подсчет количества слов в каждом файле в
# # указанной директории и выводить результаты в консоль.
# # Используйте потоки.
#
# import threading
# import time
# import os
#
# threads = []  # список для наших потоков
# start_time = time.time()
#
# # file_name = ""
#
# def count_words(file_name):
#     with open(file_name, 'r', encoding='utf-8') as f:
#         text = f.read()
#         words = text.split()
#         return len(words)
#
# def count_directory(directory):
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             file_name = os.path.join(root, file)
#             tread = threading.Thread(target=print, args=(file_name, count_words(file_name)))
#             threads.append(tread)
#             tread.start()
#
# count_directory('c:/Users/shuri/PycharmProjects/pythonProject2/seminar4')
# for thread in threads:
#     thread.join()
# print(f"Downloaded in {time.time() - start_time:2f} seconds")