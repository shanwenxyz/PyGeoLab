#!D:/library/Miniconda/python
# -*- coding: utf-8 -*-

"""
first version of pygeolab, opengl render
"""

from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtGui import QWheelEvent
from PyQt5.QtCore import QTimerEvent
from PyQt5.QtGui import QKeyEvent

from meshmodel import MeshModel


class GLArea(QOpenGLWidget):
    def __init__(self, parent):
        QOpenGLWidget.__init__(self, parent)
        self.mesh = MeshModel()

    #inherite from QOpenGLWidget
    def initializeGL(self):
        pass

    def resizeGL(self, w: int, h: int):
        pass

    def paintGL(self):
        pass

    def mousePressEvent(self, a0: QMouseEvent):
        pass

    def mouseReleaseEvent(self, a0: QMouseEvent):
        pass

    def mouseMoveEvent(self, a0: QMouseEvent):
        pass

    def wheelEvent(self, a0: QWheelEvent):
        pass

    def timerEvent(self, a0: QTimerEvent):
        pass

    def keyPressEvent(self, a0: QKeyEvent):
        pass


    # functions belong to itself
    def slotOpenFileDialog(self):
        pass











