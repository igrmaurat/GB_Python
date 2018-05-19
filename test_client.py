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
print(args)

port = int(args.port)
adress = str(args.addr)

s = socket.create_connection((adress, port))

message_to_send = json.dumps(hello_message)
s.send(message_to_send.encode('utf-8'))

# Получаем ответ сервера, размер не больше 1024 байт
data_1 = s.recv(1024)
print(data_1.decode('utf-8'))
s.close()


# Отправляем и получаем второе сообщение
# Сначала также создаем соединение

s = socket.create_connection((adress, port))
message_to_send = json.dumps(add_message)
s.send(message_to_send.encode('utf-8'))
data_2 = s.recv(1024)
print(data_2.decode('utf-8'))

s.close()