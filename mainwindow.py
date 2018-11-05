#!D:/library/Miniconda/python
# -*- coding: utf-8 -*-

"""
first version of pygeolab, opengl render
"""

"""

import sys
from PyQt5.QtWidgets import QApplication, QOpenGLWidget


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QOpenGLWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())
"""

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMdiArea
from PyQt5.QtWidgets import QMdiSubWindow
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDir

from glarea import GLArea
from meshmodel import MeshModel


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.center_widget = QMdiArea(self)
        self.setCentralWidget(self.center_widget)
        self.setGeometry(200, 100, 1200, 750)
        self.create_actions()
        self.create_toolbars()

        self.addToolBar(self.main_toolbar)
        self.setWindowTitle("GeoLab")

        self.list_mesh = []

    # gui functions
    # todo(ShanWen): add images for icons
    def create_actions(self):
        self.open_act = QAction('open...', self)
        self.open_act.setShortcut("Ctrl+O")
        self.open_act.triggered.connect(self.open_file)

        self.saveas_act = QAction('Save As...', self)
        self.saveas_act.setShortcut("Ctrl+S")
        self.saveas_act.triggered.connect(self.save_file)

    def create_menus(self):
        pass

    def create_toolbars(self):
        self.main_toolbar = QToolBar(self)
        self.main_toolbar.addAction(self.open_act)
        self.main_toolbar.addAction(self.saveas_act)

    def add_to_menu(self):
        pass

    def open_file(self, file_name=str()):
        if not file_name:
            file_name = QFileDialog.getOpenFileName(self, "Open File", QDir.currentPath())[0]

        if file_name:
            _mesh = MeshModel()

            if not _mesh.open(file_name):
                QMessageBox().information(self, "Plug & Paint", "Cannot load " + file_name)
            else:
                self.list_mesh.append(_mesh)
                _glarea = GLArea(self.center_widget)
                _glarea.mesh = _mesh

                _sub_window = QMdiSubWindow(self)
                _sub_window.setWidget(_glarea)
                self.center_widget.addSubWindow(_sub_window)
                _sub_window.showMaximized()
                _sub_window.setWindowTitle(file_name)

    def save_file(self):
        _initial_path = QDir.currentPath()
        file_name = QFileDialog.getSaveFileName(self, "Save as", _initial_path)[0]
        print(file_name)
        if not file_name:
            return False
        else:
            self.center_widget.currentSubWindow().widget().mesh.save(file_name)
            return True






