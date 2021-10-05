from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import winreg, locale, os, tempfile, subprocess
from urllib.request import urlopen

tdir = tempfile.TemporaryDirectory()
tempDir = tdir.name

import time, sys, threading, datetime, webbrowser
from pynput.keyboard import Controller, Key

version = 1.4
lastTheme = 0
seconddoubleclick = False

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

locale.setlocale(locale.LC_ALL, readRegedit(r"Control Panel\International", "LocaleName", "en_US"))
dateTimeFormat = "%H:%M\n%d/%m/%Y"

dateMode = readRegedit(r"Control Panel\International", "sShortDate", "dd/MM/yyyy")
print(dateMode)
dateMode = dateMode.replace("dd", "%$").replace("d", "%#d").replace("$", "d").replace("MMM", "%b").replace("MM", "%m").replace("M", "%#m").replace("yyyy", "%Y").replace("yy", "%y")

timeMode = readRegedit(r"Control Panel\International", "sShortTime", "H:mm")
print(timeMode)
timeMode = timeMode.replace("HH", "%$").replace("H", "%#H").replace("$", "H").replace("hh", "%I").replace("h", "%#I").replace("mm", "%M").replace("m", "%#M").replace("tt", "%p").replace("t", "%p")
print(timeMode)

dateTimeFormat = dateTimeFormat.replace("%d/%m/%Y", dateMode).replace("%H:%M", timeMode)
print(dateTimeFormat)


class RestartSignal(QObject):
    
    restartSignal = Signal()
    
    def __init__(self) -> None:
        super().__init__()

class Clock(QMainWindow):
    
    refresh = Signal()
    def __init__(self, w, h, dpix, dpiy, fontSizeMultiplier):
        super().__init__()
        global lastTheme
        self.shouldBeVisible = True
        self.refresh.connect(self.refreshandShow)
        self.keyboard = Controller()
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.Tool)
        self.setToolTip(f"ElevenClock version {version}\n\nClick once to show notifications\nClick 4 times to show help")
        try:
            if(readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\StuckRects3", "Settings", b'0\x00\x00\x00\xfe\xff\xff\xffz\xf4\x00\x00\x03\x00\x00\x00T\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x08\x04\x00\x00\x80\x07\x00\x008\x04\x00\x00`\x00\x00\x00\x01\x00\x00\x00')[12] == 1):
                h = 48*dpiy
        except:
            pass
        self.move(w-(82*dpix), h-(48*dpiy))
        self.resize(72*dpix, 48*dpiy)
        self.setStyleSheet(f"background-color: rgba(0, 0, 0, 0.01);margin: 5px; border-radius: 5px; ")#font-size: {int(12*fontSizeMultiplier)}px;")
        self.font: QFont = QFont("Segoe UI Variable")
        self.font.setPointSizeF(9)
        self.font.setStyleStrategy(QFont.PreferOutline)
        self.font.setLetterSpacing(QFont.PercentageSpacing, 105)
        self.font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
        self.label = Label(datetime.datetime.now().strftime(dateTimeFormat))
        self.label.setFont(self.font)
        self.label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        if(readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "SystemUsesLightTheme",  1) == 0):
            lastTheme = 0
            self.label.setStyleSheet("padding: 1px; color: white;")# font-family: \"Segoe UI Variable\"; font-weight: bold;")
            self.font.setWeight(500)
            self.label.setFont(self.font)
        else:
            lastTheme = 1
            self.label.setStyleSheet("padding: 1px; color: black;")# font-family: \"Segoe UI Variable\"; font-weight: lighter;")
            self.font.setWeight(400)
            self.label.setFont(self.font)
        self.label.clicked.connect(lambda: self.showCalendar())
        self.setCentralWidget(self.label)
        threading.Thread(target=self.fivesecsloop, daemon=True).start()
        self.show()
        self.raise_()
        self.setFocus()
        
    def fivesecsloop(self):
        while True:
            time.sleep(0.1)
            self.refresh.emit()
        
    def showCalendar(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press('n')
        self.keyboard.release('n')
        self.keyboard.release(Key.cmd)
        
    def refreshandShow(self):
        global lastTheme
        if(self.shouldBeVisible):
            self.show()
            self.raise_()
            theme = readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "SystemUsesLightTheme", 1)
            if(theme != lastTheme):
                if(theme == 0):
                    lastTheme = 0
                    self.label.setStyleSheet("padding: 1px; color: white;")# font-family: \"Segoe UI Variable\"; font-weight: bold;")
                    self.font.setWeight(500)
                    self.label.setFont(self.font)
                else:
                    lastTheme = 1
                    self.label.setStyleSheet("padding: 1px; color: black;")# font-family: \"Segoe UI Variable\"; font-weight: lighter;")
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
        

QApplication.setAttribute(Qt.AA_DisableHighDpiScaling)


app = QApplication()

signal = RestartSignal()

clocks = []
oldScreens = []
firstWinSkipped = False # This value should be set to false to hide first monitor clock


def updateIfPossible():
    try:
        print("Starting update check")
        response = urlopen("http://www.somepythonthings.tk/versions/elevenclock.ver")
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
            subprocess.run('start /B "" "{0}" /silent'.format(filename), shell=True)
        else:
            print("updates not found")

    except Exception as e:
        print(f"Exception: {e}")

threading.Thread(target=updateIfPossible, daemon=True).start()

def loadClocks():
    global clocks, oldScreens, firstWinSkipped
    firstWinSkipped = False
    oldScreens = []
    for screen in app.screens():
        oldScreens.append(getGeometry(screen))
        screen: QScreen
        fontSizeMultiplier = screen.logicalDotsPerInchX()/96
        if(firstWinSkipped):
            clocks.append(Clock(screen.geometry().x()+screen.geometry().width(), screen.geometry().y()+screen.geometry().height(), screen.logicalDotsPerInchX()/96, screen.logicalDotsPerInchY()/96, fontSizeMultiplier))
        else: # Skip the primary display, as it has already the clock
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
    
def restartClocks():
    global clocks
    for clock in clocks:
        clock.hide()
        clock.close()
    loadClocks()
    threading.Thread(target=screenCheckThread, daemon=True).start()


signal.restartSignal.connect(restartClocks)
    

loadClocks()
threading.Thread(target=screenCheckThread, daemon=True).start()

app.exec_()
sys.exit(0)
