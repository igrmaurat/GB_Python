# “action”: “presence” - присутствие. Сервисное сообщение для извещения сервера о присутствии
# клиента online;
# “action”: “prоbe” - проверка присутствия. Сервисное сообщение от сервера для проверки
# присутствии клиента online;
# “action”: “msg” - простое сообщение пользователю или в чат;
# “action”: “quit” - отключение от сервера;
# “action”: “authenticate” - авторизация на сервере;
# “action”: “join” - присоединиться к чату;
# “action”: “leave” - покинуть чат.
# Протокол может быть расширен новыми методами.

import time

# Функции конвертации байтов в строки и обратно и отправки сообщения
# def message_to_bytes(_dict):
#
#     return(_bytes)
#
# def message_from_bytes(_bytes)
#     return(_dict)
#
# def send_message(_bytes, user_from, user_to):
#     pass

# Client
# При подключении отсылаем сервисное сообщение на сервер
jim_presence = {
    "action" : "presence" ,
    "time" : time.ctime(time.time()),
    "type" : "status" ,
    "user" : {
        "account_name" : "C0deMaver1ck" ,
        "status" : "Yep, I am here!"
    }
}

# Аутентификация
jim_authentificate = {
    "action": "authenticate",
    "time": time.ctime(time.time()),
    "user": {
            "account_name": "C0deMaver1ck",
            "password": "CorrectHorseBatterStaple"
            }
}

# Отключение от сервера
jim_quit = {
    "action" : "quit"
}

#Client to client message
jim_message = {
    "action" : "msg" ,
    "time" : time.ctime(time.time()),
    "to" : "account_name" ,
    "from" : "account_name" ,
    "encoding" : "ascii" ,
    "message" : "message"
}

#print(jim_aut["user"])

# Client to Chat message
jim_to_chat = {
    "action" : "msg" ,
    "time" : time.ctime(time.time()),
    "to" : "#room_name" ,
    "from" : "account_name" ,
    "message" : "Hello World"
}
jim_connect_to_chat = {
    "action" : "join" ,
    "time" : time.ctime(time.time()),
    "room" : "#room_name"
}

jim_exit_chat = {
    "action" : "leave" ,
    "time" : time.ctime(time.time()),
    "room" : "#room_name"
}

# Server

# В ответ на запрос клиента отсылаем одно из этих сообщений
jim_responce = {
    'jim_200': {
        "response" : 200 ,
        "alert" : "Необязательное сообщение/уведомление"
    },
    'jim_402':{
        "response" : 402 ,
        "error" : 'This could be " wrong password " or " no account with that name "'
    },
    'jim_409':{
    "response" : 409 ,
    "error" : "Someone is already connected with the given user name"
    }
}

# Проверка доступности клиента
jim_probe = {
    "action" : "probe" ,
    "time" : time.ctime(time.time()),
}


