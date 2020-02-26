from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

from dbtree_view import DBTreeView
from cached_tree_view import CachedTreeView


class DBEditorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)

        self.setWindowTitle('DBEditor')

        self.resize(640, 480)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)

        self.centralWidget = QWidget(self)
        plt = self.centralWidget.palette()
        plt.setColor(self.centralWidget.backgroundRole(), QColor(100, 200, 100, 100))
        self.centralWidget.setPalette(plt)
        self.centralWidget.setAutoFillBackground(True)

        self.dbTreeView = DBTreeView()
        self.dbTreeView.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.cachedTreeView = CachedTreeView()
        self.cachedTreeView.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.loadNodeButton = QPushButton(self)
        self.loadNodeButton.setText('<<<')
        self.loadNodeButton.setFixedSize(60, 26)

        self.addNodeButton = QPushButton(self)
        self.addNodeButton.setText('+')
        self.addNodeButton.setFixedSize(26, 26)

        self.removeNodeButton = QPushButton(self)
        self.removeNodeButton.setText('-')
        self.removeNodeButton.setFixedSize(26, 26)

        self.editNodeButton = QPushButton(self)
        self.editNodeButton.setText('a')
        self.editNodeButton.setFixedSize(26, 26)

        self.applyButton = QPushButton(self)
        self.applyButton.setText('Apply')
        self.applyButton.setFixedHeight(26)
        self.applyButton.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        self.resetButton = QPushButton(self)
        self.resetButton.setText('Reset')
        self.resetButton.setFixedHeight(26)
        self.resetButton.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        self.midLayout = QVBoxLayout()
        self.midLayout.setContentsMargins(0, 50, 0, 0)
        self.midLayout.setSpacing(0)
        self.midLayout.addWidget(self.loadNodeButton, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.bottomButtonsLayout = QHBoxLayout()
        self.bottomButtonsLayout.setContentsMargins(0, 0, 0, 0)
        self.bottomButtonsLayout.setSpacing(4)
        self.bottomButtonsLayout.addWidget(self.addNodeButton)
        self.bottomButtonsLayout.addWidget(self.removeNodeButton)
        self.bottomButtonsLayout.addWidget(self.editNodeButton)
        self.bottomButtonsLayout.addStretch()
        self.bottomButtonsLayout.addWidget(self.applyButton)
        self.bottomButtonsLayout.addWidget(self.resetButton)

        self.leftLayout = QVBoxLayout()
        self.leftLayout.setContentsMargins(0, 0, 0, 0)
        self.leftLayout.setSpacing(6)
        self.leftLayout.addWidget(self.cachedTreeView)
        self.leftLayout.addLayout(self.bottomButtonsLayout)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.setContentsMargins(10, 20, 10, 20)
        self.mainLayout.setSpacing(10)
        self.mainLayout.addLayout(self.leftLayout)
        self.mainLayout.addLayout(self.midLayout)
        self.mainLayout.addWidget(self.dbTreeView)

        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)
