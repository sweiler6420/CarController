from turtle import isvisible
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from pyqtgraph.opengl import GLViewWidget, MeshData, GLMeshItem
import numpy as np
from stl import mesh
from enum import Enum
import sys

from py_widget import PySlider, PyGlView

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # this will hide the title bar
        # self.setWindowFlag(Qt.FramelessWindowHint)

        #load the ui file
        uic.loadUi("Controller_V2.ui", self)
        self.setWindowTitle("Porsche Controller")

        #DEFINE OUR WIDGETS
        self.StackedLayout = QStackedLayout()
        self.StackedLayout.setStackingMode(QStackedLayout.StackAll)

        self.CarView = self.findChild(PyGlView, "CarView")
        self.CoolView = self.findChild(PyGlView, "CoolFanView")
        self.HeatView = self.findChild(PyGlView, "HeatFanView")
        self.SliderWidget = self.findChild(QWidget, "SliderWidget")
     
        self.TempSlider = self.findChild(PySlider, "TempSlider")
        self.VentSlider = self.findChild(PySlider, "VentSlider")
        self.DefrostSlider = self.findChild(PySlider, "DefrostSlider")

        self.VentSlider.setType(2)
        self.DefrostSlider.setType(2)

        print(self.CarView.getViewport())


        # LOAD 3d STL
        self.CarView.addMesh('Resources\lowPoly.stl')
        self.CoolView.addMesh('Resources\lowPoly.stl')
        self.HeatView.addMesh('Resources\lowPoly.stl')

        # ADD LAYOUTS TO LAYOUT STACK
        self.StackedLayout.insertWidget(0,self.CarView)
        self.StackedLayout.insertWidget(1,self.CoolView)
        self.StackedLayout.insertWidget(2,self.HeatView)
        self.StackedLayout.insertWidget(3,self.SliderWidget)

        # SETTING OBJECT SIGNALS
        #self.CoolView.clicked.connect(lambda : self.WidgetClicked(self.CoolWidget))

        # SET WIDGET ACTIONS
        self.timer = QTimer()
        #self.timer.timeout.connect(lambda: self.CoolView.orbit(-1,0) and self.HeatWidget.orbit(-1,0))
        self.timer.start(20)

        #show the app
        self.show()   

    def WidgetClicked(self, clicked: QWidget):
        self.StackedLayout.setStackingMode(QStackedLayout.StackOne)
        self.StackedLayout.setCurrentWidget(clicked)
        WidgetGeometry = clicked.geometry()
        x = WidgetGeometry.x()
        y = WidgetGeometry.y()
        width = WidgetGeometry.width()
        height = WidgetGeometry.height()
        print(str(x))
        print(str(self.x()))
        print(str(width))
        print(str(self.width()))
        if width != self.width():
            self.StackedLayout.setCurrentWidget(clicked)
            if x != self.x():
                clicked.setMaximumSize(1080,720)
                # clicked.setGeometry(0,0,1800,720)
                self.VideoWidget.setProperty
                self.animation = QPropertyAnimation(clicked,b'geometry')
                self.animation.setDuration(700)
                self.animation.setStartValue(QRect(x,y,width,height))
                self.animation.setEndValue(QRect(0,0,1080,720))
                self.animation.start()
                
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
