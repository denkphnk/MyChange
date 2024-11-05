import sys
import sqlite3 as sq
from PyQt6.QtWidgets import QApplication
from MainForm import MainForm
from RegForm import RegForm

db = 'usersInfo.db'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = MainForm()
    mc.show()
    sys.exit(app.exec())
