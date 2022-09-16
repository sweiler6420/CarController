from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class PyDash(QCheckBox):
    def __init__(self, super, width = 80, height = 5, HBwidth = 100, HBheight = 40, bg_color = "#000000", active_color = "#00BCff"):
        QCheckBox.__init__(self)

        # SET DEFAULT PARAMETERS
        self.setFixedSize(HBwidth, HBheight)

        # Variables
        self._bg_color = bg_color
        self._active_color = active_color
        self._width = width
        self._height = height
        self._offset = 0

        #self.stateChanged.connect(self.debug)

    def debug(self):
        print(f"State: {self.isChecked()}")

    # SET NEW HITBOX AREA
    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)

    def setSize(self, width, height):
        self._width = width
        self._height = height
        self._offset = (self.width() - width) / 2
    
    def setColors(self, bg_color = "#777", active_color = "#00BCff"):
        # COLORS
        self._bg_color = bg_color
        self._active_color = active_color

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        # SET AS NO PEN
        p.setPen(Qt.NoPen)

        # DRAW RECTANGLE
        #self.rect = QRect(0,0,self.width(), self.height())

        # SET CUSTOM HITBOX ROUNDED RECT
        p.setBrush(QColor("#000000"))
        p.drawRect(0, 0, self.width(), self.height())

        if not self.isChecked():
            # DRAW BG
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect(self._offset, 20, self._width, self._height, self._height / 2, self._height / 2)
        else:
            # DRAW BG
            p.setBrush(QColor(self._active_color))
            p.drawRoundedRect(self._offset, 20, self._width, self._height, self._height / 2, self._height / 2)

        # END DRAW
        p.end()