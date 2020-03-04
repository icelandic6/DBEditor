from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

from cached_tree_controller import CachedTreeController
from db_tree_controller import DBTreeController


class DBEditorWindow(QMainWindow):
    def __init__(self, parent=None):
        super(DBEditorWindow, self).__init__(parent)

        self.setWindowTitle('DBEditor')

        self.resize(640, 480)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)

        self.central_widget = QWidget(self)
        plt = self.central_widget.palette()
        plt.setColor(self.central_widget.backgroundRole(), QColor(100, 150, 200, 100))
        self.central_widget.setPalette(plt)
        self.central_widget.setAutoFillBackground(True)

        self.db_tree_controller = DBTreeController()
        self.db_tree_controller.reset()

        self.cached_tree_controller = CachedTreeController()
        self.cached_tree_controller.reset_tree()

        self.load_to_cache_button = QPushButton(self)
        self.load_to_cache_button.setText('<<<')
        self.load_to_cache_button.setFixedSize(60, 26)

        self.add_node_button = QPushButton(self)
        self.add_node_button.setText('+')
        self.add_node_button.setFixedSize(26, 26)

        self.remove_node_button = QPushButton(self)
        self.remove_node_button.setText('-')
        self.remove_node_button.setFixedSize(26, 26)

        self.edit_node_button = QPushButton(self)
        self.edit_node_button.setText('a')
        self.edit_node_button.setFixedSize(26, 26)

        self.apply_button = QPushButton(self)
        self.apply_button.setText('Apply')
        self.apply_button.setFixedHeight(26)
        self.apply_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        self.reset_button = QPushButton(self)
        self.reset_button.setText('Reset')
        self.reset_button.setFixedHeight(26)
        self.reset_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        self.mid_layout = QVBoxLayout()
        self.mid_layout.setContentsMargins(0, 50, 0, 0)
        self.mid_layout.setSpacing(0)
        self.mid_layout.addWidget(self.load_to_cache_button, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.bottom_buttons_layout = QHBoxLayout()
        self.bottom_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.bottom_buttons_layout.setSpacing(4)
        self.bottom_buttons_layout.addWidget(self.add_node_button)
        self.bottom_buttons_layout.addWidget(self.remove_node_button)
        self.bottom_buttons_layout.addWidget(self.edit_node_button)
        self.bottom_buttons_layout.addStretch()
        self.bottom_buttons_layout.addWidget(self.apply_button)
        self.bottom_buttons_layout.addWidget(self.reset_button)

        self.left_layout = QVBoxLayout()
        self.left_layout.setContentsMargins(0, 0, 0, 0)
        self.left_layout.setSpacing(6)
        self.left_layout.addWidget(self.cached_tree_controller.tree_view())
        self.left_layout.addLayout(self.bottom_buttons_layout)

        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(10, 20, 10, 20)
        self.main_layout.setSpacing(10)
        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addLayout(self.mid_layout)
        self.main_layout.addWidget(self.db_tree_controller.tree_view())

        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

        self.load_to_cache_button.clicked.connect(self.load_to_cache_button_clicked)
        self.reset_button.clicked.connect(self.reset_button_clicked)

    def load_to_cache_button_clicked(self):
        node = self.db_tree_controller.selected_node()

        if node is not None:
            self.cached_tree_controller.add_node(node)

    def reset_button_clicked(self):
        self.db_tree_controller.reset()
