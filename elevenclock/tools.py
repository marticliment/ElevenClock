from ctypes import c_int, windll
windll.shcore.SetProcessDpiAwareness(c_int(2))

import os
import sys
import winreg
import threading
import locale
 
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtWinExtras import QtWin
import platform

from external.blurwindow import GlobalBlur
import pyautogui



import globals
from languages import *
from external.FramelessWindow import QFramelessDialog

import win32gui
from win32con import *

version = 3.41
versionName = "3.4.1"


try:
    winver = int(platform.version().split('.')[2])
except Exception as e:
    print(e)
    winver = 22000

def _(s): #Translate function
    global lang
    try:
        t = lang.lang[s]
        return (t+"✅[Found]✅" if debugLang else t) if t else f"{s}⚠️[UntranslatedString]⚠️" if debugLang else s
    except KeyError:
        if debugLang: print(s)
        return f"{s}🔴[MissingString]🔴" if debugLang else s

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

def isWindowDark() -> str:
    return readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "AppsUseLightTheme", 1)==0

def isTaskbarDark() -> str:
    return readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "SystemUsesLightTheme", 1)==0


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

def getSettings(s: str):
    try:
        try:
            return globals.settingsCache[s]
        except KeyError:
            v = os.path.exists(os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock"), s))
            globals.settingsCache[s] = v
            return v
    except Exception as e:
        report(e)

def setSettings(s: str, v: bool, r: bool = True):
    try:
        globals.settingsCache = {}
        if(v):
            open(os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock"), s), "w").close()
        else:
            try:
                os.remove(os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock"), s))
            except FileNotFoundError:
                pass
        try:
            globals.loadTimeFormat()
            globals.sw.updateCheckBoxesStatus()
        except (NotImplementedError, AttributeError):
            pass
        if(r):
            globals.restartClocks()
            if(getSettings("DisableSystemTray")):
                globals.trayIcon.hide()
            else:
                globals.trayIcon.show()
    except Exception as e:
        report(e)

def getSettingsValue(s: str):
    try:
        try:
            return globals.settingsCache[s+"Value"]
        except KeyError:
            with open(os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock"), s), "r") as sf:
                v = sf.read()
                globals.settingsCache[s+"Value"] = v
                return v
    except FileNotFoundError:
        return ""
    except Exception as e:
        report(e)
        return ""

def setSettingsValue(s: str, v: str, r: bool = True):
    try:
        globals.settingsCache = {}
        with open(os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock"), s), "w") as sf:
            sf.write(v)
        globals.loadTimeFormat()
        if(r):
            globals.restartClocks()
    except Exception as e:
        report(e)


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

def getMousePos() -> QPoint:
    try:
        p = QPoint(pyautogui.position()[0], pyautogui.position()[1])
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
    #window.setAttribute(Qt.WA_TranslucentBackground)
    #window.setAttribute(Qt.WA_NoSystemBackground)

    if not useTaskbarModeCheck:
        mode = isWindowDark()
    else:
        mode = isTaskbarDark()

    if not avoidOverrideStyleSheet:
        window.setStyleSheet("background-color: transparent;")
    if mode:
        GlobalBlur(hwnd, Acrylic=True, hexColor="#21212140", Dark=True, smallCorners=smallCorners)
        if shadow:
            QtWin.extendFrameIntoClientArea(window, -1, -1, -1, -1)
    else:
        GlobalBlur(hwnd, Acrylic=True, hexColor="#eeeeee40", Dark=True, smallCorners=smallCorners)
        if shadow: 
            QtWin.extendFrameIntoClientArea(window, -1, -1, -1, -1)

class Menu(QMenu):
    def __init__(self, title: str):
        self.setAttribute(Qt.WA_StyledBackground)
        super().__init__(title)
        

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
        self.settingsAction.triggered.connect(lambda: globals.sw.show())
        menu.addAction(self.settingsAction)
        self.reloadAction = QAction(_("Reload Clocks"), app)
        self.reloadAction.triggered.connect(lambda: globals.restartClocks())
        menu.addAction(self.reloadAction)
        menu.addSeparator()
        self.nameAction = QAction(_("ElevenClock v{0}").format(versionName), app)
        self.nameAction.setEnabled(False)
        menu.addAction(self.nameAction)
        menu.addSeparator()
        self.restartAction = QAction(_("Restart ElevenClock"), app)
        self.restartAction.triggered.connect(lambda: os.startfile(sys.executable))
        menu.addAction(self.restartAction)
        self.hideAction = QAction(_("Hide ElevenClock"), app)
        self.hideAction.triggered.connect(lambda: globals.closeClocks())
        menu.addAction(self.hideAction)
        self.quitAction = QAction(_("Quit ElevenClock"), app)
        self.quitAction.triggered.connect(lambda: globals.app.quit())
        menu.addAction(self.quitAction)
        menu.addSeparator()
        
        self.toolsMenu = menu.addMenu(_("Monitor tools"))
        self.toolsMenu.setParent(menu)
        self.toolsMenu.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.toolsMenu.setWindowFlags(menu.windowFlags() | Qt.FramelessWindowHint)
        self.toolsMenu.setAttribute(Qt.WA_TranslucentBackground)

        def blacklist():
            setSettingsValue("BlacklistedMonitors", getSettingsValue("BlacklistedMonitors")+f"_{self.toolsMenu.screen().name()}_")

        def warnBlacklist():
            global msg
            msg = QFramelessDialog(parent=None, closeOnClick=True, xoff=self.toolsMenu.screen().geometry().x(), yoff=self.toolsMenu.screen().geometry().y())
            msg.setAutoFillBackground(True)
            msg.setStyleSheet(globals.sw.styleSheet())
            msg.setAttribute(Qt.WA_StyledBackground)
            msg.setObjectName("QMessageBox")
            msg.setTitle(_("Blacklist Monitor"))
            msg.setText(f"""{_("Blacklisting a monitor will hide the clock on this monitor permanently.")}<br>
                            {_("This action can be reverted from the settings window, under <b>Clock position and size</b>")}.<br><br>

                            <b>{_('Are you sure do you want to blacklist the monitor "{0}"?').format(self.toolsMenu.screen().name())}</b>
    """)
            msg.addButton(_("Yes"), QDialogButtonBox.ButtonRole.ApplyRole, lambda: blacklist())
            msg.addButton(_("No"), QDialogButtonBox.ButtonRole.RejectRole)
            msg.setDefaultButtonRole(QDialogButtonBox.ButtonRole.ApplyRole, globals.sw.styleSheet())
            msg.setWindowTitle("ElevenClock has updated!")
            msg.show()

        self.monitorInfoAction = QAction(_("Clock on monitor {0}"), app)
        self.monitorInfoAction.setEnabled(False)
        self.toolsMenu.addAction(self.monitorInfoAction)
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

        def reloadClocksIfRequired(reason: QSystemTrayIcon.ActivationReason) -> None:
            if(reason != QSystemTrayIcon.ActivationReason.Context):
                globals.restartClocks()

        self.activated.connect(lambda r: reloadClocksIfRequired(r))

        if(getSettings("DisableSystemTray")):
            self.hide()
            print("🟡 System tray icon disabled")
        else:
            self.show()
            print("🔵 System tray icon enabled")
        self.applyStyleSheet()
    

    def showMenu(self, clock):
        pos = QPoint(0, 0)
        self.menuScreen = clock.screen()

        if(self.contextMenu().height() != 480):
            menuHeight = self.contextMenu().height()
        else:
            if getSettings("HideTaskManagerButton"):
                menuHeight = clock.getPx(260)
            else:
                menuHeight = clock.getPx(370)

        if(self.contextMenu().width() != 640):
            menuWidth = self.contextMenu().width()
        else:
            menuWidth = clock.getPx(225)

        if clock.clockOnTheLeft:
            pos.setX(clock.screen().geometry().x()+clock.getPx(5))
        else:
            pos.setX(clock.screen().geometry().x()+clock.screen().geometry().width()-clock.getPx(5)-menuWidth)
        
        if clock.clockOnTop:
            pos.setY(clock.screen().geometry().y()+clock.getPx(5)+clock.height())
        else:
            pos.setY(clock.screen().geometry().y()+clock.screen().geometry().height()-clock.height()-clock.getPx(5)-menuHeight)
        
        self.execMenu(pos)


    def execMenu(self, pos: QPoint):
        try:
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
            self.monitorInfoAction.setText(_("Clock on monitor {0}").format(screenName.replace("_", "\\")))
            self.contextMenu().exec_(pos)
            self.applyStyleSheet()
        except Exception as e:
            report(e)

    def getPx(self, original) -> int:
        return round(original*(self.menuScreen.logicalDotsPerInchX()/96))

    def applyStyleSheet(self) -> None:
        if isTaskbarDark():
            self.iconMode = "white"
            GlobalBlur(self.contextMenu().winId(), Acrylic=True, hexColor="#21212140", Dark=True)
            GlobalBlur(self.toolsMenu.winId(), Acrylic=True, hexColor="#21212140", Dark=True)
            QtWin.extendFrameIntoClientArea(self.contextMenu(), -1, -1, -1, -1)
            QtWin.extendFrameIntoClientArea(self.toolsMenu, -1, -1, -1, -1)

            self.contextMenu().setStyleSheet(f"""
                * {{
                    border-radius: {self.getPx(8)}px;
                    background-color: transparent;
                }}
                QWidget{{
                    background-color: transparent;
                    border-radius: {self.getPx(8)}px;
                }}  
                QMenu {{
                    border: {self.getPx(1)}px solid #111111;
                    padding: {self.getPx(2)}px;
                    outline: 0px;
                    color: white;
                    icon-size: {self.getPx(32)}px;
                    background: rgba(0, 0, 0, 0.01%);
                    border-radius: {self.getPx(8)}px;
                }}
                QMenu::separator {{
                    margin: {self.getPx(-2)}px;
                    margin-top: {self.getPx(2)}px;
                    margin-bottom: {self.getPx(2)}px;
                    height: {self.getPx(1)}px;
                    background-color: rgba(255, 255, 255, 20%);
                }}
                QMenu::icon {{
                    padding-left: {self.getPx(10)}px;
                    padding-left: {self.getPx(10)}px;
                }}
                QMenu::item {{
                    height: {self.getPx(30)}px;
                    border: none;
                    background: transparent;
                    padding-right: {self.getPx(20)}px;
                    padding-left: {self.getPx(0)}px;
                    border-radius: {self.getPx(4)}px;
                    margin: {self.getPx(2)}px;
                }}
                QMenu::item:selected {{
                    background: rgba(255, 255, 255, 6%);
                    height: {self.getPx(30)}px;
                    outline: none;
                    border: none;
                    padding-right: {self.getPx(20)}px;
                    padding-left: {self.getPx(0)}px;
                    border-radius: {self.getPx(4)}px;
                }}  
                QMenu::item:selected:disabled {{
                    background: transparent;
                    height: {self.getPx(30)}px;
                    outline: none;
                    border: none;
                    padding-right: {self.getPx(20)}px;
                    padding-left: {self.getPx(0)}px;
                    border-radius: {self.getPx(4)}px;
                }}            
                """)
        else:
            self.iconMode = "black"
            GlobalBlur(self.contextMenu().winId(), Acrylic=True, hexColor="#eeeeee40", Dark=False)
            GlobalBlur(self.toolsMenu.winId(), Acrylic=True, hexColor="#eeeeee40", Dark=False)
            QtWin.extendFrameIntoClientArea(self.contextMenu(), -1, -1, -1, -1)
            QtWin.extendFrameIntoClientArea(self.toolsMenu, -1, -1, -1, -1)
            self.contextMenu().setStyleSheet(f"""
                QWidget{{
                    background-color: transparent;
                }}  
                QMenu {{
                    border: {self.getPx(1)}px solid rgb(200, 200, 200);
                    padding: {self.getPx(2)}px;
                    outline: 0px;
                    color: black;
                    icon-size: {self.getPx(32)}px;
                    background: rgba(220, 220, 220, 1%)/*#262626*/;
                    border-radius: {self.getPx(8)}px;
                }}
                QMenu::separator {{
                    margin: {self.getPx(-2)}px;
                    margin-top: {self.getPx(2)}px;
                    margin-bottom: {self.getPx(2)}px;
                    height: {self.getPx(1)}px;
                    background-color: rgba(0, 0, 0, 20%);
                }}
                QMenu::icon{{
                    padding-left: {self.getPx(10)}px;
                }}
                QMenu::item{{
                    height: {self.getPx(30)}px;
                    border: none;
                    background: transparent;
                    padding-right: {self.getPx(20)}px;
                    padding-left: {self.getPx(0)}px;
                    border-radius: {self.getPx(4)}px;
                    margin: {self.getPx(2)}px;
                }}
                QMenu::item:selected{{
                    background: rgba(0, 0, 0, 10%);
                    height: {self.getPx(30)}px;
                    outline: none;
                    border: none;
                    padding-right: {self.getPx(20)}px;
                    padding-left: {self.getPx(0)}px;
                    border-radius: {self.getPx(4)}px;
                }}  
                QMenu::item:selected:disabled{{
                    background: transparent;
                    height: {self.getPx(30)}px;
                    outline: none;
                    border: none;
                    padding-right: {self.getPx(20)}px;
                    padding-left: {self.getPx(0)}px;
                    border-radius: {self.getPx(4)}px;
                }}            
                """)
        self.datetimeprefs.setIcon(QIcon(getPath(f"settings_{self.iconMode}.png")))
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
        self.blacklistAction.setIcon(QIcon(getPath(f"blacklistscreen_{self.iconMode}.png")))



if hasattr(sys, 'frozen'):
    realpath = sys._MEIPASS
else:
    realpath = '/'.join(sys.argv[0].replace("\\", "/").split("/")[:-1])

try:
    os.chdir(os.path.expanduser("~"))
    os.chdir(".elevenclock")
except FileNotFoundError:
    os.mkdir(".elevenclock")


if getSettingsValue("PreferredLanguage") == "":
    setSettingsValue("PreferredLanguage", "default", False)

if getSettingsValue("PreferredLanguage") == "default":
    langName = "default"
    try:
        langName = locale.getdefaultlocale()[0][0:2]
        if(langName != "zh" and langName != "pt"):
            lang = languages[langName]
        elif(locale.getdefaultlocale()[0].replace("\n", "").strip() == "pt_PT"):
            langName = "pt_PT"
            lang = languages["pt_PT"]
        elif(locale.getdefaultlocale()[0].replace("\n", "").strip() == "pt_BR"):
            langName = "pt_BR"
            lang = languages["pt_BR"]
        elif(locale.getdefaultlocale()[0].replace("\n", "").strip() == "zh_TW"):
            langName = "zh_TW"
            lang = languages["zh_TW"]
        elif(locale.getdefaultlocale()[0].replace("\n", "").strip() == "zh_CN"):
            langName = "zh_CN"
            lang = languages["zh_CN"]
        else:
            raise KeyError(f"Value not found for {langName}")
    except KeyError:
        lang = lang_en
        print("unknown language")
    except Exception as e:
        report(e)
        lang = lang_en
else:
    try:
        langName = getSettingsValue("PreferredLanguage")[0:2]
        if(langName != "zh" and langName != "pt"):
            lang = languages[langName]
        elif(getSettingsValue("PreferredLanguage").replace("\n", "").strip() == "pt_PT"):
            langName = "pt_PT"
            lang = languages["pt_PT"]
        elif(getSettingsValue("PreferredLanguage").replace("\n", "").strip() == "pt_BR"):
            langName = "pt_BR"
            lang = languages["pt_BR"]
        elif(getSettingsValue("PreferredLanguage").replace("\n", "").strip() == "zh_TW"):
            langName = "zh_TW"
            lang = languages["zh_TW"]
        elif(getSettingsValue("PreferredLanguage").replace("\n", "").strip() == "zh_CN"):
            langName = "zh_CN"
            lang = languages["zh_CN"]
        else:
            raise KeyError(f"Value not found for {langName}")
    except KeyError:
        lang = lang_en
        langName = "en"
        print("🔴 Unknown language")
    except Exception as e:
        report(e)
        lang = lang_en
        langName = "en"

if lang == None:
    lang = lang_en
    
    
if __name__ == "__main__":
    import __init__