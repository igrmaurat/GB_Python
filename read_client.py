# python read_client.py

import name_message
import jim_message
import jim_to_bytes

# Добавить сообщение

from socket import socket, AF_INET, SOCK_STREAM


ADDRESS = ('localhost', 8888)


class ClientRead:
    def __init__(self, ADDRESS):
        self.ADDRESS = ADDRESS

    def echo_client(self):
        with socket(AF_INET, SOCK_STREAM) as sock:  # Создать сокет TCP
            sock.connect(self.ADDRESS)  # Соединиться с сервером
            # техническое сообщение jim_presence
            message = jim_message.jim_presence
            # Задаем имя пользователя
            name = input('Введи имя  ')
            message = name_message.name_passing(message, name)
            #oтправляем техническое сообщение
            sock.send(jim_to_bytes.to_bytes(message))

            while True:
                # Получаем ответ сервера, размер не больше 1024 байт
                data_from_server = jim_to_bytes.bytes_to_json(sock.recv(1024))
                #if data_from_server: # если сообщение в принципе есть
                    #print(data_from_server)
                # Если тип сообщения action = msg
                if data_from_server['action'] == 'msg':
                    print('Сообщение от %s::::::::%s'%(data_from_server['from'],data_from_server['message']))


if __name__ == '__main__':
    client = ClientRead(ADDRESS)
    client.echo_client()