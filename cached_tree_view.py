from PyQt5.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem, QHBoxLayout


class CachedTreeView(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.tree_widget = QTreeWidget()
        self.tree_widget.setColumnCount(1)
        self.tree_widget.setHeaderHidden(True)

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(self.tree_widget)

        self.setLayout(main_layout)

    def clear(self):
        self.tree_widget.clear()