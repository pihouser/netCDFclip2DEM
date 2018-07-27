### You MUST run the three export path commands (may be missing one, code crashes on Line 24 (QgsApplication.initQgis())
# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Applications/QGIS3.app/Contents/MacOS/lib/:/Applications/QGIS3.app/Contents/Frameworks/
# export PYTHONPATH=/Applications/QGIS3.app/Contents/Resources/python
# export LD_LIBRARY_PATH=/opt/Qt5.6.2/path/to/lib:$LD_LIBRARY_PATH
----------

import os, sys
import gdal, osgeo

#sys.path line REQUIRED for the egis.core import statement 
sys.path.append('/Applications/QGIS3.app/Contents/Resources/python')
    
from qgis.core import *
from qgis.core import QgsApplication

import PyQt5
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from qgis.core import QgsMapCanvas, QgsVectorLayer, QgsMapLayerRegistry, QgsMapCanvasLayer

app = QgsApplication([], True)
QgsApplication.setPrefixPath("/usr", True)
QgsApplication.initQgis()


#### TEST____________________AREA__________________________________________
#QgsApplication.setPrefixPath("/Applications/QGIS3.app", True)


#uri='NETCDF:"/Users/pihouser/Desktop/FLDASNOAH01AE1.nc”:Rainf_f_tavg’




#fileName = "/path/to/file/myfile.nc"
#fileInfo = QtCore.QFileInfo(fileName)


#THIS LINE CRASHES PYTHON!
app = QgsApplication([], True)
QgsApplication.setPrefixPath("/usr", True)
QgsApplication.initQgis()
