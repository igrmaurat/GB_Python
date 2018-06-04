from lesson_2_server import new_listen_socket
import socket
import unittest


class TestServer(unittest.TestCase):

    def setUp(self):
        print('Я выполняюсь перед каждым тестом')
        self.func = new_listen_socket(('', 9889))

    def tearDown(self):
        print('Я выполняюсь после каждого теста')
        # очистка базы данных, файла, памяти
        try:
            self.func.close()
        except:
            pass

    def test_type(self):
        '''Создаем новое подключение.
    Проверяем что его тип socket.socket'''
        self.assertEqual(type(self.func), socket.socket)


# Запустить тестирование
if __name__ == '__main__':
    unittest.main()