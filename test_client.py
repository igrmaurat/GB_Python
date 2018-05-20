#python test_client.py

import socket
import json
import time
import argparse

# парсим командную строку
# в зависимости от аргумента - формируем сообщение

hello_message = {
"action": "presence",
"time": time.time(),
"type": "status",
"user": {
"account_name": "C0deMaver1ck",
"status": "Yep, I am here!"
    }
}

add_message = {
    'action': 'add',
    'name': 'Max'
}

message_message = {
    'action': 'msg',
    'who': 'Max',
    'text': 'Hello Max'
}


parser = argparse.ArgumentParser()
parser.add_argument("--port", default=7777, help="Это порт")
parser.add_argument("--addr", default='', help="Это адрес сервера" )


args = parser.parse_args()

port = int(args.port)
adress = str(args.addr)

s = socket.create_connection((adress, port))

message_to_send = json.dumps(hello_message)
s.send(message_to_send.encode('utf-8'))

# Получаем ответ сервера, размер не больше 1024 байт
data_from_server = s.recv(1024).decode('utf-8')
data_from_server = json.loads(data_from_server)
print(data_from_server)

# Если ответ 200 - то отправляем следующее сообщение
if data_from_server['response'] == 200:
    print('Можно отправлять следующее сообщение')

    s.close()

else:
    # Потом добавить сюда разные реакции на разные ответы сервера
    pass

# Отправляем и получаем второе сообщение
# Сначала также создаем соединение

s = socket.create_connection((adress, port))
message_to_send = json.dumps(add_message)
s.send(message_to_send.encode('utf-8'))
data_2 = s.recv(1024)
print(data_2.decode('utf-8'))

s.close()