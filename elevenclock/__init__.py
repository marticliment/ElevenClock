import os
import io
import sys
import time
import glob
import socket
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
import win32api
import pythoncom
import win32process
import win32com.client
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from pynput.keyboard import Controller, Key
from pynput.mouse import Controller as MouseController


from languages import *
import globals

old_stdout = sys.stdout
sys.stdout = buffer = io.StringIO()

from settings import *
from tools import *

appsWhereElevenClockShouldClose = ["msrdc.exe", "mstsc.exe", "CDViewer.exe", "wfica32.exe", "vmware-view.exe"]

print("---------------------------------------------------------------------------------------------------")
print("")
print(f"   ElevenClock's {versionName} (v{version}) log: Select all the text and hit Ctrl+C to copy it")
print(f"   All modules loaded successfully and sys.stdout patched correctly, starting main script")
print(f"   Translator function set language to \"{langName}\"")
print("")
print("---------------------------------------------------------------------------------------------------")
print("")
print(" Log legend:")
print(" 🔵: Verbose")
print(" 🟢: Information")
print(" 🟡: Expected warning")
print(" 🟠: Unexpected warning")
print(" 🔴: Error")
print("")


def checkRDP():
    def checkIfElevenClockRunning(processess, blacklistedProcess) -> bool:
        for p_name in processess:
            if p_name in blacklistedProcess:
                print(f"🟡 Blacklisted procName {p_name} detected, hiding...")
                return True
        return False

    global isRDPRunning
    print("🔵 Starting RDP thread")
    while True:
        pythoncom.CoInitialize()
        _wmi = win32com.client.GetObject('winmgmts:')
        processes = _wmi.ExecQuery('Select Name from win32_process')
        procs = [p.Name for p in processes]
        isRDPRunning = checkIfElevenClockRunning(procs, appsWhereElevenClockShouldClose)
        time.sleep(5)

def getMousePos():
    return QPoint(mController.position[0], mController.position[1])

def updateChecker():
    while True:
        updateIfPossible()
        time.sleep(7200)

def updateIfPossible(force = False):
    try:
        if(not(getSettings("DisableAutoCheckForUpdates")) or force):
            print("🔵 Starting update check")
            integrityPass = False
            dmname = socket.gethostbyname_ex("versions.somepythonthings.tk")[0]
            if(dmname == "769432b9-3560-4f94-8f90-01c95844d994.id.repl.co" or getSettings("BypassDomainAuthCheck")): # Check provider IP to prevent exploits
                integrityPass = True
            try:
                response = urlopen("https://versions.somepythonthings.tk/versions/elevenclock.ver" if not getSettings("AlternativeUpdateServerProvider") else "http://www.somepythonthings.tk/versions/elevenclock.ver")
            except Exception as e:
                report(e)
                response = urlopen("http://www.somepythonthings.tk/versions/elevenclock.ver")
                integrityPass = True
            print("🔵 Version URL:", response.url)
            response = response.read().decode("utf8")
            new_version_number = response.split("///")[0]
            provided_hash = response.split("///")[2].replace("\n", "").lower()
            if float(new_version_number) > version:
                print("🟢 Updates found!")
                if(not(getSettings("DisableAutoInstallUpdates")) or force):
                    if(integrityPass):
                        url = "https://github.com/martinet101/ElevenClock/releases/latest/download/ElevenClock.Installer.exe"
                        filedata = urlopen(url)
                        datatowrite = filedata.read()
                        filename = ""
                        with open(os.path.join(tempDir, "SomePythonThings-ElevenClock-Updater.exe"), 'wb') as f:
                            f.write(datatowrite)
                            filename = f.name
                        if(hashlib.sha256(datatowrite).hexdigest().lower() == provided_hash):
                            print("🔵 Hash: ", provided_hash)
                            print("🟢 Hash ok, starting update")
                            if(getSettings("EnableSilentUpdates") and not(force)):
                                mousePos = getMousePos()
                                time.sleep(5)
                                while mousePos != getMousePos():
                                    print("🟡 User is using the mouse, waiting")
                                    mousePos = getMousePos()
                                    time.sleep(5)
                                subprocess.run('start /B "" "{0}" /verysilent'.format(filename), shell=True)
                            else:
                                subprocess.run('start /B "" "{0}" /silent'.format(filename), shell=True)
                        else:
                            print("🔴 Hash not ok")
                            print("🔴 File hash: ", hashlib.sha256(datatowrite).hexdigest())
                            print("🔴 Provided hash: ", provided_hash)
                            showWarn.infoSignal.emit("Updates found!", f"ElevenClock Version {new_version_number} is available, but ElevenClock can't verify the authenticity of the package. Please go ElevenClock's homepage and download the latest version from there.\n\nDo you want to open the download page?")

                    else:
                        print("🔴 Can't verify update server authenticity, aborting")
                        showWarn.infoSignal.emit("Updates found!", f"ElevenClock Version {new_version_number} is available, but ElevenClock can't verify the authenticity of the updates server. Please go ElevenClock's homepage and download the latest version from there.\n\nDo you want to open the download page?")
                else:
                    showNotif.infoSignal.emit("Updates found!", f"ElevenClock Version {new_version_number} is available. Go to ElevenClock's Settings to update")

            else:
                print("🟢 Updates not found")
        else:
            print("🟠 Update checking disabled")
        #old_stdout.write(buffer.getvalue())
        #old_stdout.flush()

    except Exception as e:
        report(e)
        #old_stdout.write(buffer.getvalue())
        #old_stdout.flush()

restartCount = 0

def resetRestartCount():
    global restartCount
    while True:
        if(restartCount>0):
            print("🔵 Restart loop:", restartCount)
            restartCount -= 1
        time.sleep(0.3)

threading.Thread(target=resetRestartCount, daemon=True).start()

def loadClocks():
    global clocks, oldScreens, st, restartCount, st
    try:
        st.kill()
    except AttributeError:
        pass
    showOnFirstMon = getSettings("ForceClockOnFirstMonitor")
    oldScreens = []
    clocks = []
    process = psutil.Process(os.getpid())
    
    if restartCount<20 and (process.memory_info().rss/1048576) <= 150:
        restartCount += 1
        for screen in app.screens():
            screen: QScreen
            oldScreens.append(getGeometry(screen))
            #old_stdout.write(buffer.getvalue())
            #old_stdout.flush()
            if not screen == QGuiApplication.primaryScreen() or showOnFirstMon: #Check if we are not on the primary screen
                clocks.append(Clock(screen.logicalDotsPerInchX()/96, screen.logicalDotsPerInchY()/96, screen))
            else: # Skip the primary display, as it has already the clock
                print("🟡 This is the primary screen and is set to be skipped")
        st = KillableThread(target=screenCheckThread, daemon=True)
        st.start()
    else:
        os.startfile(sys.executable)
        print("🔴 Overloading system, killing!")
        app.quit()
        sys.exit(1)

def getGeometry(screen: QScreen):
    """
    Return a tuple containing: (screen_width, screen_height, screen_pos_x, screen_pos_y, screen_DPI, desktopWindowRect)
    """
    #win32api.EnumDisplayMonitors()
    geometry = screen.geometry()
    g = (geometry.width(), geometry.height(), geometry.x(), geometry.y(), screen.logicalDotsPerInch(), win32api.EnumDisplayMonitors())
    return g

def theyMatch(oldscreens, newscreens):
    if len(oldscreens) != len(newscreens) or len(app.screens()) != len(win32api.EnumDisplayMonitors()):
        return False  # The number of displays has changed

    # Check that all screen dimensions and dpi are the same as before
    return all(old == getGeometry(new) for old, new in zip(oldscreens, newscreens))

def screenCheckThread():
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

def restartClocks(caller: str = ""):
    global clocks, st, rdpThread, timethread

    closeClocks()
    loadClocks()
    loadTimeFormat()

    try:
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
                print("🔴 KILLING, NEWER VERSION RUNNING")
                killSignal.infoSignal.emit("", "")
        except Exception as e:
            report(e)
        time.sleep(2)

def wanrUserAboutUpdates(a, b):
    if(QMessageBox.question(sw, a, b, QMessageBox.Open | QMessageBox.Cancel, QMessageBox.Open) == QMessageBox.Open):
        os.startfile("https://github.com/martinet101/ElevenClock/releases/latest")

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
    dateTimeFormat = "%HH:%M\n%A\n(W%W) %d/%m/%Y"


    if getSettings("DisableTime"):
        dateTimeFormat = dateTimeFormat.replace("%HH:%M\n", "")

    if getSettings("DisableDate"):
        if("\n" in dateTimeFormat):
            dateTimeFormat = dateTimeFormat.replace("\n(W%W) %d/%m/%Y", "")
        else:
            dateTimeFormat = dateTimeFormat.replace("(W%W) %d/%m/%Y", "")
    elif not getSettings("EnableWeekNumber"):
        dateTimeFormat = dateTimeFormat.replace("(W%W) ", "")

    if not getSettings("EnableWeekDay"):
        try:
            dateTimeFormat = dateTimeFormat.replace("%A", "").replace("\n\n", "\n")
            if dateTimeFormat[-1] == "\n":
                dateTimeFormat = dateTimeFormat[0:-1]
            if dateTimeFormat[0] == "\n":
                dateTimeFormat = dateTimeFormat[1:]
        except IndexError as e:
            print("🟠 Date/Time string looks to be empty!")
        except Exception as e:
            report(e)
            

    tDateMode = readRegedit(r"Control Panel\International", "sShortDate", "dd/MM/yyyy")
    dateMode = ""
    for i, ministr in enumerate(tDateMode.split("'")):
        if i%2==0:
            dateMode += ministr.replace("dddd", "%A").replace("ddd", "%a").replace("dd", "%$").replace("d", "%#d").replace("$", "d").replace("MMMM", "%B").replace("MMM", "%b").replace("MM", "%m").replace("M", "%#m").replace("yyyy", "%Y").replace("yy", "%y")
        else:
            dateMode += ministr
        
    tTimeMode = readRegedit(r"Control Panel\International", "sShortTime", "H:mm")
    timeMode = ""

    for i, ministr in enumerate(tTimeMode.split("'")):
        if i%2==0:
            timeMode += ministr.replace("HH", "%$").replace("H", "%#H").replace("$", "H").replace("hh", "%I").replace("h", "%#I").replace("mm", "%M").replace("m", "%#M").replace("tt", "%p").replace("t", "%p").replace("ss", "%S").replace("s", "%#S")
            if not("S" in timeMode) and showSeconds==1:
                for separator in ":.-/_":
                    if(separator in timeMode):
                        timeMode += f"{separator}%S"
        else:
            timeMode += ministr

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
                timeStr = datetime.datetime.now().strftime(dateTimeFormat).replace("t-", "t -")
                time.sleep(0.1)
        else:
            for _ in range(36000):
                timeStr = datetime.datetime.now().strftime(dateTimeFormat)
                time.sleep(0.1)

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
    callInMainSignal = Signal(object)

    def __init__(self, dpix, dpiy, screen):
        super().__init__()
        self.lastTheme = 0
        self.callInMainSignal.connect(lambda f: f())

        self.preferedwidth = 200
        self.preferedHeight = 48
        
        self.bgcolor = getSettingsValue("UseCustomBgColor") if getSettingsValue("UseCustomBgColor") else "0, 0, 0, 0"
        print("🔵 Using bg color:", self.bgcolor)

        try:
            if readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "TaskbarSi", 1) == 0 or (not getSettings("DisableTime") and not getSettings("DisableDate") and getSettings("EnableWeekDay")):
                self.setStyleSheet(f"background-color: rgba({self.bgcolor}%); margin: {self.getPx(5)}px;margin-top: 0px;margin-bottom: 0px; border-radius: {self.getPx(5)}px;")
                if not(not getSettings("DisableTime") and not getSettings("DisableDate") and getSettings("EnableWeekDay")):
                    print("🟡 Small sized taskbar")
                    self.preferedHeight = 32
                    self.preferedwidth = 200
            else:
                print("🟢 Regular sized taskbar")
                self.setStyleSheet(f"background-color: rgba({self.bgcolor}%);margin: {self.getPx(3)}px;border-radius: {self.getPx(5)}px;padding: {self.getPx(2)}px;")
        except Exception as e:
            print("🟡 Regular sized taskbar")
            report(e)
            self.setStyleSheet(f"background-color: rgba({self.bgcolor}%);margin: {self.getPx(3)}px;border-radius: {self.getPx(5)}px;;padding: {self.getPx(2)}px;")

        self.win32screen = {"Device": None, "Work": (0, 0, 0, 0), "Flags": 0, "Monitor": (0, 0, 0, 0)}
        for win32screen in win32api.EnumDisplayMonitors():
            try:
                if win32api.GetMonitorInfo(win32screen[0].handle)["Device"] == screen.name():
                    self.win32screen = win32api.GetMonitorInfo(win32screen[0].handle)
            except Exception as e:
                report(e)
                
        if self.win32screen == {"Device": None, "Work": (0, 0, 0, 0), "Flags": 0, "Monitor": (0, 0, 0, 0)}: #If no display is matching
            os.startfile(sys.executable) # Restart elevenclock
            app.quit()
        
        self.screenGeometry = QRect(self.win32screen["Monitor"][0], self.win32screen["Monitor"][1], self.win32screen["Monitor"][2]-self.win32screen["Monitor"][0], self.win32screen["Monitor"][3]-self.win32screen["Monitor"][1])
        print("🔵 Monitor geometry:", self.screenGeometry)
        
        self.shouldBeVisible = True
        self.refresh.connect(self.refreshandShow)
        self.hideSignal.connect(self.hide)
        self.keyboard = Controller()
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.Tool)
        hex_blob = b'0\x00\x00\x00\xfe\xff\xff\xffz\xf4\x00\x00\x03\x00\x00\x00T\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x08\x04\x00\x00\x80\x07\x00\x008\x04\x00\x00`\x00\x00\x00\x01\x00\x00\x00'
        registry_read_result = readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\StuckRects3", "Settings", hex_blob)
        self.autoHide = registry_read_result[8] == 123
        self.setToolTip(f"ElevenClock version {versionName}\n\nClick once to show notifications")
        try:
            if (registry_read_result[12] == 1 and not getSettings("ForceOnBottom")) or getSettings("ForceOnTop"):
                h = self.screenGeometry.y()
                print("🟢 Taskbar at top")
            else:
                h = self.screenGeometry.y()+self.screenGeometry.height()-(self.preferedHeight*dpiy)
                print("🟢 Taskbar at bottom")
        except Exception as e:
            report(e)
            h = self.screenGeometry.y()+self.screenGeometry.height()-(self.preferedHeight*dpiy)
            print("🟡 Taskbar at bottom")
        self.label = Label(timeStr, self)
        if(getSettings("ClockOnTheLeft")):
            w = self.screenGeometry.x()+8*dpix
            print("🟢 Clock on the right")
            self.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        else:
            self.label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            print("🟡 Clock on the left")
            w = self.screenGeometry.x()+self.screenGeometry.width()-((self.preferedwidth)*dpix)
            
        if getSettings("CenterAlignment"):
            self.label.setAlignment(Qt.AlignCenter)


        self.w = w
        self.h = h
        self.dpix = dpix
        self.dpiy = dpiy

        if not(getSettings("EnableWin32API")):
            print("🟢 Using qt's default positioning system")
            self.move(w, h)
            self.resize(self.preferedwidth*dpix, self.preferedHeight*dpiy)
        else:
            print("🟡 Using win32 API positioning system")
            self.user32 = windll.user32
            self.user32.SetProcessDPIAware() # forces functions to return real pixel numbers instead of scaled values
            win32gui.SetWindowPos(self.winId(), 0, int(w), int(h), int(self.preferedwidth*dpix), int(self.preferedHeight*dpiy), False)
        print("🔵 Clock geometry:", self.geometry())
        self.font: QFont = QFont()
        customFont = getSettingsValue("UseCustomFont")
        if customFont == "":
            if lang == lang_ko:
                self.fontfamilies = ["Malgun Gothic", "Segoe UI Variable", "sans-serif"]
            elif lang == lang_zh_TW or lang == lang_zh_CN:
                self.fontfamilies = ["Microsoft JhengHei UI", "Segoe UI Variable", "sans-serif"]
            else:
                self.fontfamilies = ["Segoe UI Variable Display", "sans-serif"]
        else:
            self.fontfamilies = [customFont]
        print(f"🔵 Font families: {self.fontfamilies}")
        customSize = getSettingsValue("UseCustomFontSize")
        if customSize == "":
            self.font.setPointSizeF(9.3)
        else:
            try:
                self.font.setPointSizeF(float(customSize))
            except Exception as e:
                self.font.setPointSizeF(9.3)
                report(e)
        print(f"🔵 Font size: {self.font.pointSizeF()}")
        self.font.setStyleStrategy(QFont.PreferOutline)
        self.font.setLetterSpacing(QFont.PercentageSpacing, 100)
        self.font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.label.setFont(self.font)

        def make_style_sheet(a, b, c, d, color):
            return f"padding: {a}px;padding-right: {b}px;margin-right: {c}px;padding-left: {d}px; color: {color};"

        if getSettings("UseCustomFontColor"):
            print("🟡 Using custom text color:", getSettingsValue('UseCustomFontColor'))
            self.lastTheme = -1
            style_sheet_string = make_style_sheet(self.getPx(1), self.getPx(3), self.getPx(12), self.getPx(5), f"rgb({getSettingsValue('UseCustomFontColor')})")
            self.label.setStyleSheet(style_sheet_string)
            self.label.bgopacity = .1
            self.fontfamilies = [element.replace("Segoe UI Variable Display", "Segoe UI Variable Display Semib") for element in self.fontfamilies]
            self.font.setFamilies(self.fontfamilies)
            if lang == lang_ko:
                self.font.setWeight(QFont.Weight.Normal)
            elif lang == lang_zh_TW or lang == lang_zh_CN:
                self.font.setWeight(QFont.Weight.Normal)
            else:
                self.font.setWeight(QFont.Weight.DemiBold)
            self.label.setFont(self.font)        
        elif readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "SystemUsesLightTheme",  1) == 0:
            print("🟢 Using white text (dark mode)")
            self.lastTheme = 0
            style_sheet_string = make_style_sheet(self.getPx(1), self.getPx(3), self.getPx(12), self.getPx(5), "white")
            self.label.setStyleSheet(style_sheet_string)
            self.label.bgopacity = .1
            self.fontfamilies = [element.replace("Segoe UI Variable Display", "Segoe UI Variable Display Semib") for element in self.fontfamilies]
            self.font.setFamilies(self.fontfamilies)
            if lang == lang_ko:
                self.font.setWeight(QFont.Weight.Normal)
            elif lang == lang_zh_TW or lang == lang_zh_CN:
                self.font.setWeight(QFont.Weight.Normal)
            else:
                self.font.setWeight(QFont.Weight.DemiBold)
            self.label.setFont(self.font)
        else:
            print("🟢 Using black text (light mode)")
            self.lastTheme = 1
            style_sheet_string = make_style_sheet(self.getPx(1), self.getPx(3), self.getPx(12), self.getPx(5), "black")
            self.label.setStyleSheet(style_sheet_string)
            self.label.bgopacity = .5
            self.fontfamilies = [element.replace("Segoe UI Variable Display Semib", "Segoe UI Variable Display") for element in self.fontfamilies]
            self.font.setFamilies(self.fontfamilies)
            self.font.setWeight(QFont.Weight.ExtraLight)
            self.label.setFont(self.font)
        self.label.clicked.connect(lambda: self.showCalendar())
        self.label.move(0, 0)
        self.label.setFixedHeight(self.height())
        self.label.resize(self.width()-self.getPx(8), self.height())
        self.label.show()
        loadTimeFormat()
        self.show()
        self.raise_()
        self.setFocus()

        self.isRDPRunning = True

        self.full_screen_rect = (self.screenGeometry.x(), self.screenGeometry.y(), self.screenGeometry.x()+self.screenGeometry.width(), self.screenGeometry.y()+self.screenGeometry.height())
        print("🔵 Full screen rect: ", self.full_screen_rect)


        self.forceDarkTheme = getSettings("ForceDarkTheme")
        self.forceLightTheme = getSettings("ForceLightTheme")

        self.user32 = windll.user32
        self.user32.SetProcessDPIAware() # optional, makes functions return real pixel numbers instead of scaled values
        self.loop = KillableThread(target=self.fivesecsloop, daemon=True)
        self.loop2 = KillableThread(target=self.refreshProcesses, daemon=True)
        self.loop.start()
        self.loop2.start()
        
        class QHoverButton(QPushButton):
            hovered = Signal()
            unhovered = Signal()
            
            def __init__(self, text: str = "", parent: QObject = None) -> None:
                super().__init__(text=text, parent=parent)
            
            def enterEvent(self, event: QtCore.QEvent) -> None:
                self.hovered.emit()
                return super().enterEvent(event)
            
            def leaveEvent(self, event: QtCore.QEvent) -> None:
                self.unhovered.emit()
                return super().leaveEvent(event)
            
        if(readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "TaskbarSd", 0) == 1) or getSettings("ShowDesktopButton"):
            self.desktopButton = QHoverButton(parent=self)
            self.desktopButton.clicked.connect(lambda: self.showDesktop())
            self.desktopButton.show()
            self.desktopButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.desktopButton.move(self.width()-self.getPx(12), 0)
            self.desktopButton.resize(self.getPx(12), self.getPx(self.preferedHeight))
            self.desktopButton.hovered.connect(lambda: self.desktopButton.setIcon(QIcon(getPath("showdesktop.png"))))
            self.desktopButton.unhovered.connect(lambda: self.desktopButton.setIcon(QIcon()))
            self.setFixedHeight(self.getPx(self.preferedHeight))
            self.desktopButton.setStyleSheet(f"""
                QPushButton{{
                    background-color: rgba(0, 0, 0, 0.01); 
                    margin: 0px;
                    padding: 0px; 
                    margin-top: 0px;
                    border-radius: 0px;
                    margin-bottom: 0px;
                    border-left: 0px solid rgba(0, 0, 0, 0.05);
                    border-right: 0px solid rgba(0, 0, 0, 0.05);
                }}
                QPushButton:hover{{
                    background-color: rgba(127, 127, 127, 1%); 
                    margin: 0px;
                    margin-top: 0px;
                    border-radius: 0px;
                    margin-bottom: 0px;
                    border-left: 0px solid rgba(0, 0, 0, 0.05);
                    border-right: 0px solid rgba(0, 0, 0, 0.05);
                }}
                QPushButton:pressed{{
                    background-color: rgba(127, 127, 127, 1%); 
                    margin: 0px;
                    margin-top: 0px;
                    border-radius: 0px;
                    margin-bottom: 0px;
                    border-left: 0px solid rgba(0, 0, 0, 0.05);
                    border-right: 0px solid rgba(0, 0, 0, 0.05);
                }}
            """)
        #old_stdout.write(buffer.getvalue())
        #old_stdout.flush()
        

    def getPx(self, original) -> int:
        return round(original*(self.screen().logicalDotsPerInch()/96))

    def refreshProcesses(self):
        global isRDPRunning
        while True:
            self.isRDPRunning = isRDPRunning
            time.sleep(0.5)

    def theresFullScreenWin(self, clockOnFirstMon, newMethod):
        try:
            fullscreen = False

            def compareFullScreenRects(window, screen, newMethod):
                try:
                    if(newMethod):
                        return  window[0] <= screen[0] and window[1] <= screen[1] and window[2] >= screen[2] and window[3] >= screen[3]
                    else:
                        return  window[0] == screen[0] and window[1] == screen[1] and window[2] == screen[2] and window[3] == screen[3]
                except Exception as e:
                    report(e)

            def winEnumHandler( hwnd, ctx ):
                nonlocal fullscreen
                if win32gui.IsWindowVisible( hwnd ):
                    if(compareFullScreenRects(win32gui.GetWindowRect(hwnd), self.full_screen_rect, newMethod)):
                        if(clockOnFirstMon):
                            pythoncom.CoInitialize()
                            _, pid = win32process.GetWindowThreadProcessId(hwnd)
                            _wmi = win32com.client.GetObject('winmgmts:')

                            # collect all the running processes
                            processes = _wmi.ExecQuery(f'Select Name from win32_process where ProcessId = {pid}')
                            for p in processes:
                                if(p.Name != "TextInputHost.exe"):
                                    if(win32gui.GetWindowText(hwnd) not in ("", "Program Manager")):
                                        print("🟡 Fullscreen window detected!", win32gui.GetWindowText(hwnd), win32gui.GetWindowRect(hwnd), "Fullscreen rect:", self.full_screen_rect)
                                        fullscreen = True
                        else:
                            if(win32gui.GetWindowText(hwnd) not in ("", "Program Manager")):
                                print("🟡 Fullscreen window detected!", win32gui.GetWindowText(hwnd), win32gui.GetWindowRect(hwnd), "Fullscreen rect:", self.full_screen_rect)
                                fullscreen = True

            win32gui.EnumWindows(winEnumHandler, 0)
            return fullscreen
        except Exception as e:
            report(e)
            return False

    def fivesecsloop(self):
        EnableHideOnFullScreen = not(getSettings("DisableHideOnFullScreen"))
        DisableHideWithTaskbar = getSettings("DisableHideWithTaskbar")
        EnableHideOnRDP = getSettings("EnableHideOnRDP")
        clockOnFirstMon = getSettings("ForceClockOnFirstMonitor")
        newMethod = getSettings("NewFullScreenMethod")
        print(f"🔵 Show/hide loop started with parameters: HideonFS:{EnableHideOnFullScreen}, NotHideOnTB:{DisableHideWithTaskbar}, HideOnRDP:{EnableHideOnRDP}, ClockOn1Mon:{clockOnFirstMon}, NefWSMethod:{newMethod}")
        if clockOnFirstMon:
            INTLOOPTIME = 15
        else:
            INTLOOPTIME = 2
        while True:
            isFullScreen = self.theresFullScreenWin(clockOnFirstMon, newMethod)
            for i in range(INTLOOPTIME):
                if not(isFullScreen) or not(EnableHideOnFullScreen):
                    if self.autoHide and not(DisableHideWithTaskbar):
                        mousePos = getMousePos()
                        if (mousePos.y()+1 == self.screenGeometry.y()+self.screenGeometry.height()) and self.screenGeometry.x() < mousePos.x() and self.screenGeometry.x()+self.screenGeometry.width() > mousePos.x():
                            self.refresh.emit()
                        elif (mousePos.y() <= self.screenGeometry.y()+self.screenGeometry.height()-self.preferedHeight):
                            self.hideSignal.emit()
                    else:
                        if(self.isRDPRunning and EnableHideOnRDP):
                            self.hideSignal.emit()
                        else:
                            self.refresh.emit()
                else:
                    self.hideSignal.emit()
                time.sleep(0.1)

    def showCalendar(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press('n')
        self.keyboard.release('n')
        self.keyboard.release(Key.cmd)

    def showDesktop(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press('d')
        self.keyboard.release('d')
        self.keyboard.release(Key.cmd)

    def focusOutEvent(self, event: QFocusEvent) -> None:
        self.refresh.emit()

    def refreshandShow(self):
        if(self.shouldBeVisible):
            self.show()
            self.setVisible(True)
            self.raise_()
            if(self.lastTheme >= 0): # If tet color is not customized
                theme = readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "SystemUsesLightTheme", 1)
                if(theme != self.lastTheme):
                    if (theme == 0 or self.forceDarkTheme) and not self.forceLightTheme:
                        self.lastTheme = 0
                        self.label.setStyleSheet(f"padding: {self.getPx(1)}px;padding-right: {self.getPx(3)}px;margin-right: {self.getPx(12)}px;padding-left: {self.getPx(5)}px; color: white;")#background-color: rgba({self.bgcolor}%)")
                        self.label.bgopacity = 0.1
                        self.fontfamilies = [element.replace("Segoe UI Variable Display", "Segoe UI Variable Display Semib") for element in self.fontfamilies]
                        self.font.setFamilies(self.fontfamilies)
                        if lang == lang_ko:
                            self.font.setWeight(QFont.Weight.Normal)
                        elif lang == lang_zh_TW or lang == lang_zh_CN:
                            self.font.setWeight(QFont.Weight.Normal)
                        else:
                            self.font.setWeight(QFont.Weight.DemiBold)
                        self.label.setFont(self.font)
                    else:
                        self.lastTheme = 1
                        self.label.setStyleSheet(f"padding: {self.getPx(1)}px;padding-right: {self.getPx(3)}px;margin-right: {self.getPx(12)}px;padding-left: {self.getPx(5)}px; color: black;")#background-color: rgba({self.bgcolor}%)")
                        self.label.bgopacity = .5
                        self.fontfamilies = [element.replace("Segoe UI Variable Display Semib", "Segoe UI Variable Display") for element in self.fontfamilies]
                        self.font.setFamilies(self.fontfamilies)
                        self.font.setWeight(QFont.Weight.ExtraLight)
                        self.label.setFont(self.font)
            self.label.setText(timeStr)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.shouldBeVisible = False
        print(f"🟡 Closing clock on {self.win32screen}")
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
        self.installEventFilter(self)
        self.bgopacity = 0.1
        self.backgroundwidget.setStyleSheet(f"background-color: rgba(127, 127, 127, 0.01);border-top: {self.getPx(1)}px solid rgba({self.color},0);margin-top: {self.getPx(2)}px; margin-bottom: {self.getPx(2)};")
        self.backgroundwidget.show()
        self.showBackground = QVariantAnimation()
        self.showBackground.setStartValue(.01) # Not 0 to prevent white flashing on the border
        self.showBackground.setEndValue(self.bgopacity)
        self.showBackground.setDuration(100)
        self.showBackground.setEasingCurve(QEasingCurve.InOutQuad) # Not strictly required, just for the aesthetics
        self.showBackground.valueChanged.connect(lambda opacity: self.backgroundwidget.setStyleSheet(f"background-color: rgba({self.color}, {opacity/2});border-top: {self.getPx(1)}px solid rgba({self.color}, {opacity-0.01});"))
        self.hideBackground = QVariantAnimation()
        self.hideBackground.setStartValue(self.bgopacity)
        self.hideBackground.setEndValue(.01) # Not 0 to prevent white flashing on the border
        self.hideBackground.setDuration(100)
        self.hideBackground.setEasingCurve(QEasingCurve.InOutQuad) # Not strictly required, just for the aesthetics
        self.hideBackground.valueChanged.connect(lambda opacity: self.backgroundwidget.setStyleSheet(f"background-color: rgba({self.color}, {opacity/2});border-top: {self.getPx(1)}px solid rgba({self.color}, {opacity});"))
        self.setAutoFillBackground(True)
        self.backgroundwidget.setGeometry(0, 0, self.width(), self.height())
        
        self.opacity=QGraphicsOpacityEffect(self)
        self.opacity.setOpacity(1.00)
        self.setGraphicsEffect(self.opacity)
        
    def getPx(self, i: int) -> int:
        return self.window().getPx(i)



    def enterEvent(self, event: QEvent, r=False) -> None:
        geometry: QRect = self.width()
        self.showBackground.setStartValue(.01)
        self.showBackground.setEndValue(self.bgopacity) # Not 0 to prevent white flashing on the border
        if(not(getSettings("ClockOnTheLeft"))):
            self.backgroundwidget.move(0, 2)
            self.backgroundwidget.resize(geometry, self.height()-4)
        else:
            self.backgroundwidget.move(0, 2)
            self.backgroundwidget.resize(geometry, self.height()-4)
        self.showBackground.start()
        if not r:
            self.enterEvent(event, r=True)
        return super().enterEvent(event)

    def leaveEvent(self, event: QEvent) -> None:
        self.hideBackground.setStartValue(self.bgopacity)
        self.hideBackground.setEndValue(.01) # Not 0 to prevent white flashing on the border
        self.hideBackground.start()
        return super().leaveEvent(event)

    def getTextUsedSpaceRect(self):
        text = self.text().strip()
        if len(text.split("\n"))>=3:
            mult = 0.633333333333333333
        elif len(text.split("\n"))==2:
            mult = 1
        else:
            mult = 1.5
        return self.fontMetrics().boundingRect(text).width()*mult

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        self.setWindowOpacity(0.7)
        self.setWindowOpacity(0.7)
        self.opacity.setOpacity(0.80)
        self.setGraphicsEffect(self.opacity)
        return super().mousePressEvent(ev)

    def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        self.setWindowOpacity(1)
        self.setWindowOpacity(1)
        self.opacity.setOpacity(1.00)
        self.setGraphicsEffect(self.opacity)
        if(ev.button() == Qt.RightButton):
            mousePos = getMousePos()
            if(i.contextMenu().height() != 480):
                mousePos.setY(self.window().y()-i.contextMenu().height())
            else:
                if getSettings("HideTaskManagerButton"):
                    mousePos.setY(self.window().y()-int(220*(i.contextMenu().screen().logicalDotsPerInchX()/96)))
                else:
                    mousePos.setY(self.window().y()-int(330*(i.contextMenu().screen().logicalDotsPerInchX()/96)))
            i.execMenu(mousePos)
        else:
            self.clicked.emit()
        return super().mouseReleaseEvent(ev)
    
    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == event.Paint:
            w = self.minimumSizeHint().width()
            if w<self.window().getPx(self.window().preferedwidth) and not getSettings("ClockOnTheLeft"):
                self.move(self.window().getPx(self.window().preferedwidth)-self.minimumSizeHint().width(), 0)
                self.resize(self.minimumSizeHint().width(), self.height())
            else:
                self.move(0, 0)
                self.resize(w, self.height())
            
        return super().eventFilter(watched, event)

# Start of main script
try:
    tdir = tempfile.TemporaryDirectory()
    tempDir = tdir.name
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

    sw = SettingsWindow() # Declare settings window

    i = TaskbarIconTray(app)

    app.setQuitOnLastWindowClosed(False)
    app.primaryScreenChanged.connect(lambda: os.startfile(sys.executable))
    app.screenAdded.connect(lambda: os.startfile(sys.executable))
    app.screenRemoved.connect(lambda: os.startfile(sys.executable))
    signal = RestartSignal()
    showNotif = InfoSignal()
    showWarn = InfoSignal()
    killSignal = InfoSignal()
    showNotif.infoSignal.connect(lambda a, b: showMessage(a, b))
    showWarn.infoSignal.connect(lambda a, b: wanrUserAboutUpdates(a, b))
    killSignal.infoSignal.connect(lambda: app.quit())

    KillableThread(target=updateChecker, daemon=True).start()
    KillableThread(target=isElevenClockRunning, daemon=True).start()
    KillableThread(target=checkIfWokeUp, daemon=True).start()

    st: KillableThread = None # Will be defined on loadClocks
    rdpThread = KillableThread(target=checkRDP, daemon=True)
    timethread = KillableThread(target=timeStrThread, daemon=True)
    timethread.start()
    if getSettings("EnableHideOnRDP"):
        rdpThread.start()
    
    signal.restartSignal.connect(lambda: restartClocks("checkLoop"))
    loadClocks()

    globals.app = app
    globals.buffer = buffer # Register them
    globals.loadTimeFormat = loadTimeFormat # Register them
    globals.updateIfPossible = updateIfPossible # Register them
    globals.restartClocks = restartClocks # Register them
    globals.closeClocks = closeClocks # Register them
    globals.sw = sw
    globals.trayIcon = i

    if not(getSettings("Updated2.9Already")) and not(getSettings("EnableSilentUpdates")):
        print("Show2.8Welcome")
        sw.show()
        setSettings("Updated2.9Already", True)
        QMessageBox.information(sw, "ElevenClock updated!", f"ElevenClock has updated to version {versionName} successfully. \n\nThis update brings:\n - Added an early crash detector\n - Added the ability to toggle the desktop button from the settings\n - Better settings headers UI (added descritions and collapse buttons)\n - Fixed scaling issues with icons\n - Added a better context menu for the clock and the system tray icon\n - Added Slovak, Brazilian Portuguese, Hungarian and Hebrew\n - Lots of other bugfixes and other improvements\n\nAnd, of course, Merry Christmas for everybody :)")

    showSettings = False
    if("--settings" in sys.argv or showSettings):
        sw.show()

    if("--quit-on-loaded" in sys.argv):
        sys.exit(0)
        

    app.exec_()
    sys.exit(0)

except Exception as e:
    import webbrowser, traceback, platform
    os_info = f"" + \
        f"                        OS: {platform.system()}\n"+\
        f"                   Version: {platform.win32_ver()}\n"+\
        f"           OS Architecture: {platform.machine()}\n"+\
        f"          APP Architecture: {platform.architecture()[0]}\n"+\
        f"                   Program: ElevenClock"+\
        "\n\n-----------------------------------------------------------------------------------------"
    traceback_info = "Traceback (most recent call last):\n"
    try:
        for line in traceback.extract_tb(e.__traceback__).format():
            traceback_info += line
        traceback_info += f"\n{type(e).__name__}: {str(e)}"
    except:
        traceback_info += "\nUnable to get traceback"
    traceback_info += str(type(e))
    traceback_info += ": "
    traceback_info += str(e)
    webbrowser.open("https://www.somepythonthings.tk/error-report/?appName=ElevenClock&errorBody="+os_info.replace('\n', '{l}').replace(' ', '{s}')+"{l}{l}{l}{l}ElevenClock Log:{l}"+str("\n\n\n\n"+traceback_info).replace('\n', '{l}').replace(' ', '{s}'))
    print(traceback_info)
    sys.exit(1)