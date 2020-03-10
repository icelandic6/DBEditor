from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import QObject, pyqtSignal

from ui.cache_tree_view import CacheTreeView
from data_base import DataBase


class CacheController(QObject):
    item_edited = pyqtSignal(int, str)

    def __init__(self, parent=None):
        super(CacheController, self).__init__(parent)

        self.cache_data_base = DataBase()

        self.__cache_tree_view = CacheTreeView()
        self.__cache_tree_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.__cache_tree_view.item_changed.connect(self.on_item_changed)

    def tree_view(self):
        return self.__cache_tree_view

    def reset(self):
        self.cache_data_base.clear()
        self.__cache_tree_view.clear()

    def __update_tree_view(self):
        self.__cache_tree_view.clear()

        for item_id, v in self.sorted_data().items():
            self.__add_tree_item(item_id, v)

        self.__cache_tree_view.expand_all()

    def __add_tree_item(self, item_id, item):
        self.__cache_tree_view.add_item(item_id,
                                        item.parent_id,
                                        item.value,
                                        item.exists)

    def add_item(self, item_id, item):
        if self.cache_data_base.has_item(item.parent_id) and not self.cache_data_base.get_item(item.parent_id).exists:
            item.exists = False

        self.cache_data_base.add_item(item_id, item)

        self.__update_tree_view()

    def sorted_data(self):
        new_dict = self.cache_data_base.get_data()
        sorted_dict = {}
        added_parent_ids = []

        while new_dict:
            for key, value in new_dict.items():
                if value.parent_id not in self.cache_data_base.get_ids() or value.parent_id in added_parent_ids:
                    sorted_dict[key] = value
                    new_dict.pop(key)
                    added_parent_ids.append(key)
                    break

        return sorted_dict

    def remove_item(self, item_id):
        self.__remove_item(item_id)
        self.__update_tree_view()

    def __remove_item(self, item_id):
        item = self.cache_data_base.get_item(item_id)

        if not item:
            return

        item.exists = False

        for key, value in self.cache_data_base.get_items():
            if value.parent_id == item_id:
                self.remove_item(key)

    def get_item(self, item_id):
        return self.cache_data_base.get_item(item_id)

    def on_item_changed(self, item_id, value):
        if self.cache_data_base.has_item(item_id):
            self.cache_data_base.edit_item(item_id, value)

            self.item_edited.emit(item_id, value)

    def selected_item(self):
        selected_id = self.__cache_tree_view.selected_item_id()

        if selected_id is None:
            return None, None

        selected_item_id = selected_id if self.cache_data_base.has_item(selected_id) else None

        return selected_item_id, self.cache_data_base.get_item(selected_item_id)

    def enter_item_edit_mode(self, item_id):
        if self.cache_data_base.has_item(item_id):
            self.__cache_tree_view.enter_item_edit_mode(item_id)
