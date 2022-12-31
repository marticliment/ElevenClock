from ctypes import c_int, windll
windll.shcore.SetProcessDpiAwareness(c_int(2))

#
#
# This file comes from https://github.com/mustafaahci/FramelessWindow
#
#

import winreg
from win32mica import ApplyMica, MICAMODE

from ctypes.wintypes import DWORD, LONG, LPCVOID

from win32con import PAN_SERIF_SQUARE, WM_NCCALCSIZE, GWL_STYLE, WM_NCHITTEST, WS_MAXIMIZEBOX, WS_THICKFRAME, \
    WS_CAPTION, HTTOPLEFT, HTBOTTOMRIGHT, HTTOPRIGHT, HTBOTTOMLEFT, \
    HTTOP, HTBOTTOM, HTLEFT, HTRIGHT, HTCAPTION, WS_POPUP, WS_SYSMENU, WS_MINIMIZEBOX


from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from external.blurwindow import ExtendFrameIntoClientArea

def readRegedit(aKey, sKey, default, storage=winreg.HKEY_CURRENT_USER):
    registry = winreg.ConnectRegistry(None, storage)
    reg_keypath = aKey
    try:
        reg_key = winreg.OpenKey(registry, reg_keypath)
    except FileNotFoundError as e:
        return default
    except Exception as e:
        print(e)
        return default

    for i in range(1024):
        try:
            value_name, value, _ = winreg.EnumValue(reg_key, i)
            if value_name == sKey:
                return value
        except OSError as e:
            return default
        except Exception as e:
            print(e)
            return default

def isWindowDark() -> bool:
    return readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "AppsUseLightTheme", 1)==0


class QFramelessWindow(QMainWindow):
    BORDER_WIDTH = 10

    def __init__(self, parent=None):
        self.updateSize = True
        self.settingsWidget = QWidget()
        super().__init__(parent=parent)
        self.hwnd = self.winId().__int__()
        self.setObjectName("QFramelessWindow")
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.CustomizeWindowHint)
        #window_style = win32gui.GetWindowLong(self.hwnd, GWL_STYLE)
        #win32gui.SetWindowLong(self.hwnd, GWL_STYLE, window_style | WS_POPUP | WS_THICKFRAME | WS_CAPTION | WS_SYSMENU | WS_MAXIMIZEBOX | WS_MINIMIZEBOX)

        ExtendFrameIntoClientArea(self.winId().__int__())

        self.setAutoFillBackground(True)

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
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor("#272727"))
        self.setPalette(p)

        self._layout.addWidget(self.mainWidget)
        self.setLayout(self._layout)

        return super(QFramelessWindow, self).changeEvent(event)
    
    def showEvent(self, event) -> None:
        ApplyMica(self.winId(), MICAMODE.DARK if isWindowDark() else MICAMODE.LIGHT)
        return super().showEvent(event)

    def moveEvent(self, event) -> None:
        self.repaint()
        return super().moveEvent(event)


class QFramelessDialog(QFramelessWindow):
    clicked = Signal(QDialogButtonBox.ButtonRole)
    def __init__(self, parent=None, closeOnClick=True, xoff = 0, yoff = 0):
        self.xoff = xoff
        self.yoff = yoff
        super().__init__(parent=None)
        self.windows = parent
        self.closeOnClick = closeOnClick
        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_StyledBackground)
        l = QVBoxLayout()
        l.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel("Title")
        self.title.setStyleSheet(f"font-size: 16pt;padding: {self.getPx(30)}px; padding-bottom: {self.getPx(5)}px;")
        l.addWidget(self.title)
        self.body = QLabel("This is the body. Here comes the warning")
        self.body.setOpenExternalLinks(True)
        self.body.setStyleSheet(f"font-size: 10pt;font-weight: light;font-family: \"Segoe UI Variable Display\";padding: {self.getPx(30)}px; padding-top: {self.getPx(5)}px;")
        l.addWidget(self.body)
        self.buttonWidget = QDialogButtonBox(self)
        self.buttonWidget.setObjectName("dialogButtonWidget")
        self.buttonWidget.setStyleSheet(f"QPushButton{{margin: {self.getPx(2)}px;height: {self.getPx(30)}px;}}")
        self.buttonWidget.clicked.connect(self.click)
        bwd = QWidget()
        bwd.setContentsMargins(self.getPx(15), self.getPx(15), self.getPx(15), self.getPx(15))
        bwd.setObjectName("dialogButtonWidget")
        tl = QVBoxLayout()
        tl.addWidget(self.buttonWidget)
        bwd.setLayout(tl)
        l.addWidget(bwd)
        self.setLayout(l)
        w = QWidget(self)
        w.setObjectName("bgDialog")
        w.setLayout(l)
        self.setCentralWidget(w)

        self.setWindowModality(Qt.WindowModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)

    def closeEvent(self, event: QCloseEvent) -> None:
        #self.parent().window().setWindowOpacity(1)
        return super().closeEvent(event)

    def click(self, btn: QAbstractButton) -> None:
        btnRole = self.buttonWidget.buttonRole(btn)
        self.clicked.emit(btnRole)
        if self.closeOnClick:
            self.close()

    def addButton(self, text: str, btnRole: QDialogButtonBox.ButtonRole, action: object = None) -> None:
        b = self.buttonWidget.addButton(text, btnRole)
        if action:
            b.clicked.connect(action)

    def setDefaultButtonRole(self, btnRole: QDialogButtonBox.ButtonRole, stylesheet: str) -> None:
        for btn in self.buttonWidget.buttons():
            btn: QPushButton
            if self.buttonWidget.buttonRole(btn) == btnRole:
                btn.setObjectName("AccentButton")
                btn.setStyleSheet(stylesheet+f"QPushButton{{margin: {self.getPx(2)}px;height: {self.getPx(30)}px;}}")
                break

    def getBtn(self, btnRole: QDialogButtonBox.ButtonRole) -> QPushButton:
        for btn in self.buttonWidget.buttons():
            btn: QPushButton
            if self.buttonWidget.buttonRole(btn) == btnRole:
                return btn


    def setTitle(self, t: str):
        self.title.setText(t)
        pass

    def setText(self, t: str):
        self.body.setText(t)
        pass

    def parent(self) -> QWidget:
        return super().parent()

    def showEvent(self, event: QShowEvent) -> None:
        self.setFixedSize(self.minimumSizeHint())
        w = self.width()
        h = self.height()
        try:
            self.move(
                self.xoff+self.windows.x()+(self.windows.width()-w)//2,
                self.yoff+self.windows.y()+(self.windows.height()-h)//2
            )
        except AttributeError:
            pass
        #self.parent().window().setWindowOpacity(0.7)
        return super().showEvent(event)

    def getPx(self, i: int) -> int:
        return i

    def get6px(self, i: int) -> int:
        return round(i*self.screen().devicePixelRatio())




if __name__ == "__main__":
    from ctypes import c_int, windll
    windll.shcore.SetProcessDpiAwareness(c_int(2))
    import __init__