# python server.py
# Дает к себе подключиться разным клиентам.
# Затем получает сообщение от клиента, который отправляет сообщение и пересылает всем клиентам, которые слушают сервер.

import time
import select
from socket import socket, AF_INET, SOCK_STREAM
import jim_to_bytes
import sql_module
import time

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

        except Exception as err:
            print(err)

        else:
            print("Получен запрос на соединение с %s" % str(addr))
            _ip, _port = addr
            clients.append(conn)

            # Здесь запись в базу porta и ip клиента и времени подключения

            db_name = 'mydatabase.db3'
            table_name = 'connection_table'
            user_name = _ip # Добавить имя из запроса клиента
            _nick = _port # Добавить ник из запроса клиента
            timestamp = time.ctime(time.time())

            request_create = """ create table if not exists {} (
                                id  INTEGER primary key autoincrement,
                                name TEXT,
                                nick_name TEXT,
                               timestamp Text
                            );
                            """.format(table_name)

            request_insert = """insert into {} (name, nick_name, timestamp)
                            VALUES (?, ?, ?);""".format(table_name)

            try:
                # Пишем в базу данные о сеансе

                sql_module.make_sql_request(db_name, table_name, request_create, request_insert, user_name, _nick, timestamp)
            except:
                # Добавить обработку исключений позже - ручное прерывание оставить. Остальные пасс пока
                pass

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
                try:
                    data = jim_to_bytes.bytes_to_json(s_client.recv(1024))
                    # Если 'presence' - не отправляем всем, пишем в базу данные о сеансе
                    if data['action'] == 'presence':

                        # Вместо print реализовать запись в базу данных о сеансе
                        print(data)
                        pass
                        # добавить запись данных в базу
                    # Если не 'presence' - отправляем всем.
                    # Позже добавить в исключение autentificate и другие типы сообщений
                    elif data['action'] == 'msg':
                        print(data)

                        for read_client in w:
                            #read_client.send(b'It is Test') # Добавить расшифровку ascii
                            read_client.send(jim_to_bytes.to_bytes(data))

                except ConnectionResetError as con_err:
                    # Удаляем клиента, который отключился
                    print('Отключился пользователь %s'%(str(s_client)))
                    clients.remove(s_client)


if __name__ == "__main__":
    print('Эхо-сервер запущен!')
    mainloop()