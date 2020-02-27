from PyQt5.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem, QHBoxLayout

import db_tree_test


class DBTreeView(QWidget):
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

    def add_root_item(self, value):
        root_item = QTreeWidgetItem([value])
        root_item.setExpanded(True)

        self.tree_widget.addTopLevelItem(root_item)

        return root_item

    @staticmethod
    def add_tree_item(parent_item, value):
        child_item = QTreeWidgetItem(parent_item, [value])
        return child_item

    def clear(self):
        self.tree_widget.clear()

    def selected_item(self):
        return self.tree_widget.selectedItems()
