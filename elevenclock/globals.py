from ctypes import c_int, windll
windll.shcore.SetProcessDpiAwareness(c_int(2))


import io
from types import FunctionType


from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *


def loadTimeFormat():
    raise NotImplementedError("loadTimeFormat function has not been defined!")

def updateIfPossible():
    raise NotImplementedError("updateIfPossible function has not been defined!")

def restartClocks():
    raise NotImplementedError("restartClocks function has not been defined!")

def closeClocks():
    raise NotImplementedError("closeClocks function has not been defined!")

def _(a):
    try:
        raise NotImplementedError("_ function has not been defined!")
    except Exception as e:
        print("🟠", e)
    return a


app: QApplication = None
buffer: io.StringIO = None
old_stdout: io.StringIO = None
mController: object = None
trayIcon: QSystemTrayIcon = None
sw: QMainWindow = None
ww: QMainWindow = None
tempDir: str = None
dateTimeFormat: str = "%HH:%M\n%A\n%d/%m/%Y"
settingsCache = {}
canEraseTempDirs: bool = False
newInstanceLaunched: bool = False
