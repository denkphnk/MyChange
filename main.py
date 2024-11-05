import sys
import sqlite3 as sq
from PyQt6.QtWidgets import QApplication
from AuthForm import AuthForm

db = 'usersInfo.db'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = AuthForm()
    mc.show()
    sys.exit(app.exec())
