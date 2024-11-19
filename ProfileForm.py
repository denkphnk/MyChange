from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox
from PyQt6.QtGui import QPixmap
import sqlite3 as sq
from datetime import datetime as dt

db = 'data/usersInfo.db'

with open('data/last_date.txt', 'r+', encoding='utf8') as f_in:
    data = f_in.readlines()
    date_now_str = str(dt.now().date())
    if not data:
        f_in.write(date_now_str)
        flag = False
    else:
        date_now = list(map(int, str(dt.now().date()).split('-')))
        data = list(map(int, data[0].split('-')))

        flag = all([data[i] == date_now[i] for i in range(3)])
        f_in.seek(0)
        f_in.write(date_now_str)
        


with open('data/curAccount.txt', 'r') as f_in:

    data = f_in.readlines()
    if data:
        data = data[0].split(';')
        userName = data[0]
        userGender = data[1]
    
with sq.connect(db) as con:
    cur = con.cursor()

    # Завершенные цели
    sql = """SELECT * FROM targets
                WHERE isFinished = 'False' and targetText <> ''"""
    unfinished = list(cur.execute(sql))
    sql = """SELECT * FROM targets
                WHERE targetText <> ''"""
    allTargets = list(cur.execute(sql))
    allFinished = not bool(unfinished)

    # Обнуление завершенности
    if not flag:
        sql = """UPDATE targets
                    SET isFinished = 'False'"""
        cur.execute(sql)

        con.commit()


if len(allTargets) == len(unfinished):
    rank = -1
if len(allTargets) > len(unfinished):
    rank = 0
if len(unfinished) == 0:
    rank = 1
image = 'images/' + str(rank) + '.jpg'


class ProfileForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(550, 150, 300, 400)
        self.setWindowTitle('Profile')

        # Смена аккаунта
        self.switchBtn = QPushButton(self)
        self.switchBtn.move(110, 20)
        self.switchBtn.setText('Log out')
        self.switchBtn.clicked.connect(self.logOut)

        # Ранг
        self.pixmap = QPixmap(image)

        self.userRank = QLabel(self)
        self.userRank.setGeometry(90, 50, 120, 120)
        self.userRank.setPixmap(self.pixmap)

        # Очки
        # self.userPoints = QLabel(self)
        # self.userPoints.move(50, 150)
        # self.userPoints.setStyleSheet('font: 15pt')
        # self.userPoints.setText(f'Points:    {points}')

        # Имя
        self.userName = QLabel(self)
        self.userName.move(50, 200)
        self.userName.setStyleSheet('font: 15pt')
        self.userName.setText(f'Name: ')

        self.userNameEdit = QLineEdit(self)
        self.userNameEdit.setGeometry(130, 203, 150, 25)
        self.userNameEdit.setText(userName)


        # Пол
        self.userGender = QLabel(self)
        self.userGender.move(50, 250)
        self.userGender.setStyleSheet('font: 15pt')
        self.userGender.setText(f'Gender: ')

        self.userGenderEdit = QComboBox(self)
        self.userGenderEdit.addItems(['Male', 'Female'])
        self.userGenderEdit.setGeometry(130, 253, 150, 25)
        self.userGenderEdit.setCurrentIndex(['Male', 'Female'].index(userGender))

        # Кнопка сохранения
        self.applyBtn = QPushButton(self)
        self.applyBtn.setGeometry(75, 320, 150, 30)
        self.applyBtn.setStyleSheet('font: 12pt')
        self.applyBtn.setText('Apply')
        self.applyBtn.clicked.connect(self.apply)

        # Кнопка отмены
        self.cancelBtn = QPushButton(self)
        self.cancelBtn.setGeometry(120, 360, 60, 20)
        self.cancelBtn.setText('Cancel')
        self.cancelBtn.clicked.connect(self.cancel)

    # ------------------------------------------------------------------ЛОГИКА
    def logOut(self):
        with open('data/curAccount.txt', 'w') as f_in:
            f_in.write('')
            QApplication.quit()

    def apply(self):
        if self.userNameEdit.text():
            print(self.userNameEdit.text())
            print(self.userGenderEdit.currentText())
            self.hide()

    def cancel(self):
        self.hide()
