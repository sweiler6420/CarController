import sys
import time
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

from py_widget import PyDash, PyPlus, PyMinus, PySlider

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # this will hide the title bar
        # self.setWindowFlag(Qt.FramelessWindowHint)

        #load the ui file
        uic.loadUi("Controller.ui", self)
        self.setWindowTitle("Porsche Controller")

        #DEFINE OUR WIDGETS
        self.DashLarge1 = self.findChild(PyDash, "DashLarge1")
        self.DashLarge2 = self.findChild(PyDash, "DashLarge2")

        self.DashMedium1 = self.findChild(PyDash, "DashMedium1")
        self.DashMedium2 = self.findChild(PyDash, "DashMedium2")

        self.DashSmall1 = self.findChild(PyDash, "DashSmall1")
        self.DashSmall2 = self.findChild(PyDash, "DashSmall2")

        self.DashTiny1 = self.findChild(PyDash, "DashTiny1")
        self.DashTiny2 = self.findChild(PyDash, "DashTiny2")

        self.Plus1 = self.findChild(PyPlus, "Plus1")
        self.Plus2 = self.findChild(PyPlus, "Plus2")

        self.Minus1 = self.findChild(PyMinus, "Minus1")
        self.Minus2 = self.findChild(PyMinus, "Minus2")

        self.TempSlider = self.findChild(PySlider, "TempSlider")
        self.VentSlider = self.findChild(PySlider, "VentSlider")
        self.DefrostSlider = self.findChild(PySlider, "DefrostSlider")

        self.Video = self.findChild(QVideoWidget, "VideoPlayer")

        # LOAD MEDIA PLAYER
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('Resources\Bugattirender.avi')))
        self.mediaPlayer.setVideoOutput(self.Video)
        self.mediaPlayer.setPlaybackRate(0.8)
        
        self.mediaPlayer.play()

        # SET WIDGET PROPERTIES123
        self.DashLarge1.setSize(80,5)
        self.DashLarge2.setSize(80,5)
        self.DashLarge1.setColors("#FFFFFF", "#00BDBE")
        self.DashLarge2.setColors("#FFFFFF", "#00BDBE")

        self.DashMedium1.setSize(70,5)
        self.DashMedium2.setSize(70,5)
        self.DashMedium1.setColors("#FFFFFF", "#00BDBE")
        self.DashMedium2.setColors("#FFFFFF", "#00BDBE")

        self.DashSmall1.setSize(60,5)
        self.DashSmall2.setSize(60,5)
        self.DashSmall1.setColors("#FFFFFF", "#00BDBE")
        self.DashSmall2.setColors("#FFFFFF", "#00BDBE")

        self.DashTiny1.setSize(50,5)
        self.DashTiny2.setSize(50,5)
        self.DashTiny1.setColors("#FFFFFF", "#00BDBE")
        self.DashTiny2.setColors("#FFFFFF", "#00BDBE")

        self.VentSlider.setType(2)
        self.DefrostSlider.setType(2)

        # SET WIDGET ACTIONS
        self.DashLarge1.clicked.connect(lambda: self.dashClicked(value=1, button = "Large"))
        self.DashLarge2.clicked.connect(lambda: self.dashClicked(value=2, button = "Large"))

        self.DashMedium1.clicked.connect(lambda: self.dashClicked(value=1, button = "Medium"))
        self.DashMedium2.clicked.connect(lambda: self.dashClicked(value=2, button = "Medium"))

        self.DashSmall1.clicked.connect(lambda: self.dashClicked(value=1, button = "Small"))
        self.DashSmall2.clicked.connect(lambda: self.dashClicked(value=2, button = "Small"))

        self.DashTiny1.clicked.connect(lambda: self.dashClicked(value=1, button = "Tiny"))
        self.DashTiny2.clicked.connect(lambda: self.dashClicked(value=2, button = "Tiny"))

        self.Plus1.clicked.connect(lambda: self.incDash(value = 1))
        self.Plus2.clicked.connect(lambda: self.incDash(value = 2))

        self.Minus1.clicked.connect(lambda: self.decDash(value = 1))
        self.Minus2.clicked.connect(lambda: self.decDash(value = 2))

        self.mediaPlayer.stateChanged.connect(self.restartPlayer)

        #move the slider

        #show the app
        self.show()

    def restartPlayer(self):
        self.mediaPlayer.play()

    def dashClicked(self, value, button):
        if value == 1:
            if button == "Large":
                self.DashLarge1.setChecked(True)
                self.DashMedium1.setChecked(True)
                self.DashSmall1.setChecked(True)
                self.DashTiny1.setChecked(True)
            elif button == "Medium":
                self.DashLarge1.setChecked(False)
                self.DashMedium1.setChecked(True)
                self.DashSmall1.setChecked(True)
                self.DashTiny1.setChecked(True)
            elif button == "Small":
                self.DashLarge1.setChecked(False)
                self.DashMedium1.setChecked(False)
                self.DashSmall1.setChecked(True)
                self.DashTiny1.setChecked(True)
            elif button == "Tiny":
                if self.DashSmall1.isChecked():
                    self.DashTiny1.setChecked(True)
                self.DashLarge1.setChecked(False)
                self.DashMedium1.setChecked(False)
                self.DashSmall1.setChecked(False) 
        elif value == 2:  
            if button == "Large":
                self.DashLarge2.setChecked(True)
                self.DashMedium2.setChecked(True)
                self.DashSmall2.setChecked(True)
                self.DashTiny2.setChecked(True)
            elif button == "Medium":
                self.DashLarge2.setChecked(False)
                self.DashMedium2.setChecked(True)
                self.DashSmall2.setChecked(True)
                self.DashTiny2.setChecked(True)
            elif button == "Small":
                self.DashLarge2.setChecked(False)
                self.DashMedium2.setChecked(False)
                self.DashSmall2.setChecked(True)
                self.DashTiny2.setChecked(True)
            elif button == "Tiny":
                if self.DashSmall2.isChecked():
                    self.DashTiny2.setChecked(True)
                self.DashLarge2.setChecked(False)
                self.DashMedium2.setChecked(False)
                self.DashSmall2.setChecked(False)     
        self.update    
            

    def incDash(self, value):
        if value == 1:
            if not self.DashTiny1.isChecked():
                self.DashTiny1.setChecked(True)
            elif not self.DashSmall1.isChecked():
                self.DashSmall1.setChecked(True)
            elif not self.DashMedium1.isChecked():
                self.DashMedium1.setChecked(True)
            elif not self.DashLarge1.isChecked():
                self.DashLarge1.setChecked(True)
        elif value == 2:
            if not self.DashTiny2.isChecked():
                self.DashTiny2.setChecked(True)
            elif not self.DashSmall2.isChecked():
                self.DashSmall2.setChecked(True)
            elif not self.DashMedium2.isChecked():
                self.DashMedium2.setChecked(True)
            elif not self.DashLarge2.isChecked():
                self.DashLarge2.setChecked(True)
        self.update

    def decDash(self, value):
        if value == 1:
            if self.DashLarge1.isChecked():
                self.DashLarge1.setChecked(False)
            elif self.DashMedium1.isChecked():
                self.DashMedium1.setChecked(False)
            elif self.DashSmall1.isChecked():
                self.DashSmall1.setChecked(False)
            elif self.DashTiny1.isChecked():
                self.DashTiny1.setChecked(False)
        elif value == 2:
            if self.DashLarge2.isChecked():
                self.DashLarge2.setChecked(False)
            elif self.DashMedium2.isChecked():
                self.DashMedium2.setChecked(False)
            elif self.DashSmall2.isChecked():
                self.DashSmall2.setChecked(False)
            elif self.DashTiny2.isChecked():
                self.DashTiny2.setChecked(False)
        self.update

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
