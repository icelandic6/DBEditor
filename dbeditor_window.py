from PyQt5.QtWidgets import *

class DBEditorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)

        self.setWindowTitle('DBEditor')
