from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class PyMinus(QPushButton):
    def __init__(self, super, width = 44, height = 44, color = "#00BDBE"):
        QPushButton.__init__(self)

        # SET DEFAULT PARAMETERS
        self.setFixedSize(width, height)

        # COLORS
        self._color = color

    # SET NEW HITBOX AREA
    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        # SET AS NO PEN
        p.setPen(Qt.NoPen)

        # CREATE HITBOX RECT
        rect = QRect(0,0,self.width(), self.height())

        # DRAW BG
        p.setBrush(QColor(self._color))
        p.drawEllipse(0, 0, self.width(), self.height())
        p.setBrush(QColor("#000000"))
        p.drawEllipse(5, 5, self.width()-10, self.height()-10)

        # DRAW PLUS SIGN
        p.setBrush(QColor(self._color))
        p.drawRoundedRect(10, self.width()/2-3, self.width()-20, 6, 3, 3)
        

        # END DRAW
        p.end()