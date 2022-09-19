import sys
import time

import numpy as np
from PyQt5.QtWidgets import QApplication
from pyqtgraph.opengl import *
from stl import mesh
from PyQt5.QtCore import *
from PyQt5.QtGui import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = GLViewWidget()
    stl_mesh = mesh.Mesh.from_file('Resources\lowPoly.stl')

    points = stl_mesh.points.reshape(-1, 3)
    faces = np.arange(points.shape[0]).reshape(-1, 3)

    mesh_data = MeshData(vertexes=points, faces=faces)
    mesh = GLMeshItem(meshdata=mesh_data, smooth=True, drawFaces=False, drawEdges=True, edgeColor=(0, 189, 190, .5))
    view.addItem(mesh)
    
    # view.pan(15,15,150)
    # def setCameraPosition(self, pos=None, distance=None, elevation=None, azimuth=None, rotation=None):
    view.setCameraPosition(QVector3D(-5.015859651283621e-16, 3.5121427064511513e-16, 10.0), distance=150)
    view.orbit(0,90)
    

    view.show()
    app.exec()