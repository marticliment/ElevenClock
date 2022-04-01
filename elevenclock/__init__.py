try:
    _globals = globals
    
    from ctypes import c_int, windll
    windll.shcore.SetProcessDpiAwareness(c_int(2))

    import time

    FirstTime = time.time()

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
    import subprocess
    from threading import Thread
    from urllib.request import urlopen

    try:
        import psutil
        importedPsutil = True
    except ImportError:
        importedPsutil = False
    import win32gui
    import win32api
    import pythoncom
    import win32process
    import win32com.client
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
    #from PySide2.QtCore import pyqtSignal as Signal
    import pyautogui
    from external.FramelessWindow import QFramelessDialog

    from languages import *
    import globals

    old_stdout = sys.stdout
    buffer = io.StringIO()
    sys.stdout = buffer = io.StringIO()

    from settings import *
    from tools import *
    import tools

    from external.WnfReader import isFocusAssistEnabled, getNotificationNumber

    blacklistedProcesses = ["msrdc.exe", "mstsc.exe", "CDViewer.exe", "wfica32.exe", "vmware-view.exe", "vmware.exe"]
    blacklistedFullscreenApps = ("", "Program Manager", "NVIDIA GeForce Overlay", "ElenenClock_IgnoreFullscreenEvent") # The "" codes for titleless windows

    seconddoubleclick = False
    isRDPRunning = False
    restartCount = 0
    tempDir = ""
    timeStr = ""
    dateTimeFormat = ""
    clocks = []
    oldScreens = []
    isFocusAssist = False
    shouldFixSeconds = False
    numOfNotifs = 0

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
    print(" 🟡: Warning")
    print(" 🟠: Handled unexpected exception")
    print(" 🔴: Unhandled unexpected exception")
    print(" 🟣: Handled expected exception")
    print("")

    def _(s) -> str:
        return tools._(s)

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
            isRDPRunning = checkIfElevenClockRunning(procs, blacklistedProcesses)
            time.sleep(5)


    def updateChecker():
        updateIfPossible()
        time.sleep(60)
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
                        if not getSettings("EnableSilentUpdates"):
                            showNotif.infoSignal.emit(_("ElevenClock Updater"), _("ElevenClock is downloading updates"))
                        try:
                            for clock in clocks:
                                clock.progressbar.show()
                        except Exception as e:
                            report(e)
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
                                    subprocess.run('start /B "" "{0}" /verysilent'.format(filename), shell=True)
                            else:
                                try:
                                    for clock in clocks:
                                        clock.progressbar.hide()
                                except Exception as e:
                                    report(e)
                                print("🟠 Hash not ok")
                                print("🟠 File hash: ", hashlib.sha256(datatowrite).hexdigest())
                                print("🟠 Provided hash: ", provided_hash)
                                showWarn.infoSignal.emit(("Updates found!"), f"ElevenClock Version {new_version_number} is available, but ElevenClock can't verify the authenticity of the package. Please go ElevenClock's homepage and download the latest version from there.\n\nDo you want to open the download page?")

                        else:
                            try:
                                for clock in clocks:
                                    clock.progressbar.hide()
                            except Exception as e:
                                report(e)
                            print("🟠 Can't verify update server authenticity, aborting")
                            print("🟠 Provided DmName:", dmname)
                            print("🟠 Expected DmNane: 769432b9-3560-4f94-8f90-01c95844d994.id.repl.co")
                            showWarn.infoSignal.emit(("Updates found!"), f"ElevenClock Version {new_version_number} is available, but ElevenClock can't verify the authenticity of the updates server. Please go ElevenClock's homepage and download the latest version from there.\n\nDo you want to open the download page?")
                    else:
                        showNotif.infoSignal.emit(("Updates found!"), f"ElevenClock Version {new_version_number} is available. Go to ElevenClock's Settings to update")

                else:
                    print("🟢 Updates not found")
            else:
                print("🟠 Update checking disabled")

        except Exception as e:
            report(e)
            try:
                for clock in clocks:
                    clock.progressbar.hide()
            except Exception as e:
                report(e)

    def resetRestartCount():
        global restartCount
        while True:
            if(restartCount>0):
                print("🔵 Restart loop:", restartCount)
                restartCount -= 1
            time.sleep(0.3)


    def loadClocks():
        global clocks, oldScreens, st, restartCount, st, shouldFixSeconds
        try:
            st.kill()
        except AttributeError:
            pass
        shouldFixSeconds = not(getSettings("UseCustomFont"))
        ForceClockOnFirstMonitor = getSettings("ForceClockOnFirstMonitor")
        HideClockOnSecondaryMonitors = getSettings("HideClockOnSecondaryMonitors")
        oldScreens = []
        clocks = []
        if importedPsutil:
            process = psutil.Process(os.getpid())
            memOk = (process.memory_info().rss/1048576) <= 150
        else:
            print("🟠 Psutil couldn't be imported!")
            memOk = True
        try:
            isPrefsWinOpen = globals.sw.isVisible()
        except AttributeError:
            isPrefsWinOpen = True
        if (restartCount<20 and memOk) or isPrefsWinOpen:
            restartCount += 1
            i = 0
            for screen in app.screens():
                screen: QScreen
                oldScreens.append(getGeometry(screen))
                if not screen == QGuiApplication.primaryScreen() or ForceClockOnFirstMonitor: # Check if we are not on the primary screen
                    if not HideClockOnSecondaryMonitors or screen == QGuiApplication.primaryScreen(): # First monitor is not affected by HideClockOnSecondaryMonitors
                        clocks.append(Clock(screen.logicalDotsPerInchX()/96, screen.logicalDotsPerInchY()/96, screen, i))
                        i += 1
                    else:
                        print("🟠 This is a secondary screen and is set to be skipped")
                else: # Skip the primary display, as it has already the clock
                    print("🟡 This is the primary screen and is set to be skipped")
            st = KillableThread(target=screenCheckThread, daemon=True, name="Main [loaded]: Screen listener")
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
        try:
            geometry = screen.geometry()
            g = (geometry.width(), geometry.height(), geometry.x(), geometry.y(), screen.logicalDotsPerInch(), win32api.EnumDisplayMonitors())
            return g
        except Exception as e:
            report(e)
            geometry = QGuiApplication.primaryScreen().geometry()
            g = (geometry.width(), geometry.height(), geometry.x(), geometry.y(), screen.logicalDotsPerInch(), win32api.EnumDisplayMonitors())
            return g

    def theyMatch(oldscreens, newscreens):
        if len(oldscreens) != len(newscreens) or len(app.screens()) != len(win32api.EnumDisplayMonitors()):
            return False  # The number of displays has changed

        # Check that all screen dimensions and dpi are the same as before
        return all(old == getGeometry(new) for old, new in zip(oldscreens, newscreens))

    def wnfDataThread():
        global isFocusAssist, numOfNotifs
        while True:
            isFocusAssist = isFocusAssistEnabled()
            time.sleep(0.3)
            numOfNotifs = getNotificationNumber()
            time.sleep(0.3)


    def screenCheckThread():
        while theyMatch(oldScreens, app.screens()):
            time.sleep(1)
        signal.restartSignal.emit()
        pass

    def closeClocks():
        for clock in clocks:
            clock.hide()
            clock.close()

    def showMessage(title: str, body: str, uBtn: bool = True) -> None:
        """
        Shows a Windows Notification
        """
        lastState = i.isVisible()
        i.show()
        i.showMessage(title, body)
        if uBtn:
            sw.updateButton.show()
        i.setVisible(lastState)

    def restartClocks(caller: str = ""):
        global clocks, st, rdpThread

        closeClocks()
        loadClocks()
        loadTimeFormat()

        try:
            rdpThread.kill()
        except AttributeError:
            pass
        rdpThread = KillableThread(target=checkRDP, daemon=True)
        if(getSettings("EnableHideOnRDP")):
            rdpThread.start()


    def isElevenClockRunningThread():
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
                            try:
                                os.remove(file)
                            except FileNotFoundError:
                                print("🟠 Can't remove lock file, file exist status:", os.path.exists(file))
                                if os.path.exists(file):
                                    try:
                                        os.remove(file)
                                    except Exception as e:
                                        print("🟠 Can't delete, tried again")
                                        report(e)
                        elif float(file.replace(os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock"), "ElevenClockRunning"), "")) > nowTime:
                            if not getSettings("DisableNewInstanceChecker"):
                                print("🟠 KILLING, NEWER VERSION RUNNING")
                                killSignal.infoSignal.emit("", "")
                if not(getSettings(name)):
                    print("🟠 KILLING, NEWER VERSION RUNNING")
                    killSignal.infoSignal.emit("", "")
            except Exception as e:
                report(e)
            time.sleep(2)

    def wanrUserAboutUpdates(a, b):
        if(QMessageBox.question(sw, a, b, QMessageBox.Open | QMessageBox.Cancel, QMessageBox.Open) == QMessageBox.Open):
            os.startfile("https://github.com/martinet101/ElevenClock/releases/latest")

    def checkIfWokeUpThread():
        while True:
            lastTime = time.time()
            time.sleep(3)
            if((lastTime+6) < time.time()):
                os.startfile(sys.executable)

    def loadTimeFormat():
        global dateTimeFormat
        try:
            locale.setlocale(locale.LC_ALL, readRegedit(r"Control Panel\International", "LocaleName", "en_US"))
            if getSettingsValue("CustomClockStrings") != "":
                dateTimeFormat = getSettingsValue("CustomClockStrings")
                print("🟡 Custom loaded date time format:", dateTimeFormat)
                globals.dateTimeFormat = dateTimeFormat
            else:
                showSeconds = readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "ShowSecondsInSystemClock", 0) or getSettings("EnableSeconds")
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
                else:
                    if not lang in (lang_zh_CN, lang_zh_TW):
                        dateTimeFormat = dateTimeFormat.replace("(W%W) ", f"({_('W')}%W) ")
                    else:
                        dateTimeFormat = dateTimeFormat.replace("(W%W) ", f"(第%W{_('W')}) ")

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
                print("🔵 tDateMode:", tDateMode)
                dateMode = ""
                for i, ministr in enumerate(tDateMode.split("'")):
                    if i%2==0:
                        dateMode += ministr.replace("dddd", "%A").replace("ddd", "%a").replace("dd", "%$").replace("d", "%#d").replace("$", "d").replace("MMMM", "%B").replace("MMM", "%b").replace("MM", "%m").replace("M", "%#m").replace("yyyy", "%Y").replace("yy", "%y")
                    else:
                        dateMode += ministr
                    
                tTimeMode = readRegedit(r"Control Panel\International", "sShortTime", "H:mm")
                print("🔵 tTimeMode:", tTimeMode)
                timeMode = ""

                for i, ministr in enumerate(tTimeMode.split("'")):
                    if i%2==0:
                        timeMode += ministr.replace("HH", "%$").replace("H", "%#H").replace("$", "H").replace("hh", "%I").replace("h", "%#I").replace("mm", "%M").replace("m", "%#M").replace("tt", "%p").replace("t", "%p").replace("ss", "%S").replace("s", "%#S")
                        if not("S" in timeMode) and showSeconds == 1:
                            for separator in ":.-/_":
                                if(separator in timeMode):
                                    timeMode += f"{separator}%S"
                    else:
                        timeMode += ministr

                for separator in ":.-/_":
                    timeMode = timeMode.replace(f" %p{separator}%S", f"{separator}%S %p")
                    timeMode = timeMode.replace(f" %p{separator}%#S", f"{separator}%#S %p")


                dateTimeFormat = dateTimeFormat.replace("%d/%m/%Y", dateMode).replace("%HH:%M", timeMode).replace("%S", "%S ").replace("%#S", "%#S ")
                print("🔵 Loaded date time format:", dateTimeFormat)
                globals.dateTimeFormat = dateTimeFormat

        except Exception as e:
            report(e)


    def timeStrThread():
        global timeStr, dateTimeFormat
        fixHyphen = getSettings("EnableHyphenFix")
        adverted = False
        while True:
            for integer in range(36000):
                try:
                    timeStr = datetime.datetime.now().strftime(dateTimeFormat.replace("\u200a", "hairsec")).replace("hairsec", "\u200a")
                    adverted = False
                    if fixHyphen:
                        timeStr = timeStr.replace("t-", "t -")
                    try:
                        secs = datetime.datetime.now().strftime("%S")
                        if secs[-1] == "1" and shouldFixSeconds:
                            timeStr = timeStr.replace(" ", " \u200e")
                        else:
                            timeStr = timeStr.replace(" ", "")
                    except IndexError as e:
                        report(e)
                except ValueError as e:
                    try:
                        timeStr = _("Invalid time format\nPlease modify it\nin the settings")
                    except:
                        timeStr = "Invalid time format\nPlease modify it\nin the settings"
                    if not adverted:
                        try:
                            showNotif.infoSignal.emit("Format error", "The specified date and time format is invalid. Please check your preferences")
                            adverted = True
                            report(e)
                        except NameError:
                            adverted = True
                            print("🟣 Expected NameError on timeStrThread")
                    report(e)
                except Exception as e:
                    report(e)
                time.sleep(0.2)


    class RestartSignal(QObject):

        restartSignal = Signal()

        def __init__(self) -> None:
            super().__init__()

    class InfoSignal(QObject):

        infoSignal = Signal(str, str)

        def __init__(self) -> None:
            super().__init__()

    class CustomToolTip(QLabel):
        def __init__(self, screen: QScreen, text: str = "", pos: tuple[int, int] = (0, 0)):
            super().__init__(text)
            self.scr = screen
            self.setFixedHeight(self.getPx(30))
            self.setMaximumWidth(self.getPx(200))
            self.setContentsMargins(self.getPx(10), self.getPx(5), self.getPx(10), self.getPx(5))
            self.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            self.setWindowFlag(Qt.WindowStaysOnTopHint)
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setWindowFlag(Qt.Tool)
            if isTaskbarDark():
                self.setStyleSheet("*{font-size:9pt;font-family: \"Segoe UI Variable Display semib\"; background-color: transparent;color: #eeeeee;}")
            else:
                self.setStyleSheet("*{font-size:9pt;font-family: \"Segoe UI Variable Display\"; color: black;background-color: transparent}")
            self.move(pos[0], pos[1])
            ApplyMenuBlur(self.winId().__int__(), self, smallCorners=True, avoidOverrideStyleSheet = True, shadow=False, useTaskbarModeCheck = True)

        def show(self):
            lDateMode = readRegedit(r"Control Panel\International", "sLongDate", "dd/MM/yyyy")
            print("🔵 Long date string:", lDateMode)
            dateMode = ""
            for i, ministr in enumerate(lDateMode.split("'")):
                if i%2==0:
                    dateMode += ministr.replace("dddd", "%A").replace("ddd", "%a").replace("dd", "%$").replace("d", "%#d").replace("$", "d").replace("MMMM", "%B").replace("MMM", "%b").replace("MM", "%m").replace("M", "%#m").replace("yyyy", "%Y").replace("yy", "%y")
                else:
                    dateMode += ministr
            try:
                self.setText(str(datetime.datetime.now().strftime(dateMode)))
            except Exception as e:
                report(e)
                self.setText(str(datetime.datetime.now().strftime("%A, %#d %B %Y")))
            super().show()
            
        def getPx(self, original) -> int:
            return round(original*(self.scr.logicalDotsPerInch()/96))

    class Clock(QWidget):

        refresh = Signal()
        hideSignal = Signal()
        callInMainSignal = Signal(object)
        styler = Signal(str)

        preferedwidth = 200
        isHovered = False
        isTooltipWaiting = False
        preferedHeight = 48
        focusassitant = True
        lastTheme = 0
        clockShouldBeHidden = False
        shouldBeVisible = True
        isRDPRunning = True
        clockOnTheLeft = False
        textInputHostHWND = 0
        INTLOOPTIME = 2

        def __init__(self, dpix: float, dpiy: float, screen: QScreen, index: int):

            super().__init__()
            if f"_{screen.name()}_" in getSettingsValue("BlacklistedMonitors"):
                print("🟠 Monitor blacklisted!")
                self.hide()
            else:

                self.index = index
                self.tooltipEnabled = not getSettings("DisableToolTip")

                print(f"🔵 Initializing clock {index}...")
                self.callInMainSignal.connect(lambda f: f())
                self.styler.connect(self.setStyleSheet)
                
                self.taskbarBackgroundColor = not getSettings("DisableTaskbarBackgroundColor") and not (getSettings("UseCustomBgColor") or getSettings("AccentBackgroundcolor"))
                self.transparentBackground = getSettings("DisableTaskbarBackgroundColor") and not (getSettings("UseCustomBgColor") or getSettings("AccentBackgroundcolor"))
                
                if self.taskbarBackgroundColor:
                    print("🔵 Using taskbar background color")
                    self.bgcolor = "0, 0, 0, 0"
                else:
                    print("🟡 Not using taskbar background color")
                    if getSettings("AccentBackgroundcolor"):
                        self.bgcolor = f"{getColors()[5 if isTaskbarDark() else 1]},100"
                    else:
                        self.bgcolor = getSettingsValue("UseCustomBgColor") if getSettingsValue("UseCustomBgColor") else "0, 0, 0, 0"
                    print("🔵 Using bg color:", self.bgcolor)

                self.prefMargins = 0

                try:
                    if readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "TaskbarSi", 1) == 0 or (not getSettings("DisableTime") and not getSettings("DisableDate") and getSettings("EnableWeekDay")):
                        self.prefMargins = self.getPx(1)
                        self.widgetStyleSheet = f"background-color: rgba(bgColor%); margin: {self.getPx(0)}px;margin-top: 0px;margin-bottom: 0px; border-radius: {self.getPx(4)}px;"
                        if not(not getSettings("DisableTime") and not getSettings("DisableDate") and getSettings("EnableWeekDay")):
                            print("🟡 Small sized taskbar")
                            self.preferedHeight = 32
                            self.preferedwidth = 200
                    else:
                        print("🟢 Regular sized taskbar")
                        self.prefMargins = self.getPx(3)
                        self.widgetStyleSheet = f"background-color: rgba(bgColor%);margin: {self.getPx(0)}px;border-radius: {self.getPx(4)}px;padding: {self.getPx(2)}px;"
                except Exception as e:
                    print("🟡 Regular sized taskbar")
                    report(e)
                    self.prefMargins = self.getPx(3)
                    self.widgetStyleSheet = f"background-color: rgba(bgColor%);margin: {self.getPx(0)}px;border-radius: {self.getPx(4)}px;;padding: {self.getPx(2)}px;"
                    
                self.setStyleSheet(self.widgetStyleSheet.replace("bgColor", self.bgcolor))

                if getSettings("ClockFixedHeight"):
                    print("🟡 Custom height being used!")
                    try:
                        self.preferedHeight = int(getSettingsValue("ClockFixedHeight"))
                    except ValueError as e:
                        report(e)

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
                
                self.refresh.connect(self.refreshandShow)
                self.hideSignal.connect(self.hide)
                #self.keyboard = Controller()
                self.setWindowFlag(Qt.WindowStaysOnTopHint)
                self.setWindowFlag(Qt.FramelessWindowHint)
                self.setAttribute(Qt.WA_ShowWithoutActivating)
                self.setAttribute(Qt.WA_TranslucentBackground)
                self.setWindowFlag(Qt.Tool)
                hex_blob = b'0\x00\x00\x00\xfe\xff\xff\xffz\xf4\x00\x00\x03\x00\x00\x00T\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x08\x04\x00\x00\x80\x07\x00\x008\x04\x00\x00`\x00\x00\x00\x01\x00\x00\x00'
                registry_read_result = readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\StuckRects3", "Settings", hex_blob)
                self.autoHide = registry_read_result[8] == 123
                
                if self.autoHide:
                    print("🟡 ElevenClock set to hide with the taskbar")

                self.clockOnTheLeft = getSettings("ClockOnTheLeft")
                screenName = screen.name().replace("\\", "_")
                if not self.clockOnTheLeft:
                    if getSettings(f"SpecificClockOnTheLeft{screenName}"):
                        self.clockOnTheLeft = True
                        print(f"🟡 Clock {screenName} on the left (forced)")
                else:
                    if getSettings(f"SpecificClockOnTheRight{screenName}"):
                        self.clockOnTheLeft = False
                        print(f"🟡 Clock {screenName} on the right (forced)")

                try:
                    if (registry_read_result[12] == 1 and not getSettings("ForceOnBottom")) or (getSettings("ForceOnTop") and not getSettings(f"SpecificClockOnTheBottom{screenName}")) or getSettings(f"SpecificClockOnTheTop{screenName}"):
                        h = self.screenGeometry.y()
                        self.clockOnTop = True
                        print("🟡 Clock on the top")
                    else:
                        h = self.screenGeometry.y()+self.screenGeometry.height()-(self.preferedHeight*dpiy)
                        self.clockOnTop = False
                        print("🟢 Clock on the bottom")
                except Exception as e:
                    report(e)
                    h = self.screenGeometry.y()+self.screenGeometry.height()-(self.preferedHeight*dpiy)
                    self.clockOnTop = False
                    print("🟠 Clock on the bottom (by exception)")
                self.label = Label(timeStr, self)
                if self.clockOnTheLeft:
                    print("🟡 Clock on the left")
                    w = self.screenGeometry.x()+8*dpix
                    self.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                else:
                    self.label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    print("🟢 Clock on the right")
                    w = self.screenGeometry.x()+self.screenGeometry.width()-((self.preferedwidth)*dpix)
                    
                if getSettings("CenterAlignment"):
                    self.label.setAlignment(Qt.AlignCenter)

                xoff = 0
                yoff = 0

                if getSettings("ClockXOffset"):
                    print("🟡 X offset being used!")
                    try:
                        xoff = int(getSettingsValue("ClockXOffset"))
                    except ValueError as e:
                        report(e)

                if getSettings("ClockYOffset"):
                    print("🟡 Y offset being used!")
                    try:
                        yoff = int(getSettingsValue("ClockYOffset"))
                    except ValueError as e:
                        report(e)

                self.w = int(w) + xoff
                self.h = int(h) + yoff
                self.dpix = dpix
                self.dpiy = dpiy

                if not(getSettings("EnableWin32API")):
                    print("🟢 Using qt's default positioning system")
                    self.move(self.w, self.h+self.getPx(1))
                    self.resize(int(self.preferedwidth*dpix), int(self.preferedHeight*dpiy)-self.getPx(2))
                else:
                    print("🟡 Using win32 API positioning system")
                    self.user32 = windll.user32
                    self.user32.SetProcessDPIAware() # forces functions to return real pixel numbers instead of scaled values
                    win32gui.SetWindowPos(self.winId(), 0, int(w), int(h+self.getPx(1)), int(self.preferedwidth*dpix), int(self.preferedHeight*dpiy)-self.getPx(2), False)
                print("🔵 Clock geometry:", self.geometry())
                self.font: QFont = QFont()
                customFont = getSettingsValue("UseCustomFont")
                if customFont == "":
                    if lang == lang_ko:
                        self.fontfamilies = ["Malgun Gothic", "Segoe UI Variable", "sans-serif"]
                    elif lang == lang_zh_TW:
                        self.fontfamilies = ["Microsoft JhengHei UI", "Segoe UI Variable", "sans-serif"]
                    elif lang == lang_zh_CN:
                        self.fontfamilies = ["Microsoft YaHei UI", "Segoe UI Variable", "sans-serif"]
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

                accColors = getColors()
                def make_style_sheet(a, b, c, d, color):
                    bg = 1 if isTaskbarDark() else 4
                    fg = 6 if isTaskbarDark() else 1
                    return f"*{{padding: {a}px;padding-right: {b}px;margin-right: {c}px;padding-left: {d}px; color: {color};}}#notifIndicator{{background-color: rgb({accColors[bg]});color:rgb({accColors[fg]});}}"

                
                self.progressbar = QProgressBar(self)
                self.progressbar.setFixedHeight(self.getPx(2))
                self.progressbar.setRange(0, 200)
                self.progressbar.setValue(0)
                self.progressbar.setStyleSheet(f"*{{border: 0px;margin:0px;padding:0px;}}QProgressBar::chunk{{background-color:rgb({accColors[1 if isTaskbarDark() else 4]})}}")
                self.progressbar.hide()

                self.pgsbarleftSlow = QtCore.QVariantAnimation()
                self.pgsbarleftSlow.setStartValue(0)
                self.pgsbarleftSlow.setEndValue(200)
                self.pgsbarleftSlow.setDuration(500)
                self.pgsbarleftSlow.valueChanged.connect(lambda v: self.progressbar.setValue(v))
                
                self.pgsbarrightSlow = QtCore.QVariantAnimation()
                self.pgsbarrightSlow.setStartValue(200)
                self.pgsbarrightSlow.setEndValue(0)
                self.pgsbarrightSlow.setDuration(500)
                self.pgsbarrightSlow.valueChanged.connect(lambda v: self.progressbar.setValue(v))
                
                self.pgsbarleftFast = QtCore.QVariantAnimation()
                self.pgsbarleftFast.setStartValue(0)
                self.pgsbarleftFast.setEndValue(200)
                self.pgsbarleftFast.setDuration(200)
                self.pgsbarleftFast.valueChanged.connect(lambda v: self.progressbar.setValue(v))
                
                self.pgsbarrightFast = QtCore.QVariantAnimation()
                self.pgsbarrightFast.setStartValue(200)
                self.pgsbarrightFast.setEndValue(0)
                self.pgsbarrightFast.setDuration(200)
                self.pgsbarrightFast.valueChanged.connect(lambda v: self.progressbar.setValue(v))
                
                def loadProgressBarLoop():
                    nonlocal self
                    time.sleep(0.5)
                    while True:
                        if self.progressbar.isVisible():
                            self.callInMainSignal.emit(self.pgsbarleftSlow.start)
                            time.sleep(0.7)
                            self.callInMainSignal.emit(lambda: self.progressbar.setInvertedAppearance(not(self.progressbar.invertedAppearance())))
                            self.callInMainSignal.emit(self.pgsbarrightSlow.start)
                            time.sleep(0.7)
                            self.callInMainSignal.emit(lambda: self.progressbar.setInvertedAppearance(not(self.progressbar.invertedAppearance())))
                            self.callInMainSignal.emit(self.pgsbarleftFast.start)
                            time.sleep(0.3)
                            self.callInMainSignal.emit(lambda: self.progressbar.setInvertedAppearance(not(self.progressbar.invertedAppearance())))
                            self.callInMainSignal.emit(self.pgsbarrightFast.start)
                            time.sleep(0.3)
                            self.callInMainSignal.emit(lambda: self.progressbar.setInvertedAppearance(not(self.progressbar.invertedAppearance())))
                        else:
                            time.sleep(0.1)


                Thread(target=loadProgressBarLoop, daemon=True).start()


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
                elif isTaskbarDark():
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


                self.full_screen_rect = (self.screenGeometry.x(), self.screenGeometry.y(), self.screenGeometry.x()+self.screenGeometry.width(), self.screenGeometry.y()+self.screenGeometry.height())
                print("🔵 Full screen rect: ", self.full_screen_rect)


                self.forceDarkTheme = getSettings("ForceDarkTheme")
                self.forceLightTheme = getSettings("ForceLightTheme")
                self.hideClockWhenClicked = getSettings("HideClockWhenClicked")
                self.isLowCpuMode = getSettings("EnableLowCpuMode")
                self.primary_screen = QGuiApplication.primaryScreen()
                self.oldBgColor = 0

                self.user32 = windll.user32
                self.user32.SetProcessDPIAware() # optional, makes functions return real pixel numbers instead of scaled values
                self.loop0 = KillableThread(target=self.updateTextLoop, daemon=True, name=f"Clock[{index}]: Time updater loop")
                self.loop1 = KillableThread(target=self.mainClockLoop, daemon=True, name=f"Clock[{index}]: Main clock loop")
                self.loop2 = KillableThread(target=self.backgroundLoop, daemon=True, name=f"Clock[{index}]: Background color loop")
                self.loop0.start()
                self.loop1.start()
                self.loop2.start()

                

                self.setMouseTracking(True)

                self.tooltip = CustomToolTip(screen, "placeholder")
                
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
                    print("🟡 Desktop button enabled")
                    self.desktopButton = QHoverButton(parent=self)
                    self.desktopButton.clicked.connect(lambda: self.showDesktop())
                    self.desktopButton.show()
                    self.desktopButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                    self.desktopButton.move(self.width()-self.getPx(10), 0)
                    self.desktopButton.resize(self.getPx(10), self.getPx(self.preferedHeight))
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

        def updateToolTipStatus(self, mouseIn: bool =False) -> None:
            if mouseIn:
                self.isHovered = True
                if not self.isTooltipWaiting:
                    Thread(target=self.waitAndShowToolTip, daemon=True, name=f"Clock[{self.index}]: Tooltip").start()
                    self.isTooltipWaiting = True
            else:
                self.tooltip.close()
                self.isHovered = False
                self.isTooltipWaiting = False

        def waitAndShowToolTip(self):
            time.sleep(0.3)
            if self.isHovered:
                if self.tooltipEnabled:
                    print("🔵 Showing tooltip")
                    self.callInMainSignal.emit(lambda: self.showToolTip())
                else:
                    print("🟡 NOT showing tooltip, it has been disabled")


        def showToolTip(self):
            self.tooltip.show()
            xPos = self.screen().geometry().x()+self.screen().size().width()-self.getPx(10)-self.tooltip.width() if not self.clockOnTheLeft else self.screen().geometry().x()+self.getPx(10)
            yPos = self.pos().y()-self.getPx(5)-self.tooltip.height() if not self.clockOnTop else self.pos().y()+self.getPx(5)+self.height()
            self.tooltip.move(xPos, yPos)

        def getPx(self, original) -> int:
            return round(original*(self.screen().logicalDotsPerInch()/96))

        def backgroundLoop(self):
            while True:
                try:
                    if self.taskbarBackgroundColor and not self.isLowCpuMode and not globals.trayIcon.contextMenu().isVisible():
                        if self.isVisible():
                            intColor = self.primary_screen.grabWindow(0, self.x()+self.label.x()-1, self.y()+2, 1, 1).toImage().pixel(0, 0)
                            if intColor != self.oldBgColor:
                                self.oldBgColor = intColor
                                color = QColor(intColor)
                                self.styler.emit(self.widgetStyleSheet.replace("bgColor", f"{color.red()}, {color.green()}, {color.blue()}, 100"))
                except AttributeError:
                    print("🟣 Expected AttributeError on backgroundLoop thread")
                time.sleep(0.5)

        def theresFullScreenWin(self, clockOnFirstMon, newMethod, legacyMethod):
            try:
                fullscreen = False

                def compareFullScreenRects(window, screen, newMethod):
                    try:
                        if(newMethod):
                            return  window[0] <= screen[0] and window[1] <= screen[1] and window[2] >= screen[2] and window[3] >= screen[3] and window[0]+8 != screen[0] and window[1]+8 != screen[1]
                        else:
                            return  window[0] == screen[0] and window[1] == screen[1] and window[2] == screen[2] and window[3] == screen[3]
                    except Exception as e:
                        report(e)

                def winEnumHandler(hwnd, _):
                    nonlocal fullscreen
                    if win32gui.IsWindowVisible(hwnd):
                        if compareFullScreenRects(win32gui.GetWindowRect(hwnd), self.full_screen_rect, newMethod):
                            if clockOnFirstMon and self.textInputHostHWND == 0:
                                    pythoncom.CoInitialize()
                                    _, pid = win32process.GetWindowThreadProcessId(hwnd)
                                    _wmi = win32com.client.GetObject('winmgmts:')

                                    # collect all the running processes
                                    processes = _wmi.ExecQuery(f'Select Name from win32_process where ProcessId = {pid}')
                                    for p in processes:
                                        if p.Name != "TextInputHost.exe":
                                            if(win32gui.GetWindowText(hwnd) not in blacklistedFullscreenApps):
                                                print("🟡 Fullscreen window detected!", win32gui.GetWindowText(hwnd), win32gui.GetWindowRect(hwnd), "Fullscreen rect:", self.full_screen_rect)
                                                fullscreen = True
                                        else:
                                            print("🟢 Cached text input host hwnd:", hwnd)
                                            self.textInputHostHWND = hwnd
                                            self.INTLOOPTIME = 2
                            else:
                                if win32gui.GetWindowText(hwnd) not in blacklistedFullscreenApps and hwnd != self.textInputHostHWND:
                                    print("🟡 Fullscreen window detected!", win32gui.GetWindowText(hwnd), win32gui.GetWindowRect(hwnd), "Fullscreen rect:", self.full_screen_rect)
                                    fullscreen = True
                if not legacyMethod:
                    win32gui.EnumWindows(winEnumHandler, 0)
                else:
                    hwnd = win32gui.GetForegroundWindow()
                    if(compareFullScreenRects(win32gui.GetWindowRect(hwnd), self.full_screen_rect, newMethod)):
                        if(win32gui.GetWindowText(hwnd) not in blacklistedFullscreenApps):
                            print("🟡 Fullscreen window detected!", win32gui.GetWindowText(hwnd), win32gui.GetWindowRect(hwnd), "Fullscreen rect:", self.full_screen_rect)
                            fullscreen = True
                return fullscreen
            except Exception as e:
                report(e)
                return False

        def mainClockLoop(self):
            global isRDPRunning, numOfNotifs
            EnableHideOnFullScreen = not(getSettings("DisableHideOnFullScreen"))
            DisableHideWithTaskbar = getSettings("DisableHideWithTaskbar")
            EnableHideOnRDP = getSettings("EnableHideOnRDP")
            clockOnFirstMon = getSettings("ForceClockOnFirstMonitor")
            newMethod = getSettings("NewFullScreenMethod")
            notifs = not getSettings("DisableNotifications")
            legacyMethod = getSettings("legacyFullScreenMethod")
            oldNotifNumber = 0
            print(f"🔵 Show/hide loop started with parameters: HideonFS:{EnableHideOnFullScreen}, NotHideOnTB:{DisableHideWithTaskbar}, HideOnRDP:{EnableHideOnRDP}, ClockOn1Mon:{clockOnFirstMon}, NefWSMethod:{newMethod}, DisableNotifications:{notifs}, legacyFullScreenMethod:{legacyMethod}")
            if self.isLowCpuMode or clockOnFirstMon:
                self.INTLOOPTIME = 15
            else:
                self.INTLOOPTIME = 2
            while True:
                self.isRDPRunning = isRDPRunning
                isFullScreen = self.theresFullScreenWin(clockOnFirstMon, newMethod, legacyMethod)
                for i in range(self.INTLOOPTIME):
                    if (not(isFullScreen) or not(EnableHideOnFullScreen)) and not self.clockShouldBeHidden:
                        if notifs:
                            if isFocusAssist:
                                self.callInMainSignal.emit(self.label.enableFocusAssistant)
                            if numOfNotifs > 0:
                                if oldNotifNumber != numOfNotifs:
                                    if isFocusAssist:
                                        self.callInMainSignal.emit(self.label.enableFocusAssistant)
                                    else:
                                        self.callInMainSignal.emit(self.label.enableNotifDot)
                            else:
                                if not isFocusAssist:
                                    self.callInMainSignal.emit(self.label.disableClockIndicators)
                        oldNotifNumber = numOfNotifs
                        if self.autoHide and not(DisableHideWithTaskbar):
                            mousePos = getMousePos()
                            if (mousePos.y()+1 == self.screenGeometry.y()+self.screenGeometry.height()) and self.screenGeometry.x() < mousePos.x() and self.screenGeometry.x()+self.screenGeometry.width() > mousePos.x():
                                if self.isHidden():
                                    time.sleep(0.22)
                                self.refresh.emit()
                            elif (mousePos.y() <= self.screenGeometry.y()+self.screenGeometry.height()-self.preferedHeight):
                                if globals.trayIcon != None:
                                    menu = globals.trayIcon.contextMenu()
                                    if menu.isVisible():
                                        self.refresh.emit()
                                    else:
                                        self.hideSignal.emit()
                                else:
                                    self.hideSignal.emit()
                        else:
                            if(self.isRDPRunning and EnableHideOnRDP):
                                self.hideSignal.emit()
                            else:
                                self.refresh.emit()
                    else:
                        self.hideSignal.emit()
                    time.sleep(0.2)
                time.sleep(0.2)
    
        def updateTextLoop(self) -> None:
            global timeStr
            while True:
                self.callInMainSignal.emit(lambda: self.label.setText(timeStr))
                time.sleep(0.1)

        def showCalendar(self):
            pyautogui.hotkey("win", "n")
            if self.hideClockWhenClicked:
                print("🟡 Hiding clock because clicked!")
                self.clockShouldBeHidden = True
                
                def showClockOn10s(self: Clock):
                    time.sleep(10)
                    print("🟢 Showing clock because 10s passed!")
                    self.clockShouldBeHidden = False
                    
                KillableThread(target=showClockOn10s, args=(self,), name=f"Temporary: 10s thread").start()

        def showDesktop(self):
            pyautogui.hotkey("win", "d")

        def focusOutEvent(self, event: QFocusEvent) -> None:
            self.refresh.emit()

        def refreshandShow(self):
            if(self.shouldBeVisible):
                self.show()
                self.raise_()
                if(self.lastTheme >= 0): # If the color is not customized
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

        def closeEvent(self, event: QCloseEvent) -> None:
            self.shouldBeVisible = False
            try:
                print(f"🟡 Closing clock on {self.win32screen}")
                self.loop0.kill()
                self.loop1.kill()
                self.loop2.kill()
            except AttributeError:
                pass
            event.accept()
            return super().closeEvent(event)
        

        def resizeEvent(self, event: QResizeEvent = None):
            self.progressbar.move(self.label.x(), self.height()-self.progressbar.height())
            self.progressbar.setFixedWidth(self.label.width())
            if event:
                return super().resizeEvent(event)

    class Label(QLabel):
        clicked = Signal()
        outline = True
        def __init__(self, text, parent):
            super().__init__(text, parent=parent)
            try:
                self.winver = int(platform.version().split('.')[2])
            except Exception as e:
                report(e)
                self.winver = 22000
            try:
                self.specifiedMinimumWidth = int(getSettingsValue("ClockFixedWidth"))
            except ValueError:
                self.specifiedMinimumWidth = 0
            except Exception as e: 
                self.specifiedMinimumWidth = 0
                report(e)
                
            self.setMouseTracking(True)
            self.backgroundwidget = QWidget(self)
            self.color = "255, 255, 255"
            QGuiApplication.instance().installEventFilter(self)
            self.bgopacity = 0.2
            self.backgroundwidget.setContentsMargins(0, self.window().prefMargins, 0, self.window().prefMargins)
            self.backgroundwidget.setStyleSheet(f"background-color: rgba(127, 127, 127, 0.01);border-top: {self.getPx(1)}px solid rgba({self.color},0);margin-top: {self.window().prefMargins}px; margin-bottom: {self.window().prefMargins};")
            self.backgroundwidget.show()
            if self.window().transparentBackground:
                colorOffset = .01
            else:
                colorOffset = 0
            self.showBackground = QVariantAnimation()
            self.showBackground.setStartValue(0+colorOffset) # Not 0 to prevent white flashing on the border
            self.showBackground.setEndValue(self.bgopacity)
            self.showBackground.setDuration(100)
            self.showBackground.setEasingCurve(QEasingCurve.InOutQuad) # Not strictly required, just for the aesthetics
            self.showBackground.valueChanged.connect(lambda opacity: self.backgroundwidget.setStyleSheet(f"background-color: rgba({self.color}, {opacity/2});border-top: {self.getPx(1)}px solid rgba({self.color}, {opacity+colorOffset});margin-top: {self.window().prefMargins}px; margin-bottom: {self.window().prefMargins};"))
            self.hideBackground = QVariantAnimation()
            self.hideBackground.setStartValue(self.bgopacity)
            self.hideBackground.setEndValue(0+colorOffset) # Not 0 to prevent white flashing on the border
            self.hideBackground.setDuration(100)
            self.hideBackground.setEasingCurve(QEasingCurve.InOutQuad) # Not strictly required, just for the aesthetics
            self.hideBackground.valueChanged.connect(lambda opacity: self.backgroundwidget.setStyleSheet(f"background-color: rgba({self.color}, {opacity/2});border-top: {self.getPx(1)}px solid rgba({self.color}, {opacity+colorOffset});margin-top: {self.window().prefMargins}px; margin-bottom: {self.window().prefMargins};"))
            self.setAutoFillBackground(True)
            self.backgroundwidget.setGeometry(0, 0, self.width(), self.height())
            
            self.opacity=QGraphicsOpacityEffect(self)
            self.opacity.setOpacity(1.00)
            self.backgroundwidget.setGraphicsEffect(self.opacity)
            
            self.focusassitant = True
            self.focusAssitantLabel = QPushButton(self)
            self.focusAssitantLabel.move(self.width(), 0)
            self.focusAssitantLabel.setAttribute(Qt.WA_TransparentForMouseEvents)
            self.focusAssitantLabel.setStyleSheet("background: transparent; margin: none; padding: none;")
            self.focusAssitantLabel.resize(self.getPx(30), self.height())
            if self.winver < 22581:
                self.focusAssitantLabel.setIcon(QIcon(getPath(f"moon_{getTaskbarIconMode()}.png")))
            else:
                if numOfNotifs == 0:
                    self.focusAssitantLabel.setIcon(QIcon(getPath(f"notif_assist_empty_{getTaskbarIconMode()}.png")))
                else:
                    self.focusAssitantLabel.setIcon(QIcon(getPath(f"notif_assist_filled_{getTaskbarIconMode()}.png")))
            self.focusAssitantLabel.setIconSize(QSize(self.getPx(16), self.getPx(16)))
            
            accColors = getColors()
            
            self.notifdot = True
            self.notifDotLabel = QLabel("", self)
            self.notifDotLabel.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            self.notifDotLabel.setObjectName("notifIndicator")
            self.notifDotLabel.setStyleSheet(f"font-size: 8pt;font-family: \"Segoe UI Variable Display\";border-radius: {self.getPx(8)}px;padding: 0px;padding-bottom: {self.getPx(2)}px;padding-left: {self.getPx(3)}px;padding-right: {self.getPx(2)}px;margin: 0px;border:0px;")
            

            self.moonIconBlack = QIcon(getPath("moon_black.png"))
            self.moonIconWhite = QIcon(getPath("moon_white.png"))
            self.emptyBellBlack = QIcon(getPath("notif_assist_empty_black.png"))
            self.emptyBellWhite = QIcon(getPath("notif_assist_empty_white.png"))
            self.filledBellBlack = QIcon(getPath(f"notif_assist_filled_black.png"))
            self.filledBellWhite = QIcon(getPath(f"notif_assist_filled_white.png"))

            self.lastFocusAssistIcon = None
            
            self.disableClockIndicators()
            
        def enableFocusAssistant(self):
            if self.lastFocusAssistIcon != self.focusAssitantLabel.icon():
                if self.winver < 22581:
                    self.focusAssitantLabel.setIcon(self.moonIconWhite if isTaskbarDark() else self.moonIconBlack)
                else:
                    if numOfNotifs == 0:
                        self.focusAssitantLabel.setIcon(self.emptyBellWhite if isTaskbarDark() else self.emptyBellBlack)
                    else:
                        self.focusAssitantLabel.setIcon(self.filledBellWhite if isTaskbarDark() else self.filledBellBlack)
            if not self.focusassitant:
                cprint("assist", isFocusAssist)
                if self.notifdot:
                    self.disableClockIndicators()
                self.focusassitant = True
                self.setContentsMargins(self.getPx(5), self.getPx(2), self.getPx(43), self.getPx(2))
                self.focusAssitantLabel.move(self.width()-self.contentsMargins().right(), 0)
                self.focusAssitantLabel.setFixedWidth(self.getPx(30))
                self.focusAssitantLabel.setFixedHeight(self.height())
                self.focusAssitantLabel.setIconSize(QSize(self.getPx(16), self.getPx(16)))
                self.focusAssitantLabel.show()
                
        def enableNotifDot(self):
            self.notifDotLabel.setText(str(numOfNotifs))
            if not self.notifdot:
                self.notifdot = True
                self.setContentsMargins(self.getPx(5), self.getPx(2), self.getPx(43), self.getPx(2))
                topBottomPadding = (self.height()-self.getPx(16))/2 # top-bottom margin
                leftRightPadding = (self.getPx(30)-self.getPx(16))/2 # left-right margin
                self.notifDotLabel.move(int(self.width()-self.contentsMargins().right()+leftRightPadding), int(topBottomPadding))
                self.notifDotLabel.resize(self.getPx(16), self.getPx(16))
                self.notifDotLabel.setStyleSheet(f"font-size: 8pt;font-family: \"Segoe UI Variable Display\";border-radius: {self.getPx(8)}px;padding: 0px;padding-bottom: {self.getPx(2)}px;padding-left: {self.getPx(3)}px;padding-right: {self.getPx(2)}px;margin: 0px;border:0px;")
                self.notifDotLabel.show()
            
        def disableClockIndicators(self):
            if self.focusassitant:
                self.focusassitant = False
                self.setContentsMargins(self.getPx(6), self.getPx(2), self.getPx(13), self.getPx(2))
                self.focusAssitantLabel.hide()
            if self.notifdot:
                self.notifdot = False
                self.setContentsMargins(self.getPx(6), self.getPx(2), self.getPx(13), self.getPx(2))
                self.notifDotLabel.hide()
                
            
        def getPx(self, i: int) -> int:
            return round(i*(self.screen().logicalDotsPerInch()/96))

        def enterEvent(self, event: QEvent, r=False) -> None:
            geometry: QRect = self.width()
            self.showBackground.setStartValue(.01)
            self.showBackground.setEndValue(self.bgopacity) # Not 0 to prevent white flashing on the border
            if not self.window().clockOnTheLeft:
                self.backgroundwidget.move(0, 2)
                self.backgroundwidget.resize(geometry, self.height()-4)
            else:
                self.backgroundwidget.move(0, 2)
                self.backgroundwidget.resize(geometry, self.height()-4)
            self.showBackground.start()
            if not r:
                self.enterEvent(event, r=True)
            self.window().updateToolTipStatus(True)
            return super().enterEvent(event)

        def leaveEvent(self, event: QEvent) -> None:
            self.hideBackground.setStartValue(self.bgopacity)
            self.hideBackground.setEndValue(.01) # Not 0 to prevent white flashing on the border
            self.hideBackground.start()
            self.window().updateToolTipStatus(False)
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
            self.opacity.setOpacity(0.60)
            self.backgroundwidget.setGraphicsEffect(self.opacity)
            return super().mousePressEvent(ev)

        def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
            self.setWindowOpacity(1)
            self.setWindowOpacity(1)
            self.opacity.setOpacity(1.00)
            self.backgroundwidget.setGraphicsEffect(self.opacity)
            if(ev.button() == Qt.RightButton):
                i.showMenu(self.window())
            else:
                self.clicked.emit()
            return super().mouseReleaseEvent(ev)
        
        def paintEvent(self, event: QPaintEvent) -> None:
            w = self.minimumSizeHint().width()
            mw = self.specifiedMinimumWidth
            if mw > w:
                w = mw
            if w<self.window().getPx(self.window().preferedwidth) and not self.window().clockOnTheLeft:
                self.move(self.window().getPx(self.window().preferedwidth)-w+self.getPx(2), 0)
                self.resize(w, self.height())
            else:
                self.move(0, 0)
                self.resize(w, self.height())

            return super().paintEvent(event)
        
        def resizeEvent(self, event: QResizeEvent) -> None:
            if self.focusassitant:
                self.focusassitant = False
                self.enableFocusAssistant()
            elif self.notifdot:
                self.notifdot = False
                self.enableNotifDot()
            else:
                self.notifdot = True
                self.focusassitant = True
                self.disableClockIndicators()
            self.window().resizeEvent(None)
            return super().resizeEvent(event)

        def window(self) -> Clock:
            return super().window()

        
        

        

    # Start of main script
    
    QApplication.setAttribute(Qt.AA_DisableHighDpiScaling)
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    
    #mController: MouseController = None
    sw: SettingsWindow = None
    i: TaskbarIconTray = None
    st: KillableThread = None # Will be defined on loadClocks
    shouldFixSeconds = not(getSettings("UseCustomFont"))

    KillableThread(target=resetRestartCount, daemon=True, name="Main: Restart counter").start()
    KillableThread(target=timeStrThread, daemon=True, name="Main: Locale string loader").start()
    
    loadClocks()
    
    print(f"🟢 Loaded clocks in {time.time()-FirstTime}")
    
    tdir = tempfile.TemporaryDirectory()
    tempDir = tdir.name
    sw = SettingsWindow() # Declare settings window
    i = TaskbarIconTray(app)
    #mController = MouseController()
    
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
    signal.restartSignal.connect(lambda: restartClocks("checkLoop"))

    KillableThread(target=updateChecker, daemon=True, name="Main: Updater").start()
    KillableThread(target=isElevenClockRunningThread, daemon=True, name="Main: Instance controller").start()
    if not getSettings("EnableLowCpuMode"): KillableThread(target=checkIfWokeUpThread, daemon=True, name="Main: Sleep listener").start()
    if not getSettings("EnableLowCpuMode"): KillableThread(target=wnfDataThread, daemon=True, name="Main: WNF Data listener").start()
    print("🔵 Low cpu mode is set to", str(getSettings("EnableLowCpuMode"))+". DisableNotifications is set to", getSettings("DisableNotifications"))
    
    rdpThread = KillableThread(target=checkRDP, daemon=True, name="Main: Remote desktop controller")
    if getSettings("EnableHideOnRDP"):
        pass
        rdpThread.start()
    

    globals.tempDir = tempDir # Register global variables
    globals.old_stdout = old_stdout # Register global variables
    globals.buffer = buffer # Register global variables
    globals.app = app # Register global variables
    globals.sw = sw # Register global variables
    globals.trayIcon = i # Register global variables
    #globals.mController = mController
    globals.loadTimeFormat = loadTimeFormat # Register global functions
    globals.updateIfPossible = updateIfPossible # Register global functions
    globals.restartClocks = restartClocks # Register global functions
    globals.closeClocks = closeClocks  # Register global functions

    if not(getSettings(f"Updated{versionName}Already")) and not(getSettings("EnableSilentUpdates")):
        setSettings(f"Updated{versionName}Already", True, False)
        if getSettings("DefaultPrefsLoaded"):
            showMessage(_("ElevenClock Updater"), _("ElevenClock has updated to version {0} successfully\nPlease see GitHub for the changelog").format(versionName), False)
        #msg = QFramelessDialog(parent=None, closeOnClick=False)
        #msg.setAutoFillBackground(True)
        #msg.setStyleSheet(sw.styleSheet())
        #msg.setAttribute(QtCore.Qt.WA_StyledBackground)
        #msg.setObjectName("QMessageBox")
        #msg.setTitle("ElevenClock Updater")
        #msg.setText(f"""<b>ElevenClock has updated to version {versionName} successfully.</b>
        #<br><br>This update brings:<br>
        #<ul><li><b>Lots of fixes!</b></li>
        #<li> Fixed the "Invaid Time Format" error</li>
        #3<li> Fixed the clock being black</li>
        #<li> Fixed the clock changing color</li>
        #<li> Added the ability to disable tooltips</li>
        #<li> Other bugfixing and improvements</li></ul>""")
        #msg.addButton("Ok", QDialogButtonBox.ButtonRole.ApplyRole, lambda: msg.close())
        #msg.addButton("Full changelog", QDialogButtonBox.ButtonRole.ResetRole, lambda: os.startfile("https://github.com/martinet101/ElevenClock/releases"))
        #def settNClose():
        #    sw.show()
        #    msg.close()
        #msg.addButton("Settings", QDialogButtonBox.ButtonRole.ActionRole, lambda: settNClose())
        #msg.setDefaultButtonRole(QDialogButtonBox.ButtonRole.ApplyRole, sw.styleSheet())
        #msg.setWindowTitle("ElevenClock has updated!")
        #msg.show()

    showSettings = False
    if "--settings" in sys.argv or showSettings:
        sw.show()

        
    if not getSettings("DefaultPrefsLoaded"):
        setSettings("AlreadyInstalled", True)
        setSettings("NewFullScreenMethod", True)
        setSettings("ForceClockOnFirstMonitor", True)
        showMessage("Welcome to ElevenClock", "You can customize ElevenClock from the ElevenClock Settings. You can search them on the start menu or right-clicking on any clock -> ElevenClock Settings", uBtn=False)
        print("🟢 Default settings loaded")
        setSettings("DefaultPrefsLoaded", True)
        
        
    showWelcomeWizard = False
    if showWelcomeWizard or "--welcome" in sys.argv:
        import welcome
        ww = welcome.WelcomeWindow()

    print(f"🟢 Loaded everything in {time.time()-FirstTime}")
    
    if "--quit-on-loaded" in sys.argv: # This is a testing feature to test if the script can load successfully 
        app.quit()
        
    app.exec_()
    app.quit()

except Exception as e:
    import webbrowser, traceback, platform
    if not "versionName" in locals() and not "versionName" in _globals():
        versionName = "Unknown"
    if not "version" in locals() and not "version" in _globals():
        version = "Unknown"
    os_info = f"" + \
        f"                        OS: {platform.system()}\n"+\
        f"                   Version: {platform.win32_ver()}\n"+\
        f"           OS Architecture: {platform.machine()}\n"+\
        f"          APP Architecture: {platform.architecture()[0]}\n"+\
        f"               APP Version: {versionName}\n"+\
        f"          APP Version Code: {version}\n"+\
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
    webbrowser.open(("https://www.somepythonthings.tk/error-report/?appName=ElevenClock&errorBody="+os_info.replace('\n', '{l}').replace(' ', '{s}')+"{l}{l}{l}{l}ElevenClock Log:{l}"+str("\n\n\n\n"+traceback_info).replace('\n', '{l}').replace(' ', '{s}')).replace("#", "|=|"))
    print(traceback_info)
    
