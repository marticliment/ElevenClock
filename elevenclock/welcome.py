from ctypes import c_int, windll
windll.shcore.SetProcessDpiAwareness(c_int(2))

import platform
import subprocess
import os
import sys
import locale
import time
import ctypes
from PySide2 import QtGui
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
#from PySide2.QtCore import pyqtSignal as Signal
import external.FramelessWindow as FramelessWindow

import globals

from languages import * 
from tools import *
from tools import _


dwm = ctypes.windll.dwmapi

class WelcomeWindow(QMainWindow):
    def __init__(self, parent: QObject = None, flags: Qt.WindowFlags = Qt.WindowFlags()) -> None:
        super().__init__()
        
        self.switched = False
        
        self.widgetOrder = (
            FirstRunSlide(self),
            SelectModeSlide(self),
            SelectFullScreenSlide(self),
            LastSlide(self),
        )
        
        for w in self.widgetOrder:
            w.next.connect(self.nextWidget)
            w.previous.connect(self.previousWidget)
            w.skipped.connect(self.lastWidget)
            w.finished.connect(self.close)
            
        
        self.currentIndex = -1
        
        self.setFixedSize(self.getPx(800), self.getPx(600))
        self.setStyleSheet("background-color: transparent;")
        self.bgWidget = QStackedWidget(self)
        self.bgWidget.setObjectName("BackgroundWidget")
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        self.setWindowTitle(_("Welcome to ElevenClock"))
        self.setWindowIcon(QIcon(getPath("icon.png")))
        self.setCentralWidget(self.bgWidget)
        
        
        self.bgWindow = QMainWindow()
        self.bgWindow.setFocusPolicy(Qt.NoFocus)
        self.bgWindow.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowDoesNotAcceptFocus | Qt.Tool)
        self.bgWindow.setAttribute(Qt.WA_TranslucentBackground)
        self.bgWindow.setCentralWidget(QWidget())
        self.bgWindow.centralWidget().setStyleSheet("background-color: rgba(30, 30, 30, 0.6)")
        self.bgWindow.hide()
        self.bgWindow.setWindowTitle("ElenenClock_IgnoreFullscreenEvent")
        self.bgWindow.move(0, 0)
        self.bgWindow.resize(1, 1)
        
        colors = getColors()
                    
                    
        self.bgWidget.setStyleSheet(f"""
            * {{
                color: #eeeeee;
                background-color: transparent;
                border-radius: 4px;
                font-family: "Segoe UI Variable Display"
            }}
            #BackgroundWidget {{
                border: 0px solid #121212;
                padding: 20px;
                background-color: #282828;
                border-radius: 0px;
                padding-left: 30px;
                padding-right: 30px;
            }}
            QLabel {{
                background-color: none;
            }}
            #SampleItem {{
                font-family: "Segoe UI Variable Display semib";
                width: 100px;
                background-color: #303030;
                padding: 20px;
                border-radius: {self.getPx(8)}px;
                border: {self.getPx(1)}px solid #393939;
                height: {self.getPx(25)}px;
                border-top: {self.getPx(1)}px solid #404040;
            }}
            #FramelessSampleItem {{
                font-family: "Segoe UI Variable Display semib";
                width: 100px;
                background-color: transparent;
                padding: 20px;
                border-radius: {self.getPx(8)}px;
                border: none;
                height: {self.getPx(25)}px;
            }}
            QPushButton {{
                font-family: "Segoe UI Variable Display semib";
                font-size: 8pt;
                width: 100px;
                background-color: rgba(63, 63, 63, 50%);
                border-radius: {self.getPx(4)}px;
                border: {self.getPx(1)}px solid rgba(77, 77, 77, 50%);
                height: {self.getPx(25)}px;
                border-top: {self.getPx(1)}px solid rgba(87, 87, 87, 50%);
            }}
            QPushButton:hover {{
                background-color: rgba(77, 77, 77, 50%);
                border: {self.getPx(1)}px solid rgba(89, 89, 89, 50%);
                height: {self.getPx(25)}px;
                border-top: {self.getPx(1)}px solid rgba(95, 95, 95, 50%);
            }}
            QPushButton:pressed {{
                background-color: rgba(89, 89, 89, 50%);
                border: {self.getPx(1)}px solid rgba(95, 95, 95, 50%);
                height: {self.getPx(25)}px;
                border-top: {self.getPx(1)}px solid rgba(99, 99, 99 , 50%);
            }}
            #AccentButton{{
                color: black;
                background-color: rgb({colors[1]});
                border-color: rgb({colors[1]});
                border-bottom-color: rgb({colors[2]});
            }}
            #AccentButton:hover{{
                background-color: rgba({colors[1]}, 80%);
                border-color: rgb({colors[1]});
                border-bottom-color: rgb({colors[2]});
            }}
            #AccentButton:disabled{{
                background-color: #212121;
                border-color: #303030;
                border-bottom-color: #363636;
            }}
            #FocusSelector {{
                border: 5px solid rgb({colors[1]});
                border-radius: 5px;
                background-color: rgb({colors[1]});
            }}
            QLabel {{
                border: none;
                border-radius: 6px;
            }}
            #TitleLabel {{
                font-size: 26pt;
            }}
            """)
        
        self.nextWidget(anim=False)

        self.show()
        
    def fillScreen(self) -> None:
        if not self.switched:
            self.switched = True
            GlobalBlur(self.bgWindow.winId(), Acrylic=False)
            fGeometry = QGuiApplication.primaryScreen().geometry()
            self.bgWindow.setGeometry(self.geometry())
            bgAnim = QPropertyAnimation(self.bgWindow, b"geometry", self)
            bgAnim.setStartValue(self.geometry())
            bgAnim.setEndValue(fGeometry)
            bgAnim.setEasingCurve(QEasingCurve.InOutCirc)
            bgAnim.setDuration(400)
            bgAnim.start()
            self.bgWindow.show()
            x = (QGuiApplication.primaryScreen().geometry().width()-self.getPx(800))//2
            y = (QGuiApplication.primaryScreen().geometry().height()-self.getPx(600))//2
            self.resize(self.getPx(800), self.getPx(600))
            self.setFixedSize(self.getPx(800), self.getPx(600))
            self.hide()
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
            self.show()
            uiAnim = QPropertyAnimation(self, b"pos", self)
            uiAnim.setStartValue(self.pos())
            uiAnim.setEndValue(QPoint(x, y))
            uiAnim.setEasingCurve(QEasingCurve.InOutCirc)
            uiAnim.setDuration(400)
            uiAnim.start()
            
            
            DwmSetWindowAttribute = dwm.DwmSetWindowAttribute
            DwmSetWindowAttribute(int(self.winId().__int__()), 33, ctypes.byref(ctypes.c_int(2)), ctypes.sizeof(ctypes.c_int))
    
    def paintEvent(self, event: QMouseEvent) -> None:
        self.bgWindow.show()
        self.bgWindow.raise_()
        return super().paintEvent(event)
    
    def getPx(self, original) -> int:
        return round(original*(self.screen().logicalDotsPerInch()/96))
        
    def setWidget(self, w: QWidget, back=False, anim=True) -> None:
        self.bgWidget.setCurrentIndex(self.bgWidget.addWidget(w))
        if anim:
            if back:
                w.invertedinAnim()
            else:
                w.inAnim()
        
    def nextWidget(self, anim=True) -> None:
        if self.currentIndex == len(self.widgetOrder)-1:
            self.close()
        else:
            self.currentIndex += 1
            w: BasicNavWidget = self.widgetOrder[self.currentIndex]
            self.setWidget(w, anim=anim)
    
    def previousWidget(self) -> None:
        if self.currentIndex == 0:
            try:
                raise ValueError("The specified index is not present in the list of wizard widgets")
            except Exception as e:
                report(e)
        else:
            self.currentIndex -= 1
            w: BasicNavWidget = self.widgetOrder[self.currentIndex]
            self.setWidget(w, back=True)
    
    def lastWidget(self) -> None:
        self.currentIndex = len(self.widgetOrder)-1
        w: BasicNavWidget = self.widgetOrder[-1]
        self.setWidget(w)
        
        
    def closeEvent(self, event: QCloseEvent) -> None:
        self.bgWindow.close()
        return super().closeEvent(event)

class BasicNavWidget(QWidget):
    next = Signal()
    previous = Signal()
    finished = Signal()
    skipped = Signal()
    
    def __init__(self, parent=None, startEnabled=False, closeEnabled=False, finishEnabled=False, nextGreyed=False) -> None:
        super().__init__(parent=parent)
        self.l = QVBoxLayout()
        self.setLayout(self.l)
        
        if(readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "AppsUseLightTheme", 1)==0):
            self.iconMode = "white"
            self.negIconMode = "black"
        else:
            self.iconMode = "black"
            self.negIconMode = "white"
        
        self.navLayout = QHBoxLayout()
        if closeEnabled:
            closeButton = QPushButton(_("Skip"))
            closeButton.setFixedSize(self.getPx(96), self.getPx(36))
            closeButton.setIcon(QIcon(getPath(f"close_{self.iconMode}.png")))
            closeButton.clicked.connect(lambda: self.outAnim(self.skipped.emit))
            self.navLayout.addWidget(closeButton)
        self.navLayout.addStretch()
        if startEnabled:
            startButton = QPushButton(_("Start"))
            startButton.setLayoutDirection(Qt.RightToLeft)
            startButton.setFixedSize(self.getPx(96), self.getPx(36))
            startButton.setIcon(QIcon(getPath(f"next_{self.negIconMode}.png")))
            startButton.clicked.connect(lambda: self.outAnim(self.next.emit))
            startButton.setObjectName("AccentButton")
            self.navLayout.addWidget(startButton)
        else:
            backButton = QPushButton("")
            backButton.setFixedSize(self.getPx(36), self.getPx(36))
            backButton.clicked.connect(lambda: self.invertedOutAnim(self.previous.emit))
            backButton.setIcon(QIcon(getPath(f"previous_{self.iconMode}.png")))
            self.navLayout.addWidget(backButton)
            if finishEnabled:
                finishButton = QPushButton(_("Finish"))
                finishButton.setObjectName("AccentButton")
                finishButton.setFixedSize(self.getPx(96), self.getPx(36))
                finishButton.setLayoutDirection(Qt.RightToLeft)
                finishButton.clicked.connect(lambda: self.outAnim(self.finished.emit))
                self.navLayout.addWidget(finishButton)
            else:
                self.nextButton = QPushButton("")
                self.nextButton.setEnabled(not nextGreyed)
                self.nextButton.setFixedSize(self.getPx(36), self.getPx(36))
                self.nextButton.clicked.connect(lambda:self.outAnim(self.next.emit))
                self.nextButton.setIcon(QIcon(getPath(f"next_{self.negIconMode}.png")))
                self.nextButton.setObjectName("AccentButton")
                self.navLayout.addWidget(self.nextButton)
                
    def enableNextButton(self) -> None:
        self.nextButton.setEnabled(True)
           
    def nextWidget(self):
        self.outAnim(self.next.emit)
    
    def setCentralWidget(self, w: QWidget) -> QWidget:
        self.l.addWidget(w, stretch=1)
        self.l.addLayout(self.navLayout, stretch=0)
        
    def inAnim(self) -> None:
        bgAnim = QPropertyAnimation(self, b"pos", self)
        pos = self.pos()
        pos.setX(pos.x()+self.width())
        bgAnim.setStartValue(pos)
        bgAnim.setEndValue(self.pos())
        bgAnim.setEasingCurve(QEasingCurve.OutExpo)
        bgAnim.setDuration(200)
        bgAnim.start()
        
    def invertedinAnim(self) -> None:
        bgAnim = QPropertyAnimation(self, b"pos", self)
        pos = self.pos()
        pos.setX(pos.x()-self.width())
        bgAnim.setStartValue(pos)
        bgAnim.setEndValue(self.pos())
        bgAnim.setEasingCurve(QEasingCurve.OutExpo)
        bgAnim.setDuration(200)
        bgAnim.start()
        
    def outAnim(self, f) -> None:
        bgAnim = QPropertyAnimation(self, b"pos", self)
        bgAnim.setStartValue(self.pos())
        pos = self.pos()
        pos.setX(pos.x()-self.width())
        bgAnim.setEndValue(pos)
        bgAnim.setEasingCurve(QEasingCurve.InExpo)
        bgAnim.setDuration(200)
        bgAnim.start()
        bgAnim.finished.connect(f)
    
    def invertedOutAnim(self, f) -> None:
        bgAnim = QPropertyAnimation(self, b"pos", self)
        bgAnim.setStartValue(self.pos())
        pos = self.pos()
        pos.setX(pos.x()+self.width())
        bgAnim.setEndValue(pos)
        bgAnim.setEasingCurve(QEasingCurve.InExpo)
        bgAnim.setDuration(200)
        bgAnim.start()
        bgAnim.finished.connect(f)
    
    def getPx(self, original) -> int:
        return round(original*(self.screen().logicalDotsPerInch()/96))
    
    def window(self) -> WelcomeWindow:
        return super().window()

class IconLabel(QWidget):
    def __init__(self, size=96, frame=True) -> None:
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground)
        if frame:
            self.setObjectName("SampleItem")
        else:
            self.setObjectName("FramelessSampleItem")
        self.iconSize = size
        self.setLayout(QHBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.iconLabel = QLabel()
        self.iconLabel.setMinimumHeight(self.getPx(self.iconSize+40))
        self.iconLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setMinimumHeight(self.getPx(self.iconSize))
        self.textLabel = QLabel()
        self.textLabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.textLabel.setWordWrap(True)
        self.textLabel.setStyleSheet("font-size: 10pt;")
        self.textLabel.setOpenExternalLinks(True)
        if frame: self.layout().addSpacing(self.getPx(40/96*self.iconSize))
        self.layout().addWidget(self.iconLabel, stretch=0)
        self.layout().addSpacing(self.getPx(30/96*self.iconSize))
        self.layout().addWidget(self.textLabel, stretch=1)
        if frame: self.layout().addSpacing(self.getPx(30/96*self.iconSize))
        
    def setText(self, text: str) -> None:
        self.textLabel.setText(text)
        
    def setIcon(self, path: str) -> None:
        self.iconLabel.setPixmap(QIcon(getPath(path)).pixmap(self.getPx(self.iconSize), self.getPx(self.iconSize)))
        
    def getPx(self, original) -> int:
        return round(original*(self.screen().logicalDotsPerInch()/96))

class ButtonLabel(QWidget):
    clicked = Signal()
    def __init__(self, size=96) -> None:
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground)
        self.setObjectName("SampleItem")
        self.iconSize = size
        self.setLayout(QHBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.iconLabel = QLabel()
        self.iconLabel.setMinimumHeight(self.getPx(self.iconSize+40))
        self.iconLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setMinimumHeight(self.getPx(self.iconSize))
        self.textLabel = QLabel()
        self.textLabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.textLabel.setWordWrap(True)
        self.textLabel.setStyleSheet("font-size: 10pt;")
        self.textLabel.setOpenExternalLinks(True)
        self.button = QPushButton()
        self.button.clicked.connect(self.clicked.emit)
        self.layout().addSpacing(self.getPx(40/96*self.iconSize))
        self.layout().addWidget(self.iconLabel, stretch=0)
        self.layout().addSpacing(self.getPx(20/96*self.iconSize))
        self.layout().addWidget(self.textLabel, stretch=1)
        self.layout().addSpacing(self.getPx(20/96*self.iconSize))
        self.layout().addWidget(self.button, stretch=0)
        self.layout().addSpacing(self.getPx(40/96*self.iconSize))
        
    def setText(self, text: str) -> None:
        self.textLabel.setText(text)
    
    def setButtonText(self, t: str) -> None:
        self.button.setText(t)
        
    def setIcon(self, path: str) -> None:
        self.iconLabel.setPixmap(QIcon(getPath(path)).pixmap(self.getPx(self.iconSize), self.getPx(self.iconSize)))
        
    def getPx(self, original) -> int:
        return round(original*(self.screen().logicalDotsPerInch()/96))

class ClickableLabel(QLabel):
    clicked = Signal()
    def __init__(self) -> None:
        super().__init__()
        self.setMouseTracking(True)
    
    def mousePressEvent(self, ev) -> None:
        self.clicked.emit()
        return super().mousePressEvent(ev)
    
class ClickableButtonLabel(QPushButton):
    clicked = Signal()
    def __init__(self, size=96) -> None:
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground)
        self.setObjectName("ButtonItem")
        self.iconSize = size
        self.setLayout(QHBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.iconLabel = QLabel()
        self.iconLabel.setMinimumHeight(self.getPx(self.iconSize))
        self.iconLabel.setMinimumWidth(self.getPx(size))
        self.iconLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setMinimumHeight(self.getPx(self.iconSize))
        self.textLabel = QLabel()
        self.textLabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.textLabel.setWordWrap(True)
        self.textLabel.setStyleSheet("font-size: 10pt;")
        self.textLabel.setOpenExternalLinks(True)
        self.layout().addSpacing(self.getPx(40/96*self.iconSize))
        self.layout().addWidget(self.iconLabel, stretch=0)
        self.layout().addSpacing(self.getPx(20/96*self.iconSize))
        self.layout().addWidget(self.textLabel, stretch=1)
        self.layout().addSpacing(self.getPx(40/96*self.iconSize))
        
    def setText(self, text: str) -> None:
        self.textLabel.setText(text)
    
    def setButtonText(self, t: str) -> None:
        self.button.setText(t)
        
    def setIcon(self, path: str) -> None:
        self.iconLabel.setPixmap(QIcon(getPath(path)).pixmap(self.getPx(self.iconSize), self.getPx(self.iconSize), Mode=Qt.KeepAspectRatio))
        
    def getPx(self, original) -> int:
        return round(original*(self.screen().logicalDotsPerInch()/96))

class MovableFocusSelector(QLabel):
    def __init__(self, parent: QWidget = None) -> None:
        super().__init__(parent=parent)
        self.setObjectName("FocusSelector")
        
    def move(self, x: int, y: int) -> None:
        return super().move(x, y)
    
    def resize(self, w: int, h: int) -> None:
        return super().resize(w+17, h+17)

class ClickableButtonLabelWithBiggerIcon(QPushButton):
    def __init__(self, size=96) -> None:
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground)
        self.setObjectName("ButtonItem")
        self.iconSize = size
        self.setCheckable(True)
        self.setLayout(QHBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.iconLabel = ClickableLabel()
        self.iconLabel.setMinimumHeight(self.getPx(self.iconSize))
        self.iconLabel.setMinimumWidth(self.getPx(size))
        self.iconLabel.clicked.connect(self.animateClick)
        self.iconLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setMinimumHeight(self.getPx(self.iconSize))
        self.textLabel = ClickableLabel()
        self.textLabel.clicked.connect(self.animateClick)
        self.textLabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.textLabel.setWordWrap(True)
        self.textLabel.setStyleSheet("font-size: 10pt;")
        self.textLabel.setOpenExternalLinks(True)
        self.layout().addSpacing(self.getPx(20/96*self.iconSize))
        self.layout().addWidget(self.iconLabel, stretch=0)
        self.layout().addSpacing(self.getPx(20/96*self.iconSize))
        self.layout().addWidget(self.textLabel, stretch=1)
        self.layout().addSpacing(self.getPx(40/96*self.iconSize))
        
    def setText(self, text: str) -> None:
        self.textLabel.setText(text)
    
    def setButtonText(self, t: str) -> None:
        self.button.setText(t)
        
    def setIcon(self, path: str) -> None:
        self.iconLabel.setPixmap(QIcon(getPath(path)).pixmap(QSize(self.getPx(self.iconSize+20), self.getPx(self.iconSize+20)), mode=QIcon.Normal))
        
    def getPx(self, original) -> int:
        return round(original*(self.screen().logicalDotsPerInch()/96))  
   
class FirstRunSlide(BasicNavWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent, startEnabled=True, closeEnabled=True)
        widget = QWidget()
        self.next.connect(self.startWin)
        l = QHBoxLayout()
        l.setContentsMargins(0, self.getPx(10), 0, self.getPx(10))
        widget.setLayout(l)
        vl = QVBoxLayout()
        l.addSpacing(self.getPx(10))
        l.addLayout(vl)
        vl.addSpacing(self.getPx(30))
        
        label1 = IconLabel(size=64, frame=False)
        label1.setIcon("icon.png")
        label1.setText(f"""
             <h1>Welcome to Elevenclock!</h1>
             If you already know how does this work, or you want to skip the welcome wizard, please click on the bottom-left <i>Skip</i> button.""")
        
        
        label3 = IconLabel(size=64)
        label3.setIcon("msstore_color.png")
        label3.setText("""
             <h3>Wait a minute!</h3>
             Please make sure to install ElevenClock from official sources only, such as the Microsoft Store, Github, SomePythonThings or other trustworthy webpages. Also, using ElevenClock implies the acceptation of the <b>Apache 2.0 license</b>""")

        label2 = IconLabel(size=64)
        label2.setIcon("customize_color.png")
        label2.setText("""
             <h3>Do you have a minute? This wizard will help you configure and customize ElevenClock. Click Start to get started!</h3>
             Remember that this wizard can be run at any time from the Settings Window""")
        
        vl.addWidget(label1)
        vl.addStretch()
        vl.addWidget(label2)
        vl.addStretch()
        vl.addWidget(label3)
        vl.addStretch()
        self.setCentralWidget(widget)
        
    def startWin(self) -> None:
        self.window().fillScreen()
    
    def getPx(self, original) -> int:
        return round(original*(self.screen().logicalDotsPerInch()/96))
           
class LastSlide(BasicNavWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent, finishEnabled=True)
        widget = QWidget()
        l = QHBoxLayout()
        l.setContentsMargins(0, self.getPx(10), 0, self.getPx(10))
        widget.setLayout(l)
        vl = QVBoxLayout()
        l.addSpacing(self.getPx(10))
        l.addLayout(vl)
        
        label1 = IconLabel(size=64, frame=False)
        label1.setIcon("")
        label1.setText(f"""<h1>You are now ready to go!</h1>
                       <h3>But here are other things you can do:</h3>""")
        
        settings = ButtonLabel(size=64)
        settings.setIcon("deskSettings_color.png")
        settings.setText("""
             <h3>Customize ElevenClock even more</h3>
             Open the settings window and customize ElevenClock even more.""")
        settings.setButtonText("Open")
        settings.clicked.connect(lambda: closeAndOpenSettings())
        
        def closeAndOpenSettings():
            globals.sw.show()
            self.finished.emit()
        
        donate = ButtonLabel(size=64)
        donate.setIcon("coffee_color.png")
        donate.setText("""
             <h3>Suport the developer</h3>
             Developing is hard, and this aplication is free. But if you liked the application, you can always <b>buy me a coffee</b> :)""")
        donate.setButtonText("Make a donation!")
        donate.clicked.connect(lambda: os.startfile("https://ko-fi.com/martinet101"))
        
        report = ButtonLabel(size=64)
        report.setIcon("github_color.png")
        report.setText("""
             <h3>View ElevenClock on GitHub</h3>
             View ElevenClock's source code. From there, you can report bugs or suggest features, or even contribute direcly to The ElevenClock Project""")
        report.setButtonText("Open GitHub")
        report.clicked.connect(lambda: os.startfile("https://github.com/martinet101/ElevenClock"))

        vl.addWidget(label1)
        vl.addStretch()
        vl.addWidget(settings)
        vl.addStretch()
        vl.addWidget(donate)
        vl.addStretch()
        vl.addWidget(report)
        vl.addStretch()
        self.setCentralWidget(widget)
        
    
    def getPx(self, original) -> int:
        return round(original*(self.screen().logicalDotsPerInch()/96))
        
class SelectModeSlide(BasicNavWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent, nextGreyed=True)
        self.defaultSelected = False
        widget = QWidget()
        l = QHBoxLayout()
        l.setContentsMargins(0, self.getPx(10), 0, self.getPx(10))
        widget.setLayout(l)
        self.selector = MovableFocusSelector(self)
        self.selector.hide()
        vl = QVBoxLayout()
        l.addSpacing(self.getPx(10))
        l.addLayout(vl)
        
        label1 = IconLabel(size=self.getPx(96), frame=False)
        label1.setIcon(getPath("pcDesk_color.png"))
        label1.setText(f"""<h1>How do you want ElevenClock to work?</h1>
                       <h3>Please select one of the following and click next</h3>""")
        
        self.secondaryClock = ClickableButtonLabelWithBiggerIcon(size=96)
        self.secondaryClock.setIcon(getPath(f"defaultClock_{self.iconMode}.png"))
        self.secondaryClock.clicked.connect(lambda: self.toggleClockMode("secondary", shouldChangePrefs=True))
        self.secondaryClock.setText("""
            <h3>Add the secondary clock</h3>
            Simple clock that mimics the default clock behaviour, to add in secondary displays""")
        
        self.formattedClock = ClickableButtonLabelWithBiggerIcon(size=96)
        self.formattedClock.setIcon(getPath(f"formatClock_{self.iconMode}.png"))
        self.formattedClock.clicked.connect(lambda: self.toggleClockMode("format", shouldChangePrefs=True))
        self.formattedClock.setText("""
             <h3>Show clocks on every monitor and customize the date and time</h3>
             Replace the system clock and add a clock on secondary displays to be able to enable seconds, weekday, disable date, time, set custom formats, etc...""")
        
        self.customClock = ClickableButtonLabelWithBiggerIcon(size=96)
        self.customClock.setIcon(getPath(f"customClock_{self.iconMode}.png"))
        self.customClock.clicked.connect(lambda: self.toggleClockMode("custom", shouldChangePrefs=True))
        self.customClock.setText("""
            <h3>Show clocks on every monitor and customize them entierly</h3>
            Replace every clock and customize it adding seconds, weekday or weeknumber, removing the date, changing the font or the color background, etc...""")
        
        vl.addWidget(label1)
        vl.addStretch()
        vl.addWidget(self.secondaryClock)
        vl.addStretch()
        vl.addWidget(self.formattedClock)
        vl.addStretch()
        vl.addWidget(self.customClock)
        vl.addStretch()
        self.setCentralWidget(widget)
        
        self.clockMode = ""
        
    def toggleClockMode(self, mode: str, shouldChangePrefs: bool = False) -> None:
        self.enableNextButton()
        if shouldChangePrefs:
            self.defaultSelected = True
        if mode == "secondary":
            self.clockMode = "secondary"
            self.moveSelector(self.secondaryClock)
            setSettings("DisableTaskbarBackgroundColor", False, r=False)
            setSettings("ForceClockOnFirstMonitor", False, r=False)
            setSettings("HideClockOnSecondaryMonitors", False, r=False)
            setSettings("DisableTime", False, r=False)
            setSettings("EnableSeconds", False, r=False)
            setSettings("DisableDate", False, r=False)
            setSettings("EnableWeekNumber", False, r=False)
            setSettings("EnableWeekDay", False, r=False)
            setSettings("UseCustomFont", False, r=False)
            setSettings("UseCustomFontSize", False, r=False)
            setSettings("UseCustomFontColor", False, r=False)
            setSettings("UseCustomBgColor", False, r=False)
            setSettings("DisableTaskbarBackgroundColor", False, r=False)
            setSettings("CenterAlignment", False, r=shouldChangePrefs)
        elif mode == "format":
            self.clockMode = "format"
            self.moveSelector(self.formattedClock)
            setSettings("DisableTaskbarBackgroundColor", False, r=False)
            setSettings("UseCustomBgColor", False, r=False)
            setSettings("ForceClockOnFirstMonitor", True, r=False)
            setSettings("HideClockOnSecondaryMonitors", False, r=False)
            setSettings("UseCustomFont", False, r=False)
            setSettings("UseCustomFontSize", False, r=False)
            setSettings("UseCustomFontColor", False, r=False)
            setSettings("DisableTaskbarBackgroundColor", False, r=False)
            setSettings("CenterAlignment", False, r=shouldChangePrefs)
        elif mode == "custom":
            self.clockMode = "custom"
            self.moveSelector(self.customClock)
            setSettings("DisableTaskbarBackgroundColor", False, r=False)
            setSettings("UseCustomBgColor", False, r=False)
            setSettings("ForceClockOnFirstMonitor", True, r=False)
            setSettings("DisableTaskbarBackgroundColor", False, r=False)
            setSettings("HideClockOnSecondaryMonitors", False, r=shouldChangePrefs)
        else:
            raise ValueError("Function toggleCheckMode() called with invalid arguments. Accepted values are: custom, format, secondary")
                
    def showEvent(self, event) -> None:
        if not self.defaultSelected:
            self.toggleClockMode("format")
        return super().showEvent(event)
    
    def moveSelector(self, w: QWidget) -> None:
        if not self.selector.isVisible():
            self.selector.show()
            self.selector.move(w.pos().x(), w.pos().y())
            self.selector.resize(w.size().width(), w.size().height())
        else:
            posAnim = QPropertyAnimation(self.selector, b"pos", self)
            posAnim.setStartValue(self.selector.pos())
            posAnim.setEndValue(w.pos())
            posAnim.setEasingCurve(QEasingCurve.InOutCirc)
            posAnim.setDuration(200)
            
            sizeAnim = QPropertyAnimation(self.selector, b"size", self)
            sizeAnim.setStartValue(self.selector.size())
            s = w.size()
            s.setWidth(s.width()+18)
            s.setHeight(s.height()+18)
            sizeAnim.setEndValue(s)
            sizeAnim.setEasingCurve(QEasingCurve.InOutCirc)
            sizeAnim.setDuration(200)
            
            posAnim.start()
            sizeAnim.start()
    
    def getPx(self, original) -> int:
        return round(original*(self.screen().logicalDotsPerInch()/96))

class SelectFullScreenSlide(BasicNavWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent, nextGreyed=True)
        self.defaultSelected = False
        widget = QWidget()
        l = QHBoxLayout()
        l.setContentsMargins(0, self.getPx(10), 0, self.getPx(10))
        widget.setLayout(l)
        self.selector = MovableFocusSelector(self)
        self.selector.hide()
        vl = QVBoxLayout()
        l.addSpacing(self.getPx(10))
        l.addLayout(vl)
        
        label1 = IconLabel(size=self.getPx(96), frame=False)
        label1.setIcon(getPath("video_color.png"))
        label1.setText(f"""<h1>One last thing: Fullscreen!</h1>
                       <h3>ElevenClock can hide when there's a fullscreen window present (when you are watching a video, etc.), but it can also show over those windows (It might be useful if you use fullscreened terminals, etc.).<br><br>Please select one of the following and click next</h3>""")
        
        self.secondaryClock = ClickableButtonLabelWithBiggerIcon(size=96)
        self.secondaryClock.setIcon(getPath(f"hide_color.png"))
        self.secondaryClock.clicked.connect(lambda: self.toggleClockMode("hide", shouldChangePrefs=True))
        self.secondaryClock.setText("""
            <h3>Hide the clock (<i>Recommended</i>)</h3>
            Hide the clock, as the default windows clock would do.""")
        
        self.formattedClock = ClickableButtonLabelWithBiggerIcon(size=96)
        self.formattedClock.setIcon(getPath(f"show_color.png"))
        self.formattedClock.clicked.connect(lambda: self.toggleClockMode("show", shouldChangePrefs=True))
        self.formattedClock.setText("""
            <h3>Show the clock over the fullscreen window</h3>
            Show the clock over fullscreen windows. This might cover some in-app controls, like youtube's exit fullscreen button.""")
        
        
        vl.addWidget(label1)
        vl.addStretch()
        vl.addWidget(self.secondaryClock)
        vl.addStretch()
        vl.addWidget(self.formattedClock)
        vl.addStretch()
        self.setCentralWidget(widget)
        
        self.clockMode = ""
        
    def toggleClockMode(self, mode: str, shouldChangePrefs: bool = False) -> None:
        self.enableNextButton()
        if shouldChangePrefs:
            self.defaultSelected = True
        if mode == "hide":
            self.clockMode = "hide"
            self.moveSelector(self.secondaryClock)
            setSettings("DisableHideOnFullScreen", False, r=shouldChangePrefs)
        elif mode == "show":
            self.clockMode = "show"
            self.moveSelector(self.formattedClock)
            setSettings("DisableHideOnFullScreen", True, r=shouldChangePrefs)
        else:
            raise ValueError("Function toggleCheckMode() called with invalid arguments. Accepted values are: hide, show")
                
    def showEvent(self, event) -> None:
        if not self.defaultSelected:
            self.toggleClockMode("hide")
        return super().showEvent(event)
    
    def moveSelector(self, w: QWidget) -> None:
        if not self.selector.isVisible():
            self.selector.show()
            self.selector.move(w.pos().x(), w.pos().y())
            self.selector.resize(w.size().width(), w.size().height())
        else:
            posAnim = QPropertyAnimation(self.selector, b"pos", self)
            posAnim.setStartValue(self.selector.pos())
            posAnim.setEndValue(w.pos())
            posAnim.setEasingCurve(QEasingCurve.InOutCirc)
            posAnim.setDuration(200)
            
            sizeAnim = QPropertyAnimation(self.selector, b"size", self)
            sizeAnim.setStartValue(self.selector.size())
            s = w.size()
            s.setWidth(s.width()+18)
            s.setHeight(s.height()+18)
            sizeAnim.setEndValue(s)
            sizeAnim.setEasingCurve(QEasingCurve.InOutCirc)
            sizeAnim.setDuration(200)
            
            posAnim.start()
            sizeAnim.start()
    
    def getPx(self, original) -> int:
        return round(original*(self.screen().logicalDotsPerInch()/96))

if __name__ == "__main__":
    from ctypes import c_int, windll
    windll.shcore.SetProcessDpiAwareness(c_int(2))
    import __init__