from PyQt5.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem, QHBoxLayout
from PyQt5.QtGui import QColor
from PyQt5.QtCore import *

import dbtree_test
import dbnode


class DBTreeView(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.test_tree = dbtree_test.DBTreeTest()
        self.test_tree.create_test_tree()
        self.test_tree.print_tree()

        plt = self.palette()
        plt.setColor(self.backgroundRole(), QColor(200, 100, 200, 100))
        self.setPalette(plt)

        self.setAutoFillBackground(True)

        self.tree_widget = QTreeWidget()
        self.tree_widget.setColumnCount(1)
        self.tree_widget.setHeaderHidden(True)

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(self.tree_widget)

        self.setLayout(main_layout)

    def reset_tree(self):
        root_node = self.test_tree.get_root_node()
        root_item = QTreeWidgetItem([root_node.value])

        self.tree_widget.addTopLevelItem(root_item)

        self.fill_nodes(root_node, root_item)

    def fill_nodes(self, parent_node, parent_tree_item):
        if parent_node == self.test_tree.get_root_node():
            child_tree_item = parent_tree_item
        else:
            child_tree_item = QTreeWidgetItem(parent_tree_item, [parent_node.value])

        child_tree_item.setExpanded(True)

        for child in parent_node.get_children():
            self.fill_nodes(child, child_tree_item)
