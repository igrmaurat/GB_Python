# python test_server.py

import socket
import json
import time
import argparse

# Здесь вставить сообщения сервера

probe = {
"action": "probe",
"time": time.time(),
}

quit = {
"action": "quit"
}

# Здесь задаем параметры командной строки и парсим их
parser = argparse.ArgumentParser()
parser.add_argument("-p", help="Это порт")
parser.add_argument("-a", help="Это адрес для прослушивания", type=str)

args = parser.parse_args()

# Так можно задать значения по умолчанию, если аргументы командной строки именованные -v, --addr и т.п.
try:
    port = int(args.p)
except:
    port = 7777

if args.a:
    adress = str(args.a)
else:
    adress = ''

print('adress = {}'.format(adress))
print('port = {}'.format(port))

# Создаем сокет TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((adress, port))                # Присваивает адрес и порт

s.listen(5)

while True:
    client, addr = s.accept()  # Принять запрос на соединение

    print("Получен запрос на соединение от %s" % str(addr))
    data_from_client = client.recv(1024).decode('utf-8')
    data_from_client = json.loads(data_from_client)
    print(data_from_client)

# Проверяем какое это сообщение
    if data_from_client['action'] == 'presence':
        data_to_send = 'Привет, %s'%(data_from_client['user']['account_name'])

    elif data_from_client['action'] == 'add':
        data_to_send = 'Привет, %s'%(data_from_client['name'])


    # Обратите внимание, дальнейшая работа ведётся с сокетом клиента
    # <- По сети должны передаваться байты, поэтому выполняется кодирование строки
    client.send(data_to_send.encode('utf-8'))

# Получаем второе сообщение от клиента
    #client, addr = s.accept()
    #data_from_client = client.recv(1024)
    #print(data_from_client.decode('utf-8'))
    #if 'Пока' in data_from_client.decode('utf-8'):
    #client.send('Пока, друг'.encode('utf-8'))

    # Закрываем соединение
    #client.close()
client.close()

