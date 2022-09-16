from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class PySlider(QSlider):
    def __init__(self, super, width = 80, height = 5, bg_color = "#D1D1D1", circle_color = "#00BDBE", active_color = "#00BCff", type = 1):
        QSlider.__init__(self)

        self.setFixedSize(width, height)

        #VARIABLES
        self._bg_color = bg_color
        self._active_color = active_color
        self._circle_color = circle_color
        self._type = type

        #self.valueChanged.connect(self.debug)

    def setType(self, type):
        self._type = type

    def debug(self):
        print(f"Value: {self.value()}")

    def mousePressEvent(self, event):
        super(PySlider, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            val = self.pixelPosToRangeValue(event.pos())
            self.setValue(val)

    def pixelPosToRangeValue(self, pos):
        opt = QStyleOptionSlider()
        self.initStyleOption(opt)
        gr = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderGroove, self)
        sr = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderHandle, self)

        if self.orientation() == Qt.Horizontal:
            sliderLength = sr.width()
            sliderMin = gr.x()
            sliderMax = gr.right() - sliderLength + 1
        else:
            sliderLength = sr.height()
            sliderMin = gr.y()
            sliderMax = gr.bottom() - sliderLength + 1;
        pr = pos - sr.center() + sr.topLeft()
        p = pr.x() if self.orientation() == Qt.Horizontal else pr.y()
        return QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), p - sliderMin, sliderMax - sliderMin, opt.upsideDown)

    # SET NEW HITBOX AREA
    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)

    def paintEvent(self, e):
        if self._type == 1:
            p = QPainter(self)
            p.setRenderHint(QPainter.Antialiasing)

            # SET AS NO PEN
            #p.setPen(Qt.NoPen)

            # DRAW RECTANGLE
            rect = QRect(0,0,self.width()-20, self.height())

            # DRAW GRADIENT
            grad = QLinearGradient(50, 0, rect.width(), 0)
            # grad.setColorAt(0,QColor("#0000FF"))
            # grad.setColorAt(.45,QColor("#8080FF"))
            # grad.setColorAt(0.55,QColor("#FF8080"))
            # grad.setColorAt(1,QColor("#FC0000"))
            grad.setColorAt(0,QColor("#3A3AFF"))
            grad.setColorAt(1,QColor("#FF3A3A"))
            p.setBrush(QBrush(grad))
            p.drawRoundedRect(0, 17, self.width(), self.height() / 4, self.height() / 8, self.height() / 8)

            # DRAW BG
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect((int(self.value()))* 7.75, 17, self.width() - (int(self.value()))* 7.75, self.height() / 4, self.height() / 8, self.height() / 8)

            # DRAW CIRCLE
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse((int(self.value()))* 7.75,0,44,44)
            
            p.setBrush(QColor("#000000"))
            p.drawEllipse((int(self.value()))* 3.6 + 6 ,6,32,32)

            # END DRAW
            p.end()
        else:
            p = QPainter(self)
            p.setRenderHint(QPainter.Antialiasing)

            # SET AS NO PEN
            #p.setPen(Qt.NoPen)

            # DRAW RECTANGLE
            rect = QRect(0,0,self.width()-20, self.height())

            # DRAW GRADIENT
            grad = QLinearGradient(50, 0, rect.width(), 0)
            grad.setColorAt(0,QColor("#FFFFFF"))
            grad.setColorAt(1,QColor("#00BDBE"))
            p.setBrush(QBrush(grad))
            p.drawRoundedRect(0, 17, self.width(), self.height() / 4, self.height() / 8, self.height() / 8)

            # DRAW BG
            p.setBrush(QColor(self._bg_color))
            p.drawRoundedRect((int(self.value()))* 3.6, 17, self.width() - (int(self.value()))* 3.6, self.height() / 4, self.height() / 8, self.height() / 8)

            # DRAW CIRCLE
            p.setBrush(QColor(self._circle_color))
            p.drawEllipse((int(self.value()))* 3.6,0,44,44)

            p.setBrush(QColor("#000000"))
            p.drawEllipse((int(self.value()))* 3.6 + 6 ,6,32,32)

            # END DRAW
            p.end()

