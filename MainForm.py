import datetime
import sqlite3 as sq
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit
from ProfileForm import ProfileForm, userName

date = datetime.datetime.now()
dt = f'{date.day}.{date.month}.{date.year}'
last_date = dt

db = 'data/usersInfo.db'


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
        self.career_del_target = QPushButton(self)
        self.career_del_target.setGeometry(225, 55, 30, 30)
        self.career_del_target.setText('-')
        self.career_del_target.clicked.connect(self.del_career)

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

        with sq.connect(db) as con:
            cur = con.cursor()
            sql = """SELECT targetText, isFinished FROM targets
                        WHERE targetCat = 'Career' and userName = ?"""
            res = list(cur.execute(sql, (userName, )))
            if res[0][0] != '':
                for i in range(len(res)):
                    self.added_career_target = QLineEdit(self)
                    self.added_career_target.setGeometry(
                        200, 100 + 50 * len(self.career_targets), 200, 30)
                    self.added_career_target.show()

                    if res[i][1] == 'True':
                        self.career_targets[-1][0].setStyleSheet(
                            'background-color: #000000; color: #FFFFFF; border: none')

                    self.career_target_num = QLabel(self)
                    self.career_target_num.move(
                        185, 110 + 50 * len(self.career_targets))
                    self.career_target_num.setText(
                        f'{len(self.career_targets) + 1}.')
                    self.career_target_num.show()

                    # Завершить цель для карьеры
                    self.added_career_target_btn = QPushButton(self)
                    self.added_career_target_btn.setGeometry(
                        410, 105 + 50 * len(self.career_targets), 70, 20)

                    self.added_career_target_btn.setText('Finished!')
                    self.added_career_target_btn.clicked.connect(
                        self.finish_career)
                    self.added_career_target_btn.show()
                    self.career_targets[-1][0].setText(res[i][0])

                    self.career_targets[-1][0].setEnabled(False)
                    self.career_targets.append(
                        [self.added_career_target, self.added_career_target_btn, self.career_target_num])

        self.career_target_num = QLabel(self)
        self.career_target_num.move(185, 110)
        self.career_target_num.setText('1.')

        # --------------------------------------------------------------------------------Блок менталки
        self.mental_del_target = QPushButton(self)
        self.mental_del_target.setGeometry(640, 55, 30, 30)
        self.mental_del_target.setText('-')
        self.mental_del_target.clicked.connect(self.del_mental)

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

        with sq.connect(db) as con:
            cur = con.cursor()
            sql = """SELECT targetText, isFinished FROM targets
                        WHERE targetCat = 'Mental' and userName = ?"""
            res = list(cur.execute(sql, (userName, )))
            if res[0][0] != '':
                for i in range(len(res)):
                    self.added_mental_target = QLineEdit(self)
                    self.added_mental_target.setGeometry(
                        620, 100 + 50 * len(self.mental_targets), 200, 30)
                    self.added_mental_target.show()

                    if res[i][1] == 'True':
                        self.mental_targets[-1][0].setStyleSheet(
                            'background-color: #000000; color: #FFFFFF; border: none')

                    self.mental_target_num = QLabel(self)
                    self.mental_target_num.move(
                        605, 110 + 50 * len(self.mental_targets))
                    self.mental_target_num.setText(
                        f'{len(self.mental_targets) + 1}.')
                    self.mental_target_num.show()

                    # Завершить цель для карьеры
                    self.added_mental_target_btn = QPushButton(self)
                    self.added_mental_target_btn.setGeometry(
                        830, 105 + 50 * len(self.mental_targets), 70, 20)
                    self.added_mental_target_btn.setText('Finished!')
                    self.added_mental_target_btn.clicked.connect(
                        self.finish_mental)
                    self.added_mental_target_btn.show()
                    self.mental_targets[-1][0].setText(res[i][0])

                    self.mental_targets[-1][0].setEnabled(False)
                    self.mental_targets.append(
                        [self.added_mental_target, self.added_mental_target_btn, self.mental_target_num])

        self.mental_target_num = QLabel(self)
        self.mental_target_num.move(605, 110)
        self.mental_target_num.setText('1.')

        # --------------------------------------------------------------------------------Блок спорта
        self.sport_del_target = QPushButton(self)
        self.sport_del_target.setGeometry(1040, 55, 30, 30)
        self.sport_del_target.setText('-')
        self.sport_del_target.clicked.connect(self.del_sport)

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

        with sq.connect(db) as con:
            cur = con.cursor()
            sql = """SELECT targetText, isFinished FROM targets
                        WHERE targetCat = 'Sport' and userName = ?"""
            res = list(cur.execute(sql, (userName, )))
            if res[0][0] != '':
                for i in range(len(res)):
                    self.added_sport_target = QLineEdit(self)
                    self.added_sport_target.setGeometry(
                        1020, 100 + 50 * len(self.sport_targets), 200, 30)
                    self.added_sport_target.show()

                    if res[i][1] == 'True':
                        self.sport_targets[-1][0].setStyleSheet(
                            'background-color: #000000; color: #FFFFFF; border: none')

                    self.sport_target_num = QLabel(self)
                    self.sport_target_num.move(
                        1005, 110 + 50 * len(self.sport_targets))
                    self.sport_target_num.setText(
                        f'{len(self.sport_targets) + 1}.')
                    self.sport_target_num.show()

                    # Завершить цель для карьеры
                    self.added_sport_target_btn = QPushButton(self)
                    self.added_sport_target_btn.setGeometry(
                        1230, 105 + 50 * len(self.sport_targets), 70, 20)
                    self.added_sport_target_btn.setText('Finished!')
                    self.added_sport_target_btn.clicked.connect(
                        self.finish_sport)
                    self.added_sport_target_btn.show()
                    self.sport_targets[-1][0].setText(res[i][0])

                    self.sport_targets[-1][0].setEnabled(False)
                    self.sport_targets.append(
                        [self.added_sport_target, self.added_sport_target_btn, self.sport_target_num])


        self.sport_target_num = QLabel(self)
        self.sport_target_num.move(1005, 110)
        self.sport_target_num.setText('1.')

        # with sq.connect(db) as con:
        #     cur = con.cursor()

        #     sql = """SELECT targetID FROM targets
        #                 WHERE isFinished = 'False'"""

        #     unfinished_targets = list(cur.execute(sql))
        #     print(unfinished_targets)
    # --------------------------------------------------------------------------------ЛОГИКА

    def profile_show(self):
        self.Profile = ProfileForm()
        self.Profile.show()

    # ---------------------------------------------------------Завершить цель карьеры
    def finish_career(self):
        for i in self.career_targets:
            if i[1] == self.sender() and i[0].text() != '':
                i[0].setStyleSheet(
                    'background-color: #000000; color: #FFFFFF; border: none')

                with sq.connect(db) as con:
                    cur = con.cursor()

                    sql = """UPDATE targets
                                SET isFinished = 'True'
                                WHERE userName = ? and targetText = ? and targetCat = 'Career'"""

                    cur.execute(sql, (userName, i[0].text()))

    # ---------------------------------------------------------Завершить цель менталки
    def finish_mental(self):
        for i in self.mental_targets:
            if i[1] == self.sender() and i[0].text() != '':
                i[0].setStyleSheet(
                    'background-color: #000000; color: #FFFFFF; border: none')

                with sq.connect(db) as con:
                    cur = con.cursor()

                    sql = """UPDATE targets
                                SET isFinished = 'True'
                                WHERE userName = ? and targetText = ? and targetCat = 'Mental'"""

                    cur.execute(sql, (userName, i[0].text()))

    # ---------------------------------------------------------Завершить цель спорта
    def finish_sport(self):
        for i in self.sport_targets:
            if i[1] == self.sender() and i[0].text() != '':
                i[0].setStyleSheet(
                    'background-color: #000000; color: #FFFFFF; border: none')

                with sq.connect(db) as con:
                    cur = con.cursor()

                    sql = """UPDATE targets
                                SET isFinished = 'True'
                                WHERE userName = ? and targetText = ? and targetCat = 'Sport'"""

                    cur.execute(sql, (userName, i[0].text()))

    # ---------------------------------------------------------Добавить цель карьеры
    def add_career(self):
        if self.career_targets[-1][0].text().split() and len(self.career_targets) < 12:
            # Напечатать цель для карьеры
            self.added_career_target = QLineEdit(self)
            self.added_career_target.setGeometry(
                200, 100 + 50 * len(self.career_targets), 200, 30)
            self.added_career_target.show()

            self.career_target_num = QLabel(self)
            self.career_target_num.move(
                185, 110 + 50 * len(self.career_targets))
            self.career_target_num.setText(f'{len(self.career_targets) + 1}.')
            self.career_target_num.show()

            # Завершить цель для карьеры
            self.added_career_target_btn = QPushButton(self)
            self.added_career_target_btn.setGeometry(
                410, 105 + 50 * len(self.career_targets), 70, 20)
            self.added_career_target_btn.setText('Finished!')
            self.added_career_target_btn.clicked.connect(self.finish_career)
            self.added_career_target_btn.show()

            with sq.connect(db) as con:
                cur = con.cursor()
                if len(self.career_targets) > 1:
                    sql = """INSERT INTO targets(targetCat, targetText, userName, isFinished)
                                VALUES('Career', ?, ?, 'False')"""
                    res = cur.execute(
                        sql, (self.career_targets[-1][0].text(), userName))

                else:
                    sql = """UPDATE targets
                                SET targetText = ?
                                    WHERE targetCat = 'Career'"""
                    res = cur.execute(
                        sql, (self.career_targets[-1][0].text(), ))

                self.career_targets[-1][0].setEnabled(False)
                self.career_targets.append(
                    [self.added_career_target, self.added_career_target_btn, self.career_target_num])
                con.commit()

    # ---------------------------------------------------------Удалить цель карьеры

    def del_career(self):
        with sq.connect(db) as con:
            cur = con.cursor()

            sql = """SELECT * from targets
                        WHERE userName = ? and targetCat = ?"""

            targets = len(list(cur.execute(sql, (userName, 'Career'))))
            if targets > 1:
                sql = """DELETE from targets
                            WHERE userName = ? and targetText = ? and targetCat = ?"""

            else:
                sql = """UPDATE targets
                            SET targetText = '',
                            isFinished = 'False'
                            WHERE userName = ? and targetText = ? and targetCat = ?"""

            cur.execute(
                sql, (userName, self.career_targets[-1][0].text(), 'Career'))

            con.commit()

        if len(self.career_targets) > 1:
            for i in self.career_targets[-1]:
                i.hide()
            self.career_targets = self.career_targets[:-1]
        else:
            for i in self.career_targets[-1]:
                i.hide()
            self.career_targets = self.career_targets[:-1]

            self.career_target = QLineEdit(self)
            self.career_target.setGeometry(200, 100, 200, 30)
            self.career_target.show()

            # Завершить цель для карьеры
            self.career_target_btn = QPushButton(self)
            self.career_target_btn.setGeometry(410, 105, 70, 20)
            self.career_target_btn.setText('Finished!')
            self.career_target_btn.clicked.connect(self.finish_career)
            self.career_target_btn.show()

            self.career_target_num = QLabel(self)
            self.career_target_num.move(185, 110)
            self.career_target_num.setText('1.')
            
            self.career_targets.append([self.career_target, self.career_target_btn, self.career_target_num])

    # ---------------------------------------------------------Добавить цель менталки

    def add_mental(self):
        if self.mental_targets[-1][0].text().split() and len(self.mental_targets) < 12:
            # Напечатать цель для менталки
            self.added_mental_target = QLineEdit(self)
            self.added_mental_target.setGeometry(
                620, 100 + 50 * len(self.mental_targets), 200, 30)
            self.added_mental_target.show()

            self.mental_target_num = QLabel(self)
            self.mental_target_num.move(
                605, 110 + 50 * len(self.mental_targets))
            self.mental_target_num.setText(f'{len(self.mental_targets) + 1}.')
            self.mental_target_num.show()

            # Завершить цель для менталки
            self.added_mental_target_btn = QPushButton(self)
            self.added_mental_target_btn.setGeometry(
                830, 105 + 50 * len(self.mental_targets), 70, 20)
            self.added_mental_target_btn.setText('Finished!')
            self.added_mental_target_btn.clicked.connect(self.finish_mental)
            self.added_mental_target_btn.show()

            with sq.connect(db) as con:
                cur = con.cursor()
                if len(self.mental_targets) > 1:
                    sql = """INSERT INTO targets(targetCat, targetText, userName, isFinished)
                                VALUES('Mental', ?, ?, 'False')"""
                    res = cur.execute(
                        sql, (self.mental_targets[-1][0].text(), userName))

                else:
                    sql = """UPDATE targets
                                SET targetText = ?
                                    WHERE targetCat = 'Mental'"""
                    res = cur.execute(
                        sql, (self.mental_targets[-1][0].text(), ))

                self.mental_targets[-1][0].setEnabled(False)
                self.mental_targets.append(
                    [self.added_mental_target, self.added_mental_target_btn, self.mental_target_num])
                con.commit()

    # ---------------------------------------------------------Удалить цель менталки
    def del_mental(self):
        with sq.connect(db) as con:
            cur = con.cursor()

            sql = """SELECT * from targets
                        WHERE userName = ? and targetCat = ?"""

            targets = len(list(cur.execute(sql, (userName, 'Mental'))))
            if targets > 1:
                sql = """DELETE from targets
                            WHERE userName = ? and targetText = ? and targetCat = ?"""

            else:
                sql = """UPDATE targets
                            SET targetText = '',
                            isFinished = 'False'
                            WHERE userName = ? and targetText = ? and targetCat = ?"""

            cur.execute(
                sql, (userName, self.mental_targets[-1][0].text(), 'Mental'))

            con.commit()

        if len(self.mental_targets) > 1:
            for i in self.mental_targets[-1]:
                i.hide()
            self.mental_targets = self.mental_targets[:-1]
        else:
            for i in self.mental_targets[-1]:
                i.hide()
            self.mental_targets = self.mental_targets[:-1]

            self.mental_target = QLineEdit(self)
            self.mental_target.setGeometry(620, 100, 200, 30)
            self.mental_target.show()

            # Завершить цель для менталки
            self.mental_target_btn = QPushButton(self)
            self.mental_target_btn.setGeometry(830, 105, 70, 20)
            self.mental_target_btn.setText('Finished!')
            self.mental_target_btn.clicked.connect(self.finish_mental)
            self.mental_target_btn.show()

            self.mental_target_num = QLabel(self)
            self.mental_target_num.move(605, 110)
            self.mental_target_num.setText('1.')
            
            self.mental_targets.append([self.mental_target, self.mental_target_btn, self.mental_target_num])

    # ---------------------------------------------------------Добавить цель спорта
    def add_sport(self):
        if self.sport_targets[-1][0].text().split() and len(self.sport_targets) < 12:
            # Напечатать цель для спорта
            self.added_sport_target = QLineEdit(self)
            self.added_sport_target.setGeometry(
                1020, 100 + 50 * len(self.sport_targets), 200, 30)
            self.added_sport_target.show()

            self.sport_target_num = QLabel(self)
            self.sport_target_num.move(
                1005, 110 + 50 * len(self.sport_targets))
            self.sport_target_num.setText(f'{len(self.sport_targets) + 1}.')
            self.sport_target_num.show()

            # Завершить цель для спорта
            self.added_sport_target_btn = QPushButton(self)
            self.added_sport_target_btn.setGeometry(
                1230, 105 + 50 * len(self.sport_targets), 70, 20)
            self.added_sport_target_btn.setText('Finished!')
            self.added_sport_target_btn.clicked.connect(self.finish_sport)
            self.added_sport_target_btn.show()

            with sq.connect(db) as con:
                cur = con.cursor()
                if len(self.sport_targets) > 1:
                    sql = """INSERT INTO targets(targetCat, targetText, userName, isFinished)
                                VALUES('Sport', ?, ?, 'False')"""
                    res = cur.execute(
                        sql, (self.sport_targets[-1][0].text(), userName))

                else:
                    sql = """UPDATE targets
                                SET targetText = ?
                                    WHERE targetCat = 'Sport'"""
                    res = cur.execute(
                        sql, (self.sport_targets[-1][0].text(), ))

                self.sport_targets[-1][0].setEnabled(False)
                self.sport_targets.append(
                    [self.added_sport_target, self.added_sport_target_btn, self.sport_target_num])
                con.commit()
    # ---------------------------------------------------------Удалить цель спорта
    def del_sport(self):
        with sq.connect(db) as con:
            cur = con.cursor()

            sql = """SELECT * from targets
                        WHERE userName = ? and targetCat = ?"""

            targets = len(list(cur.execute(sql, (userName, 'Sport'))))
            if targets > 1:
                sql = """DELETE from targets
                            WHERE userName = ? and targetText = ? and targetCat = ?"""

            else:
                sql = """UPDATE targets
                            SET targetText = '',
                            isFinished = 'False'
                            WHERE userName = ? and targetText = ? and targetCat = ?"""

            cur.execute(
                sql, (userName, self.sport_targets[-1][0].text(), 'Sport'))

            con.commit()

        if len(self.sport_targets) > 1:
            for i in self.sport_targets[-1]:
                i.hide()
            self.sport_targets = self.sport_targets[:-1]
        else:
            for i in self.sport_targets[-1]:
                i.hide()
            self.sport_targets = self.sport_targets[:-1]

            self.sport_target = QLineEdit(self)
            self.sport_target.setGeometry(1020, 100, 200, 30)
            self.sport_target.show()

            # Завершить цель для менталки
            self.sport_target_btn = QPushButton(self)
            self.sport_target_btn.setGeometry(1230, 105, 70, 20)
            self.sport_target_btn.setText('Finished!')
            self.sport_target_btn.clicked.connect(self.finish_sport)
            self.sport_target_btn.show()

            self.sport_target_num = QLabel(self)
            self.sport_target_num.move(1005, 110)
            self.sport_target_num.setText('1.')
            
            self.sport_targets.append([self.sport_target, self.sport_target_btn, self.sport_target_num])

