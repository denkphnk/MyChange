from PyQt6.QtWidgets import QWidget


class ProfileForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(550, 150, 300, 400)
        self.setWindowTitle('Profile')