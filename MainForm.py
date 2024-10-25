import datetime
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit
from ProfileForm import ProfileForm

date = datetime.datetime.now()
dt = f'{date.day}.{date.month}.{date.year}'
last_date = dt

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1400, 700)
        self.setWindowTitle('MyChange')

        # Дата
        self.date_label = QLabel(self)
        self.date_label.move(692, 20)
        self.date_label.setText(dt)
        self.date_label.setStyleSheet('font: 10pt')

        # Открыть форму профиля
        self.profile_btn = QPushButton(self)
        self.profile_btn.setGeometry(10, 10, 50, 50)
        self.profile_btn.setText('Profile')
        self.profile_btn.clicked.connect(self.profile_show)

        # --------------------------------------------------------------------------------Блок карьеры
        self.career_label = QLabel(self)
        self.career_label.move(280, 60)
        self.career_label.setText('Career')
        self.career_label.setStyleSheet('font: 11pt')

        # Добавить цель для карьеры
        self.career_add_target = QPushButton(self)
        self.career_add_target.setGeometry(350, 55, 30, 30)
        self.career_add_target.setText('+')
        self.career_add_target.clicked.connect(self.add_career)

        # Напечатать цель для карьеры
        self.career_target = QLineEdit(self)
        self.career_target.setGeometry(200, 100, 200, 30)

        # Завершить цель для карьеры
        self.career_target_btn = QPushButton(self)
        self.career_target_btn.setGeometry(410, 105, 70, 20)
        self.career_target_btn.setText('Finished!')
        self.career_target_btn.clicked.connect(self.finish_career)

        # Список с целями карьеры (понадобится при добавлении новых целей)
        self.career_targets = [[self.career_target, self.career_target_btn]]

        self.career_target_num = QLabel(self)
        self.career_target_num.move(185, 110)
        self.career_target_num.setText('1.')

        # --------------------------------------------------------------------------------Блок менталки
        self.mental_label = QLabel(self)
        self.mental_label.move(700, 60)
        self.mental_label.setText('Mental')
        self.mental_label.setStyleSheet('font: 11pt')

        # Добавить цель для менталки
        self.mental_add_target = QPushButton(self)
        self.mental_add_target.setGeometry(770, 55, 30, 30)
        self.mental_add_target.setText('+')
        self.mental_add_target.clicked.connect(self.add_mental)

        # Напечатать цель для менталки
        self.mental_target = QLineEdit(self)
        self.mental_target.setGeometry(620, 100, 200, 30)

        # Завершить цель для менталки
        self.mental_target_btn = QPushButton(self)
        self.mental_target_btn.setGeometry(830, 105, 70, 20)
        self.mental_target_btn.setText('Finished!')
        self.mental_target_btn.clicked.connect(self.finish_mental)

        # Список с целями менталки (понадобится при добавлении новых целей)
        self.mental_targets = [[self.mental_target, self.mental_target_btn]]

        self.mental_target_num = QLabel(self)
        self.mental_target_num.move(605, 110)
        self.mental_target_num.setText('1.')

        # --------------------------------------------------------------------------------Блок спорта
        self.sport_label = QLabel(self)
        self.sport_label.move(1100, 60)
        self.sport_label.setText('Sport')
        self.sport_label.setStyleSheet('font: 11pt')

        # Добавить цель для спорта
        self.sport_add_target = QPushButton(self)
        self.sport_add_target.setGeometry(1170, 55, 30, 30)
        self.sport_add_target.setText('+')
        self.sport_add_target.clicked.connect(self.add_sport)

        # Напечатать цель для спорта
        self.sport_target = QLineEdit(self)
        self.sport_target.setGeometry(1020, 100, 200, 30)

        # Завершить цель для спорта
        self.sport_target_btn = QPushButton(self)
        self.sport_target_btn.setGeometry(1230, 105, 70, 20)
        self.sport_target_btn.setText('Finished!')
        self.sport_target_btn.clicked.connect(self.finish_sport)

        # Список с целями спорта (понадобится при добавлении новых целей)
        self.sport_targets = [[self.sport_target, self.sport_target_btn]]

        self.sport_target_num = QLabel(self)
        self.sport_target_num.move(1005, 110)
        self.sport_target_num.setText('1.')

    # --------------------------------------------------------------------------------ЛОГИКА

    def profile_show(self):
        self.Profile = ProfileForm()
        self.Profile.show()

    # ---------------------------------------------------------Завершить цель карьеры
    def finish_career(self):
        for i in self.career_targets:
            if i[1] == self.sender() and i[0].text() != '':
                i[0].setEnabled(False)

    # ---------------------------------------------------------Завершить цель менталки
    def finish_mental(self):
        for i in self.mental_targets:
            if i[1] == self.sender() and i[0].text() != '':
                i[0].setEnabled(False)

    # ---------------------------------------------------------Завершить цель спорта
    def finish_sport(self):
        for i in self.sport_targets:
            if i[1] == self.sender() and i[0].text() != '':
                i[0].setEnabled(False)

    # ---------------------------------------------------------Добавить цель карьеры
    def add_career(self):
        if self.career_targets[-1][0].text().split():
            # Напечатать цель для карьеры
            self.added_career_target = QLineEdit(self)
            self.added_career_target.setGeometry(200, 100 + 50 * len(self.career_targets), 200, 30)
            self.added_career_target.show()

            self.career_target_num = QLabel(self)
            self.career_target_num.move(185, 110 + 50 * len(self.career_targets))
            self.career_target_num.setText(f'{len(self.career_targets) + 1}.')
            self.career_target_num.show()

            # Завершить цель для карьеры
            self.added_career_target_btn = QPushButton(self)
            self.added_career_target_btn.setGeometry(410, 105 + 50 * len(self.career_targets), 70, 20)
            self.added_career_target_btn.setText('Finished!')
            self.added_career_target_btn.clicked.connect(self.finish_career)
            self.added_career_target_btn.show()

            self.career_targets.append([self.added_career_target, self.added_career_target_btn])

    # ---------------------------------------------------------Добавить цель менталки
    def add_mental(self):
        if self.mental_targets[-1][0].text().split():
            # Напечатать цель для менталки
            self.added_mental_target = QLineEdit(self)
            self.added_mental_target.setGeometry(620, 100 + 50 * len(self.mental_targets), 200, 30)
            self.added_mental_target.show()

            self.mental_target_num = QLabel(self)
            self.mental_target_num.move(605, 110 + 50 * len(self.mental_targets))
            self.mental_target_num.setText(f'{len(self.mental_targets) + 1}.')
            self.mental_target_num.show()

            # Завершить цель для менталки
            self.added_mental_target_btn = QPushButton(self)
            self.added_mental_target_btn.setGeometry(830, 105 + 50 * len(self.mental_targets), 70, 20)
            self.added_mental_target_btn.setText('Finished!')
            self.added_mental_target_btn.clicked.connect(self.finish_mental)
            self.added_mental_target_btn.show()

            self.mental_targets.append([self.added_mental_target, self.added_mental_target_btn])

    # ---------------------------------------------------------Добавить цель спорта
    def add_sport(self):
        if self.sport_targets[-1][0].text().split():
            # Напечатать цель для спорта
            self.added_sport_target = QLineEdit(self)
            self.added_sport_target.setGeometry(1020, 100 + 50 * len(self.sport_targets), 200, 30)
            self.added_sport_target.show()

            self.sport_target_num = QLabel(self)
            self.sport_target_num.move(1005, 110 + 50 * len(self.sport_targets))
            self.sport_target_num.setText(f'{len(self.sport_targets) + 1}.')
            self.sport_target_num.show()

            # Завершить цель для спорта
            self.added_sport_target_btn = QPushButton(self)
            self.added_sport_target_btn.setGeometry(1230, 105 + 50 * len(self.sport_targets), 70, 20)
            self.added_sport_target_btn.setText('Finished!')
            self.added_sport_target_btn.clicked.connect(self.finish_sport)
            self.added_sport_target_btn.show()

            self.sport_targets.append([self.added_sport_target, self.added_sport_target_btn])
