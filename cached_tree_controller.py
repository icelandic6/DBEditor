from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import QObject

from cached_tree_view import CachedTreeView


class CachedTreeController(QObject):
    def __init__(self, parent=None):
        super(QObject, self).__init__(parent)

        self.__cached_tree_view = CachedTreeView()
        self.__cached_tree_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def tree_view(self):
        return self.__cached_tree_view

    def reset_tree(self):
        self.__cached_tree_view.clear()
