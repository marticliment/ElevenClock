import os
import sys
import time
import glob
import socket
import winreg
import locale
import hashlib
import tempfile
import datetime
import threading
import subprocess
from ctypes import windll
from urllib.request import urlopen

import psutil
import win32gui
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from pynput.keyboard import Controller, Key
from pynput.mouse import Controller as MouseController

from lang import lang_de, lang_fr, lang_ca, lang_es, lang_ru, lang_en, lang_tr, lang_pl

def _(s): #Translate function
    global lang
    try:
        t = lang.lang[s]
        return t if t else s
    except KeyError:
        return s

def getPath(s):
    return os.path.join(realpath, s).replace("\\", "/")

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

def checkRDP():
    print("start RDP thread")
    global isRDPRunning
    while True:
        isRDPRunning = "mstsc.exe" in (p.name() for p in psutil.process_iter())
        time.sleep(10)

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
        loadTimeFormat()
        if(r):
            restartClocks()
            if(getSettings("DisableSystemTray")):
                i.hide()
            else:
                i.show()
    except Exception as e:
        print(e)

def getSettingsValue(s: str):
    try:
        with open(os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock"), s), "r") as sf:
            return sf.read()
    except Exception as e:
        print(e)
        return ""

def setSettingsValue(s: str, v: str, r: bool = True):
    try:
        with open(os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock"), s), "w") as sf:
            sf.write(v)
        loadTimeFormat()
        if(r):
            restartClocks()
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
                if(not(getSettings("DisableAutoInstallUpdates")) or force):
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
    clocks = []
    for screen in app.screens():
        oldScreens.append(getGeometry(screen))
        screen.logicalDotsPerInchChanged.connect(restartClocks)
        screen.orientationChanged.connect(restartClocks)
        screen.virtualGeometryChanged.connect(restartClocks)
        print(screen, screen.geometry(), getGeometry(screen))
        screen: QScreen
        if(firstWinSkipped):
            clocks.append(Clock(screen.logicalDotsPerInchX()/96, screen.logicalDotsPerInchY()/96, screen))
        else: # Skip the primary display, as it has already the clock
            print("This is primay screen")
            firstWinSkipped = True
    st = KillableThread(target=screenCheckThread, daemon=True)
    st.start()

def getGeometry(screen: QScreen):
    return (screen.geometry().width(), screen.geometry().height(), screen.geometry().x(), screen.geometry().y(), screen.logicalDotsPerInchX(), screen.logicalDotsPerInchY())

def theyMatch(oldscreens, newscreens):
    if(len(oldscreens) != len(newscreens)):
        return False # If there are display changes
    for i in range(len(oldscreens)):
        old, new = oldscreens[i], newscreens[i]
        if(old != getGeometry(new)): # Check if screen dimensions or dpi have changed
            return False # They have changed (screens are not equal)
    return True # they have not changed (screens still the same)

def screenCheckThread():
    print("screenCheckThread")
    while theyMatch(oldScreens, app.screens()):
        time.sleep(1)
    signal.restartSignal.emit()
    pass

def closeClocks():
    for clock in clocks:
        clock.hide()
        clock.close()

def showMessage(a, b):
    lastState = i.isVisible()
    i.show()
    i.showMessage(a, b)
    sw.updateButton.show()
    sw.resizewidget.setMinimumHeight(sw.resizewidget.sizeHint().height())
    i.setVisible(lastState)

def restartClocks():
    global clocks, st, rdpThread, timethread

    for clock in clocks:
        clock.hide()
        clock.close()
    loadClocks()

    try:
        st.kill()
        rdpThread.kill()
        timethread.kill()
    except AttributeError:
        pass
    rdpThread = KillableThread(target=checkRDP, daemon=True)
    if(getSettings("EnableHideOnRDP")):
        rdpThread.start()

    timethread = KillableThread(target=timeStrThread, daemon=True)
    timethread.start()

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

def wanrUserAboutUpdates(a, b):
    if(QMessageBox.question(sw, a, b, QMessageBox.Open | QMessageBox.Cancel, QMessageBox.Open) == QMessageBox.Open):
        os.startfile("https://github.com/martinet101/ElevenClock/releases/tag/2.0")

def checkIfWokeUp():
    while True:
        lastTime = time.time()
        time.sleep(3)
        if((lastTime+6) < time.time()):
            os.startfile(sys.executable)

def loadTimeFormat():
    global dateTimeFormat
    showSeconds = readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "ShowSecondsInSystemClock", 0) or getSettings("EnableSeconds")
    locale.setlocale(locale.LC_ALL, readRegedit(r"Control Panel\International", "LocaleName", "en_US"))
    dateTimeFormat = "%HH:%M\n%d/%m/%Y"

    if(getSettings("DisableTime")):
        dateTimeFormat = dateTimeFormat.replace("%HH:%M", "").replace("\n", "")

    if(getSettings("DisableDate")):
        dateTimeFormat = dateTimeFormat.replace("%d/%m/%Y", "").replace("\n", "")

    dateMode = readRegedit(r"Control Panel\International", "sShortDate", "dd/MM/yyyy")
    dateMode = dateMode.replace("ddd", "%a").replace("dd", "%$").replace("d", "%#d").replace("$", "d").replace("MMMM", "%B").replace("MMM", "%b").replace("MM", "%m").replace("M", "%#m").replace("yyyy", "%Y").replace("yy", "%y")

    timeMode = readRegedit(r"Control Panel\International", "sShortTime", "H:mm")
    timeMode = timeMode.replace("Uhr", "~").replace("HH", "%$").replace("H", "%#H").replace("$", "H").replace("hh", "%I").replace("h", "%#I").replace("mm", "%M").replace("m", "%#M").replace("tt", "%p").replace("t", "%p").replace("ss", "%S").replace("s", "%#S")
    if not("S" in timeMode) and showSeconds==1:
        for separator in ":.-/_":
            if(separator in timeMode):
                timeMode += f"{separator}%S"

    for separator in ":.-/_":
        timeMode = timeMode.replace(f" %p{separator}%S", f"{separator}%S %p")
        timeMode = timeMode.replace(f" %p{separator}%#S", f"{separator}%#S %p")

    dateTimeFormat = dateTimeFormat.replace("%d/%m/%Y", dateMode).replace("%HH:%M", timeMode)

def timeStrThread():
    global timeStr, dateTimeFormat
    fixHyphen = getSettings("EnableHyphenFix")
    while True:
        if(fixHyphen):
            for _ in range(36000):
                timeStr = datetime.datetime.now().strftime(dateTimeFormat).replace("~", "Uhr").replace("'", "").replace("t-", "t -")
                time.sleep(0.1)
        else:
            for _ in range(36000):
                timeStr = datetime.datetime.now().strftime(dateTimeFormat).replace("~", "Uhr").replace("'", "")
                time.sleep(0.1)

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


        self.preferedwidth = 150
        self.preferedHeight = 48

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

        self.label = Label(timeStr, self)
        if(getSettings("ClockOnTheLeft")):
            w = self.screen.geometry().x()+8*dpix
            self.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        else:
            self.label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            w = self.screen.geometry().x()+self.screen.geometry().width()-((self.preferedwidth+8)*dpix)

        if not(getSettings("EnableWin32API")):
            print("Using qt's default positioning system")
            self.move(w, h)
            self.resize(self.preferedwidth*dpix, self.preferedHeight*dpiy)
        else:
            print("Using win32 API positioning system")
            self.user32 = windll.user32
            self.user32.SetProcessDPIAware() # optional, makes functions return real pixel numbers instead of scaled values
            win32gui.SetWindowPos(self.winId(), 0, int(w), int(h), int(self.preferedwidth*dpix), int(self.preferedHeight*dpiy), False)
        print("Clock geometry:", self.geometry())
        self.font: QFont = QFont()
        self.font.setFamilies(["Segoe UI Variable", "Gullim"])
        self.font.setPointSizeF(9)
        self.font.setStyleStrategy(QFont.PreferOutline)
        self.font.setLetterSpacing(QFont.PercentageSpacing, 100)
        self.font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.label.setFont(self.font)
        if(readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "SystemUsesLightTheme",  1) == 0 or getSettings("ForceDarkTheme")):
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
        self.screen.logicalDotsPerInchChanged.connect(restartClocks)

        self.isRDPRunning = True

        self.user32 = windll.user32
        self.user32.SetProcessDPIAware() # optional, makes functions return real pixel numbers instead of scaled values
        self.loop = KillableThread(target=self.fivesecsloop, daemon=True)
        self.loop2 = KillableThread(target=self.refreshProcesses, daemon=True)
        self.loop.start()
        if(getSettings("EnableHideOnRDP")):
            self.loop2.start()

        self.full_screen_rect = (self.screen.geometry().x(), self.screen.geometry().y(), self.screen.geometry().x()+self.screen.geometry().width(), self.screen.geometry().y()+self.screen.geometry().height())
        print("Full screen rect: ", self.full_screen_rect)

    def refreshProcesses(self):
        global isRDPRunning
        while True:
            self.isRDPRunning = isRDPRunning
            time.sleep(1)

    def theresFullScreenWin(self):
        try:
            fullscreen = False

            def absoluteValuesAreEqual(a, b):
                return (a[0]) == (b[0]) and (a[1]) == (b[1]) and (a[2]) == (b[2]) and (a[3]) == (b[3])

            def winEnumHandler( hwnd, ctx ):
                nonlocal fullscreen
                if win32gui.IsWindowVisible( hwnd ):
                    if(absoluteValuesAreEqual(win32gui.GetWindowRect(hwnd), self.full_screen_rect)):
                        print(hwnd, self.full_screen_rect, win32gui.GetWindowRect(hwnd))
                        fullscreen = True

            win32gui.EnumWindows(winEnumHandler, 0)
            return fullscreen
        except Exception as e:
            return False

    def fivesecsloop(self):
        EnableHideOnFullScreen = getSettings("EnableHideOnFullScreen")
        DisableHideWithTaskbar = getSettings("DisableHideWithTaskbar")
        EnableHideOnRDP = getSettings("EnableHideOnRDP")
        while True:
            time.sleep(0.05)
            if not(self.theresFullScreenWin()) or not(EnableHideOnFullScreen):
                if self.autoHide and not(DisableHideWithTaskbar):
                    mousePos = getMousePos()
                    if (mousePos.y()+1 == self.screen.geometry().y()+self.screen.geometry().height()) and self.screen.geometry().x() < mousePos.x() and self.screen.geometry().x()+self.screen.geometry().width() > mousePos.x():
                        self.refresh.emit()
                    elif (mousePos.y() <= self.screen.geometry().y()+self.screen.geometry().height()-self.preferedHeight):
                        self.hideSignal.emit()
                else:
                    if(self.isRDPRunning and EnableHideOnRDP):
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
                if(theme == 0 or getSettings("ForceDarkTheme")):
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
            self.label.setText(timeStr)

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
            if(not(getSettings("ClockOnTheLeft"))):
                self.backgroundwidget.move(self.width()-geometry.width(), 0)
            else:
                self.backgroundwidget.move(0, 0)
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
        menu = QMenu(_("ElevenClock"))
        menu.setWindowFlag(Qt.WindowStaysOnTopHint)
        menu.addSeparator()
        quitAction = QAction(_("ElevenClock Settings"), app)
        quitAction.triggered.connect(lambda: sw.show())
        menu.addAction(quitAction)
        reloadAction = QAction(_("Reload Clocks"), app)
        reloadAction.triggered.connect(lambda: restartClocks())
        menu.addAction(reloadAction)
        menu.addSeparator()
        nameAction = QAction(_("ElevenClock v{0}").format(version), app)
        nameAction.setEnabled(False)
        menu.addAction(nameAction)
        menu.addSeparator()
        reloadAction = QAction(_("Restart ElevenClock"), app)
        reloadAction.triggered.connect(lambda: os.startfile(sys.executable))
        menu.addAction(reloadAction)
        hideAction = QAction(_("Hide ElevenClock"), app)
        hideAction.triggered.connect(lambda: closeClocks())
        menu.addAction(hideAction)
        quitAction = QAction(_("Quit ElevenClock"), app)
        quitAction.triggered.connect(lambda: sys.exit())
        menu.addAction(quitAction)

        self.setContextMenu(menu)

        def reloadClocksIfRequired(reason: QSystemTrayIcon.ActivationReason) -> None:
            if(reason != QSystemTrayIcon.ActivationReason.Context):
                restartClocks()

        self.activated.connect(lambda r: reloadClocksIfRequired(r))

        if(getSettings("DisableSystemTray")):
            self.hide()
            print("system tray icon disabled")

class QIconLabel(QWidget):
    def __init__(self, text, icon=None):
        super().__init__()
        self.setObjectName("subtitleLabel")
        self.label = QLabel(text, self)
        self.label.setStyleSheet("font-size: 13pt;background: none;font-family: \"Segoe UI Variable Display\";")
        self.image = QLabel(self)
        self.image.setPixmap(QIcon(icon).pixmap(QSize(24, 24)))
        self.image.setStyleSheet("padding: 3px;background: none;")
        self.setAttribute(Qt.WA_StyledBackground)

    def getPx(self, original) -> int:
        return int(original*(self.screen().logicalDotsPerInchX()/96))

    def setIcon(self, icon: str) -> None:
        self.image.setPixmap(QIcon(icon).pixmap(QSize(24, 24)))

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.label.move(self.getPx(60), self.getPx(25))
        self.label.setFixedHeight(self.getPx(30))
        self.image.move(self.getPx(22), self.getPx(25))
        self.image.setFixedHeight(self.getPx(30))
        self.setFixedHeight(self.getPx(70))
        self.image.setFixedHeight(self.getPx(30))
        self.label.setFixedWidth(self.width()-self.getPx(70))
        self.image.setFixedWidth(self.getPx(30))
        return super().resizeEvent(event)

class QSettingsButton(QWidget):
    clicked = Signal()
    def __init__(self, text="", btntext="", parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground)
        self.button = QPushButton(btntext+" ", self)
        self.button.setLayoutDirection(Qt.RightToLeft)
        self.setObjectName("stBtn")
        self.label = QLabel(text, self)
        self.label.setStyleSheet("font-size: 9pt;background: none;font-family: \"Segoe UI Variable Text\";font-weight: 450;")
        self.button.setStyleSheet("font-size: 9pt;font-family: \"Segoe UI Variable Text\";font-weight: 450;")
        self.label.setObjectName("StLbl")
        self.button.clicked.connect(self.clicked.emit)

    def getPx(self, original) -> int:
        return int(original*(self.screen().logicalDotsPerInchX()/96))

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.button.move(self.width()-self.getPx(140), self.getPx(10))
        self.label.move(self.getPx(60), self.getPx(10))
        self.label.setFixedWidth(self.width()-self.getPx(200))
        self.label.setFixedHeight(self.getPx(30))
        self.setFixedHeight(self.getPx(50))
        self.button.setFixedHeight(self.getPx(30))
        self.button.setFixedWidth(self.getPx(120))
        return super().resizeEvent(event)

    def setIcon(self, icon: QIcon) -> None:
        self.button.setIcon(icon)

class QSettingsComboBox(QWidget):
    clicked = Signal()
    def __init__(self, text="", btntext="", parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground)
        self.button = QComboBox(self)
        self.button.setLayoutDirection(Qt.RightToLeft)
        self.setObjectName("stBtn")
        self.label = QLabel(text, self)
        self.label.setStyleSheet("font-size: 9pt;background: none;font-family: \"Segoe UI Variable Text\";font-weight: 450;")
        self.button.setStyleSheet("font-size: 9pt;font-family: \"Segoe UI Variable Text\";font-weight: 450;")
        self.label.setObjectName("StLbl")
        self.button.clicked.connect(self.clicked.emit)

    def getPx(self, original) -> int:
        return int(original*(self.screen().logicalDotsPerInchX()/96))

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.button.move(self.width()-self.getPx(140), self.getPx(10))
        self.label.move(self.getPx(60), self.getPx(10))
        self.label.setFixedWidth(self.width()-self.getPx(200))
        self.label.setFixedHeight(self.getPx(30))
        self.setFixedHeight(self.getPx(50))
        self.button.setFixedHeight(self.getPx(30))
        self.button.setFixedWidth(self.getPx(120))
        return super().resizeEvent(event)

    def setIcon(self, icon: QIcon) -> None:
        self.button.setIcon(icon)

class QSettingsCheckBox(QWidget):
    stateChanged = Signal(bool)
    def __init__(self, text="", parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground)
        self.setObjectName("stChkBg")
        self.checkbox = QCheckBox(text, self)
        self.checkbox.setStyleSheet("font-size: 9pt;background: none;font-family: \"Segoe UI Variable Text\";font-weight: 450;")
        self.checkbox.setObjectName("stChk")
        self.checkbox.stateChanged.connect(self.stateChanged.emit)

    def setChecked(self, checked: bool) -> None:
        self.checkbox.setChecked(checked)

    def isChecked(self) -> bool:
        return self.checkbox.isChecked()

    def getPx(self, original) -> int:
        return int(original*(self.screen().logicalDotsPerInchX()/96))

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.checkbox.move(self.getPx(60), self.getPx(10))
        self.checkbox.setFixedHeight(self.getPx(30))
        self.checkbox.setFixedWidth(self.width()-self.getPx(70))
        self.setFixedHeight(self.getPx(50))
        return super().resizeEvent(event)

class SettingsWindow(QScrollArea):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.updateSize = True
        self.setWidgetResizable(True)
        self.resizewidget = QWidget()
        self.resizewidget.setObjectName("background")
        self.setWindowIcon(QIcon(os.path.join(realpath, "icon.ico")))
        layout.addSpacing(10)
        title = QLabel(_("ElevenClock Settings"))
        title.setObjectName("title")
        title.setStyleSheet("font-size: 25pt;font-family: \"Segoe UI Variable Text\";font-weight: 450;")
        layout.addWidget(title)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addSpacing(10)
        self.resize(900, 600)
        layout.addSpacing(20)
        self.setFrameShape(QFrame.NoFrame)
        if(readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "AppsUseLightTheme", 1)==0):
            self.iconMode = "white"
        else:
            self.iconMode = "black"
            
        self.generalSettingsTitle = QIconLabel(_("General Settings:"), getPath(f"settings_{self.iconMode}.png"))
        layout.addWidget(self.generalSettingsTitle)
        self.updateButton = QSettingsButton(_("<b>Update to the lastest version!</b>"), _("Install update"))
        self.updateButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;border-bottom: 0px;}")
        self.updateButton.clicked.connect(lambda: KillableThread(target=updateIfPossible, args=((True,))).start())
        self.updateButton.hide()
        layout.addWidget(self.updateButton)
        self.updatesChBx = QSettingsCheckBox(_("Automatically check for updates"))
        self.updatesChBx.setChecked(not(getSettings("DisableAutoCheckForUpdates")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("DisableAutoCheckForUpdates", not(bool(i)), r = False))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Automatically install available updates"))
        self.updatesChBx.setChecked(not(getSettings("DisableAutoInstallUpdates")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("DisableAutoInstallUpdates", not(bool(i)), r = False))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Enable really silent updates"))
        self.updatesChBx.setChecked((getSettings("EnableSilentUpdates")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("EnableSilentUpdates", bool(i), r = False))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"))
        self.updatesChBx.setChecked((getSettings("BypassDomainAuthCheck")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("BypassDomainAuthCheck", bool(i), r = False))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Show ElevenClock on system tray"))
        self.updatesChBx.setChecked(not(getSettings("DisableSystemTray")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("DisableSystemTray", not(bool(i))))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Alternative clock alignment (may not work)"))
        self.updatesChBx.setChecked((getSettings("EnableWin32API")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("EnableWin32API", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.startupButton = QSettingsButton(_("Change startup behaviour"), _("Change"))
        self.startupButton.clicked.connect(lambda: os.startfile("ms-settings:startupapps"))
        layout.addWidget(self.startupButton)
        layout.addSpacing(10)

        self.clockSettingsTitle = QIconLabel(_("Clock Settings:"), getPath(f"clock_{self.iconMode}.png"))
        layout.addWidget(self.clockSettingsTitle)
        self.updatesChBx = QSettingsCheckBox(_("Hide the clock in fullscreen mode"))
        self.updatesChBx.setChecked((getSettings("EnableHideOnFullScreen")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("EnableHideOnFullScreen", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Hide the clock when RDP client is active"))
        self.updatesChBx.setChecked((getSettings("EnableHideOnRDP")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("EnableHideOnRDP", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Show the clock when the taskbar is set to hide automatically"))
        self.updatesChBx.setChecked((getSettings("DisableHideWithTaskbar")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("DisableHideWithTaskbar", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Force the clock to be at the bottom of the screen"))
        self.updatesChBx.setChecked((getSettings("ForceOnBottom")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("ForceOnBottom", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Fix the hyphen/dash showing over the month"))
        self.updatesChBx.setChecked((getSettings("EnableHyphenFix")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("EnableHyphenFix", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Force the clock to have white text"))
        self.updatesChBx.setChecked((getSettings("ForceDarkTheme")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("ForceDarkTheme", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Show the clock at the left of the screen"))
        self.updatesChBx.setStyleSheet(f"QWidget#stChkBg{{border-bottom-left-radius: {self.getPx(6)}px;border-bottom-right-radius: {self.getPx(6)}px;border-bottom: 1px;}}")
        self.updatesChBx.setChecked((getSettings("ClockOnTheLeft")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("ClockOnTheLeft", bool(i)))
        layout.addWidget(self.updatesChBx)
        layout.addSpacing(10)

        self.dateTimeTitle = QIconLabel(_("Date & Time Settings:"), getPath(f"datetime_{self.iconMode}.png"))
        layout.addWidget(self.dateTimeTitle)
        self.updatesChBx = QSettingsCheckBox(_("Show seconds on the clock"))
        self.updatesChBx.setChecked((getSettings("EnableSeconds")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("EnableSeconds", bool(i), r = False))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Show date on the clock"))
        self.updatesChBx.setChecked(not(getSettings("DisableDate")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("DisableDate", not(bool(i)), r = False))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Show time on the clock"))
        self.updatesChBx.setChecked(not(getSettings("DisableTime")))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("DisableTime", not(bool(i)), r = False))
        layout.addWidget(self.updatesChBx)
        self.RegionButton = QSettingsButton(_("Change date and time format (Regional settings)"), _("Regional settings"))
        self.RegionButton.clicked.connect(lambda: os.startfile("intl.cpl"))
        layout.addWidget(self.RegionButton)
        layout.addSpacing(10)

        self.languageSettingsTitle = QIconLabel(_("About the language pack:").format(version), getPath(f"lang_{self.iconMode}.png"))
        layout.addWidget(self.languageSettingsTitle)
        self.PackInfoButton = QSettingsButton(_("Translated to English by martinet101"), "")
        self.PackInfoButton.button.hide()
        self.PackInfoButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;border-bottom: 0px;}")
        layout.addWidget(self.PackInfoButton)
        self.openTranslateButton = QSettingsButton(_("Translate ElevenClock to your language"), _("Get started"))
        self.openTranslateButton.clicked.connect(lambda: self.hide())
        layout.addWidget(self.openTranslateButton)
        layout.addSpacing(10)

        self.aboutTitle = QIconLabel(_("About ElevenClock version {0}:").format(version), getPath(f"about_{self.iconMode}.png"))
        layout.addWidget(self.aboutTitle)
        self.WebPageButton = QSettingsButton(_("View ElevenClock's homepage"), _("Open"))
        self.WebPageButton.clicked.connect(lambda: os.startfile("https://github.com/martinet101/ElevenClock/"))
        self.WebPageButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;border-bottom: 0px;}")
        layout.addWidget(self.WebPageButton)
        self.IssueButton = QSettingsButton(_("Report an issue/request a feature"), _("Report"))
        self.IssueButton.clicked.connect(lambda: os.startfile("https://github.com/martinet101/ElevenClock/issues/new/choose"))
        self.IssueButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;border-bottom: 0px;}")
        layout.addWidget(self.IssueButton)
        self.CofeeButton = QSettingsButton(_("Support the dev: Give me a coffee☕"), _("Open page"))
        self.CofeeButton.clicked.connect(lambda: os.startfile("https://ko-fi.com/martinet101"))
        self.CofeeButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;border-bottom: 0px;}")
        layout.addWidget(self.CofeeButton)
        self.PichonButton = QSettingsButton(_("Icons by Icons8"), _("Webpage"))
        self.PichonButton.clicked.connect(lambda: os.startfile("https://icons8.com/"))
        self.PichonButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;border-bottom: 0px;}")
        layout.addWidget(self.PichonButton)
        self.closeButton = QSettingsButton(_("Close settings"), _("Close"))
        self.closeButton.clicked.connect(lambda: os.startfile(""))
        layout.addWidget(self.closeButton)
        layout.addSpacing(10)

        self.resizewidget.setLayout(layout)
        self.setWidget(self.resizewidget)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setWindowTitle(_("ElevenClock Settings"))
        self.applyStyleSheet()
        self.setMinimumWidth(400)

    def applyStyleSheet(self):
        colors = ['215,226,228', '160,174,183', '101,116,134', '81,92,107', '69,78,94', '41,47,64', '15,18,36', '239,105,80']
        string = readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\Accent", "AccentPalette", b'\xe9\xd8\xf1\x00\xcb\xb7\xde\x00\x96}\xbd\x00\x82g\xb0\x00gN\x97\x00H4s\x00#\x13K\x00\x88\x17\x98\x00')
        i  =  0
        for color in string.split(b"\x00"):
            try:
                if(len(color)==3):
                    colors[i] = f"{color[0]},{color[1]},{color[2]}"
                else:
                    print("NullColor")
            except IndexError:
                pass
            finally:
                i += 1
        print(colors)
        if(readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "AppsUseLightTheme", 1)==0):
            self.iconMode = "white"
            self.aboutTitle.setIcon(getPath(f"about_{self.iconMode}.png"))
            self.dateTimeTitle.setIcon(getPath(f"datetime_{self.iconMode}.png"))
            self.clockSettingsTitle.setIcon(getPath(f"clock_{self.iconMode}.png"))
            self.languageSettingsTitle.setIcon(getPath(f"lang_{self.iconMode}.png"))
            self.generalSettingsTitle.setIcon(getPath(f"settings_{self.iconMode}.png"))
            self.PichonButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.closeButton.setIcon(QIcon(getPath(f"close_{self.iconMode}.png")))
            self.startupButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.RegionButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.IssueButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.WebPageButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.CofeeButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.openTranslateButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.setStyleSheet(f"""
                                #background {{
                                   color: white;
                                }}
                                * {{
                                   background-color: #212121;
                                   color: #dddddd;
                                   font-size: 8pt;
                                }}
                                QPushButton {{
                                   width: 100px;
                                   background-color: #363636;
                                   border-radius: {self.getPx(6)}px;
                                   border: {self.getPx(1)}px solid #393939;
                                   height: {self.getPx(25)}px;
                                   border-top: {self.getPx(1)}px solid #404040;
                                }}
                                QPushButton:hover {{
                                   background-color: #393939;
                                   border-radius: {self.getPx(6)}px;
                                   border: {self.getPx(1)}px solid #414141;
                                   height: {self.getPx(25)}px;
                                   border-top: {self.getPx(1)}px solid #454545;
                                }}
                                #title{{
                                   background-color: #303030;
                                   margin: {self.getPx(10)}px;
                                   margin-bottom: 0px;
                                   padding-left: {self.getPx(20)}px;
                                   padding-top: {self.getPx(15)}px;
                                   padding-bottom: {self.getPx(15)}px;
                                   border: {self.getPx(1)}px solid #1c1c1c;
                                   border-bottom: 0px;
                                   font-size: 13pt;
                                   border-radius: {self.getPx(6)}px;
                                }}
                                #subtitleLabel{{
                                   background-color: #303030;
                                   margin: {self.getPx(10)}px;
                                   margin-bottom: 0px;
                                   padding-left: {self.getPx(20)}px;
                                   padding-top: {self.getPx(15)}px;
                                   padding-bottom: {self.getPx(15)}px;
                                   border: {self.getPx(1)}px solid #1c1c1c;
                                   border-bottom: 0px;
                                   font-size: 13pt;
                                   border-top-left-radius: {self.getPx(6)}px;
                                   border-top-right-radius: {self.getPx(6)}px;
                                }}
                                #StLbl{{
                                   padding: 0px;
                                   background-color: #303030;
                                   margin: 0px;
                                   border:none;
                                   font-size: {self.getPx(11)}px;
                                }}
                                #stBtn{{
                                   background-color: #303030;
                                   margin: {self.getPx(10)}px;
                                   margin-bottom: 0px;
                                   margin-top: 0px;
                                   border: {self.getPx(1)}px solid #1c1c1c;
                                   border-bottom: 0px;
                                   border-bottom-left-radius: {self.getPx(6)}px;
                                   border-bottom-right-radius: {self.getPx(6)}px;
                                }}
                                #lastWidget{{
                                   border-bottom-left-radius: {self.getPx(6)}px;
                                   border-bottom-right-radius: {self.getPx(6)}px;
                                }}
                                #stChkBg{{
                                   padding: {self.getPx(15)}px;
                                   padding-left: {self.getPx(45)}px;
                                   background-color: #303030;
                                   margin: {self.getPx(10)}px;
                                   margin-bottom: 0px;
                                   margin-top: 0px;
                                   border: {self.getPx(1)}px solid #1c1c1c;
                                   border-bottom: 0px;
                                }}
                                #stChk::indicator{{
                                   height: {self.getPx(20)}px;
                                   width: {self.getPx(20)}px;
                                }}
                                #stChk::indicator:unchecked {{
                                    background-color: #252525;
                                    border: {self.getPx(1)}px solid #444444;
                                    border-radius: {self.getPx(6)}px;
                                }}
                                #stChk::indicator:unchecked:hover {{
                                    background-color: #2a2a2a;
                                    border: {self.getPx(1)}px solid #444444;
                                    border-radius: {self.getPx(6)}px;
                                }}
                                #stChk::indicator:checked {{
                                    border: {self.getPx(1)}px solid #444444;
                                    background-color: rgb({colors[1]});
                                    border-radius: {self.getPx(6)}px;
                                    image: url("{getPath("tick_white.png")}");
                                }}
                                #stChk::indicator:checked:hover {{
                                    border: {self.getPx(1)}px solid #444444;
                                    background-color: rgb({colors[2]});
                                    border-radius: {self.getPx(6)}px;
                                    image: url("{getPath("tick_white.png")}");
                                }}
                                QSCrollArea,QVBoxLayout{{
                                    border: none;
                                    margin: none;
                                    padding: none;
                                    outline: none;
                                }}
                                QScrollBar:vertical {{
                                    background: #303030;
                                    margin: {self.getPx(4)}px;
                                    width: {self.getPx(20)}px;
                                    border: none;
                                    border-radius: {self.getPx(5)}px;
                                }}
                                QScrollBar::handle:vertical {{
                                    margin: {self.getPx(3)}px;
                                    border-radius: {self.getPx(3)}px;
                                    background: #505050;
                                }}
                                QScrollBar::handle:vertical:hover {{
                                    margin: {self.getPx(3)}px;
                                    border-radius: {self.getPx(3)}px;
                                    background: #808080;
                                }}
                                QScrollBar::add-line:vertical {{
                                    height: 0;
                                    subcontrol-position: bottom;
                                    subcontrol-origin: margin;
                                }}
                                QScrollBar::sub-line:vertical {{
                                    height: 0;
                                    subcontrol-position: top;
                                    subcontrol-origin: margin;
                                }}
                                QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
                                    background: none;
                                }}
                                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
                                    background: none;
                                }}
                               """)
        else:
            self.iconMode = "black"
            self.aboutTitle.setIcon(getPath(f"about_{self.iconMode}.png"))
            self.dateTimeTitle.setIcon(getPath(f"datetime_{self.iconMode}.png"))
            self.clockSettingsTitle.setIcon(getPath(f"clock_{self.iconMode}.png"))
            self.generalSettingsTitle.setIcon(getPath(f"settings_{self.iconMode}.png"))
            self.languageSettingsTitle.setIcon(getPath(f"lang_{self.iconMode}.png"))
            self.PichonButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.CofeeButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.startupButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.RegionButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.WebPageButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.IssueButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.closeButton.setIcon(QIcon(getPath(f"close_{self.iconMode}.png")))
            self.openTranslateButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.setStyleSheet(f"""
                                #background {{
                                   color: white;
                                }}
                                * {{
                                   background-color: #eeeeee;
                                   color: #000000;
                                   font-size: 8pt;
                                }}
                                QPushButton {{
                                   width: 100px;
                                   background-color: #ffffff;
                                   border-radius: {self.getPx(6)}px;
                                   border: {self.getPx(1)}px solid #dddddd;
                                   height: {self.getPx(25)}px;
                                   border-bottom: {self.getPx(1)}px solid #cccccc;
                                }}
                                QPushButton:hover {{
                                   background-color: #f6f6f6;
                                   border-radius: {self.getPx(6)}px;
                                   border: {self.getPx(1)}px solid #dddddd;
                                   height: {self.getPx(25)}px;
                                   border-bottom: {self.getPx(1)}px solid #cccccc;
                                }}
                                #title{{
                                   background-color: #ffffff;
                                   margin: {self.getPx(10)}px;
                                   margin-bottom: 0px;
                                   padding-left: {self.getPx(20)}px;
                                   padding-top: {self.getPx(15)}px;
                                   padding-bottom: {self.getPx(15)}px;
                                   border: {self.getPx(1)}px solid #dddddd;
                                   border-bottom: 1px;
                                   font-size: 13pt;
                                   border-radius: {self.getPx(6)}px;
                                }}
                                #subtitleLabel{{
                                   background-color: #ffffff;
                                   margin: {self.getPx(10)}px;
                                   margin-bottom: 0px;
                                   padding-left: {self.getPx(20)}px;
                                   padding-top: {self.getPx(15)}px;
                                   padding-bottom: {self.getPx(15)}px;
                                   border: {self.getPx(1)}px solid #dddddd;
                                   border-bottom: 0px;
                                   font-size: 13pt;
                                   border-top-left-radius: {self.getPx(6)}px;
                                   border-top-right-radius: {self.getPx(6)}px;
                                }}
                                #StLbl{{
                                   padding: 0px;
                                   background-color: #ffffff;
                                   margin: 0px;
                                   border:none;
                                   font-size: {self.getPx(11)}px;
                                }}
                                #stBtn{{
                                   background-color: #ffffff;
                                   margin: {self.getPx(10)}px;
                                   margin-bottom: 0px;
                                   margin-top: 0px;
                                   border: {self.getPx(1)}px solid #dddddd;
                                   border-bottom: 0px;
                                   border-bottom-left-radius: {self.getPx(6)}px;
                                   border-bottom-right-radius: {self.getPx(6)}px;
                                }}
                                #lastWidget{{
                                   border-bottom-left-radius: {self.getPx(6)}px;
                                   border-bottom-right-radius: {self.getPx(6)}px;
                                   border-bottom: 1px;
                                }}
                                #stChkBg{{
                                   padding: {self.getPx(15)}px;
                                   padding-left: {self.getPx(45)}px;
                                   background-color: #ffffff;
                                   margin: {self.getPx(10)}px;
                                   margin-bottom: 0px;
                                   margin-top: 0px;
                                   border: {self.getPx(1)}px solid #dddddd;
                                   border-bottom: 0px;
                                }}
                                #stChk::indicator{{
                                   height: {self.getPx(20)}px;
                                   width: {self.getPx(20)}px;
                                }}
                                #stChk::indicator:unchecked {{
                                    background-color: #ffffff;
                                    border: {self.getPx(1)}px solid #bbbbbb;
                                    border-radius: {self.getPx(6)}px;
                                }}
                                #stChk::indicator:unchecked:hover {{
                                    background-color: #eeeeee;
                                    border: {self.getPx(1)}px solid #bbbbbb;
                                    border-radius: {self.getPx(6)}px;
                                }}
                                #stChk::indicator:checked {{
                                    border: {self.getPx(0)}px solid #bbbbbb;
                                    background-color: rgb({colors[4]});
                                    border-radius: {self.getPx(5)}px;
                                    image: url("{getPath("tick_black.png")}");
                                }}
                                #stChk::indicator:checked:hover {{
                                    border: {self.getPx(0)}px solid #bbbbbb;
                                    background-color: rgb({colors[3]});
                                    border-radius: {self.getPx(5)}px;
                                    image: url("{getPath("tick_black.png")}");
                                }}
                                QSCrollArea,QVBoxLayout{{
                                    border: none;
                                    margin: none;
                                    padding: none;
                                    outline: none;
                                }}
                                QScrollBar:vertical {{
                                    background: #ffffff;
                                    margin: {self.getPx(4)}px;
                                    width: {self.getPx(20)}px;
                                    border: none;
                                    border-radius: {self.getPx(5)}px;
                                }}
                                QScrollBar::handle:vertical {{
                                    margin: {self.getPx(3)}px;
                                    border-radius: {self.getPx(3)}px;
                                    background: #dddddd;
                                }}
                                QScrollBar::handle:vertical:hover {{
                                    margin: {self.getPx(3)}px;
                                    border-radius: {self.getPx(3)}px;
                                    background: #bbbbbb;
                                }}
                                QScrollBar::add-line:vertical {{
                                    height: 0;
                                    subcontrol-position: bottom;
                                    subcontrol-origin: margin;
                                }}
                                QScrollBar::sub-line:vertical {{
                                    height: 0;
                                    subcontrol-position: top;
                                    subcontrol-origin: margin;
                                }}
                                QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
                                    background: none;
                                }}
                                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
                                    background: none;
                                }}
                               """)



    def moveEvent(self, event: QMoveEvent) -> None:
        if(self.updateSize):
            self.resizewidget.resize(self.width()-self.getPx(17), self.resizewidget.height())
            self.resizewidget.setMinimumHeight(self.resizewidget.sizeHint().height())
        else:
            def enableUpdateSize(self: SettingsWindow):
                time.sleep(1)
                self.updateSize = True

            self.updateSize = False
            KillableThread(target=enableUpdateSize, args=(self,)).start()

    def resizeEvent(self, event: QMoveEvent) -> None:
        self.resizewidget.resize(self.width()-self.getPx(17), self.resizewidget.height())
        self.resizewidget.setMinimumHeight(self.resizewidget.sizeHint().height())

    def show(self) -> None:
        self.applyStyleSheet()
        return super().show()

    def showEvent(self, event: QShowEvent) -> None:
        self.resizewidget.setMinimumHeight(self.resizewidget.sizeHint().height())
        return super().showEvent(event)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.hide()
        event.ignore()

    def getPx(self, original) -> int:
        return int(original*(self.screen().logicalDotsPerInchX()/96))

# Start of main script

try:
    os.chdir(os.path.expanduser("~"))
    os.chdir(".elevenclock")
except FileNotFoundError:
    os.mkdir(".elevenclock")

if hasattr(sys, 'frozen'):
    realpath = sys._MEIPASS
else:
    realpath = '/'.join(sys.argv[0].replace("\\", "/").split("/")[:-1])

languages = {
    "en": lang_en,
    "ca": lang_ca,
    "es": lang_es,
    "ru": lang_ru,
    "fr": lang_fr,
    "de": lang_de,
    "pl": lang_pl,
    "tr": lang_tr
}

languageReference = {
    "System language": "default",
    "English": "en",
    "Catalan": "ca",
    "Spanish": "es",
    "Russian": "ru",
    "French" : "fr",
    "German" : "de",
    "Polish" : "pl",
    "Turkish": "tr",
}

if getSettingsValue("PreferredLanguage") == "":
    setSettingsValue("PreferredLanguage", "default", False)

if getSettingsValue("PreferredLanguage") == "default":
    try:
        print(locale.getdefaultlocale()[0][0:2])
        lang = languages[locale.getdefaultlocale()[0][0:2]]
    except KeyError:
        lang = lang_en
        print("unknown language")
    except Exception as e:
        print(e)
        lang = lang_en
else:
    try:
        print(getSettingsValue("PreferredLanguage")[0:2])
        lang = languages[getSettingsValue("PreferredLanguage")[0:2]]
    except KeyError:
        lang = lang_en
        print("unknown language")
    except Exception as e:
        print(e)
        lang = lang_en
    
if lang == None:
    lang = lang_en

tdir = tempfile.TemporaryDirectory()
tempDir = tdir.name
version = 2.3
seconddoubleclick = False
isRDPRunning = False
showSeconds = 0
timeStr = ""
dateTimeFormat = ""
mController = MouseController()
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


KillableThread(target=updateChecker, daemon=True).start()
KillableThread(target=isElevenClockRunning, daemon=True).start()
KillableThread(target=checkIfWokeUp, daemon=True).start()

st = KillableThread(target=screenCheckThread, daemon=True)
rdpThread = KillableThread(target=checkRDP, daemon=True)
timethread = KillableThread(target=timeStrThread, daemon=True)
timethread.start()
st.start()
if(getSettings("EnableHideOnRDP")):
    rdpThread.start()


signal.restartSignal.connect(lambda: restartClocks())
loadClocks()

if not(getSettings("Updated2.2Already")):
    print("Show2.2Welcome")
    sw.show()
    setSettings("Updated2.2Already", True)
    QMessageBox.information(sw, "ElevenClock updated!", "ElevenClock has updated to version 2.2 sucessfully. On this version, the Three monitors issue has been fixed!\n\nAdditionally, ElevenClock can now show the clock on the left side of the screen, Has fixed doubled seconds, has (hopefully) solved an issue where ElevenClock was shown over the default clock, and has a completely redesigned Settings Window\n\nTo see the full changelog, see release 2.2 on GitHub")

showSettings = False
if("--settings" in sys.argv or showSettings):
    sw.show()

app.exec_()
sys.exit(0)
