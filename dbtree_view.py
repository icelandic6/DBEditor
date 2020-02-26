from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QColor


class DBTreeView(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        plt = self.palette()
        plt.setColor(self.backgroundRole(), QColor(200, 100, 200, 100))
        self.setPalette(plt)

        self.setAutoFillBackground(True)