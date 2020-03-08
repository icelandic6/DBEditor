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

        for item_id, item in self.data_base.dict.items():
            self.__add_tree_item(item_id, item)

        self.__db_tree_view.expand_all()

    def __add_tree_item(self, item_id, item):
        self.__db_tree_view.add_item(item_id,
                                     item.parent_id,
                                     item.value,
                                     item.exists)

    def add_new_item(self, item):
        new_item_id = max(self.data_base.dict, key=int) + 1

        if item.parent_id in self.data_base.dict and not self.data_base.dict[item.parent_id].exists:
            item.exists = False

        self.data_base.dict[new_item_id] = item

        self.__update_tree_view()

        return new_item_id

    def remove_item(self, item_id):
        self.__remove_item(item_id)
        self.__update_tree_view()

    def __remove_item(self, item_id):
        item = self.data_base.get_item_by_id(item_id)

        if not item:
            return

        item.exists = False

        for key, value in self.data_base.dict.items():
            if value.parent_id == item_id:
                self.remove_item(key)

    def edit_item(self, item_id, value):
        item = self.data_base.dict.get(item_id, None)

        if not item:
            return

        item.value = value

        self.__update_tree_view()

    def selected_item(self):
        selected_id = self.__db_tree_view.selected_item_id()

        if selected_id is None:
            return None, None

        return selected_id, self.data_base.get_item_by_id(selected_id)

    def get_item_by_id(self, item_id):
        return self.data_base.get_item_by_id(item_id)
