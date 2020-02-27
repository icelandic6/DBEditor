from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import QObject

from db_tree_view import DBTreeView

import db_tree_test


class DBTreeController(QObject):
    def __init__(self, parent=None):
        super(QObject, self).__init__(parent)

        self.__db_tree_view = DBTreeView()
        self.__db_tree_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.db_tree = db_tree_test.DBTreeTest()

    def tree_view(self):
        return self.__db_tree_view

    def reset_tree(self):
        self.db_tree.create_test_tree()
        self.db_tree.print_tree()

        self.__db_tree_view.clear()

        root_node = self.db_tree.get_root_node()

        root_item = self.__db_tree_view.add_root_item(root_node.value)

        self.fill_nodes(root_node, root_item)

    def fill_nodes(self, parent_node, parent_item):
        if parent_node == self.db_tree.get_root_node():
            child_item = parent_item
        else:
            child_item = self.__db_tree_view.add_tree_item(parent_item, parent_node.value)

        child_item.setExpanded(True)

        for child in parent_node.get_children():
            self.fill_nodes(child, child_item)

    def selected_node(self):
        selected_item = self.__db_tree_view.selected_item()

        node = self.db_tree.find_node(selected_item[0].text(0))
        print("SELECTED ITEM:" + node.value)
