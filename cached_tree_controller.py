from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import QObject

from ui.cached_tree_view import CachedTreeView
from data_base import DataBase
from db_node import DBNode


class CachedTreeController(QObject):
    def __init__(self, parent=None):
        super(CachedTreeController, self).__init__(parent)

        self.cached_data_base = DataBase()

        self.__cached_tree_view = CachedTreeView()
        self.__cached_tree_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.__cache_items_index = 0

    def tree_view(self):
        return self.__cached_tree_view

    def reset(self):
        self.cached_data_base.dict.clear()
        self.__cached_tree_view.clear()

    def has_item_with_id(self, node_id):
        for index in self.cached_data_base.dict.keys():
            if self.cached_data_base.dict[index].node_id == node_id:
                return True

        return False

    def add_item(self, item):
        if self.has_item_with_id(item.node_id):
            return None

        new_item_index = self.__cache_items_index
        self.cached_data_base.dict[new_item_index] = item

        self.__cache_items_index += 1

        self.__update_tree_view()
        return new_item_index

    def __update_tree_view(self):
        self.__cached_tree_view.clear()

        for index, v in sorted(self.cached_data_base.dict.items(), key=lambda item: item[1].node_id):
            self.__add_tree_item(self.cached_data_base.dict[index])

        self.__cached_tree_view.expand_all()

    def __add_tree_item(self, node):
        self.__cached_tree_view.add_item(node.node_id,
                                         node.parent_id,
                                         node.value)

    def __create_new_node_for_selection(self):
        selected_node = self.selected_node()

        if selected_node is None:
            return

        new_node = DBNode()
        new_node.node_id

    def selected_node(self):
        selected_id = self.__cached_tree_view.selected_item_id()

        if selected_id is None:
            return

        return self.cached_data_base.find_node_by_id(selected_id)

    def get_new_cache_index(self):
        new_index = self.__cache_items_index
        self.__cache_items_index += 1

        return new_index
