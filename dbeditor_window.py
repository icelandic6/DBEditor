from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor

class DBEditorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)

        self.setWindowTitle('DBEditor')

        self.resize(640, 480)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.centralWidget = QWidget(self)
        plt = self.centralWidget.palette()
        plt.setColor(self.centralWidget.backgroundRole(), QColor(100, 200, 100, 100))
        self.centralWidget.setPalette(plt)
        self.centralWidget.setAutoFillBackground(True)

        self.testWidget = QWidget(self.centralWidget)
        self.testWidget.setAutoFillBackground(True)
        self.testWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        plt = self.testWidget.palette()
        plt.setColor(self.centralWidget.backgroundRole(), QColor(100, 100, 200))
        self.testWidget.setPalette(plt)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.addWidget(self.testWidget)
        self.centralWidget.setLayout(self.horizontalLayout)
        self.setCentralWidget(self.centralWidget)
