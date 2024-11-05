import sqlite3 as sq
import os
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QComboBox, QStatusBar



db = 'usersInfo.db'

class RegForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(550, 150, 300, 400)
        self.setWindowTitle('Registration')

        # Имя
        self.name = QLabel(self)
        self.name.move(50, 50)
        self.name.setStyleSheet('font: 15pt')
        self.name.setText(f'Name: ')

        self.nameEdit = QLineEdit(self)
        self.nameEdit.setGeometry(130, 53, 150, 25)

        # Пол
        self.gender = QLabel(self)
        self.gender.move(50, 100)
        self.gender.setStyleSheet('font: 15pt')
        self.gender.setText(f'Gender: ')

        self.genderEdit = QComboBox(self)
        self.genderEdit.addItems(['Male', 'Female'])
        self.genderEdit.setGeometry(130, 103, 150, 25)

        # Пароль
        self.password = QLabel(self)
        self.password.move(50, 150)
        self.password.setStyleSheet('font: 15pt')
        self.password.setText(f'Password: ')

        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setGeometry(140, 153, 140, 25)

        # Кнопка сохранения
        self.applyBtn = QPushButton(self)
        self.applyBtn.setGeometry(75, 320, 150, 30)
        self.applyBtn.setStyleSheet('font: 12pt')
        self.applyBtn.setText('Apply')
        self.applyBtn.clicked.connect(self.apply)

    def apply(self):
        with sq.connect(db) as con:
            userName = self.nameEdit.text()
            userGender = self.genderEdit.currentText()
            userPassword = self.passwordEdit.text()

            if userName and userGender and userPassword:
                cur = con.cursor()
                sql = """SELECT * FROM users
                            WHERE userName = ?"""
                
                cur.execute(sql, (userName, ))

                if len(list(cur)) == 0:
                    sql = """INSERT INTO users(userName, userGender, userPassword)
                                VALUES(?, ?, ?)"""
                    
                    cur.execute(sql, (userName, userGender, userPassword))
                    con.commit()
                    self.hide()

                    with open('accounts.txt', 'a') as data:
                        data.write(f'{userName}\n')


                else:
                    status_bar = QStatusBar()
                    self.setStatusBar(status_bar)
                    status_bar.showMessage('Choose another name.')
                    
            else:
                status_bar = QStatusBar()
                self.setStatusBar(status_bar)
                status_bar.showMessage('Fill in all fields')
            