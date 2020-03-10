from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import QObject

from ui.db_tree_view import DBTreeView
from test_trees.test_data_base import TestDataBase


class DBController(QObject):
    def __init__(self, parent=None):
        super(DBController, self).__init__(parent)

        self.__data_base = TestDataBase()

        self.__db_tree_view = DBTreeView()
        self.__db_tree_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def tree_view(self):
        return self.__db_tree_view

    def reset(self):
        self.__data_base.clear()
        self.__data_base.create_test_data_base()

        self.__update_tree_view()

    def __update_tree_view(self):
        self.__db_tree_view.clear()

        it = self.__data_base.get_items()
        for item_id, item in self.__data_base.get_items():
            self.__add_tree_item(item_id, item)

        self.__db_tree_view.expand_all()

    def __add_tree_item(self, item_id, item):
        self.__db_tree_view.add_item(item_id,
                                     item.parent_id,
                                     item.value,
                                     item.exists)

    def add_new_item(self, item):
        new_item_id = self.__data_base.get_new_id()

        if self.__data_base.has_item(item.parent_id) and not self.__data_base.get_item(item.parent_id).exists:
            item.exists = False

        self.__data_base.add_item(new_item_id, item)

        self.__update_tree_view()

        return new_item_id

    def remove_item(self, item_id):
        self.__remove_item(item_id)
        self.__update_tree_view()

    def __remove_item(self, item_id):
        item = self.__data_base.get_item(item_id)

        if not item:
            return

        item.exists = False

        for key, value in self.__data_base.get_items():
            if value.parent_id == item_id:
                self.remove_item(key)

    def edit_item(self, item_id, value):
        self.__data_base.edit_item(item_id, value)

        self.__update_tree_view()

    def selected_item(self):
        selected_id = self.__db_tree_view.selected_item_id()

        if selected_id is None:
            return None, None

        return selected_id, self.__data_base.get_item(selected_id)

    def get_item_by_id(self, item_id):
        return self.__data_base.get_item(item_id)
