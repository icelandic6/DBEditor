from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import QObject

from ui.cached_tree_view import CachedTreeView
from data_base import DataBase


class CachedTreeController(QObject):
    def __init__(self, parent=None):
        super(CachedTreeController, self).__init__(parent)

        self.cached_data_base = DataBase()

        self.__cached_tree_view = CachedTreeView()
        self.__cached_tree_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.__cached_tree_view.item_changed.connect(self.on_item_changed)

    def tree_view(self):
        return self.__cached_tree_view

    def reset(self):
        self.cached_data_base.dict.clear()
        self.__cached_tree_view.clear()

    def add_item(self, item_id, item):
        if item.parent_id in self.cached_data_base.dict:
            item.exists = False

        self.cached_data_base.dict[item_id] = item

        self.__update_tree_view()

    def __update_tree_view(self):
        self.__cached_tree_view.clear()

        for item_id, v in self.sorted_data().items():
            self.__add_tree_item(item_id, v)

        self.__cached_tree_view.expand_all()

    def __add_tree_item(self, item_id, item):
        self.__cached_tree_view.add_item(item_id,
                                         item.parent_id,
                                         item.value,
                                         item.exists)

    def sorted_data(self):
        new_dict = dict(self.cached_data_base.dict)
        sorted_dict = {}
        added_parent_ids = []

        while new_dict:
            for key, value in new_dict.items():
                if value.parent_id not in self.cached_data_base.dict.keys() or value.parent_id in added_parent_ids:
                    sorted_dict[key] = value
                    new_dict.pop(key)
                    added_parent_ids.append(key)
                    break

        return sorted_dict

    def remove_item(self, item_id):
        self.__remove_item(item_id)
        self.__update_tree_view()

    def __remove_item(self, item_id):
        if item_id not in self.cached_data_base.dict:
            return

        item = self.cached_data_base.dict[item_id]
        item.exists = False

        for key, value in self.cached_data_base.dict.items():
            if value.parent_id == item_id:
                self.remove_item(key)

    def on_item_changed(self, item_id, value):
        if item_id in self.cached_data_base.dict:
            self.cached_data_base.dict[item_id].value = value

    def selected_item(self):
        selected_id = self.__cached_tree_view.selected_item_id()

        if selected_id is None:
            return None, None

        selected_node_index = selected_id if selected_id in self.cached_data_base.dict else None

        return selected_node_index, self.cached_data_base.get_node_by_index(selected_node_index)

    def get_new_cache_index(self):
        new_index = self.__cache_items_index
        self.__cache_items_index += 1

        return new_index

    def enter_item_edit_mode(self, item_id):
        if item_id in self.cached_data_base.dict:
            self.__cached_tree_view.enter_item_edit_mode(item_id)
