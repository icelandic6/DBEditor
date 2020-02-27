import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
import dbtree_test

from dbeditor_window import DBEditorWindow

if __name__ == '__main__':
    QCoreApplication.setApplicationName('DBEditor')

    app = QApplication(sys.argv)

    main_window = DBEditorWindow()
    main_window.show()

    result = app.exec_()

    sys.exit(result)
