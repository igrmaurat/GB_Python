# import jim_message

# Подменяем имя в словаре на имя пользователя

def name_passing(message, name, text = None):
    if message['action'] == "presence":
        message['user']['account_name'] = name

    elif message['action'] == "msg":
        message["from"] = name
        message['message'] = text
    else:
        # потом добавить подмену имени в других типах сообщений
        pass

    return message

# Тест
#message = jim_message.jim_presence
#name = input('Введи имя')
#print(name_passing(message, name))