import json

# Переводим словарь в json

def to_bytes(message_dict):

    '''Переводим словарь в строку json, а потом в байты'''

    message_b = json.dumps(message_dict).encode('utf-8')
    return message_b


# Байты в словарь
def bytes_to_json(b_message):

    '''Переводим байты в строку json, а потом в словарь'''

    message_json = b_message.decode('utf-8')
    message_dict = json.loads(message_json)
    return message_dict

#Тест
# import jim_message
# message = jim_message.jim_presence
#
# print(to_bytes(message))
#
# print(bytes_to_json(to_bytes(message)))