from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import QObject

from cached_tree_view import CachedTreeView
from data_base import DataBase


class CachedTreeController(QObject):
    def __init__(self, parent=None):
        super(CachedTreeController, self).__init__(parent)

        self.cached_data_base = DataBase()

        self.__cached_tree_view = CachedTreeView()
        self.__cached_tree_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def tree_view(self):
        return self.__cached_tree_view

    def reset(self):
        self.cached_data_base.dict.clear()
        self.__cached_tree_view.clear()

    def add_node(self, node):
        if node.node_id in self.cached_data_base.dict:
            return

        self.cached_data_base.dict[node.node_id] = node

        self.update_tree_view()

    def update_tree_view(self):
        self.__cached_tree_view.clear()

        for index in sorted(self.cached_data_base.dict.keys()):
            self.__add_tree_item(self.cached_data_base.dict[index])

        self.__cached_tree_view.expand_all()

    def __add_tree_item(self, node):
        self.__cached_tree_view.add_item(node.node_id,
                                         node.parent_id,
                                         node.value)
