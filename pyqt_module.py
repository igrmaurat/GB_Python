import sys
from PyQt5 import QtWidgets, uic
import sql_module
import time

#if __name__ == '__main__':

# Обязательно нужно создать объект-приложение
app = QtWidgets.QApplication(sys.argv)  # [2]

# Виджет основного окна приложения и его настройка
window = uic.loadUi('messenger.ui')  # [3]
#print(window.textBrowser)

window.show()  # [7]
# Обработчик событий
def my_f():
    print('click on button')

#window.pushButton.clicked.connect(my_f)


# Запись истории в виджет HistoryListWidget
def load_history(text_message = None):
    #window.HistoryListWidget.clear()
    window.HistoryListWidget.addItem(text_message)

# Определяем виджет для ввода текста
text_edit_widget = window.plainTextEdit

# Почему-то не получилось передать в сообщение это в виде переменной
#text_message = text_edit_widget.document().toPlainText()

db_name = 'mydatabase.db3'

# Дописать присваивание имени и ника
user_name = 'Vasya'
_nick = 'vas321'
timestamp = time.ctime(time.time())

# Пишем сообщение в базу
window.pushButton.clicked.connect(lambda: sql_module.sql_history_message(db_name, user_name = user_name, _nick = _nick,
                                                                         timestamp = timestamp, text_message = text_edit_widget.document().toPlainText()))

# Вывод отправленного сообщения в верхний виджет window.HistoryListWidget при отправке сообщения
window.pushButton.clicked.connect(lambda: load_history(text_edit_widget.document().toPlainText()))

# Очищаем поле ввода при отправке сообщения
window.pushButton.clicked.connect(lambda: text_edit_widget.clear())


# Авторизация - получить данные из полей login и password по нажатию кнопки
login_widget = window.lineEdit
password_widget = window.lineEdit_2

#Пока вывод данных в консоль - добавить проверку подлинности данных
# Сравнивать с записью в базе в таблице passwords_table
# Также добавить регистрацию. Кнопка регистрация, поля логин и пароль, запись в базу в таблицу passwords_table
window.pushButton_2.clicked.connect(lambda: print('login: {}, password: {}'.format(login_widget.text(), (password_widget.text()))))

window.pushButton_2.clicked.connect(lambda: login_widget.clear())
window.pushButton_2.clicked.connect(lambda: password_widget.clear())


# Запустить приложение (цикл опроса событий)
sys.exit(app.exec_())



