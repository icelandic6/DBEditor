from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import Qt, pyqtSignal

from ui.tree_view import TreeView
import ui.tree_view_item_roles as roles


class CacheTreeView(TreeView):
    item_changed = pyqtSignal(int, str)

    def __init__(self, parent=None):
        super(CacheTreeView, self).__init__(parent)

        self._tree_model.dataChanged.connect(self.on_data_changed)

    def add_item(self, item_id, parent_id, value, exists):
        item = QStandardItem()
        item.setData(item_id, roles.ItemIdRole)
        item.setData(parent_id, roles.ParentIdRole)
        item.setData(value, Qt.DisplayRole)
        item.setEnabled(exists)

        if parent_id == 0:
            self._root_item = item

            self._tree_model.appendRow(self._root_item)
            return

        parent_item = self.find_item(parent_id)

        if parent_item is not None:
            parent_item.appendRow(item)
        else:
            if self._root_item is None:
                self._tree_model.appendRow(item)
            else:
                self._root_item.appendRow(item)

    def on_data_changed(self, first_index):
        item = self._tree_model.itemFromIndex(first_index)

        item_id = item.data(roles.ItemIdRole)
        item_value = item.data(Qt.DisplayRole)

        self.item_changed.emit(item_id, item_value)

    def enter_item_edit_mode(self, item_id):
        items_list = self._tree_model.match(self._tree_model.index(0, 0), roles.ItemIdRole, item_id,
                                             1, Qt.MatchExactly | Qt.MatchRecursive)

        if items_list:
            index = items_list.pop()
            self._tree_view.edit(index)
