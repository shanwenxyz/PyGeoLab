#!D:/library/Miniconda/python
# -*- coding: utf-8 -*-

import sys
from mainwindow import MainWindow
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWindow()

    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())
