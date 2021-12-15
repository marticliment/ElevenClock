import os
import sys
import winreg
import threading
import locale
 
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

import globals
from languages import *

version = 2.91
versionName = "3.0.0-dev"

def _(s): #Translate function
    global lang
    try:
        t = lang.lang[s]
        return (t+"✅[Found]✅" if debugLang else t) if t else f"{s}⚠️[UntranslatedString]⚠️" if debugLang else s
    except KeyError:
        if debugLang: print(s)
        return f"{s}🔴[MissingString]🔴" if debugLang else s

def getPath(s):
    return os.path.join(os.path.join(realpath, "resources"), s).replace("\\", "/")

def report(exception) -> None: # Exception reporter
    import traceback
    for line in traceback.format_exception(*sys.exc_info()):
        print("🔴 "+line)
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

def getSettings(s: str):
    try:
        return os.path.exists(os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock"), s))
    except Exception as e:
        report(e)

def setSettings(s: str, v: bool, r: bool = True):
    try:
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
        with open(os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock"), s), "r") as sf:
            return sf.read()
    except FileNotFoundError:
        return ""
    except Exception as e:
        report(e)
        return ""

def setSettingsValue(s: str, v: str, r: bool = True):
    try:
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

class Menu(QMenu):
    def __init__(self, title: str):
        self.setAttribute(Qt.WA_StyledBackground)
        super().__init__(title)

        
from BlurWindow.blurWindow import GlobalBlur
        
class TaskbarIconTray(QSystemTrayIcon):
    def __init__(self, app=None):
        super().__init__(app)
        self.setIcon(QIcon(getPath("icon.ico")))
        self.show()
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

    def execMenu(self, pos: QPoint):
        self.applyStyleSheet()
        self.contextMenu().exec_(pos)

    def getPx(self, original) -> int:
        return round(original*(self.contextMenu().screen().logicalDotsPerInchX()/96))

    def applyStyleSheet(self) -> None:
        if(readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "AppsUseLightTheme", 1)==0):
            self.iconMode = "white"
            self.datetimeprefs.setIcon(QIcon(getPath(f"settings_{self.iconMode}.png")))
            self.notifprefs.setIcon(QIcon(getPath(f"settings_{self.iconMode}.png")))
            self.takmgr.setIcon(QIcon(getPath(f"taskmgr_{self.iconMode}.png")))
            self.settingsAction.setIcon(QIcon(getPath(f"settings_{self.iconMode}.png")))
            self.reloadAction.setIcon(QIcon(getPath(f"clock_{self.iconMode}.png")))
            self.nameAction.setIcon(QIcon(getPath(f"about_{self.iconMode}.png")))
            self.restartAction.setIcon(QIcon(getPath(f"restart_{self.iconMode}.png")))
            self.hideAction.setIcon(QIcon(getPath(f"hide_{self.iconMode}.png")))
            self.quitAction.setIcon(QIcon(getPath(f"close_{self.iconMode}.png")))
            GlobalBlur(self.contextMenu().winId(), Acrylic=True, hexColor="#212121", QWidget=self.contextMenu())
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
                    background: rgba(50, 50, 50, 1%)/*#262626*/;
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
                }}
                QMenu::item {{
                    height: {self.getPx(30)}px;
                    border: none;
                    background: transparent;
                    padding-right: {self.getPx(10)}px;
                    padding-left: {self.getPx(10)}px;
                    border-radius: {self.getPx(4)}px;
                    margin: {self.getPx(2)}px;
                }}
                QMenu::item:selected {{
                    background: rgba(255, 255, 255, 6%);
                    height: {self.getPx(30)}px;
                    outline: none;
                    border: none;
                    padding-right: {self.getPx(10)}px;
                    padding-left: {self.getPx(10)}px;
                    border-radius: {self.getPx(4)}px;
                }}  
                QMenu::item:selected:disabled {{
                    background: transparent;
                    height: {self.getPx(30)}px;
                    outline: none;
                    border: none;
                    padding-right: {self.getPx(10)}px;
                    padding-left: {self.getPx(10)}px;
                    border-radius: {self.getPx(4)}px;
                }}            
                """)
        else:
            self.iconMode = "black"
            self.datetimeprefs.setIcon(QIcon(getPath(f"settings_{self.iconMode}.png")))
            self.notifprefs.setIcon(QIcon(getPath(f"settings_{self.iconMode}.png")))
            self.takmgr.setIcon(QIcon(getPath(f"taskmgr_{self.iconMode}.png")))
            self.settingsAction.setIcon(QIcon(getPath(f"settings_{self.iconMode}.png")))
            self.reloadAction.setIcon(QIcon(getPath(f"clock_{self.iconMode}.png")))
            self.nameAction.setIcon(QIcon(getPath(f"about_{self.iconMode}.png")))
            self.restartAction.setIcon(QIcon(getPath(f"restart_{self.iconMode}.png")))
            self.hideAction.setIcon(QIcon(getPath(f"hide_{self.iconMode}.png")))
            self.quitAction.setIcon(QIcon(getPath(f"close_{self.iconMode}.png")))
            GlobalBlur(self.contextMenu().winId(), Acrylic=True, Dark=False, hexColor="#ffffff", QWidget=self.contextMenu())
            self.contextMenu().setStyleSheet(f"""
                QWidget{{
                    background-color: transparent;
                }}  
                QMenu {{
                    border: {self.getPx(1)}px solid rgb(200, 200, 200);
                    padding: {self.getPx(2)}px;
                    outline: 0px;
                    color: black;
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
                    padding-right: {self.getPx(10)}px;
                    padding-left: {self.getPx(10)}px;
                    border-radius: {self.getPx(4)}px;
                    margin: {self.getPx(2)}px;
                }}
                QMenu::item:selected{{
                    background: rgba(0, 0, 0, 10%);
                    height: {self.getPx(30)}px;
                    outline: none;
                    border: none;
                    padding-right: {self.getPx(10)}px;
                    padding-left: {self.getPx(10)}px;
                    border-radius: {self.getPx(4)}px;
                }}  
                QMenu::item:selected:disabled{{
                    background: transparent;
                    height: {self.getPx(30)}px;
                    outline: none;
                    border: none;
                    padding-right: {self.getPx(10)}px;
                    padding-left: {self.getPx(10)}px;
                    border-radius: {self.getPx(4)}px;
                }}            
                """)




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