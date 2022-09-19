import sys
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from py_widget import *
from pyqtgraph.opengl import GLViewWidget, MeshData, GLMeshItem
import numpy as np
from stl import mesh

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        #load the ui file
        uic.loadUi("test2.ui", self)
        self.setWindowTitle("Porsche Controller")

        self.view = self.findChild(PyGlView, "GLWidget")
        self.btn = self.findChild(QPushButton, "pushButton")

        # LOAD 3d STL
        self.stl_mesh = mesh.Mesh.from_file('Resources\lowPoly.stl')

        self.points = self.stl_mesh.points.reshape(-1, 3)
        self.faces = np.arange(self.points.shape[0]).reshape(-1, 3)

        self.mesh_data = MeshData(vertexes=self.points, faces=self.faces)
        self.meshItem = GLMeshItem(meshdata=self.mesh_data, smooth=True, drawFaces=False, drawEdges=True, edgeColor=(0, 189, 190, .5))
        self.view.addItem(self.meshItem)
        self.view.setCameraPosition(QVector3D(-5.015859651283621e-16, 3.5121427064511513e-16, 10.0), distance=150)
        self.view.orbit(0,90)

        self.view.setAnimation(AnimEnum.SPINNING)

        self.btn.clicked.connect(lambda: self.update())

        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.view.orbit(-1,0))
        self.timer.start(20)

        self.show()





app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()