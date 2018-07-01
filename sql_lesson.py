import sqlite3

with sqlite3.connect('mydatabase.db3') as conn:

    # Создаем курсор - это специальный объект который делает запросы и получает их результаты
    cursor = conn.cursor()

    # Создание таблицы
    cursor.execute("""
                        create table if not exists Contacts (
                            id  INTEGER primary key autoincrement,
                            name TEXT,
                            nick_name TEXT
                        );
            """)

    with open('contact_list.txt', 'r', encoding='utf-8') as file:
        c_list = (file.read().split('\n'))
        print(c_list)

        for _line in c_list:
            _name, _nick =_line.split(',')

            print('имя {}... кличка {}'.format(_name, _nick))
            #print('имя {}... кличка {}'.format(_name, _nick))


            cursor.execute("""insert into Contacts (name, nick_name)
                            VALUES (?, ?);""",
               (_name, _nick))

        cursor.execute('SELECT * FROM Contacts')
        results = cursor.fetchall()

        print(results)