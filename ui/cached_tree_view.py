from PyQt5.QtWidgets import QWidget, QTreeView, QHBoxLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel, pyqtSignal

import ui.tree_view_item_roles as roles


class DBProxyModel(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super(DBProxyModel, self).__init__(parent)

    def lessThan(self, left_index, right_index):
        left_pid = left_index.data(roles.ParentIdRole)
        right_pid = right_index.data(roles.ParentIdRole)

        if left_pid == right_pid:
            left_id = left_index.data(roles.ItemIdRole)
            right_id = right_index.data(roles.ItemIdRole)

            return left_id > right_id

        return left_pid > right_pid


class CachedTreeView(QWidget):
    item_changed = pyqtSignal(int, str)

    def __init__(self, parent=None):
        super(CachedTreeView, self).__init__(parent)

        self.tree_model = QStandardItemModel()
        self.tree_model.setRowCount(0)

        self.tree_view = QTreeView(self)
        self.tree_view.setHeaderHidden(True)

        self.root_item = None

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(self.tree_view)

        self.setLayout(main_layout)

        self.proxy_model = DBProxyModel(self)
        self.proxy_model.setSourceModel(self.tree_model)
        self.tree_view.setModel(self.proxy_model)
        self.tree_view.setSortingEnabled(True)

        self.tree_model.dataChanged.connect(self.on_data_changed)

    def add_item(self, node_id, parent_id, value, exists):
        item = QStandardItem()
        item.setData(node_id, roles.ItemIdRole)
        item.setData(parent_id, roles.ParentIdRole)
        item.setData(value, Qt.DisplayRole)
        item.setEnabled(exists)

        if parent_id == 0:
            self.root_item = item

            print("root item:", self.root_item.data(Qt.DisplayRole),
                  "(", self.root_item.data(roles.ParentIdRole), ",",
                  self.root_item.data(roles.ItemIdRole), ")")

            self.tree_model.appendRow(self.root_item)
            return

        parent_item = self.find_item(parent_id)

        if parent_item is not None:
            print("item:", item.data(Qt.DisplayRole),
                  "(", item.data(roles.ParentIdRole), ",",
                  item.data(roles.ItemIdRole), ")",
                  "with parent item:", parent_item.data(Qt.DisplayRole),
                  "(", parent_item.data(roles.ParentIdRole), ",",
                  parent_item.data(roles.ItemIdRole), ")")

            parent_item.appendRow(item)
        else:
            print("item:", item.data(Qt.DisplayRole),
                  "(", item.data(roles.ParentIdRole), ",",
                  item.data(roles.ItemIdRole), ")")

            if self.root_item is None:
                self.tree_model.appendRow(item)
            else:
                self.root_item.appendRow(item)

    def find_item(self, item_id):
        items_list = self.tree_model.match(self.tree_model.index(0, 0), roles.ItemIdRole, item_id,
                                           1, Qt.MatchExactly | Qt.MatchRecursive)

        if items_list:
            index = items_list.pop()
            return self.tree_model.itemFromIndex(index)

        return None

    def on_data_changed(self, first_index):
        item = self.tree_model.itemFromIndex(first_index)

        item_id = item.data(roles.ItemIdRole)
        item_value = item.data(Qt.DisplayRole)

        self.item_changed.emit(item_id, item_value)

    def selected_item_id(self):
        indexes = self.tree_view.selectedIndexes()

        if not indexes:
            return None

        # item = self.tree_model.itemFromIndex()
        return indexes.pop().data(roles.ItemIdRole)

    def enter_item_edit_mode(self, item_id):
        items_list = self.tree_model.match(self.tree_model.index(0, 0), roles.ItemIdRole, item_id,
                                           1, Qt.MatchExactly | Qt.MatchRecursive)

        if items_list:
            index = items_list.pop()
            self.tree_view.edit(index)

    def clear(self):
        self.tree_model.clear()
        self.root_item = None

    def expand_all(self):
        self.tree_view.expandAll()

