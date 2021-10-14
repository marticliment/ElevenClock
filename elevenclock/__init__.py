from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import winreg, locale, os, tempfile, subprocess, socket, psutil, glob
from urllib.request import urlopen
import hashlib
from ctypes import windll
import win32gui
import time, sys, threading, datetime, webbrowser
from pynput.keyboard import Controller, Key
from pynput.mouse import Controller as MouseController

tdir = tempfile.TemporaryDirectory()
tempDir = tdir.name
version = 2.1
seconddoubleclick = False
showSeconds = 0
mController = MouseController()

def getMousePos():
    return QPoint(mController.position[0], mController.position[1])
  
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

def getSettings(s: str):
    try:
        return os.path.exists(os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock"), s))
    except Exception as e:
        print(e)

def setSettings(s: str, v: bool, r: bool = True):
    try:
        if(v):
            open(os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock"), s), "w").close()
        else:
            try:
                os.remove(os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock"), s))
            except FileNotFoundError:
                pass
        if(r):
            restartClocks()
            if(getSettings("DisableSystemTray")):
                i.hide()
            else:
                i.show()
    except Exception as e:
        print(e)

def updateChecker():
    while True:
        updateIfPossible()
        time.sleep(7200)

def updateIfPossible(force = False):
    try:
        if(not(getSettings("DisableAutoCheckForUpdates")) or force):
            print("Starting update check")
            integrityPass = False
            dmname = socket.gethostbyname_ex("versions.somepythonthings.tk")[0]
            if(dmname == "769432b9-3560-4f94-8f90-01c95844d994.id.repl.co" or getSettings("BypassDomainAuthCheck")): # Check provider IP to prevent exploits
                integrityPass = True
            response = urlopen("https://versions.somepythonthings.tk/versions/elevenclock.ver")
            response = response.read().decode("utf8")
            if float(response.split("///")[0]) > version:
                print("Updates found!")
                if(not(getSettings("EnableAutoInstallUpdates")) or force):
                    if(integrityPass):
                        url = "https://github.com/martinet101/ElevenClock/releases/latest/download/ElevenClock.Installer.exe"
                        print(url)
                        filedata = urlopen(url)
                        datatowrite = filedata.read()
                        filename = ""
                        with open(os.path.join(tempDir, "SomePythonThings-ElevenClock-Updater.exe"), 'wb') as f:
                            f.write(datatowrite)
                            filename = f.name
                            print(filename)
                        print(dmname)
                        if(hashlib.sha256(datatowrite).hexdigest().lower() == response.split("///")[2].replace("\n", "").lower()):
                            print("Hash: ", response.split("///")[2].replace("\n", "").lower())
                            print("Hash ok, starting update")
                            if(getSettings("EnableSilentUpdates") and not(force)):
                                subprocess.run('start /B "" "{0}" /verysilent'.format(filename), shell=True)
                            else:
                                subprocess.run('start /B "" "{0}" /silent'.format(filename), shell=True)
                        else:
                            print("Hash not ok")
                            print("File hash: ", hashlib.sha256(datatowrite).hexdigest())
                            print("Provided hash: ", response.split("///")[2].replace("\n", "").lower())
                    else:
                        showWarn.infoSignal.emit("Updates found!", f"ElevenClock Version {response.split('///')[0]} is available, but ElevenClock can't verify the autenticity of the package. Please go ElevenClock's homepage and download the latest version from there.\n\nDo you want to open the download page?")
                else:
                    showNotif.infoSignal.emit("Updates found!", f"ElevenClock Version {response.split('///')[0]} is available. Go to ElevenClock's Settings to update")
                    
            else:
                print("updates not found")
        else:
            print("update checking disabled")

    except Exception as e:
        print(f"Exception: {e}")

def loadClocks():
    global clocks, oldScreens
    firstWinSkipped = False
    oldScreens = []
    for screen in app.screens():
        oldScreens.append(getGeometry(screen))
        print(screen, screen.geometry(), getGeometry(screen))
        screen: QScreen
        if(firstWinSkipped):
            clocks.append(Clock(screen.logicalDotsPerInchX()/96, screen.logicalDotsPerInchY()/96, screen))
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

def showMessage(a, b):
    lastState = i.isVisible()
    i.show()
    i.showMessage(a, b)
    sw.updateButton.show()
    i.setVisible(lastState)

def restartClocks():
    global clocks, st
    for clock in clocks:
        clock.hide()
        clock.close()
    loadClocks()
    try:
        st.kill()
    except AttributeError:
        pass
    st = KillableThread(target=screenCheckThread, daemon=True)
    st.start()

def isElevenClockRunning():
    nowTime = time.time()
    name = f"ElevenClockRunning{nowTime}"
    setSettings(name, True, False)
    while True:
        try:
            for file in glob.glob(os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock"), "ElevenClockRunning*")):
                if(os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock"), name) == file):
                    pass
                else:
                    if(float(file.replace(os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock"), "ElevenClockRunning"), "")) < nowTime): # If lockfile is older
                        os.remove(file)
            if not(getSettings(name)):
                print("KILLING, NEWER VERSION RUNNING")
                killSignal.infoSignal.emit("", "")
        except Exception as e:
            print(e)
        time.sleep(2)

class KillableThread(threading.Thread): 
    def __init__(self, *args, **keywords): 
        threading.Thread.__init__(self, *args, **keywords) 
        self.shouldBeRuning = True

    def start(self): 
        self._run = self.run 
        self.run = self.settrace_and_run
        threading.Thread.start(self) 

    def settrace_and_run(self): 
        sys.settrace(self.globaltrace) 
        self._run()

    def globaltrace(self, frame, event, arg): 
        return self.localtrace if event == 'call' else None
        
    def localtrace(self, frame, event, arg): 
        if not(self.shouldBeRuning) and event == 'line': 
            raise SystemExit() 
        return self.localtrace
    
    def kill(self):
        self.shouldBeRuning = False

class RestartSignal(QObject):
    
    restartSignal = Signal()
    
    def __init__(self) -> None:
        super().__init__()

class InfoSignal(QObject):
    
    infoSignal = Signal(str, str)
    
    def __init__(self) -> None:
        super().__init__()

class Clock(QWidget):
    
    refresh = Signal()
    hideSignal = Signal()
    def __init__(self, dpix, dpiy, screen):
        super().__init__()
        self.lastTheme = 0
        showSeconds = readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "ShowSecondsInSystemClock", 0) or getSettings("EnableSeconds")
        locale.setlocale(locale.LC_ALL, readRegedit(r"Control Panel\International", "LocaleName", "en_US"))
        dateTimeFormat = "%HH:%M\n%d/%m/%Y"
        
        if(getSettings("DisableTime")):
            dateTimeFormat = dateTimeFormat.replace("%HH:%M", "").replace("\n", "")
            
        if(getSettings("DisableDate")):
            dateTimeFormat = dateTimeFormat.replace("%d/%m/%Y", "").replace("\n", "")

        dateMode = readRegedit(r"Control Panel\International", "sShortDate", "dd/MM/yyyy")
        dateMode = dateMode.replace("ddd", "%a").replace("dd", "%$").replace("d", "%#d").replace("$", "d").replace("MMM", "%b").replace("MM", "%m").replace("M", "%#m").replace("yyyy", "%Y").replace("yy", "%y")

        timeMode = readRegedit(r"Control Panel\International", "sShortTime", "H:mm")
        timeMode = timeMode.replace("Uhr", "~").replace("HH", "%$").replace("H", "%#H").replace("$", "H").replace("hh", "%I").replace("h", "%#I").replace("mm", "%M").replace("m", "%#M").replace("tt", "%p").replace("t", "%p").replace("ss", "%S").replace("s", "%#S")
        if not("s" in timeMode) and showSeconds==1:
            for separator in ":.-/_":
                if(separator in timeMode):
                    if("#" in timeMode):
                        timeMode += f"{separator}%#S"
                    else:
                        timeMode += f"{separator}%S"
        
        self.preferedwidth = 150
        self.preferedHeight = 48

        for separator in ":.-/_":
            timeMode = timeMode.replace(f" %p{separator}%S", f"{separator}%S %p")
            timeMode = timeMode.replace(f" %p{separator}%#S", f"{separator}%#S %p")
            
        self.dateTimeFormat = dateTimeFormat.replace("%d/%m/%Y", dateMode).replace("%HH:%M", timeMode)
        print(self.dateTimeFormat)
        try:
            if readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "TaskbarSi", 1) == 0:
                self.setStyleSheet(f"background-color: rgba(0, 0, 0, 0.01);margin: 5px;margin-top: 2px;margin-bottom: 2px; border-radius: 5px;")
                print("Small taskbar")
                self.preferedHeight = 32
                self.preferedwidth = 200
            else: 
                self.setStyleSheet(f"background-color: rgba(0, 0, 0, 0.01);margin: 5px;border-radius: 5px; ")
        except Exception as e:
            print(e)
            self.setStyleSheet(f"background-color: rgba(0, 0, 0, 0.01);margin: 5px;border-radius: 5px; ")
       
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
        self.setToolTip(f"ElevenClock version {version}\n\nClick once to show notifications")
        try:
            if(readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\StuckRects3", "Settings", b'0\x00\x00\x00\xfe\xff\xff\xffz\xf4\x00\x00\x03\x00\x00\x00T\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x08\x04\x00\x00\x80\x07\x00\x008\x04\x00\x00`\x00\x00\x00\x01\x00\x00\x00')[12] == 1 and not(getSettings("ForceOnBottom"))):
                h = self.screen.geometry().y()
                print("taskbar at top")
            else:
                h = self.screen.geometry().y()+self.screen.geometry().height()-(self.preferedHeight*dpiy)
                print("taskbar at bottom")
        except:
            h = self.screen.geometry().y()+self.screen.geometry().height()-(self.preferedHeight*dpiy)
            print("taskbar at bottom")
        
        if not(getSettings("EnableWin32API")):
            print("Using qt's default positioning system")
            self.move(self.screen.geometry().x()+self.screen.geometry().width()-((self.preferedwidth+8)*dpix), h)
            self.resize(self.preferedwidth*dpix, self.preferedHeight*dpiy)
        else:
            print("Using win32 API positioning system")
            self.user32 = windll.user32
            self.user32.SetProcessDPIAware() # optional, makes functions return real pixel numbers instead of scaled values
            win32gui.SetWindowPos(self.winId(), 0, int(self.screen.geometry().x()+self.screen.geometry().width()-(self.preferedwidth+8*dpix)), int(h), int(self.preferedwidth*dpix), int(self.preferedHeight*dpiy), False)
        print("Clock geometry:", self.geometry())
        self.font: QFont = QFont("Segoe UI Variable")
        self.font.setPointSizeF(9)
        self.font.setStyleStrategy(QFont.PreferOutline)
        self.font.setLetterSpacing(QFont.PercentageSpacing, 100)
        self.font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.label = Label(datetime.datetime.now().strftime(self.dateTimeFormat).replace("~", "Uhr").replace("'", ""), self)
        self.label.setFont(self.font)
        self.label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        if(readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "SystemUsesLightTheme",  1) == 0):
            self.lastTheme = 0
            self.label.setStyleSheet("padding: 1px;padding-right: 5px; color: white;")
            self.label.bgopacity = .1
            self.font.setWeight(QFont.Weight.Medium)
            self.label.setFont(self.font)
        else:
            self.lastTheme = 1
            self.label.setStyleSheet("padding: 1px;padding-right: 5px; color: black;")
            self.label.bgopacity = .5
            self.font.setWeight(QFont.Weight.Normal)
            self.label.setFont(self.font)
        self.label.clicked.connect(lambda: self.showCalendar())
        self.label.move(0, 0)
        self.label.setFixedHeight(self.height())
        self.label.setFixedWidth(self.width())
        self.label.show()
        self.show()
        self.raise_()
        self.setFocus()
        
        self.processes = [p.name() for p in psutil.process_iter()]
        
        self.user32 = windll.user32
        self.user32.SetProcessDPIAware() # optional, makes functions return real pixel numbers instead of scaled values
        self.loop = KillableThread(target=self.fivesecsloop, daemon=True)
        self.loop2 = KillableThread(target=self.refreshProcesses, daemon=True)
        self.loop.start()
        self.loop2.start()

        self.full_screen_rect = (self.screen.geometry().x(), self.screen.geometry().y(), self.screen.geometry().x()+self.screen.geometry().width(), self.screen.geometry().y()+self.screen.geometry().height())
        print("Full screen rect: ", self.full_screen_rect)
        
    def refreshProcesses(self):
        while True:
            time.sleep(1)
            self.processes = [p.name() for p in psutil.process_iter()]
            

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

            win32gui.EnumWindows(winEnumHandler, 0)
            return fullscreen
        except Exception as e:
            return False
            
    def fivesecsloop(self):
        while True:
            time.sleep(0.05)
            if not(self.theresFullScreenWin()) or not(getSettings("EnableHideOnFullScreen")):
                if self.autoHide:
                    mousePos = getMousePos()
                    if (mousePos.y()+1 == self.screen.geometry().y()+self.screen.geometry().height()) and self.screen.geometry().x() < mousePos.x() and self.screen.geometry().x()+self.screen.geometry().width() > mousePos.x():
                        self.refresh.emit()
                    elif (mousePos.y() <= self.screen.geometry().y()+self.screen.geometry().height()-self.preferedHeight):
                        self.hideSignal.emit()
                else:
                    if("mstsc.exe" in self.processes and getSettings("EnableHideOnRDP")):
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
        if(self.shouldBeVisible):
            self.show()
            self.setVisible(True)
            self.raise_()
            theme = readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "SystemUsesLightTheme", 1)
            if(theme != self.lastTheme):
                if(theme == 0):
                    self.lastTheme = 0
                    self.label.setStyleSheet("padding: 1px;padding-right: 5px; color: white;")
                    self.label.bgopacity = 0.1
                    self.font.setWeight(QFont.Weight.Medium)
                    self.label.setFont(self.font)
                else:
                    self.lastTheme = 1
                    self.label.setStyleSheet("padding: 1px;padding-right: 5px; color: black;")
                    self.label.bgopacity = .5
                    self.font.setWeight(QFont.Weight.Normal)
                    self.label.setFont(self.font)
                
            self.label.setText(datetime.datetime.now().strftime(self.dateTimeFormat).replace("~", "Uhr").replace("'", ""))
        
    def closeEvent(self, event: QCloseEvent) -> None:
        self.shouldBeVisible = False
        print("close")
        self.loop.kill()
        self.loop2.kill()
        event.accept()
        return super().closeEvent(event)
        
class Label(QLabel):
    clicked = Signal()
    def __init__(self, text, parent):
        super().__init__(text, parent=parent)
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
            self.backgroundwidget.resize(self.width(), self.height())
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

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        self.setWindowOpacity(0.7)
        self.window().setWindowOpacity(0.7)
        return super().mousePressEvent(ev)
        
    def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        self.setWindowOpacity(1)
        self.window().setWindowOpacity(1)
        if(ev.button() == Qt.RightButton):
            mousePos = getMousePos()
            print(i.contextMenu().height())
            if(i.contextMenu().height() != 480):
                mousePos.setY(self.window().y()-i.contextMenu().height())
            else:
                mousePos.setY(self.window().y()-156)
            i.contextMenu().exec_(mousePos)
        else:
            self.clicked.emit()
        return super().mouseReleaseEvent(ev)  
        
class TaskbarIconTray(QSystemTrayIcon):
    def __init__(self, app=None):
        super().__init__(app)
        self.setIcon(QIcon(os.path.join(realpath, "icon.ico")))
        self.show()
        menu = QMenu("ElevenClock")
        menu.setWindowFlag(Qt.WindowStaysOnTopHint)
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
        quitAction = QAction(f"Settings...", app)
        quitAction.triggered.connect(lambda: sw.show())
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
        
        if(getSettings("DisableSystemTray")):
            self.hide()
            print("system tray icon disabled")

class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.updateSize = True
        self.setWindowIcon(QIcon(os.path.join(realpath, "icon.ico")))
        title = QLabel(f"ElevenClock v{version} Settings:")
        title.setStyleSheet("font-size: 25pt;")
        layout.addWidget(title)
        layout.addStretch()
        layout.addSpacing(10)
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        
        layout.addWidget(QLabel("<b>General Settings:</b>"))
        self.updateButton = QPushButton("Update to the lastest version!")
        self.updateButton.clicked.connect(lambda: KillableThread(target=updateIfPossible, args=((True,))).start())
        self.updateButton.hide()
        layout.addWidget(self.updateButton)
        self.updatesChBx = QCheckBox("Automatically check for updates")
        self.updatesChBx.setChecked(not(getSettings("DisableAutoCheckForUpdates")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("DisableAutoCheckForUpdates", not(bool(i))))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QCheckBox("Automatically install available updates")
        self.updatesChBx.setChecked(getSettings("EnableAutoInstallUpdates"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("EnableAutoInstallUpdates", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QCheckBox("Enable really silent updates")
        self.updatesChBx.setChecked((getSettings("EnableSilentUpdates")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("EnableSilentUpdates", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QCheckBox("Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)")
        self.updatesChBx.setChecked((getSettings("BypassDomainAuthCheck")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("BypassDomainAuthCheck", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QCheckBox("Show ElevenClock on system tray")
        self.updatesChBx.setChecked(not(getSettings("DisableSystemTray")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("DisableSystemTray", not(bool(i))))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QCheckBox("Alternative clock alignment (may not work)")
        self.updatesChBx.setChecked((getSettings("EnableWin32API")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("EnableWin32API", bool(i)))
        layout.addWidget(self.updatesChBx)
        btn = QPushButton("Change startup behaviour")
        btn.clicked.connect(lambda: os.startfile("ms-settings:startupapps"))
        layout.addWidget(btn)
        layout.addSpacing(10)
        
        layout.addWidget(QLabel("<b>Clock Settings:</b>"))
        self.updatesChBx = QCheckBox("Hide the clock in fullscreen mode")
        self.updatesChBx.setChecked((getSettings("EnableHideOnFullScreen")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("EnableHideOnFullScreen", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QCheckBox("Hide the clock when RDP client is active")
        self.updatesChBx.setChecked((getSettings("EnableHideOnRDP")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("EnableHideOnRDP", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QCheckBox("Force the clock to be at the bottom of the screen")
        self.updatesChBx.setChecked((getSettings("ForceOnBottom")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("ForceOnBottom", bool(i)))
        layout.addWidget(self.updatesChBx)
        layout.addSpacing(10)
        
        layout.addWidget(QLabel("<b>Date & Time Settings:</b>"))
        self.updatesChBx = QCheckBox("Show seconds on the clock")
        self.updatesChBx.setChecked((getSettings("EnableSeconds")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("EnableSeconds", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QCheckBox("Show date on the clock")
        self.updatesChBx.setChecked(not(getSettings("DisableDate")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("DisableDate", not(bool(i))))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QCheckBox("Show time on the clock")
        self.updatesChBx.setChecked(not(getSettings("DisableTime")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("DisableTime", not(bool(i))))
        layout.addWidget(self.updatesChBx)
        btn = QPushButton("Change date & time system (Regional settings)")
        btn.clicked.connect(lambda: os.startfile("intl.cpl"))
        layout.addWidget(btn)
        layout.addSpacing(10)
        
        layout.addWidget(QLabel("<b>About ElevenClock:</b>"))
        btn = QPushButton("View ElevenClock's homepage")
        btn.clicked.connect(lambda: os.startfile("https://github.com/martinet101/ElevenClock/"))
        layout.addWidget(btn)
        btn = QPushButton("Report an issue/request a feature")
        btn.clicked.connect(lambda: os.startfile("https://github.com/martinet101/ElevenClock/issues/new/choose"))
        layout.addWidget(btn)
        layout.addStretch()
        layout.addSpacing(10)
        btn = QPushButton("Close settings")
        btn.clicked.connect(lambda: self.hide())
        layout.addWidget(btn)
        self.setLayout(layout)
        self.setFixedSize(int(500*(self.screen().logicalDotsPerInch()/96)), int(600*(self.screen().logicalDotsPerInch()/96)))
        self.setWindowTitle(f"ElevenClock Version {version} settings")
    
    def moveEvent(self, event: QMoveEvent) -> None:
        if(self.updateSize):
            self.setFixedSize(int(500*(self.screen().logicalDotsPerInch()/96)), int(600*(self.screen().logicalDotsPerInch()/96)))
        else:
            def enableUpdateSize(self: SettingsWindow):
                time.sleep(1)
                self.updateSize = True
                
            self.updateSize = False
            KillableThread(target=enableUpdateSize, args=(self,)).start()
        
    def showEvent(self, event: QShowEvent) -> None:
        self.setFixedSize(int(500*(self.screen().logicalDotsPerInch()/96)), int(600*(self.screen().logicalDotsPerInch()/96)))
    
    def closeEvent(self, event: QCloseEvent) -> None:
        self.hide()
        event.ignore()


try:
    os.chdir(os.path.expanduser("~"))
    os.chdir(".elevenclock")
except FileNotFoundError:
    os.mkdir(".elevenclock")


if hasattr(sys, 'frozen'):
    realpath = sys._MEIPASS
else:
    realpath = '/'.join(sys.argv[0].replace("\\", "/").split("/")[:-1])
  
clocks = []
oldScreens = []

QApplication.setAttribute(Qt.AA_DisableHighDpiScaling)

app = QApplication()
app.setQuitOnLastWindowClosed(False)
signal = RestartSignal()
showNotif = InfoSignal()
showWarn = InfoSignal()
killSignal = InfoSignal()
sw = SettingsWindow()
i = TaskbarIconTray(app)
showNotif.infoSignal.connect(lambda a, b: showMessage(a, b))
showWarn.infoSignal.connect(lambda a, b: wanrUserAboutUpdates(a, b))
killSignal.infoSignal.connect(lambda: sys.exit())

def wanrUserAboutUpdates(a, b):
    if(QMessageBox.question(sw, a, b, QMessageBox.Open | QMessageBox.Cancel, QMessageBox.Open) == QMessageBox.Open):
        os.startfile("https://github.com/martinet101/ElevenClock/releases/tag/2.0")

    

st = KillableThread(target=screenCheckThread, daemon=True)
st.start()

KillableThread(target=updateChecker, daemon=True).start()
KillableThread(target=isElevenClockRunning, daemon=True).start()
signal.restartSignal.connect(lambda: restartClocks())
loadClocks()

if not(getSettings("Updated2.1Already")):
    print("Show2.1Welcome")
    sw.show()
    setSettings("Updated2.1Already", True)
    QMessageBox.information(sw, "ElevenClock updated!", "ElevenClock has updated and, due to security reasons, auto-update is now disabled by default. to re-enable auto update AT YOUR OWN RISK, go to settings -> Enable auto-updates.")

if("--settings" in sys.argv):
    sw.show()
    
app.exec_()
sys.exit(0)
