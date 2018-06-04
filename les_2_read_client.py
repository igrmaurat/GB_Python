# python les_2_read_client.py
# Пока работает с сервером lesson_2_server.py

from socket import socket, AF_INET, SOCK_STREAM
from select import select
import sys

ADDRESS = ('localhost', 8888)

def echo_client():
# Начиная с Python 3.2 сокеты имеют протокол менеджера контекста
# При выходе из оператора with сокет будет автоматически закрыт

    with socket(AF_INET, SOCK_STREAM) as sock: # Создать сокет TCP
        sock.connect(ADDRESS) # Соединиться с сервером
        while True:
            # Получаем ответ сервера, размер не больше 1024 байт
            data_from_server = sock.recv(1024).decode('ascii')
            print(data_from_server)

if __name__ == '__main__':
    echo_client()