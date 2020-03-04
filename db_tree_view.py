from PyQt5.QtWidgets import QWidget, QTreeView, QHBoxLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt

ItemIdRole = Qt.UserRole + 1
ParentIdRole = Qt.UserRole + 2


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

    def add_item(self, node_id, parent_id, value):
        item = QStandardItem()
        item.setData(node_id, ItemIdRole)
        item.setData(parent_id, ParentIdRole)
        item.setData(value, Qt.DisplayRole)
        item.setEditable(False)

        if parent_id == 0:
            self.root_item = item

            print("root item:", self.root_item.data(Qt.DisplayRole),
                  "(", self.root_item.data(ParentIdRole), ",",
                  self.root_item.data(ItemIdRole), ")")

            self.tree_model.appendRow(self.root_item)
            return

        parent_item = self.find_item(parent_id)

        if parent_item is not None:
            print("item:", item.data(Qt.DisplayRole),
                  "(", item.data(ParentIdRole), ",",
                  item.data(ItemIdRole), ")",
                  "with parent item:", parent_item.data(Qt.DisplayRole),
                  "(", parent_item.data(ParentIdRole), ",",
                  parent_item.data(ItemIdRole), ")")

            parent_item.appendRow(item)
        else:
            print("item:", item.data(Qt.DisplayRole),
                  "(", item.data(ParentIdRole), ",",
                  item.data(ItemIdRole), ")",
                  "with root item:", self.root_item.data(Qt.DisplayRole),
                  "(", self.root_item.data(ParentIdRole), ",",
                  self.root_item.data(ItemIdRole), ")")

            self.root_item.appendRow(item)

    def find_item(self, item_id):
        items_list = self.tree_model.match(self.tree_model.index(0, 0), ItemIdRole, item_id,
                                           1, Qt.MatchExactly | Qt.MatchRecursive)

        if items_list:
            index = items_list.pop()
            return self.tree_model.itemFromIndex(index)

        return None

    def selected_item_id(self):
        indexes = self.tree_view.selectedIndexes()

        if not indexes:
            return None

        item = self.tree_model.itemFromIndex(indexes.pop())
        return item.data(ItemIdRole)

    def clear(self):
        self.tree_model.clear()
        self.root_item = None

    def expand_all(self):
        self.tree_view.expandAll()
