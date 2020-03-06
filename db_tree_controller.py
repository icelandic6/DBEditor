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

        for index in self.data_base.dict.keys():
            self.__add_tree_item(self.data_base.dict[index])

        self.__db_tree_view.expand_all()

    def __add_tree_item(self, node):
        self.__db_tree_view.add_item(node.node_id,
                                     node.parent_id,
                                     node.value)

    def selected_item(self):
        selected_id = self.__db_tree_view.selected_item_id()

        if selected_id is None:
            return None, None

        for key, value in self.data_base.dict.items():
            if value.node_id == selected_id:
                selected_node_index = key
                break

        return selected_node_index, self.data_base.get_node_by_index(selected_node_index)

    def get_node_by_index(self, index):
        return self.data_base.get_node_by_index(index)
