from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QInputDialog, QComboBox

rank = 'Newbie'
name = 'Daniel'
gender = 'Male'
points = 0


class ProfileForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(550, 150, 300, 400)
        self.setWindowTitle('Profile')

        # Ранг
        self.userRank = QLabel(self)
        self.userRank.move(75, 50)
        self.userRank.setStyleSheet('font: 35pt')
        self.userRank.setText(rank)

        # Очки
        self.userPoints = QLabel(self)
        self.userPoints.move(50, 150)
        self.userPoints.setStyleSheet('font: 15pt')
        self.userPoints.setText(f'Points:    {points}')

        # Имя
        self.userName = QLabel(self)
        self.userName.move(50, 200)
        self.userName.setStyleSheet('font: 15pt')
        self.userName.setText(f'Name: ')

        self.userNameEdit = QLineEdit(self)
        self.userNameEdit.setGeometry(130, 203, 150, 25)
        self.userNameEdit.setText(name)

        # Пол
        self.userGender = QLabel(self)
        self.userGender.move(50, 250)
        self.userGender.setStyleSheet('font: 15pt')
        self.userGender.setText(f'Gender: ')

        self.userGenderEdit = QComboBox(self)
        self.userGenderEdit.addItems(['Male', 'Female'])
        self.userGenderEdit.setGeometry(130, 253, 150, 25)

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
    def apply(self):
        if self.userNameEdit.text():
            print(self.userNameEdit.text())
            print(self.userGenderEdit.currentText())
            self.hide()

    def cancel(self):
        self.hide()
