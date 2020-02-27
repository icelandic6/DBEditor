from PyQt5.QtCore import QObject


class DBNode:
    def __init__(self, value=''):
        # super(QObject, self).__init__(parent)

        self.children = []
        self.value = value

    def add_child(self, value=''):
        node = DBNode(value)
        self.children.append(node)
        return node

    def value(self):
        return self.value

    def get_children(self):
        return self.children
