import sys
from PyQt6.QtWidgets import QApplication
from MainForm import MainForm
from AuthForm import AuthForm

db = 'usersInfo.db'


if __name__ == '__main__':

    with open('curAccount.txt', 'r') as f_in:
        data = f_in.readlines()
        app = QApplication(sys.argv)

        if data:
            mc = MainForm()
        else:
            mc = AuthForm()

        mc.show()
        sys.exit(app.exec())
