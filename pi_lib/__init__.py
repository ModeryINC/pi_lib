# import functions
from .functions.base_functions import errorMsg, close, help, loadFile
from .functions.dataInspect_functions import isPositive, isNegative, canBeFloat, canBeInt
from .functions.dataModify_functions import gatData, removeWhitespaces
from .functions.plot_functions import getWavLength, readWav, createPlotFromWav

# import classes
from .classes.figures_classes import Sphere, Tetrahedron, Pyramid, Cylinder, Cone, Ellipsoid
from .classes.plot_classes import PlotClass