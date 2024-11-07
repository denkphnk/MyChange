import sqlite3 as sq
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QStatusBar
from RegForm import RegForm


db = 'data/usersInfo.db'


class AuthForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(550, 150, 300, 400)
        self.setWindowTitle('Authorization')

        # Имя
        self.name = QLabel(self)
        self.name.move(50, 150)
        self.name.setStyleSheet('font: 15pt')
        self.name.setText(f'Name: ')

        self.nameEdit = QLineEdit(self)
        self.nameEdit.setGeometry(130, 153, 150, 25)

        # Пароль
        self.password = QLabel(self)
        self.password.move(50, 200)
        self.password.setStyleSheet('font: 15pt')
        self.password.setText(f'Password: ')

        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setGeometry(140, 203, 140, 25)

        # Кнопка входа
        self.enterBtn = QPushButton(self)
        self.enterBtn.setGeometry(75, 320, 150, 30)
        self.enterBtn.setStyleSheet('font: 12pt')
        self.enterBtn.setText('Enter')
        self.enterBtn.clicked.connect(self.enter)

        # Перейти к регистрации
        self.switchBtn = QPushButton(self)
        self.switchBtn.move(100, 50)
        self.switchBtn.setText('Switch to reg')
        self.switchBtn.clicked.connect(self.switch)

    def enter(self):
        with sq.connect(db) as con:
            global userName, userPassword
            userName = self.nameEdit.text()
            userPassword = self.passwordEdit.text()

            if userName and userPassword:
                cur = con.cursor()

                sql = """SELECT * FROM users
                            WHERE userName = ? and userPassword = ?"""

                res = list(cur.execute(sql, (userName, userPassword)))

                if res:
                    with open('data/curAccount.txt', 'w') as f_in:
                        f_in.write(f'{res[0][1]};{res[0][2]}')
                        QApplication.quit()
                else:
                    status_bar = QStatusBar()
                    self.setStatusBar(status_bar)
                    status_bar.showMessage('Wrong name or password')
            else:
                status_bar = QStatusBar()
                self.setStatusBar(status_bar)
                status_bar.showMessage('Fill in all fields')
  
    def switch(self):
        self.hide()
        self.af = RegForm()
        self.af.show()

