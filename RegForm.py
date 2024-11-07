import sqlite3 as sq
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QComboBox, QStatusBar

db = 'data/usersInfo.db'

class RegForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(550, 150, 300, 400)
        self.setWindowTitle('Registration')

        # Имя
        self.name = QLabel(self)
        self.name.move(50, 150)
        self.name.setStyleSheet('font: 15pt')
        self.name.setText(f'Name: ')

        self.nameEdit = QLineEdit(self)
        self.nameEdit.setGeometry(130, 153, 150, 25)

        # Пол
        self.gender = QLabel(self)
        self.gender.move(50, 200)
        self.gender.setStyleSheet('font: 15pt')
        self.gender.setText(f'Gender: ')

        self.genderEdit = QComboBox(self)
        self.genderEdit.addItems(['Male', 'Female'])
        self.genderEdit.setGeometry(130, 203, 150, 25)

        # Пароль
        self.password = QLabel(self)
        self.password.move(50, 250)
        self.password.setStyleSheet('font: 15pt')
        self.password.setText(f'Password: ')

        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setGeometry(140, 253, 140, 25)

        # Кнопка сохранения
        self.applyBtn = QPushButton(self)
        self.applyBtn.setGeometry(75, 320, 150, 30)
        self.applyBtn.setStyleSheet('font: 12pt')
        self.applyBtn.setText('Apply')
        self.applyBtn.clicked.connect(self.apply)

    # Кнопка сохранения
    def apply(self):
        with sq.connect(db) as con:
            userName = self.nameEdit.text()
            userGender = self.genderEdit.currentText()
            userPassword = self.passwordEdit.text()

            # Поля не пустые
            if userName and userPassword:
                cur = con.cursor()
                sql = """SELECT * FROM users
                            WHERE userName = ?"""
                
                res = list(cur.execute(sql, (userName, )))
                
                # Есть ли такие же имена
                if len(res) == 0:
                    sql = """INSERT INTO users(userName, userGender, userPassword)
                                VALUES(?, ?, ?)"""
                    
                    cur.execute(sql, (userName, userGender, userPassword))
                    con.commit()
                    
                    with open('data/accounts.txt', 'a') as f_in:
                        f_in.write(f'{userName};{userGender}\n')

                    QApplication.quit()

                else:
                    status_bar = QStatusBar()
                    self.setStatusBar(status_bar)
                    status_bar.showMessage('Choose another name.')
                    
            else:
                status_bar = QStatusBar()
                self.setStatusBar(status_bar)
                status_bar.showMessage('Fill in all fields')

