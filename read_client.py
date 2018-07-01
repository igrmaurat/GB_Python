# python read_client.py
# Пока работает с сервером lesson_2_server.py

from socket import socket, AF_INET, SOCK_STREAM


ADDRESS = ('localhost', 8888)


class ClientRead:
    def __init__(self, ADDRESS):
        self.ADDRESS = ADDRESS

    def echo_client(self):
        with socket(AF_INET, SOCK_STREAM) as sock:  # Создать сокет TCP
            sock.connect(self.ADDRESS)  # Соединиться с сервером
            while True:
                # Получаем ответ сервера, размер не больше 1024 байт
                data_from_server = sock.recv(1024).decode('ascii')
                print(data_from_server)


if __name__ == '__main__':
    client = ClientRead(ADDRESS)
    client.echo_client()