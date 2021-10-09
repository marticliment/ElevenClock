from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import winreg, locale, os, tempfile, subprocess
from urllib.request import urlopen
import hashlib
from ctypes import windll
import win32gui

tdir = tempfile.TemporaryDirectory()
tempDir = tdir.name

import time, sys, threading, datetime, webbrowser
from pynput.keyboard import Controller, Key
from pynput.mouse import Controller as MouseController

version = 1.9
lastTheme = 0
seconddoubleclick = False
showSeconds = 0

mController = MouseController()

def getMousePos():
    return QPoint(mController.position[0], mController.position[1])


if hasattr(sys, 'frozen'):
    realpath = sys._MEIPASS
else:
    realpath = '/'.join(sys.argv[0].replace("\\", "/").split("/")[:-1])
    
def readRegedit(aKey, sKey, default, storage=winreg.HKEY_CURRENT_USER):
    registry = winreg.ConnectRegistry(None, storage)
    reg_keypath = aKey
    try:
        reg_key = winreg.OpenKey(registry, reg_keypath)
    except FileNotFoundError as e:
        print(e)
        return default

    for i in range(1024):
        try:
            value_name, value, _ = winreg.EnumValue(reg_key, i)
            if value_name == sKey:
                return value
        except OSError as e:
            print(e)
            return default


#get system locale and formats and setting them up


showSeconds = readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "ShowSecondsInSystemClock", 0)
locale.setlocale(locale.LC_ALL, readRegedit(r"Control Panel\International", "LocaleName", "en_US"))
dateTimeFormat = "%HH:%M\n%d/%m/%Y"

dateMode = readRegedit(r"Control Panel\International", "sShortDate", "dd/MM/yyyy")
print(dateMode)
dateMode = dateMode.replace("ddd", "%a").replace("dd", "%$").replace("d", "%#d").replace("$", "d").replace("MMM", "%b").replace("MM", "%m").replace("M", "%#m").replace("yyyy", "%Y").replace("yy", "%y")

timeMode = readRegedit(r"Control Panel\International", "sShortTime", "H:mm")
print(timeMode)
timeMode = timeMode.replace("HH", "%$").replace("H", "%#H").replace("$", "H").replace("hh", "%I").replace("h", "%#I").replace("mm", "%M").replace("m", "%#M").replace("tt", "%p").replace("t", "%p").replace("ss", "%S").replace("s", "%#S")
if not("s" in timeMode) and showSeconds==1:
    for separator in ":.-/_":
        if(separator in timeMode):
            if("#" in timeMode):
                timeMode += f"{separator}%#S"
            else:
                timeMode += f"{separator}%S"

for separator in ":.-/_":
    timeMode = timeMode.replace(f" %p{separator}%S", f"{separator}%S %p")
    timeMode = timeMode.replace(f" %p{separator}%#S", f"{separator}%#S %p")
        
print(timeMode)

dateTimeFormat = dateTimeFormat.replace("%d/%m/%Y", dateMode).replace("%HH:%M", timeMode)
print(dateTimeFormat)


class RestartSignal(QObject):
    
    restartSignal = Signal()
    
    def __init__(self) -> None:
        super().__init__()

class Clock(QMainWindow):
    
    refresh = Signal()
    hideSignal = Signal()
    def __init__(self, w, h, dpix, dpiy, screen):
        super().__init__()
        global lastTheme
        self.screen: QScreen = screen
        self.shouldBeVisible = True
        self.refresh.connect(self.refreshandShow)
        self.hideSignal.connect(self.hide)
        self.keyboard = Controller()
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.Tool)
        self.autoHide = readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\StuckRects3", "Settings", b'0\x00\x00\x00\xfe\xff\xff\xffz\xf4\x00\x00\x03\x00\x00\x00T\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x08\x04\x00\x00\x80\x07\x00\x008\x04\x00\x00`\x00\x00\x00\x01\x00\x00\x00')[8]==123
        self.setToolTip(f"ElevenClock version {version}\n\nClick once to show notifications\nClick 4 times to show help")
        try:
            if(readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\StuckRects3", "Settings", b'0\x00\x00\x00\xfe\xff\xff\xffz\xf4\x00\x00\x03\x00\x00\x00T\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x08\x04\x00\x00\x80\x07\x00\x008\x04\x00\x00`\x00\x00\x00\x01\x00\x00\x00')[12] == 1):
                h = 48*dpiy
        except:
            pass
        self.move(w-(108*dpix), h-(48*dpiy))
        self.resize(100*dpix, 48*dpiy)
        print("Clock geometry:", self.geometry())
        self.setStyleSheet(f"background-color: rgba(0, 0, 0, 0.01);margin: 5px; border-radius: 5px; ")#font-size: {int(12*fontSizeMultiplier)}px;")
        self.font: QFont = QFont("Segoe UI Variable")
        self.font.setPointSizeF(9)
        self.font.setStyleStrategy(QFont.PreferOutline)
        self.font.setLetterSpacing(QFont.PercentageSpacing, 100)
        self.font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.label = Label(datetime.datetime.now().strftime(dateTimeFormat))
        self.label.setFont(self.font)
        self.label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        if(readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "SystemUsesLightTheme",  1) == 0):
            lastTheme = 0
            self.label.setStyleSheet("padding: 1px;padding-right: 5px; color: white;")
            self.label.bgopacity = .1
            self.font.setWeight(500)
            self.label.setFont(self.font)
        else:
            lastTheme = 1
            self.label.setStyleSheet("padding: 1px;padding-right: 5px; color: black;")
            self.label.bgopacity = .5
            self.font.setWeight(400)
            self.label.setFont(self.font)
        self.label.clicked.connect(lambda: self.showCalendar())
        self.setCentralWidget(self.label)
        self.show()
        self.raise_()
        self.setFocus()
        
        self.user32 = windll.user32
        self.user32.SetProcessDPIAware() # optional, makes functions return real pixel numbers instead of scaled values
        threading.Thread(target=self.fivesecsloop, daemon=True).start()

        self.full_screen_rect = (self.screen.geometry().x(), self.screen.geometry().y(), self.screen.geometry().x()+self.screen.geometry().width(), self.screen.geometry().y()+self.screen.geometry().height())
        print("Full screen rect: ", self.full_screen_rect)


    def theresFullScreenWin(self):
        try:
            fullscreen = False
            
            def absoluteValuesAreEqual(a, b):
                return abs(a[0]) == abs(b[0]) and abs(a[1]) == abs(b[1]) and abs(a[2]) == abs(b[2]) and abs(a[3]) == abs(b[3])
            
            def winEnumHandler( hwnd, ctx ):
                nonlocal fullscreen
                if win32gui.IsWindowVisible( hwnd ):
                    if(absoluteValuesAreEqual(win32gui.GetWindowRect(hwnd), self.full_screen_rect)):
                        fullscreen = True

            win32gui.EnumWindows( winEnumHandler, None )
            return fullscreen
        except Exception as e:
            print(e)
            return False
            
    def fivesecsloop(self):
        while True:
            time.sleep(0.05)
            if not(self.theresFullScreenWin()):
                if self.autoHide:
                    print(getMousePos().y())
                    print(self.screen.geometry().y()+self.screen.geometry().height())
                    if(getMousePos().y()+2 >= self.screen.geometry().y()+self.screen.geometry().height()):
                        self.refresh.emit()
                    else:
                        self.hideSignal.emit()
                else:
                    self.refresh.emit()
            else:
                self.hideSignal.emit()
        
    def showCalendar(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press('n')
        self.keyboard.release('n')
        self.keyboard.release(Key.cmd)
        
    def focusOutEvent(self, event: QFocusEvent) -> None:
        self.refresh.emit()
        
    def refreshandShow(self):
        global lastTheme
        if(self.shouldBeVisible):
            self.show()
            self.raise_()
            theme = readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "SystemUsesLightTheme", 1)
            if(theme != lastTheme):
                if(theme == 0):
                    lastTheme = 0
                    self.label.setStyleSheet("padding: 1px;padding-right: 5px; color: white;")
                    self.label.bgopacity = 0.1
                    self.font.setWeight(500)
                    self.label.setFont(self.font)
                else:
                    lastTheme = 1
                    self.label.setStyleSheet("padding: 1px;padding-right: 5px; color: black;")
                    self.label.bgopacity = .5
                    self.font.setWeight(400)
                    self.label.setFont(self.font)
                
            self.label.setText(datetime.datetime.now().strftime(dateTimeFormat))
        
    def closeEvent(self, event: QCloseEvent) -> None:
        self.shouldBeVisible = False
        return super().closeEvent(event)
        
class Label(QLabel):
    clicked = Signal()
    def __init__(self, text):
        super().__init__(text)
        self.setMouseTracking(True)
        self.backgroundwidget = QWidget(self)
        self.color = "255, 255, 255"
        self.bgopacity = 0.1
        self.backgroundwidget.setStyleSheet(f"background-color: rgba({self.color}, 0);border-top: 1px solid rgba({self.color},0);")
        self.backgroundwidget.show()
        self.showBackground = QVariantAnimation()
        self.showBackground.setStartValue(.001) # Not 0 to prevent white flashing on the border
        self.showBackground.setEndValue(self.bgopacity)
        self.showBackground.setDuration(100)
        self.showBackground.setEasingCurve(QEasingCurve.InOutQuad) # Not strictly required, just for the aesthetics
        self.showBackground.valueChanged.connect(lambda opacity: self.backgroundwidget.setStyleSheet(f"background-color: rgba({self.color}, {opacity/2});border-top: 1px solid rgba({self.color}, {opacity});"))
        self.hideBackground = QVariantAnimation()
        self.hideBackground.setStartValue(self.bgopacity)
        self.hideBackground.setEndValue(.001) # Not 0 to prevent white flashing on the border
        self.hideBackground.setDuration(100)
        self.hideBackground.setEasingCurve(QEasingCurve.InOutQuad) # Not strictly required, just for the aesthetics
        self.hideBackground.valueChanged.connect(lambda opacity: self.backgroundwidget.setStyleSheet(f"background-color: rgba({self.color}, {opacity/2});border-top: 1px solid rgba({self.color}, {opacity});"))
        
        
    def enterEvent(self, event: QEvent) -> None:
        geometry: QRect = self.getTextUsedSpaceRect()
        self.showBackground.setStartValue(.001)
        self.showBackground.setEndValue(self.bgopacity) # Not 0 to prevent white flashing on the border
        if(self.width() > geometry.width()):
            self.backgroundwidget.move(self.width()-geometry.width(), 0)
            self.backgroundwidget.resize(geometry.width(), self.height())
        else:
            print("Background widget is bigger than parent!")
            self.backgroundwidget.move(0, 0)
            self.backgroundwidget.resize(100, self.height())
        self.showBackground.start()
        
        
        
        return super().enterEvent(event)
    
    def leaveEvent(self, event: QEvent) -> None:
        self.hideBackground.setStartValue(self.bgopacity)
        self.hideBackground.setEndValue(.001) # Not 0 to prevent white flashing on the border
        self.hideBackground.start()
        return super().leaveEvent(event)
    
    def getTextUsedSpaceRect(self):
        effectiveIndent = self.indent()
        trueMargin = self.margin()
        if(effectiveIndent < 0):
            if(self.frameWidth() == 0 or self.margin() > 0):
                effectiveIndent = 0
            elif(self.frameWidth() > 0):
                fm = QFontMetrics(self.font())
                effectiveIndent = fm.horizontalAdvance("x")
            if(self.frameWidth() > 0 and self.margin() < 0):
                trueMargin = 0

        fm = QFontMetrics(self.font())
        bRect: QRect = fm.boundingRect(self.text())
        bRect.setWidth(fm.horizontalAdvance(self.text()))

        indentOffset = effectiveIndent + trueMargin + self.frameWidth()
        offsetX = 0
        offsetY = 0
        if(self.alignment() and Qt.AlignHCenter):
            offsetX = self.rect().width() / 2 - bRect.width() / 2
        elif(self.alignment() and Qt.AlignRight):
            offsetX = self.rect().width() - bRect.width() - indentOffset
        elif(self.alignment() and Qt.AlignJustify):
            offsetX = trueMargin + self.frameWidth()
        elif(self.alignment() and Qt.AlignLeft):
            offsetX = indentOffset
        
        if(self.alignment() and Qt.AlignVCenter):
            offsetY = self.rect().height() / 2 - bRect.height() / 2
        elif(self.alignment() and Qt.AlignBottom):
            offsetY = self.rect().height() - bRect.height() - indentOffset
        elif(self.alignment() and Qt.AlignTop):
            offsetY = indentOffset
        

        bRect.moveTopLeft(self.rect().topLeft())
        bRect.setX(bRect.x() + offsetX)
        bRect.setWidth(bRect.width() + offsetX)
        bRect.setY(bRect.y() + offsetY)
        bRect.setHeight(bRect.height() + offsetY)

        return bRect


        
    def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        self.clicked.emit()
        return super().mouseReleaseEvent(ev)
    
    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:

        def toggleSeconddoubleclick():
            global seconddoubleclick
            time.sleep(1)
            seconddoubleclick = False
            
        global seconddoubleclick
        if(seconddoubleclick):
            webbrowser.open("http://www.somepythonthings.tk/redirect/?elevenclock")
        else:
            seconddoubleclick = True
            threading.Thread(target=toggleSeconddoubleclick).start()
        return super().mouseDoubleClickEvent(event)
        
class TaskbarIconTray(QSystemTrayIcon):
    def __init__(self, app=None):
        super().__init__(app)
        self.setIcon(QIcon(os.path.join(realpath, "icon.ico")))
        self.show()
        menu = QMenu("ElevenClock")
        reloadAction = QAction(f"Reload ElevenClock", app)
        reloadAction.triggered.connect(lambda: restartClocks())
        menu.addAction(reloadAction)
        hideAction = QAction(f"Hide ElevenClock", app)
        hideAction.triggered.connect(lambda: closeClocks())
        menu.addAction(hideAction)
        quitAction = QAction(f"Quit ElevenClock", app)
        quitAction.triggered.connect(lambda: sys.exit())
        menu.addAction(quitAction)
        menu.addSeparator()
        quitAction = QAction(f"Enable/Disable Seconds", app)
        quitAction.triggered.connect(lambda: os.startfile("https://www.howtogeek.com/325096/how-to-make-windows-10s-taskbar-clock-display-seconds/"))
        menu.addAction(quitAction)
        menu.addSeparator()
        nameAction = QAction(f"ElevenClock v{version}", app)
        nameAction.setEnabled(False)
        menu.addAction(nameAction)
        reportAction = QAction(f"Report a bug", app)
        reportAction.triggered.connect(lambda: os.startfile("https://github.com/martinet101/ElevenClock/issues/new/choose"))
        menu.addAction(reportAction)
        
        self.setContextMenu(menu)
        
        self.activated.connect(lambda: restartClocks())
        
        
        

QApplication.setAttribute(Qt.AA_DisableHighDpiScaling)



app = QApplication()
signal = RestartSignal()
i = TaskbarIconTray(app)
clocks = []
oldScreens = []
firstWinSkipped = False # This value should be set to false to hide first monitor clock

def updateChecker():
    while True:
        updateIfPossible()
        time.sleep(7200)

def updateIfPossible():
    try:
        print("Starting update check")
        response = urlopen("https://www.somepythonthings.tk/versions/elevenclock.ver")
        response = response.read().decode("utf8")
        if float(response.split("///")[0]) > version:
            print("Updates found!")
            url = response.split("///")[1].replace('\n', '')
            print(url)
            filedata = urlopen(url)
            datatowrite = filedata.read()
            filename = ""
            with open(os.path.join(tempDir, "SomePythonThings-ElevenClock-Updater.exe"), 'wb') as f:
                f.write(datatowrite)
                filename = f.name
            print(filename)
            if(hashlib.sha256(datatowrite).hexdigest().lower() == response.split("///")[2].replace("\n", "").lower()):
                print("Hash: ", response.split("///")[2].replace("\n", "").lower())
                print("Hash ok, starting update")
                subprocess.run('start /B "" "{0}" /silent'.format(filename), shell=True)
            else:
                print("Hash not ok")
                print("File hash: ", hashlib.sha256(datatowrite).hexdigest())
                print("Provided hash: ", response.split("///")[2].replace("\n", "").lower())
        else:
            print("updates not found")

    except Exception as e:
        print(f"Exception: {e}")

def loadClocks():
    global clocks, oldScreens, firstWinSkipped
    firstWinSkipped = False
    oldScreens = []
    for screen in app.screens():
        oldScreens.append(getGeometry(screen))
        print(screen, screen.geometry(), getGeometry(screen))
        screen: QScreen
        fontSizeMultiplier = screen.logicalDotsPerInchX()/96
        if(firstWinSkipped):
            clocks.append(Clock(screen.geometry().x()+screen.geometry().width(), screen.geometry().y()+screen.geometry().height(), screen.logicalDotsPerInchX()/96, screen.logicalDotsPerInchY()/96, screen))
        else: # Skip the primary display, as it has already the clock
            print("This is primay screen")
            firstWinSkipped = True

def getGeometry(screen: QScreen):
    return (screen.geometry().width(), screen.geometry().height(), screen.logicalDotsPerInchX(), screen.logicalDotsPerInchY())

def theyMatch(oldscreens, newscreens):
    if(len(oldscreens) != len(newscreens)):
        return False # If there are display changes
        
    for i in range(len(oldscreens)):
        old, new = oldscreens[i], newscreens[i]
        if(old != getGeometry(new)): # Check if screen dimensions or dpi have changed
            return False # They have changed (screens are not equal)
    return True # they have not changed (screens still the same)
            
def screenCheckThread():
    while theyMatch(oldScreens, app.screens()):
        time.sleep(1)
    signal.restartSignal.emit()
    
def closeClocks():
    for clock in clocks:
        clock.hide()
        clock.close()

def restartClocks():
    global clocks, dateTimeFormat, dateMode, timeMode, showSeconds
    
    
    showSeconds = readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "ShowSecondsInSystemClock", 0)
    locale.setlocale(locale.LC_ALL, readRegedit(r"Control Panel\International", "LocaleName", "en_US"))
    dateTimeFormat = "%HH:%M\n%d/%m/%Y"

    dateMode = readRegedit(r"Control Panel\International", "sShortDate", "dd/MM/yyyy")
    print(dateMode)
    dateMode = dateMode.replace("ddd", "%a").replace("dd", "%$").replace("d", "%#d").replace("$", "d").replace("MMM", "%b").replace("MM", "%m").replace("M", "%#m").replace("yyyy", "%Y").replace("yy", "%y")

    timeMode = readRegedit(r"Control Panel\International", "sShortTime", "H:mm")
    print(timeMode)
    timeMode = timeMode.replace("HH", "%$").replace("H", "%#H").replace("$", "H").replace("hh", "%I").replace("h", "%#I").replace("mm", "%M").replace("m", "%#M").replace("tt", "%p").replace("t", "%p").replace("ss", "%S").replace("s", "%#S")
    if not("s" in timeMode) and showSeconds==1:
        for separator in ":.-/_":
            if(separator in timeMode):
                if("#" in timeMode):
                    timeMode += f"{separator}%#S"
                else:
                    timeMode += f"{separator}%S"

    for separator in ":.-/_":
        timeMode = timeMode.replace(f" %p{separator}%S", f"{separator}%S %p")
        timeMode = timeMode.replace(f" %p{separator}%#S", f"{separator}%#S %p")
            
    print(timeMode)

    dateTimeFormat = dateTimeFormat.replace("%d/%m/%Y", dateMode).replace("%HH:%M", timeMode)
    print(dateTimeFormat)

    dateTimeFormat = dateTimeFormat.replace("%d/%m/%Y", dateMode).replace("%HH:%M", timeMode)
    print(dateTimeFormat)
    
    
    print(timeMode)
    for clock in clocks:
        clock.hide()
        clock.close()
    loadClocks()
    threading.Thread(target=screenCheckThread, daemon=True).start()

threading.Thread(target=updateChecker, daemon=True).start()
signal.restartSignal.connect(restartClocks)
loadClocks()
threading.Thread(target=screenCheckThread, daemon=True).start()

app.exec_()
sys.exit(0)
