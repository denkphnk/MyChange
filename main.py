import sys
from PyQt6.QtWidgets import QApplication
from MainForm import MainForm


app = QApplication(sys.argv)
st = MainForm()
st.show()
sys.exit(app.exec())
