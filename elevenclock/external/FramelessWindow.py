#
#
# This file comes from https://github.com/mustafaahci/FramelessWindow
#
#


import ctypes
import win32api
import win32gui

from ctypes.wintypes import LONG

from win32con import PAN_SERIF_SQUARE, WM_NCCALCSIZE, GWL_STYLE, WM_NCHITTEST, WS_MAXIMIZEBOX, WS_THICKFRAME, \
    WS_CAPTION, HTTOPLEFT, HTBOTTOMRIGHT, HTTOPRIGHT, HTBOTTOMLEFT, \
    HTTOP, HTBOTTOM, HTLEFT, HTRIGHT, HTCAPTION, WS_POPUP, WS_SYSMENU, WS_MINIMIZEBOX

from PySide2.QtCore import Qt
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QMainWindow, QWidget, QPushButton, QApplication, QVBoxLayout, QSizePolicy, QHBoxLayout
from PySide2.QtWinExtras import QtWin



class QFramelessWindow(QMainWindow):
    BORDER_WIDTH = 10

    def __init__(self):
        self.updateSize = True
        self.settingsWidget = QWidget()
        super().__init__()
        self.hwnd = self.winId().__int__()
        self.setObjectName("QFramelessWindow")
        window_style = win32gui.GetWindowLong(self.hwnd, GWL_STYLE)
        win32gui.SetWindowLong(self.hwnd, GWL_STYLE, window_style | WS_POPUP | WS_THICKFRAME | WS_CAPTION | WS_SYSMENU | WS_MAXIMIZEBOX | WS_MINIMIZEBOX)

        if QtWin.isCompositionEnabled():
            # Aero Shadow
            QtWin.extendFrameIntoClientArea(self, -1, -1, -1, -1)
        else:
            QtWin.resetExtendedFrame(self)

        # Window Widgets
        self.resize(800, 600)
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)


        # main widget is here
        self.mainWidget = QWidget()
        self.mainWidgetLayout = QVBoxLayout()
        self.mainWidgetLayout.setContentsMargins(0, 0, 0, 0)
        self.mainWidget.setLayout(self.mainWidgetLayout)
        self.mainWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # set background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor("#272727"))
        self.setPalette(p)

        self._layout.addWidget(self.mainWidget)
        self.setLayout(self._layout)

    def changeEvent(self, event):
        if event.type() == event.WindowStateChange:
            if self.windowState() & Qt.WindowMaximized:
                margin = abs(self.mapToGlobal(self.rect().topLeft()).y())
                self.setContentsMargins(margin, margin, margin, margin)
            else:
                self.setContentsMargins(0, 0, 0, 0)

        return super(QFramelessWindow, self).changeEvent(event)

    def nativeEvent(self, event, message):
        return_value, result = super().nativeEvent(event, message)

        # if you use Windows OS
        if event == b'windows_generic_MSG':
            msg = ctypes.wintypes.MSG.from_address(message.__int__())
            # Get the coordinates when the mouse moves.
            x = win32api.LOWORD(LONG(msg.lParam).value)
            # converted an unsigned int to int (for dual monitor issue)
            if x & 32768: x = x | -65536
            y = win32api.HIWORD(LONG(msg.lParam).value)
            if y & 32768: y = y | -65536

            x -= self.frameGeometry().x()
            y -= self.frameGeometry().y()

            # Determine whether there are other controls(i.e. widgets etc.) at the mouse position.
            if self.childAt(x, y) is not None and self.childAt(x, y) is not self.findChild(QWidget, "ControlWidget"):
                # passing
                if self.width() - self.BORDER_WIDTH > x > self.BORDER_WIDTH and y < self.height() - self.BORDER_WIDTH:
                    return return_value, result

            if msg.message == WM_NCCALCSIZE:
                # Remove system title
                return True, 0

            if msg.message == WM_NCHITTEST:
                w, h = self.width(), self.height()
                lx = x < self.BORDER_WIDTH
                rx = x > w - self.BORDER_WIDTH
                ty = y < self.BORDER_WIDTH
                by = y > h - self.BORDER_WIDTH
                if lx and ty:
                    return True, HTTOPLEFT
                if rx and by:
                    return True, HTBOTTOMRIGHT
                if rx and ty:
                    return True, HTTOPRIGHT
                if lx and by:
                    return True, HTBOTTOMLEFT
                if ty:
                    return True, HTTOP
                if by:
                    return True, HTBOTTOM
                if lx:
                    return True, HTLEFT
                if rx:
                    return True, HTRIGHT
                # Title
                return True, HTCAPTION

        return return_value, result
    
    def moveEvent(self, event) -> None:
        self.repaint()
        return super().moveEvent(event)
    
if __name__ == "__main__":
    import __init__ 