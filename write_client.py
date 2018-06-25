# python write_client.py
# Пока работает с сервером server.py

from socket import socket, AF_INET, SOCK_STREAM
import name_message
import jim_message
import jim_to_bytes

ADDRESS = ('localhost', 8888)

def echo_client():
# Начиная с Python 3.2 сокеты имеют протокол менеджера контекста
# При выходе из оператора with сокет будет автоматически закрыт

    with socket(AF_INET, SOCK_STREAM) as sock: # Создать сокет TCP
        sock.connect(ADDRESS) # Соединиться с сервером
        while True:

            text = input('Ваше сообщение: ')
            if text == 'exit':
                break
            else:
                # Передаем сообщение
                message = jim_message.jim_message
                name = input('Введите ваше имя  ')
                message = name_message.name_passing(message, name, text)

            # sock.send(msg.encode('ascii')) # Отправить прям из ввода в кодировке ascii
            sock.send(jim_to_bytes.to_bytes(message)) # Отправить!

if __name__ == '__main__':
    echo_client()
