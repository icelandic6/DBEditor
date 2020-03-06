from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import QObject

from ui.db_tree_view import DBTreeView
from test_trees.test_data_base import TestDataBase


class DBTreeController(QObject):
    def __init__(self, parent=None):
        super(DBTreeController, self).__init__(parent)

        self.data_base = TestDataBase()

        self.__db_tree_view = DBTreeView()
        self.__db_tree_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def tree_view(self):
        return self.__db_tree_view

    def reset(self):
        self.data_base.dict.clear()
        self.data_base.create_test_data_base()

        self.__update_tree_view()

    def __update_tree_view(self):
        self.__db_tree_view.clear()

        for node_id, node in self.data_base.dict.items():
            self.__add_tree_item(node_id, node)

        self.__db_tree_view.expand_all()

    def __add_tree_item(self, node_id, node):
        self.__db_tree_view.add_item(node_id,
                                     node.parent_id,
                                     node.value)

    def selected_item(self):
        selected_id = self.__db_tree_view.selected_item_id()

        if selected_id is None:
            return None, None

        return selected_id, self.data_base.get_node_by_index(selected_id)

    def get_node_by_index(self, index):
        return self.data_base.get_node_by_index(index)
