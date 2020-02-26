import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
import dbtree_test

from dbeditor_window import DBEditorWindow

if __name__ == '__main__':
    QCoreApplication.setApplicationName('DBEditor')

    app = QApplication(sys.argv)

    mainWindow = DBEditorWindow()
    mainWindow.show()

    test_tree = dbtree_test.DBTreeTest()
    test_tree.create_test_tree()
    test_tree.print_tree()

    result = app.exec_()

    sys.exit(result)
