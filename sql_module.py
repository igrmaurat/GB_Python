# Здесь будет весь код для работы с базой
import sqlite3
import time

# with sqlite3.connect('mydatabase.db3') as conn:
#
#     # Создаем курсор - это специальный объект который делает запросы и получает их результаты
#     cursor = conn.cursor()
#
#     # Создание таблицы
#     cursor.execute("""
#                         create table if not exists Contacts (
#                             id  INTEGER primary key autoincrement,
#                             name TEXT,
#                             nick_name TEXT
#                         );
#             """)
#
#     with open('contact_list.txt', 'r', encoding='utf-8') as file:
#         c_list = (file.read().split('\n'))
#         print(c_list)
#
#         for _line in c_list:
#             _name, _nick =_line.split(',')
#
#             print('имя {}... кличка {}'.format(_name, _nick))
#             #print('имя {}... кличка {}'.format(_name, _nick))
#
#
#             cursor.execute("""insert into Contacts (name, nick_name)
#                             VALUES (?, ?);""",
#                (_name, _nick))
#
#         cursor.execute('SELECT * FROM Contacts')
#         # Получаем результат от запроса к базе
#         results = cursor.fetchall()
#
#         print(results)


# Создание таблицы - лучше запрос сделать парамтером функции. Возможно объединить с функцией ниже



def make_sql_request(db_name, table_name, request_create, request_insert, user_name, _nick, timestamp):

    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(request_create)
        cursor.execute(request_insert, (user_name, _nick, timestamp))

        cursor.execute('SELECT * FROM {}'.format(table_name))
        # Получаем результат от запроса к базе
        results = cursor.fetchall()
        print(results)


# # Test
# db_name = 'mydatabase.db3'
#
# table_name = 'connection_table'
# user_name = 'Vasya'
# _nick = 'vas321'
# timestamp = time.ctime(time.time())
#
# request_create = """ create table if not exists {} (
#                     id  INTEGER primary key autoincrement,
#                     name TEXT,
#                     nick_name TEXT,
#                    timestamp Text
#                 );
#                 """.format(table_name)
#
#
# request_insert = """insert into {} (name, nick_name, timestamp)
#                 VALUES (?, ?, ?);""".format(table_name)
#
# make_sql_request(db_name, table_name, request_create, request_insert, user_name, _nick, timestamp)

