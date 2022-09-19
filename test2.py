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

import sys

from py_widget import PyDash, PyPlus, PyMinus, PySlider

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #load the ui file
        uic.loadUi("test.ui", self)
        self.setWindowTitle("Porsche Controller")

        #DEFINE OUR WIDGETS
        self.StackedLayout = QStackedLayout()
        self.StackedLayout.setStackingMode(QStackedLayout.StackAll)

        self.VideoWidget = self.findChild(QWidget, "VideoWidget")
        self.ButtonWidget = self.findChild(QWidget, "ButtonWidget")

        self.VideoButton = self.findChild(QPushButton, "VideoButton")
        self.ControlsButton = self.findChild(QPushButton, "ControlsButton")

        self.TestButton = self.findChild(QPushButton, "TestButton")
        self.TestSlider = self.findChild(QSlider, "TestSlider")

        self.Video = self.findChild(GLViewWidget, "Video")

        # LOAD 3d STL
        stl_mesh = mesh.Mesh.from_file('Resources\lowPoly.stl')

        points = stl_mesh.points.reshape(-1, 3)
        faces = np.arange(points.shape[0]).reshape(-1, 3)

        mesh_data = MeshData(vertexes=points, faces=faces)
        meshItem = GLMeshItem(meshdata=mesh_data, smooth=True, drawFaces=False, drawEdges=True, edgeColor=(0, 189, 190, .5))
        self.Video.addItem(meshItem)
        self.Video.setCameraPosition(QVector3D(-5.015859651283621e-16, 3.5121427064511513e-16, 10.0), distance=150)
        self.Video.orbit(0,90)

        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.Video.orbit(-1,0))
        self.timer.start(20)

        # LOAD MEDIA PLAYER
        # self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        # self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('Resources\Bugattirender.avi')))
        # self.mediaPlayer.setVideoOutput(self.Video)
        # self.mediaPlayer.setPlaybackRate(0.8)
        
        # self.mediaPlayer.play()

        # self.mediaPlayer.stateChanged.connect(self.restartPlayer)

        # ADD LAYOUTS TO LAYOUT STACK
        self.StackedLayout.insertWidget(0,self.VideoWidget)
        self.StackedLayout.insertWidget(1,self.ButtonWidget)

        self.VideoButton.clicked.connect(lambda : self.WidgetClicked(self.VideoWidget))
        # self.ControlsButton.clicked.connect(lambda : self.Stack.setCurrentWidget(self.Page_2))
        
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



    # def restartPlayer(self):
    #     self.mediaPlayer.play()

    # def changeFrame(self, side):

    #     if side == "left":
    #         if self.rightfrm.isVisible():
    #             self.rightfrm.hide()
    #             self.leftfrm.setGeometry(20,20,1080,700)
    #             self.leftbtn.resize(1080,23)
    #         else:
    #             self.rightfrm.show()
    #             self.leftfrm.setGeometry(20,20,530,700)
    #             self.leftbtn.resize(530,23)
    #     elif side == "right":
    #         if self.leftfrm.isVisible():
    #             self.leftfrm.hide()
    #         else:
    #             self.leftfrm.show()


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()