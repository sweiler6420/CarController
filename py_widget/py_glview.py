from turtle import isvisible
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pyqtgraph.opengl import GLViewWidget, MeshData, GLMeshItem
import numpy as np
from stl import mesh
from enum import Enum

class PyGlView(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.layout = QHBoxLayout( self)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)
        self.viewport = GLViewWidget()
        self.layout.addWidget(self.viewport)
        #self.viewport.opts['viewport'] = (-500,-500,1000,1000)

    def addMesh(self, file_location):
        stl_mesh = mesh.Mesh.from_file(file_location)

        points = stl_mesh.points.reshape(-1, 3)
        faces = np.arange(points.shape[0]).reshape(-1, 3)

        mesh_data = MeshData(vertexes=points, faces=faces)
        meshItem = GLMeshItem(meshdata=mesh_data, smooth=True, drawFaces=False, drawEdges=True, edgeColor=(0, 189, 190, .5))
        self.viewport.addItem(meshItem)
        self.viewport.setCameraPosition(QVector3D(-5.015859651283621e-16, 3.5121427064511513e-16, 10.0), distance=150)
        self.viewport.orbit(0,90)

    def getViewport(self):
        return self.viewport.getViewport()


#     def mouseDoubleClickEvent(self, event):
#         print("DoubleClicked")
#         # widget = self.childAt(event.pos())
#         # if widget is not None and widget.objectName():
#         #     print('dblclick:', widget.objectName())

# class AnimEnum(Enum):
#     SPINNING = 1
#     IDLE = 2






