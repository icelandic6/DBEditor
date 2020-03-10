from PyQt5.QtWidgets import QWidget, QTreeView, QHBoxLayout
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import Qt

import ui.tree_view_item_roles as roles


class TreeView(QWidget):
    def __init__(self, parent=None):
        super(TreeView, self).__init__(parent)

        self._tree_model = QStandardItemModel()
        self._tree_model.setRowCount(0)

        self._tree_view = QTreeView(self)
        self._tree_view.setHeaderHidden(True)
        self._tree_view.setModel(self._tree_model)

        self._root_item = None

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(self._tree_view)

        self.setLayout(main_layout)

    def find_item(self, item_id):
        items_list = self._tree_model.match(self._tree_model.index(0, 0), roles.ItemIdRole, item_id,
                                             1, Qt.MatchExactly | Qt.MatchRecursive)

        if items_list:
            index = items_list.pop()
            return self._tree_model.itemFromIndex(index)

        return None

    def selected_item_id(self):
        indexes = self._tree_view.selectedIndexes()

        if not indexes:
            return None

        return indexes.pop().data(roles.ItemIdRole)

    def clear(self):
        self._tree_model.clear()
        self._root_item = None

    def expand_all(self):
        self._tree_view.expandAll()
