from PyQt5.QtWidgets import QWidget, QTreeView, QHBoxLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel

import ui.tree_view_item_roles as roles


class DBTreeView(QWidget):
    def __init__(self, parent=None):
        super(DBTreeView, self).__init__(parent)

        self.tree_model = QStandardItemModel()
        self.tree_model.setRowCount(0)

        self.tree_view = QTreeView(self)
        self.tree_view.setHeaderHidden(True)
        self.tree_view.setModel(self.tree_model)

        self.root_item = None

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(self.tree_view)

        self.setLayout(main_layout)

    def add_item(self, item_id, parent_id, value, exists):
        item = QStandardItem()
        item.setData(item_id, roles.ItemIdRole)
        item.setData(parent_id, roles.ParentIdRole)
        item.setData(value, Qt.DisplayRole)
        item.setEnabled(exists)
        item.setEditable(False)

        if parent_id == 0:
            self.root_item = item

            self.tree_model.appendRow(self.root_item)
            return

        parent_item = self.find_item(parent_id)

        if parent_item is not None:
            parent_item.appendRow(item)
        else:
            self.root_item.appendRow(item)

    def find_item(self, item_id):
        items_list = self.tree_model.match(self.tree_model.index(0, 0), roles.ItemIdRole, item_id,
                                           1, Qt.MatchExactly | Qt.MatchRecursive)

        if items_list:
            index = items_list.pop()
            return self.tree_model.itemFromIndex(index)

        return None

    def selected_item_id(self):
        indexes = self.tree_view.selectedIndexes()

        if not indexes:
            return None

        return indexes.pop().data(roles.ItemIdRole)

    def clear(self):
        self.tree_model.clear()
        self.root_item = None

    def expand_all(self):
        self.tree_view.expandAll()
