from ctypes import c_int, windll
from functools import partial
import json, sys
import time
import datetime
import traceback
windll.shcore.SetProcessDpiAwareness(c_int(2))


from versions import *
import os
import sys
import winreg
import locale

from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import platform
import win32gui

from external.blurwindow import GlobalBlur, ExtendFrameIntoClientArea

import globals
from lang.languages import *
from external.FramelessWindow import QFramelessDialog
from threading import Thread
from urllib.request import urlopen

from win32con import *

import pywintypes
import pythoncom
import win32process
import win32api
import win32con
import re

isMoment4 = False


specificSettings = {}
missingTranslationList = []
lastMenuTheme = -1

try:
    winver = int(platform.version().split('.')[2])
except Exception as e:
    print(e)
    winver = 22000



def ptToPx(value: float, screen: QScreen) -> float:
    return value/72*screen.logicalDotsPerInch()

def touch(f):
    try:
        f = open(f, "w")
        f.close()
    except FileExistsError:
        pass


def _(s): # Translate function
    global lang
    try:
        t = lang[s]
        return (t+"✅[Found]✅" if debugLang else t) if t else f"{s}⚠️[UntranslatedString]⚠️" if debugLang else eng_(s)
    except KeyError:
        if debugLang: print(s)
        if not s in missingTranslationList:
            missingTranslationList.append(s)
        return f"{eng_(s)}🔴[MissingString]🔴" if debugLang else eng_(s)

def eng_(s): # English translate function
    try:
        t = englang[s]
        return t if t else s
    except KeyError:
        if debugLang:
            print(s)
        return s


def cprint(*args):
    """
    Prints on the console instead of on the log
    """
    print(*args, file=globals.old_stdout)

def getPath(s):
    return os.path.join(os.path.join(realpath, "resources"), s).replace("\\", "/")

def getAppIconMode() -> str:
    return "white" if isWindowDark() else "black"

def getTaskbarIconMode() -> str:
    return "white" if isTaskbarDark() else "black"

def isWindowDark() -> bool:
    return readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "AppsUseLightTheme", 1) == 0

def isTaskbarDark() -> bool:
    return readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "SystemUsesLightTheme", 1) == 0

def getint(s: str, fallback: int) -> int:
    try:
        return int(s) if s != "" else fallback
    except:
        return fallback

def report(exception) -> None: # Exception reporter
    import traceback
    for line in traceback.format_exception(*sys.exc_info()):
        print("🔴 "+line)
        cprint("🔴 "+line)
    print(f"🔴 Note this traceback was caught by reporter and has been added to the log ({exception})")

def readRegedit(aKey, sKey, default, storage=winreg.HKEY_CURRENT_USER):
    registry = winreg.ConnectRegistry(None, storage)
    reg_keypath = aKey
    try:
        reg_key = winreg.OpenKey(registry, reg_keypath)
    except FileNotFoundError as e:
        return default
    except Exception as e:
        report(e)
        return default

    for i in range(1024):
        try:
            value_name, value, _ = winreg.EnumValue(reg_key, i)
            if value_name == sKey:
                return value
        except OSError as e:
            return default
        except Exception as e:
            report(e)
            return default


def IsCopilotEnabled():
    return readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "ShowCopilotButton", 0) == 1 ^ getSettings("EnableCopilotIcon")

if winver == 22621:
    if readRegedit(r"SOFTWARE\Microsoft\Windows NT\CurrentVersion", "UBR", 0, winreg.HKEY_LOCAL_MACHINE) >= 2361:
        isMoment4 = True
elif winver > 22621:
    isMoment4 = True


def evaluate_simple_expression(expression: str):  # supported expressions are of form x +/- y
        tokens = re.split(r'(\+|\-)', expression)
        first_token = tokens[0].strip()
        padded_with_zero = first_token.startswith("0")
        result = int(first_token)

        for i in range(1, len(tokens), 2):
            operator = tokens[i].strip()
            operand = int(tokens[i + 1].strip())

            if operator == "+":
                result += operand
            elif operator == "-":
                result -= operand
        
        if padded_with_zero:
            return f'0{result}'
        else:
            return result

def evaluate_expression_string(d, s: str, offset=0):
    def evaluate_match_time(match):
        expression=extract_sec_from_format(match.group(1))
        return str(datetime.datetime.fromtimestamp(d+int(expression[1])).strftime(expression[0]))
    def evaluate_match(match):
        expression = match.group(1)
        if re.fullmatch(r'\d+(\s*[\+\-]\s*\d+)*', expression):  # a valid expression is of form x +/- y
            return str(evaluate_simple_expression(expression))
        else:
            return match.group(0)  # Return the original text if not a valid expression

    time_formated = re.sub(r'\(([^)]*\{sec([+-]\d*)\})\)', evaluate_match_time, s)  # a valid expression is of (*{sec+/-N})
    time_formated = datetime.datetime.fromtimestamp(d-offset).strftime(time_formated)
    time_formated = re.sub(r'\{([^}]*)\}', evaluate_match, time_formated)  # a valid expression is of {*}
    return time_formated

def extract_sec_from_format(expression: str):
    extract_sec=re.findall(r'(.*)(\{sec([+-]\d*)\})$', expression) # a valid expression is of {sec+/-N} where N is any integer
    result=[]
    if extract_sec.__len__()>0 and extract_sec[0][1] != '':
        result.append(extract_sec[0][0])
        result.append(extract_sec[0][2])
    else:
        result.append(expression)
        result.append(0)
    return result

def getColors() -> list:
    colors = ['215,226,228', '160,174,183', '101,116,134', '81,92,107', '69,78,94', '41,47,64', '15,18,36', '239,105,80']
    string = readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\Accent", "AccentPalette", b'\xe9\xd8\xf1\x00\xcb\xb7\xde\x00\x96}\xbd\x00\x82g\xb0\x00gN\x97\x00H4s\x00#\x13K\x00\x88\x17\x98\x00')
    i = 0
    j = 0
    while (i+2)<len(string):
        colors[j] = f"{string[i]},{string[i+1]},{string[i+2]}"
        j += 1
        i += 4
    return colors

def getSettings(s: str, env: str = ""):
    settingsName = (env+s).replace("\\", "").replace("/", "")
    try:
        if not settingsName in globals.settingsCache:
            v = os.path.exists(os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock"), settingsName))
            globals.settingsCache[settingsName] = v
        return globals.settingsCache[settingsName]
    
    except Exception as e:
        report(e)

def setSettings(s: str, v: bool, r: bool = True, thread = False, env: str = ""):
    """
    if thread is set to true, effecs of r are eliminated
    """
    settingsName = (env+s).replace("\\", "").replace("/", "")
    try:
        globals.settingsCache = {}
        globals.settingsCache[settingsName] = v
        FILE = os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock"), settingsName)
        if(v):
            open(FILE, "w").close()
        else:
            try:
                if os.path.exists(FILE):
                    os.remove(FILE)
            except FileNotFoundError:
                pass
        try:
            if not thread and globals.SettingsWindow is not None:
                globals.SettingsWindow.updateCheckBoxesStatus()
                for sw in specificSettings.values():
                    sw.updateCheckBoxesStatus()
        except (NotImplementedError, AttributeError):
            pass
        if r and not thread:
            globals.restartClocks()
            if globals.TrayIcon:
                if(getSettings("DisableSystemTray") and len(globals.clocks)>0):
                    globals.TrayIcon.hide()
                else:
                    globals.TrayIcon.show()
    except Exception as e:
        report(e)

def getSettingsValue(s: str, env: str = "") -> str:
    settingsName = (env+s).replace("\\", "").replace("/", "")
    try:
        if settingsName+"Value" not in globals.settingsCache:
            FILE = os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock"), settingsName)
            if not os.path.exists(FILE): 
                return ""
            with open(FILE, "r") as sf:
                v = sf.read()
                globals.settingsCache[settingsName+"Value"] = v
        return str(globals.settingsCache[settingsName+"Value"])
    except FileNotFoundError:
        return ""
    except Exception as e:
        report(e)
        return ""

def setSettingsValue(s: str, v: str, r: bool = True, env: str = ""):
    settingsName = (env+s).replace("\\", "").replace("/", "")
    try:
        globals.settingsCache = {}
        globals.settingsCache[settingsName+"Value"] = v
        with open(os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock"), settingsName), "w") as sf:
            sf.write(v)
        globals.loadTimeFormat()
        if(r):
            globals.restartClocks()
    except Exception as e:
        report(e)


class KillableThread(Thread):
    def __init__(self, *args, **keywords):
        Thread.__init__(self, *args, **keywords)
        self.shouldBeRuning = True

    def start(self):
        self._run = self.run
        self.run = self.settrace_and_run
        Thread.start(self)

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

def getMousePos() -> QPoint:
    try:
        p = QCursor.pos()
        if p.x() == None:
            p.setX(0)
        if p.y() == None:
            p.setY(0)
        return p
    except AttributeError:
        print("🟣 Mouse thread returned AttributeError")
        return QPoint(0, 0)
    except Exception as e:
        report(e)
        return QPoint(0, 0)

def isDark():
    try:
        raise DeprecationWarning("This function has been deprecated and must be replaced with isWindowDark or isTaskbarDark!")
    except DeprecationWarning as e:
        report(e)
    return isWindowDark()

def ApplyMenuBlur(hwnd: int, window: QWidget, smallCorners: bool = False, avoidOverrideStyleSheet: bool = False, shadow: bool = True, useTaskbarModeCheck: bool = False):
    hwnd = int(hwnd)
    try:

        if not useTaskbarModeCheck:
            mode = isWindowDark()
        else:
            mode = isTaskbarDark()

        if not avoidOverrideStyleSheet:
            window.setStyleSheet("background-color: transparent;")
        if mode:
            GlobalBlur(hwnd, Acrylic=True, hexColor="#21212140", Dark=True, smallCorners=smallCorners)
            ExtendFrameIntoClientArea(hwnd)

        else:
            GlobalBlur(hwnd, Acrylic=True, hexColor="#eeeeee40", Dark=True, smallCorners=smallCorners)
            ExtendFrameIntoClientArea(hwnd)
    except Exception as e:
        report(e)

class Menu(QMenu):
    def __init__(self, title: str):
        self.setAttribute(Qt.WA_StyledBackground)
        super().__init__(title)

def getWindowHwnds(wName, prevHwnd = 0):
    try:
        hwnd = win32gui.FindWindowEx(0, prevHwnd, wName, None)
        if hwnd != 0:
            return [hwnd] + getWindowHwnds(wName, hwnd)
        else:
            return []
    except Exception as e:
        report(e)
        return []
    
def openClockSettings(clockInstance: 'Clock'):
    try:
        globals.BLOCK_RELOAD = True
        id, data = clockInstance.getClockID()
        
        if not id in specificSettings:
            print(f"🟢 Specific clock settings for clock {id} missing, generating one...")
            specificSettings[id] = globals.CustomSettings(id, data)
        specificSettings[id].show()
        globals.BLOCK_RELOAD = False    
    except Exception as e:
        report(e)

class QHoverButton(QPushButton):
    hovered = Signal()
    unhovered = Signal()
    pressed = Signal()
    unpressed = Signal()

    def __init__(self, text: str = "", parent: QObject = None) -> None:
        super().__init__(text=text, parent=parent)

    def enterEvent(self, event: QEvent) -> None:
        self.hovered.emit()
        return super().enterEvent(event)

    def leaveEvent(self, event: QEvent) -> None:
        self.unhovered.emit()
        return super().leaveEvent(event)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.pressed.emit()
        return super().mousePressEvent(e)

    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        self.unpressed.emit()
        return super().mouseReleaseEvent(e)
    
clockToHide: '__init__.Clock' = None
def hideClockFromMenu():
    global clockToHide
    if clockToHide:
        clockToHide.close()
                    
class TaskbarIconTray(QSystemTrayIcon):
    def __init__(self, app=None):
        super().__init__(app)
        self.menuScreen = QGuiApplication.primaryScreen()
        self.setIcon(QIcon(getPath("icon.ico")))
        self.show()
        self.setToolTip("ElevenClock - "+_("Customize the clock on Windows 11"))
        menu = QMenu(_("ElevenClock"))

        menu.setWindowFlag(Qt.WindowStaysOnTopHint)
        menu.setWindowFlags(menu.windowFlags() | Qt.FramelessWindowHint)
        menu.setAttribute(Qt.WA_TranslucentBackground)
        menu.addSeparator()
        self.settingsAction = QAction(_("ElevenClock Settings"), app)
        self.settingsAction.triggered.connect(lambda: globals.SettingsWindow.show())
        menu.addAction(self.settingsAction)
        self.reloadAction = QAction(_("Reload Clocks"), app)
        self.reloadAction.triggered.connect(lambda: globals.restartClocks())
        menu.addAction(self.reloadAction)
        self.reloadInternetAction = QAction(_("Sync time with the internet"), app)
        self.reloadInternetAction.triggered.connect(lambda: setSettings("ReloadInternetTime", True))
        menu.addAction(self.reloadInternetAction)
        menu.addSeparator()
        self.nameAction = QAction(_("ElevenClock v{0}").format(versionName), app)
        self.nameAction.setEnabled(False)
        menu.addAction(self.nameAction)
        menu.addSeparator()
        self.restartAction = QAction(_("Restart ElevenClock"), app)
        self.restartAction.triggered.connect(lambda: (os.startfile(sys.executable), globals.app.quit()))
        menu.addAction(self.restartAction)
        self.hideAction = QAction(_("Hide this clock"), app)
        self.hideAction.triggered.connect(hideClockFromMenu)
        menu.addAction(self.hideAction)
        self.quitAction = QAction(_("Quit ElevenClock"), app)
        self.quitAction.triggered.connect(lambda: globals.app.quit())
        menu.addAction(self.quitAction)
        menu.addSeparator()

        self.toolsMenu = menu.addMenu(_("Clock tools"))
        self.toolsMenu.setParent(menu)
        self.toolsMenu.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.toolsMenu.setWindowFlags(menu.windowFlags() | Qt.FramelessWindowHint)
        self.toolsMenu.setAttribute(Qt.WA_TranslucentBackground)
        self.toolsMenu.aboutToShow.connect(self.applyStyleSheet)
        menu.aboutToShow.connect(self.applyStyleSheet)
        
        def toggleCopliotMode():
            setSettings("EnableCopilotIcon", not getSettings("EnableCopilotIcon"))

        self.enableCopilot = QAction("COPILOT_ICON", app)
        self.enableCopilot.triggered.connect(toggleCopliotMode)
        menu.addAction(self.enableCopilot)
        
        def blacklist():
            setSettingsValue("BlacklistedMonitors", getSettingsValue("BlacklistedMonitors")+f"_{self.toolsMenu.screen().name()}_")

        def warnBlacklist():
            global msg
            msg = QFramelessDialog(parent=None, closeOnClick=True, xoff=self.toolsMenu.screen().geometry().x(), yoff=self.toolsMenu.screen().geometry().y())
            msg.setAutoFillBackground(True)
            msg.setStyleSheet(globals.SettingsWindow.styleSheet())
            msg.setAttribute(Qt.WA_StyledBackground)
            msg.setObjectName("QMessageBox")
            msg.setTitle(_("Blacklist Monitor"))
            msg.setText(f"""{_("Blacklisting a monitor will hide the clock on this monitor permanently.")}<br>
                            {_("This action can be reverted from the settings window, under <b>Clock position and size</b>")}.<br><br>

                            <b>{_('Are you sure do you want to blacklist the monitor "{0}"?').format(self.toolsMenu.screen().name())}</b>
    """)
            msg.addButton(_("Yes"), QDialogButtonBox.ButtonRole.ApplyRole, lambda: blacklist())
            msg.addButton(_("No"), QDialogButtonBox.ButtonRole.RejectRole)
            msg.setDefaultButtonRole(QDialogButtonBox.ButtonRole.ApplyRole, globals.SettingsWindow.styleSheet())
            msg.setWindowTitle("ElevenClock was updated!")
            msg.show()
        
        self.monitorInfoAction = QAction(_("Clock {0} on monitor {1}"), app)
        self.monitorInfoAction.setEnabled(False)
        self.toolsMenu.addAction(self.monitorInfoAction)
        self.toolsMenu.setEnabled(False)
        self.toolsMenu.addSeparator()
        
        self.individualSettings = QAction(_("Settings for this clock"))
        self.toolsMenu.addAction(self.individualSettings)
        
        self.toolsMenu.addSeparator()

        self.blacklistAction = QAction(_("Blacklist this monitor"), app)
        self.blacklistAction.triggered.connect(lambda: warnBlacklist())
        self.toolsMenu.addAction(self.blacklistAction)

        def toggleClockHorPosAction():
            screen = self.contextMenu().screen().name().replace("\\", "_")
            if getSettings("ClockOnTheLeft"):
                if getSettings(f"SpecificClockOnTheRight{screen}"):
                    setSettings(f"SpecificClockOnTheRight{screen}", False)
                else:
                    setSettings(f"SpecificClockOnTheRight{screen}", True)
            else:
                if getSettings(f"SpecificClockOnTheLeft{screen}"):
                    setSettings(f"SpecificClockOnTheLeft{screen}", False)
                else:
                    setSettings(f"SpecificClockOnTheLeft{screen}", True)

        self.moveToLeftAction = QAction("Placeholder text", app)
        self.moveToLeftAction.triggered.connect(lambda: toggleClockHorPosAction())
        self.toolsMenu.addAction(self.moveToLeftAction)

        def toggleClockVerPosAction():
            screen = self.contextMenu().screen().name().replace("\\", "_")
            if getSettings("ForceOnTop"):
                if getSettings(f"SpecificClockOnTheBottom{screen}"):
                    setSettings(f"SpecificClockOnTheBottom{screen}", False)
                else:
                    setSettings(f"SpecificClockOnTheBottom{screen}", True)
            else:
                if getSettings(f"SpecificClockOnTheTop{screen}"):
                    setSettings(f"SpecificClockOnTheTop{screen}", False)
                else:
                    setSettings(f"SpecificClockOnTheTop{screen}", True)

        self.moveToTopAction = QAction("Placeholder text", app)
        self.moveToTopAction.triggered.connect(lambda: toggleClockVerPosAction())
        self.toolsMenu.addAction(self.moveToTopAction)


        menu.addSeparator()
        self.takmgr = QAction(_("Task Manager"), app)
        self.takmgr.triggered.connect(lambda: os.startfile('taskmgr'))
        if not getSettings("HideTaskManagerButton"):
            menu.addAction(self.takmgr)
        self.datetimeprefs = QAction(_("Change date and time"), app)
        self.datetimeprefs.triggered.connect(lambda: os.startfile('ms-settings:dateandtime'))
        if not getSettings("HideTaskManagerButton"):
            menu.addAction(self.datetimeprefs)
        self.notifprefs = QAction(_("Notification settings"), app)
        self.notifprefs.triggered.connect(lambda: os.startfile('ms-settings:notifications'))
        if not getSettings("HideTaskManagerButton"):
            menu.addAction(self.notifprefs)

        self.setContextMenu(menu)
        self.menuScreen = self.contextMenu().screen()

        def activationHandler(reason: QSystemTrayIcon.ActivationReason) -> None:
            match reason:
                case QSystemTrayIcon.ActivationReason.DoubleClick:
                    globals.SettingsWindow.show()
                case QSystemTrayIcon.ActivationReason.Context:
                    return
                case _:
                    globals.restartClocks()

        self.activated.connect(lambda r: activationHandler(r))

        
        self.applyStyleSheet()

    def showMenu(self, clock: '__init__.Clock'):
        pos = QPoint(0, 0)
        self.menuScreen = clock.screen()

        menuHeight = self.contextMenu().height()
        if menuHeight == 480:
            self.contextMenu().show() # Force a draw of the window and fetch the data again
            menuHeight = self.contextMenu().height()
                        
        menuWidth = self.contextMenu().width()

        if clock.CLOCK_ON_THE_LEFT:
            pos.setX(clock.screen().geometry().x()+(5))
        else:
            pos.setX(clock.screen().geometry().x()+clock.screen().geometry().width()-(5)-menuWidth)

        if clock.CLOCK_ON_TOP:
            pos.setY(clock.screen().geometry().y()+(5)+clock.height())
        else:
            pos.setY(clock.screen().geometry().y()+clock.screen().geometry().height()-clock.height()-(5)-menuHeight)

        self.execMenu(pos, clockInstance=clock)


    def execMenu(self, pos: QPoint, clockInstance: '__init__.Clock'):
        global clockToHide
        clockToHide = clockInstance
        try:
            self.toolsMenu.setEnabled(True)
            try:
                screen = globals.app.screenAt(pos)
                screenName = screen.name().replace("\\", "_")
            except AttributeError:
                pos.setY(pos.y() if pos.y() > 0 else 1)
                pos.setX(pos.x() if pos.x() > 0 else 1)
                screen = globals.app.screenAt(pos)
                screenName = screen.name().replace("\\", "_")
            if getSettings("ClockOnTheLeft"):
                if getSettings(f"SpecificClockOnTheRight{screenName}"):
                    self.moveToLeftAction.setText(_("Restore horizontal position"))
                else:
                    self.moveToLeftAction.setText(_("Move this clock to the right"))
            else:
                if getSettings(f"SpecificClockOnTheLeft{screenName}"):
                    self.moveToLeftAction.setText(_("Restore horizontal position"))
                else:
                    self.moveToLeftAction.setText(_("Move this clock to the left"))

            if getSettings("ForceOnTop"):
                if getSettings(f"SpecificClockOnTheBottom{screenName}"):
                    self.moveToTopAction.setText(_("Restore vertical position"))
                else:
                    self.moveToTopAction.setText(_("Move this clock to the bottom"))
            else:
                if getSettings(f"SpecificClockOnTheTop{screenName}"):
                    self.moveToTopAction.setText(_("Restore vertical position"))
                else:
                    self.moveToTopAction.setText(_("Move this clock to the top"))
            if clockInstance:
                self.monitorInfoAction.setText(_("Clock {0} on monitor {1}").format(clockInstance.getClockID()[1][0], clockInstance.getClockID()[1][1]))
                self.toolsMenu.setEnabled(True)
            else:
                self.toolsMenu.setEnabled(False)
            
            if clockInstance:
                self.enableCopilot.setEnabled(True)
                self.enableCopilot.setText(_("Enable Copilot button") if not IsCopilotEnabled() else _("Disable Copilot button"))
            else:
                self.enableCopilot.setEnabled(False)
            
            self.individualSettings.triggered.disconnect()
            self.individualSettings.triggered.connect(partial(openClockSettings, clockInstance))
            self.contextMenu().exec(pos)
            self.applyStyleSheet()
        except Exception as e:
            report(e)

    def get6px(self, i: int) -> int:
        return round(i*self.screen().devicePixelRatio())

    def applyStyleSheet(self) -> None:
        global lastMenuTheme
        if isTaskbarDark():
            GlobalBlur(self.contextMenu().winId(), Acrylic=True, hexColor="#21212140", Dark=True)
            GlobalBlur(self.toolsMenu.winId(), Acrylic=True, hexColor="#21212140", Dark=True)
            ExtendFrameIntoClientArea(self.toolsMenu.winId())
            ExtendFrameIntoClientArea(self.contextMenu().winId())
            if lastMenuTheme != 0:
                lastMenuTheme = 0
                self.iconMode = "white"

                if "zh_TW" in lang["locale"]:
                    fontStr = "font-family: \"Microsoft Jhenghei UI\""
                elif "zh_CN" in lang["locale"]:
                    fontStr = "font-family: \"Microsoft YaHei UI\""
                else:
                    fontStr = "font-family: \"Segoe UI Variable Text\""
                
                self.contextMenu().setStyleSheet(f"""
                    * {{
                        border-radius: 8px;
                        background-color: transparent;
                        font-size: 9pt;
                        {fontStr};
                    }}
                    QWidget{{
                        background-color: transparent;
                        border-radius: 8px;
                    }}
                    QMenu {{
                        border: 1px solid #111111;
                        padding: 2px;
                        outline: 0;
                        color: white;
                        icon-size: {(32)}px;
                        background: rgba(0, 0, 0, 0.01%);
                        border-radius: 8px;
                    }}
                    QMenu::separator {{
                        margin: {(-2)}px;
                        margin-top: 2px;
                        margin-bottom: 2px;
                        height: 1px;
                        background-color: rgba(255, 255, 255, 20%);
                    }}
                    QMenu::icon {{
                        padding-left: 10px;
                        padding-left: 10px;
                    }}
                    QMenu::item {{
                        height: 30px;
                        border: none;
                        background: transparent;
                        padding-right: {(20)}px;
                        padding-left: 0;
                        border-radius: 4px;
                        margin: 2px;
                    }}
                    QMenu::item:selected {{
                        background: rgba(255, 255, 255, 6%);
                        height: 30px;
                        outline: none;
                        border: none;
                        padding-right: {(20)}px;
                        padding-left: 0;
                        border-radius: 4px;
                    }}
                    QMenu::item:disabled {{
                        background: transparent;
                        height: 30px;
                        outline: none;
                        border: none;
                        color: grey;
                        padding-right: {(20)}px;
                        padding-left: 0;
                        border-radius: 4px;
                    }}
                    QMenu::item:selected:disabled {{
                        background: transparent;
                        height: 30px;
                        outline: none;
                        border: none;
                        padding-right: {(20)}px;
                        padding-left: 0;
                        border-radius: 4px;
                    }}
                    """)
        else:
            GlobalBlur(self.contextMenu().winId(), Acrylic=True, hexColor="#eeeeee40", Dark=False)
            GlobalBlur(self.toolsMenu.winId(), Acrylic=True, hexColor="#eeeeee40", Dark=False)
            ExtendFrameIntoClientArea(self.toolsMenu.winId())
            ExtendFrameIntoClientArea(self.contextMenu().winId())
            if lastMenuTheme != 1:
                lastMenuTheme = 1
                self.iconMode = "black"
                
                if "zh_TW" in lang["locale"]:
                    fontStr = "font-family: \"Microsoft Jhenghei UI\""
                elif "zh_CN" in lang["locale"]:
                    fontStr = "font-family: \"Microsoft YaHei UI\""
                else:
                    fontStr = "font-family: \"Segoe UI Variable Text\""
                
                self.contextMenu().setStyleSheet(f"""
                    * {{
                        {fontStr};
                    }}
                    QWidget{{
                        background-color: transparent;
                    }}
                    QMenu {{
                        border: 1px solid rgb(200, 200, 200);
                        padding: 2px;
                        outline: 0;
                        color: black;
                        icon-size: {(32)}px;
                        background: rgba(220, 220, 220, 1%)/*#262626*/;
                        border-radius: 8px;
                    }}
                    QMenu::separator {{
                        margin: {(-2)}px;
                        margin-top: 2px;
                        margin-bottom: 2px;
                        height: 1px;
                        background-color: rgba(0, 0, 0, 20%);
                    }}
                    QMenu::icon{{
                        padding-left: 10px;
                    }}
                    QMenu::item{{
                        height: 30px;
                        border: none;
                        background: transparent;
                        padding-right: {(20)}px;
                        padding-left: 0;
                        border-radius: 4px;
                        margin: 2px;
                    }}
                    QMenu::item:selected{{
                        background: rgba(0, 0, 0, 10%);
                        height: 30px;
                        outline: none;
                        border: none;
                        padding-right: {(20)}px;
                        padding-left: 0;
                        border-radius: 4px;
                    }}
                    QMenu::item:selected:disabled{{
                        background: transparent;
                        height: 30px;
                        outline: none;
                        border: none;
                        padding-right: {(20)}px;
                        padding-left: 0;
                        border-radius: 4px;
                    }}
                    """)
        self.datetimeprefs.setIcon(QIcon(getPath(f"settings_{self.iconMode}.png")))
        self.individualSettings.setIcon(QIcon(getPath(f"settings_{self.iconMode}.png")))
        self.notifprefs.setIcon(QIcon(getPath(f"settings_{self.iconMode}.png")))
        self.takmgr.setIcon(QIcon(getPath(f"taskmgr_{self.iconMode}.png")))
        self.settingsAction.setIcon(QIcon(getPath(f"settings_{self.iconMode}.png")))
        self.reloadAction.setIcon(QIcon(getPath(f"clock_{self.iconMode}.png")))
        self.nameAction.setIcon(QIcon(getPath(f"about_{self.iconMode}.png")))
        self.monitorInfoAction.setIcon(QIcon(getPath(f"about_{self.iconMode}.png")))
        self.moveToLeftAction.setIcon(QIcon(getPath(f"move_horizontal_{self.iconMode}.png")))
        self.moveToTopAction.setIcon(QIcon(getPath(f"move_vertical_{self.iconMode}.png")))
        self.restartAction.setIcon(QIcon(getPath(f"restart_{self.iconMode}.png")))
        self.hideAction.setIcon(QIcon(getPath(f"hide_{self.iconMode}.png")))
        self.quitAction.setIcon(QIcon(getPath(f"close_{self.iconMode}.png")))
        self.toolsMenu.setIcon(QIcon(getPath(f"tools_{self.iconMode}.png")))
        self.reloadInternetAction.setIcon(QIcon(getPath(f"internet_{self.iconMode}.png")))
        self.blacklistAction.setIcon(QIcon(getPath(f"blacklistscreen_{self.iconMode}.png")))
        self.enableCopilot.setIcon(QIcon(getPath(f"copilot_color.png")))



if hasattr(sys, 'frozen'):
    realpath = sys._MEIPASS
else:
    realpath = '/'.join(sys.argv[0].replace("\\", "/").split("/")[:-1])

try:
    os.chdir(os.path.expanduser("~"))
    os.chdir(".elevenclock")
except FileNotFoundError:
    os.mkdir(".elevenclock")


def loadLangFile(file: str, bundled: bool = False) -> dict:
    try:
        path = os.path.join(os.path.expanduser("~"), ".elevenclock/lang/"+file)
        if not os.path.exists(path) or getSettings("DisableLangAutoUpdater") or bundled:
            print(f"🟡 Using bundled lang file (forced={bundled})")
            path = getPath("../lang/"+file)
        else:
            print("🟢 Using cached lang file")
        with open(path, "r", encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        report(e)
        return {}

def resetSettingsWindow():
    ow = globals.SettingsWindow
    from settings import SettingsUI
    globals.SettingsWindow = SettingsUI()
    ow.hide()
    ow.close()
    del ow

def drawVerticalLine(canvas: QSize, lineHeight: int, alpha = 255) -> QPixmap:
    width = canvas.width()
    height = canvas.height()
    pixmap = QPixmap(canvas)
    pixmap.fill(Qt.transparent)
    linePainter = QPainter(pixmap)
    lineColor = QColor(255, 255, 255, alpha) if isTaskbarDark() else QColor(0, 0, 0, alpha)
    y = (height-lineHeight)/2-1
    linePainter.setPen(lineColor)
    linePainter.drawLine(width/2, y, width/2, y+lineHeight)    
    linePainter.end()
    return pixmap

def verifyHwndValidity(hwnd):
    """
    This function checks if the given hwnd is not part of the *TextInputHost.exe process family. This function should be called as an individual thread
    """ 
    rect = win32gui.GetWindowRect(hwnd)
    pythoncom.CoInitialize()
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    pHandle = 0
    try:
        pHandle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION or win32con.PROCESS_VM_READ, False, pid)
    except pywintypes.error:
        pass
    if pHandle != 0:
        pname = win32process.GetModuleFileNameEx(pHandle, 0)
        if str(pname).lower().endswith("textinputhost.exe") or str(pname).lower().endswith("lockapp.exe") or str(pname).lower().endswith("rtkuwp.exe"):
            globals.cachedInputHosts.append(hwnd)
            print(f"🟡 Blacklisted hwnd {hwnd} under title {win32gui.GetWindowText(hwnd)} (Process name is {str(pname).lower()})")
        else:
            globals.notTextInputHost.append(hwnd)
            print(f"🟢 Hwnd {hwnd} under title {win32gui.GetWindowText(hwnd)} was verified as a valid window (Process name is {str(pname).lower()})")


def updateLangFile(file: str):
    global lang
    try:
        try:
            oldlang = open(os.path.join(os.path.expanduser("~"), ".elevenclock/lang/"+file), "rb").read()
        except FileNotFoundError:
            oldlang = ""
        newlang = urlopen("https://raw.githubusercontent.com/marticliment/ElevenClock/main/elevenclock/lang/"+file)
        if newlang.status == 200:
            langdata: bytes = newlang.read()
            if not os.path.isdir(os.path.join(os.path.expanduser("~"), ".elevenclock/lang/")):
                os.makedirs(os.path.join(os.path.expanduser("~"), ".elevenclock/lang/"))
            if oldlang != langdata:
                print("🟢 Updating outdated language file...")
                with open(os.path.join(os.path.expanduser("~"), ".elevenclock/lang/"+file), "wb") as f:
                    f.write(langdata)
                    f.close()
                    lang = loadLangFile(file) | {"locale": lang["locale"] if "locale" in lang.keys() else "en"}
                    while globals.SettingsWindow == None:
                        time.sleep(0.1)
                        print("🟠 Waiting for sw to not be null")
                    while globals.SettingsWindow.isVisible():
                        time.sleep(0.1)
                        print("🟠 Waiting for sw to be hidden")
                    globals.SettingsWindow.callInMain.emit(resetSettingsWindow)
            else:
                print("🔵 Language file up-to-date")
                
    except Exception as e:
        report(e)

def textToClipboard(text: str):
    globals.app.clipboard().setText(text.strip())

t0 = time.time()

langName = getSettingsValue("PreferredLanguage")
if langName == "":
    if not QApplication.instance():
        a = QApplication(sys.argv)
    else:
        a = QApplication.instance()
    w = QWidget()
    w.setWindowIcon(QIcon(getPath("icon.png")))
    ans = QInputDialog.getItem(w, "Welcome to ElevenClock", "Please select the language you want ElevenClock to use:", languageReference.values(), editable=False)
    w.deleteLater()
    w.close()
    if ans[1] == False:
        setSettingsValue("PreferredLanguage", "default", r=False)
    else:
        value = ans[0]
        for key in languageReference.keys():
            if languageReference[key] == value:
                langName = key
                break
        if langName == "":
            langName = "default"
        setSettingsValue("PreferredLanguage", langName, r=False)
        
try:
    if (langName == "default"):
        langName = locale.getdefaultlocale()[0]
    langNames = [langName, langName[0:2]]
    langFound = False
    for ln in langNames:
        if (ln in languages):
            lang = loadLangFile(languages[ln]) | {"locale": ln}
            langFound = True
            if not getSettings("DisableLangAutoUpdater"):
                Thread(target=updateLangFile, args=(languages[ln],), name=f"DAEMON: Update lang_{ln}.json").start()
            break
    if (langFound == False):
        raise Exception(f"Value not found for {langNames}")
except Exception as e:
    report(e)
    lang = loadLangFile(languages["en"]) | {"locale": "en"}
    print("🔴 Unknown language")

langName = lang['locale']

try:
    englang = loadLangFile(languages["en"], bundled=True) | {"locale": "en"}
except Exception as e:
    report(e)
    englang = {"locale": "en"}

print(f"It took {time.time()-t0} to load all language files")

if __name__ == "__main__":
    import __init__
