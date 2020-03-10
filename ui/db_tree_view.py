from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import Qt

from ui.tree_view import TreeView
import ui.tree_view_item_roles as roles


class DBTreeView(TreeView):
    def __init__(self, parent=None):
        super(DBTreeView, self).__init__(parent)

    def add_item(self, item_id, parent_id, value, exists):
        item = QStandardItem()
        item.setData(item_id, roles.ItemIdRole)
        item.setData(parent_id, roles.ParentIdRole)
        item.setData(value, Qt.DisplayRole)
        item.setEnabled(exists)
        item.setEditable(False)

        if parent_id == 0:
            self._root_item = item

            self._tree_model.appendRow(self._root_item)
            return

        parent_item = self.find_item(parent_id)

        if parent_item is not None:
            parent_item.appendRow(item)
        else:
            self._root_item.appendRow(item)
