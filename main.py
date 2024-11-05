import sys
from PyQt6.QtWidgets import QApplication
from MainForm import MainForm

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mc = MainForm()
    mc.show()
    sys.exit(app.exec())
