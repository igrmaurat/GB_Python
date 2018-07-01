# python lesson_2_server.py
# Дает к себе подключиться разным клиентам.
# Затем получает сообщение от клиента, который отправляет сообщение и пересылает всем клиентам, которые слушают сервер.

import time
import select
from socket import socket, AF_INET, SOCK_STREAM

def new_listen_socket(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(5)
    sock.settimeout(0.2) # Таймаут для операций с сокетом
    # Таймаут необходим, чтобы не ждать появления данных в сокете
    return sock

def mainloop():
    ''' Основной цикл обработки запросов клиентов'''
    address = ('', 8888)
    clients = []
    sock = new_listen_socket(address)
    while True:
        try:
            conn, addr = sock.accept()  # Проверка подключений
        except OSError as e:
            pass  # timeout вышел
        else:
            print("Получен запрос на соединение с %s" % str(addr))
            clients.append(conn)
        finally:
            # Проверить наличие событий ввода-вывода без таймаута
            w = []
            r = []
            try:
                r, w, e = select.select(clients, clients, [], 0)
                # r, w, e = select.select(clients,[], [], 0)
                #r, w, e = select.select([], clients, [], 0)
            except Exception as e:
            # Исключение произойдёт, если какой - то клиент отключится
                pass  # Ничего не делать, если какой-то клиент отключился
        # Обойти список клиентов, читающих из сокета
        #     for s_client in w:
        #         timestr = time.ctime(time.time()) + "\n"
        #         try:
        #             s_client.send(timestr.encode('ascii'))
        #         except:
        #             # Удаляем клиента, который отключился
        #             clients.remove(s_client)

            for s_client in r:
                data = s_client.recv(1024).decode('ascii')
                try:
                    print(data)
                    for read_client in w:
                        read_client.send(data.encode('ascii'))
                except:
                    # Удаляем клиента, который отключился
                    clients.remove(s_client)

print('Эхо-сервер запущен!')

mainloop()