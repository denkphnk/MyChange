from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox
import sqlite3 as sq

db = 'data/usersInfo.db'

with open('data/curAccount.txt', 'r') as f_in:

    data = f_in.readlines()
    if data:
        data = data[0].split(';')
        userName = data[0]
        userGender = data[1]
    
with sq.connect(db) as con:
    cur = con.cursor()

    sql = """SELECT * FROM targets
                WHERE isFinished = 'False' and targetText <> ''"""
    unfinished = list(cur.execute(sql))

    sql = """SELECT * FROM targets
                WHERE targetText <> ''"""
    allTargets = list(cur.execute(sql))
    
    allFinished = not bool(unfinished)

if len(allTargets) == len(unfinished):
    rank = -1
if len(allTargets) > len(unfinished):
    rank = 0
if len(unfinished) == 0:
    rank = 1

print(rank)


class ProfileForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(550, 150, 300, 400)
        self.setWindowTitle('Profile')

        # Смена аккаунта
        self.switchBtn = QPushButton(self)
        self.switchBtn.move(105, 20)
        self.switchBtn.setText('Log out')
        self.switchBtn.clicked.connect(self.logOut)

        # Ранг
        self.userRank = QLabel(self)
        self.userRank.move(75, 50)
        self.userRank.setStyleSheet('font: 35pt')
        self.userRank.setText(str(rank))

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
