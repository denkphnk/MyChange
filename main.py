import sys
from PyQt6.QtWidgets import QApplication
from AuthForm import AuthForm

db = 'data/usersInfo.db'


if __name__ == '__main__':

    with open('data/curAccount.txt', 'r') as f_in:
        data = f_in.readlines()
        app = QApplication(sys.argv)

        if data:
            from MainForm import MainForm
            mc = MainForm()
        else:
            mc = AuthForm()

        mc.show()
        sys.exit(app.exec())
