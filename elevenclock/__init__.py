try:
    _globals = globals
    from functools import partial
    from ctypes import c_int, windll
    windll.shcore.SetProcessDpiAwareness(c_int(2))

    import time

    FirstTime = time.time()

    import os
    from versions import *
    import io
    import sys
    import time
    import glob
    import socket
    import locale
    import hashlib
    import tempfile
    import datetime
    import winshell
    import subprocess
    import pytz
    from threading import Thread
    from urllib.request import urlopen

    try:
        import psutil
        importedPsutil = True
    except ImportError:
        importedPsutil = False
    import win32gui
    import pythoncom
    import win32com.client
    from PySide6.QtGui import *
    from PySide6.QtCore import *
    from PySide6.QtWidgets import *
    import pyautogui
    import keyboard
    pyautogui.FAILSAFE = False # Prevent pyautogui from blocking the bottom-right corner click.
    from external.FramelessWindow import QFramelessDialog
    from external.timezones import win_tz

    from languages import *
    from versions import *
    import globals

    old_stdout = sys.stdout
    buffer = io.StringIO()
    sys.stdout = buffer = io.StringIO()

    from settings import *
    from tools import *
    from tools import _

    from external.WnfReader import isFocusAssistEnabled, getNotificationNumber
    from external.blurwindow import ExtendFrameIntoClientArea

    blacklistedProcesses = ["msrdc.exe", "mstsc.exe", "CDViewer.exe", "wfica32.exe", "vmware-view.exe", "vmware.exe"]

    seconddoubleclick = False
    isRDPRunning = False
    restartCount = 0
    tempDir = ""
    timeStr = ""
    dateTimeFormat = ""
    globals.clocks = []
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
                dmname = socket.gethostbyname_ex("versions.marticliment.com")[0]
                if(dmname == "769432b9-3560-4f94-8f90-01c95844d994.id.repl.co" or getSettings("BypassDomainAuthCheck")): # Check provider IP to prevent exploits
                    integrityPass = True
                try:
                    response = urlopen("https://versions.marticliment.com/versions/elevenclock.ver" if not getSettings("AlternativeUpdateServerProvider") else "http://www.marticliment.com/versions/elevenclock.ver")
                except Exception as e:
                    report(e)
                    response = urlopen("http://www.marticliment.com/versions/elevenclock.ver")
                    integrityPass = True
                print("🔵 Version URL:", response.url)
                response = response.read().decode("utf8")
                new_version_number = response.split("///")[0]
                provided_hash = response.split("///")[2].replace("\n", "").lower()
                if float(new_version_number) > version:
                    print("🟢 Updates found!")
                    if((not(getSettings("DisableAutoInstallUpdates")) and not(getSettings("DisableAutoCheckForUpdates"))) or force):
                        if not getSettings("EnableSilentUpdates"):
                            showNotif.infoSignal.emit(_("ElevenClock Updater"), _("ElevenClock is downloading updates"))
                        try:
                            for clock in globals.clocks:
                                clock.callInMainSignal.emit(clock.progressbar.show)
                        except Exception as e:
                            report(e)
                        if(integrityPass):
                            url = "https://github.com/marticliment/ElevenClock/releases/latest/download/ElevenClock.Installer.exe"
                            filedata = urlopen(url)
                            datatowrite = filedata.read()
                            filename = ""
                            with open(os.path.join(tempDir, "elevenclock-updater.exe"), 'wb') as f:
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
                                    for clock in globals.clocks:
                                        clock.progressbar.hide()
                                except Exception as e:
                                    report(e)
                                print("🟠 Hash not ok")
                                print("🟠 File hash: ", hashlib.sha256(datatowrite).hexdigest())
                                print("🟠 Provided hash: ", provided_hash)
                                showWarn.infoSignal.emit(("Updates found!"), f"ElevenClock Version {new_version_number} is available, but ElevenClock can't verify the authenticity of the package. Please go ElevenClock's homepage and download the latest version from there.\n\nDo you want to open the download page?")

                        else:
                            try:
                                for clock in globals.clocks:
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
                for clock in globals.clocks:
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
        global restartCount
        globals.clocks = []
        if importedPsutil:
            process = psutil.Process(os.getpid())
            memOk = (process.memory_info().rss/1048576) <= 250
        else:
            print("🟠 Psutil couldn't be imported!")
            memOk = True
        
        if globals.sw: isPrefsWinOpen = globals.sw.isVisible()
        else: isPrefsWinOpen = False
        if globals.ww: isWizardOpen = globals.ww.isVisible()
        else: isWizardOpen = False
        
        if (restartCount<20 and memOk) or isPrefsWinOpen or isWizardOpen:
            restartCount += 1
            i = 0
            for screen in app.screens():
                screen: QScreen
                globals.clocks.append(Clock(screen.logicalDotsPerInchX()/96, screen.logicalDotsPerInchY()/96, screen, i))
                i += 1
            
            if getSettings("AutoReloadClocks"):
               Thread(target=lambda: (time.sleep(5*60), restartClocksSignal.restartSignal.emit())).start()
            
            if globals.trayIcon:
                if(getSettings("DisableSystemTray") and len(globals.clocks)>0):
                    globals.trayIcon.hide()
                else:
                    globals.trayIcon.show()
        else:
            cprint("🔴 Overloading system, killing!")
            os.startfile(sys.executable)
            app.quit()
            sys.exit(1)

    def getGeometry(screen: QScreen):
        """
        Return a tuple containing: (screen_width, screen_height, screen_pos_x, screen_pos_y, screen_DPI, desktopWindowRect)
        """
        try:
            geometry = screen.geometry()
            g = (geometry.width(), geometry.height(), geometry.x(), geometry.y(), screen.devicePixelRatio())
            return g
        except Exception as e:
            report(e)
            geometry = QGuiApplication.primaryScreen().geometry()
            g = (geometry.width(), geometry.height(), geometry.x(), geometry.y(), screen.devicePixelRatio())
            return g

    def theyMatch(oldscreens, newscreens):
        if len(oldscreens) != len(newscreens):
            return False  # The number of displays has changed
        return all(old == getGeometry(new) for old, new in zip(oldscreens, newscreens)) # Check that all screen dimensions and dpi are the same as before


    def wnfDataThread():
        global isFocusAssist, numOfNotifs
        while True:
            isFocusAssist = isFocusAssistEnabled()
            numOfNotifs = getNotificationNumber()
            time.sleep(0.3)


    def screenCheckThread():
        global oldScreens
        while True:
            if not theyMatch(oldScreens, app.screens()):
                oldScreens = []
                for screen in app.screens():
                    oldScreens.append(getGeometry(screen))
                restartClocksSignal.restartSignal.emit()
            time.sleep(1)

    def closeClocks():
        for clock in globals.clocks:
            clock.close()
            
        for clock in globals.clocks.copy():
            globals.clocks.remove(clock)
            del clock

        globals.clocks = []

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
        global st
        closeClocks()
        loadClocks()
        setSettings("ReloadInternetTime", True, thread=True)
        globals.doCacheHost = True

    def isElevenClockRunningThread():
        nowTime = time.time()
        LockFile = f"ElevenClockRunning{nowTime}"
        LockFilePath = os.path.join(os.path.expanduser("~"), ".elevenclock", LockFile)
        LockFileLocation = os.path.join(os.path.expanduser("~"), ".elevenclock")
        setSettings(LockFile, True, False)
        while True:
            try:
                if os.path.isfile(os.path.join(LockFileLocation, "ReloadClocks")):
                    try:
                        print("🟠 Restart clocks block file found!")
                        restartClocksSignal.restartSignal.emit()
                        os.remove(os.path.join(LockFileLocation, "ReloadClocks"))
                    except Exception as e:
                        report(e)
                for file in glob.glob(os.path.join(LockFileLocation, "ElevenClockRunning*")):
                    if(LockFilePath == file):
                        pass
                    else:
                        if(float(file.replace(os.path.join(LockFileLocation, "ElevenClockRunning"), "")) < nowTime): # If lockfile is older
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
                        elif float(file.replace(os.path.join(LockFileLocation, "ElevenClockRunning"), "")) > nowTime:
                            globals.newInstanceLaunched = True
                            print("🟠 KILLING, NEWER VERSION RUNNING")
                            killSignal.infoSignal.emit("", "")
                if not os.path.exists(LockFilePath):
                    globals.newInstanceLaunched = True
                    print("🟠 KILLING, NEWER VERSION RUNNING")
                    killSignal.infoSignal.emit("", "")
                if not globals.newInstanceLaunched:
                    globals.canEraseTempDirs = True
            except Exception as e:
                report(e)
            time.sleep(2)

    def wanrUserAboutUpdates(a, b):
        if(QMessageBox.question(sw, a, b, QMessageBox.Open | QMessageBox.Cancel, QMessageBox.Open) == QMessageBox.Open):
            os.startfile("https://github.com/marticliment/ElevenClock/releases/latest")

    def checkIfWokeUpThread():
        while True:
            lastTime = time.time()
            time.sleep(3)
            if((lastTime+6) < time.time()):
                os.startfile(sys.executable)
                app.quit()

    class RestartSignal(QObject):

        restartSignal = Signal()

        def __init__(self) -> None:
            super().__init__()

    class InfoSignal(QObject):

        infoSignal = Signal(str, str)

        def __init__(self) -> None:
            super().__init__()

    class CustomToolTip(QLabel):
        def __init__(self, screen: QScreen, text: str = "", pos: tuple[int, int] = (0, 0), clockId: str = ""):
            self.settingsEnvironment = clockId if getSettings(f"Individualize{clockId}") else ""
            super().__init__(text)
            self.scr = screen
            self.setFixedHeight(60)
            self.setMaximumWidth(200)
            self.setContentsMargins(10, 5, 10, 5)
            self.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
            self.setWindowFlag(Qt.WindowStaysOnTopHint)
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setWindowFlag(Qt.Tool)
            cFont = getSettingsValue("TooltipUseCustomFont", env=self.settingsEnvironment)
            fColor = getSettingsValue("TooltipUseCustomFontColor", env=self.settingsEnvironment)
            bgColor = getSettingsValue("TooltipUseCustomBgColor", env=self.settingsEnvironment)
            if cFont == "":
                if "zh_TW" in lang["locale"]:
                    fontStr = "font-family: \"Microsoft Jhenghei UI\""
                elif "zh_CN" in lang["locale"]:
                    fontStr = "font-family: \"Microsoft YaHei UI\""
                else:
                    fontStr = "font-family: \"Segoe UI Variable Text\""
            else:
                f = QFont()
                f.fromString(cFont)
                fontStr = f"font-family: \"{f.family()}\""
            self.setStyleSheet(f"*{{font-size:{getint(getSettingsValue('TooltipUseCustomFontSize', env=self.settingsEnvironment), 9)}pt;{fontStr}; background-color: rgba({'0,0,0,0' if bgColor == '' else bgColor});color: rgb({('255,255,255' if isTaskbarDark() else '0,0,0') if fColor == '' else fColor})}}")
            self.move(pos[0], pos[1])
            if not getSettings("TooltipDisableTaskbarBackgroundColor", env=self.settingsEnvironment):
                ApplyMenuBlur(self.winId().__int__(), self, smallCorners=True, avoidOverrideStyleSheet = True, shadow=False, useTaskbarModeCheck = True)
            else:
                ExtendFrameIntoClientArea(self.winId().__int__())

        def show(self):
            additionalClocks = ""
            height = 30
            if not getSettings("TooltipDisableTaskbarBackgroundColor", env=self.settingsEnvironment):
                ApplyMenuBlur(self.winId().__int__(), self, smallCorners=True, avoidOverrideStyleSheet = True, shadow=False, useTaskbarModeCheck = True)
            else:
                ExtendFrameIntoClientArea(self.winId().__int__())

            lDateMode = readRegedit(r"Control Panel\International", "sLongDate", "dd/MM/yyyy")
            sDateMode = readRegedit(r"Control Panel\International", "sShortTime", "dd/MM/yyyy")

            for additionalClockNum in ["1", "2"]:
                regKey = f"Control Panel\\TimeDate\\AdditionalClocks\\{additionalClockNum}"
                if readRegedit(regKey, "Enable", 0) == 1:
                    additionalClocks += "\n"
                    height += 15
                    self.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    print("🔵 Short date string:", sDateMode)
                    dateMode = ""
                    for i, ministr in enumerate(sDateMode.split("'")):
                        if i%2==0:
                            dateMode += ministr.replace("dddd", "%A").replace("ddd", "%a").replace("dd", "%$").replace("d", "%#d").replace("$", "d").replace("MMMM", "%B").replace("MMM", "%b").replace("MM", "%m").replace("M", "%#m").replace("yyyy", "%Y").replace("yy", "%y").replace("HH", "%$").replace("H", "%#H").replace("$", "H").replace("hh", "%I").replace("h", "%#I").replace("mm", "%M").replace("m", "%#M").replace("tt", "%p").replace("t", "%p").replace("ss", "%S").replace("s", "%#S")
                        else:
                            dateMode += ministr
                    timezoneName = win_tz[readRegedit(regKey, "TzRegKeyName", "UTC")]
                    tzInfo = pytz.timezone(timezoneName)
                    print(f"🔵 TZ {additionalClockNum} is", tzInfo)
                    additionalClocks += str(datetime.datetime.now(tz=tzInfo).strftime("%a "+dateMode))
                    additionalClockName = str(readRegedit(regKey, "DisplayName", "")).strip()
                    if additionalClockName == "": additionalClockName = timezoneName
                    additionalClocks += f" ({additionalClockName})"

            if not additionalClocks == "":
                additionalClocks = f"\n{additionalClocks}"
                height += 15

            print("🔵 Long date string:", lDateMode)
            self.setFixedHeight(height)
            dateMode = ""
            for i, ministr in enumerate(lDateMode.split("'")):
                if i%2==0:
                    dateMode += ministr.replace("dddd", "%A").replace("ddd", "%a").replace("dd", "%$").replace("d", "%#d").replace("$", "d").replace("MMMM", "%B").replace("MMM", "%b").replace("MM", "%m").replace("M", "%#m").replace("yyyy", "%Y").replace("yy", "%y")
                else:
                    dateMode += ministr
            try:
                self.setText(str(datetime.datetime.now().strftime(dateMode))+additionalClocks)
            except Exception as e:
                report(e)
                self.setText(str(datetime.datetime.now().strftime("%A, %#d %B %Y"))+additionalClocks)
            super().show()

        def get6px(self, i: int) -> int:
            return round(i*self.screen().devicePixelRatio())

    class Clock(QWidget):

        refresh = Signal()
        hideSignal = Signal()
        callInMainSignal = Signal(object)
        styler = Signal(str)
        font: QFont = QFont()
        preferedwidth = 200
        coverPreferedWidth = 200
        isHovered = False
        isTooltipWaiting = False
        preferedHeight = 48
        coverPreferedHeight = 48
        focusassitant = True
        lastTheme = 0
        clockShouldBeHidden = False
        shouldBeVisible = True
        isRDPRunning = True
        clockOnTheLeft = False
        INTLOOPTIME = 2
        tempMakeClockTransparent = False
        AWindowIsInFullScreen: bool = False
        clockCover = None
        isIgnoringClicks = False
        shownBackgroundOnSolidColor: bool = False
        clockId: str = ""
        clockNumber: bool = 0
        internetTimeOffset: int = 0
        clockFormat: str = ""
        settingsEnvironment: str = ""
        currentTaskbarHwnd: int = 0
        
        LastCapturedBackgroundColor: int = -1
        LastCapturedForegroundColor: str = ""

        def __init__(self, dpix: float, dpiy: float, screen: QScreen, index: int, isCover: bool = False, isSecondary: bool = False):
            super().__init__()
            self.shouldCoverWindowsClock = False
            self.isCover = isCover
            self.isSecondary = isSecondary
            self.clockId = self.getClockID(screen)[0]
            self.clockName = _("Clock {0} on {1}").format(self.getClockID(screen)[1][0], self.getClockID(screen)[1][1])
            self.isCustomClock = getSettings(f"Individualize{self.clockId}")
            if self.isCustomClock:
                self.settingsEnvironment = self.clockId
            if isCover:
                self.shouldAddSecondaryClock = False
            else:
                self.shouldAddSecondaryClock = getSettings("EnableSecondClock")

            if f"_{screen.name()}_" in getSettingsValue("BlacklistedMonitors"):
                print("🟠 Monitor blacklisted!")
                self.hide()
                self.close()
                if self in globals.clocks:
                    globals.clocks.remove(self)
                
            elif isCover and getSettings("DisableSystemClockCover"):
                self.hide()
                self.close()
                if self in globals.clocks:
                    globals.clocks.remove(self)
                
            else:
                self.taskbarHwnds = getWindowHwnds("Shell_SecondaryTrayWnd") + getWindowHwnds("Shell_TrayWnd")
                for taskbar in self.taskbarHwnds:
                    tbPoint = win32gui.GetWindowRect(taskbar)
                    g = QRect(screen.geometry().x(), screen.geometry().y(), screen.size().width()*screen.devicePixelRatio(), screen.size().height()*screen.devicePixelRatio())
                    if g.contains(QPoint(tbPoint[0], tbPoint[1])):
                        self.currentTaskbarHwnd = taskbar
                        break
                    
                self.index = index
                self.tooltipEnabled = not self.getSettings("DisableToolTip")
                print(f"🔵 Initializing clock {index}...")
                self.callInMainSignal.connect(lambda f: f())
                self.styler.connect(self.setStyleSheet)

                self.UseTaskbarBackgroundColor = not self.getSettings("DisableTaskbarBackgroundColor") and not (self.getSettings("UseCustomBgColor") or self.getSettings("AccentBackgroundcolor"))
                self.transparentBackground = self.getSettings("DisableTaskbarBackgroundColor") and not (self.getSettings("UseCustomBgColor") or self.getSettings("AccentBackgroundcolor"))

                if self.UseTaskbarBackgroundColor:
                    print("🔵 Using taskbar background color")
                    self.bgcolor = "0, 0, 0, 0"
                else:
                    print("🟡 Not using taskbar background color")
                    if self.getSettings("AccentBackgroundcolor"):
                        self.bgcolor = f"{getColors()[5 if isTaskbarDark() else 1]},100"
                    else:
                        self.bgcolor = self.getSettingsValue("UseCustomBgColor") if self.getSettingsValue("UseCustomBgColor") else "0, 0, 0, 0"
                    print("🔵 Using bg color:", self.bgcolor)

                self.prefMargins = 0
                try:
                    if readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "TaskbarSi", 1) == 0 or (not self.getSettings("DisableTime") and not self.getSettings("DisableDate") and self.getSettings("EnableWeekDay")):
                        self.prefMargins = 1
                        self.widgetStyleSheet = f"background-color: rgba(bgColor%); margin: 0;margin-top: 0;margin-bottom: 0; border-radius: 4px;"
                        if not(not self.getSettings("DisableTime") and not self.getSettings("DisableDate") and self.getSettings("EnableWeekDay")):
                            print("🟡 Small sized taskbar")
                            self.preferedHeight = 32
                            self.coverPreferedHeight = 32
                            self.preferedwidth = 200
                            self.coverPreferedWidth = 200
                    else:
                        print("🟢 Regular sized taskbar")
                        self.prefMargins = 1
                        self.widgetStyleSheet = f"background-color: rgba(bgColor%);margin: 0;border-radius: 6px;padding: 2px;"
                except Exception as e:
                    print("🟡 Regular sized taskbar")
                    report(e)
                    self.prefMargins = 1
                    self.widgetStyleSheet = f"background-color: rgba(bgColor%);margin: 0;border-radius: 6px;padding: 2px;"
                self.setStyleSheet(self.widgetStyleSheet.replace("bgColor", self.bgcolor))

                if self.getSettings("ClockFixedHeight"):
                    print("🟡 Custom height being used!")
                    try:
                        if self.getSettingsValue("ClockFixedHeight") != "":
                            self.preferedHeight = int(self.getSettingsValue("ClockFixedHeight"))
                            self.coverPreferedHeight = int(self.getSettingsValue("ClockFixedHeight"))
                    except ValueError as e:
                        report(e)
                                
                self.screenGeometry = screen.geometry()
                
                self.refresh.connect(self.refreshAndShow)
                self.hideSignal.connect(self.hide)
                if not(self.getSettings("PinClockToTheDesktop")) or self.isCover:
                    self.setWindowFlag(Qt.WindowStaysOnTopHint)
                else:
                    print("🟡 Clock pinned to desktop")
                    self.setWindowFlag(Qt.WindowStaysOnBottomHint)
                self.setWindowFlag(Qt.FramelessWindowHint)
                self.setAttribute(Qt.WA_ShowWithoutActivating)
                self.setAttribute(Qt.WA_TranslucentBackground)
                self.setWindowFlag(Qt.Tool)
                hexBlob = b'0\x00\x00\x00\xfe\xff\xff\xffz\xf4\x00\x00\x03\x00\x00\x00T\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x08\x04\x00\x00\x80\x07\x00\x008\x04\x00\x00`\x00\x00\x00\x01\x00\x00\x00'
                registryReadResult = readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\StuckRects3", "Settings", hexBlob)
                self.TASKBAR_DOES_AUTOHIDE = registryReadResult[8] == 123

                if self.isCover:
                    print("🟠 Clock is cover!!!")
                    self.UseTaskbarBackgroundColor = True
                    self.transparentBackground = False
                    self.bgcolor = "0, 0, 0, 0"
                    self.tooltipEnabled = False

                if self.TASKBAR_DOES_AUTOHIDE:
                    print("🟡 ElevenClock set to hide with the taskbar")

                self.clockOnTheLeft = self.getSettings("ClockOnTheLeft")
                screenName = screen.name().replace("\\", "_")
                self.setScreen(screen)
                if not self.clockOnTheLeft:
                    if self.getSettings(f"SpecificClockOnTheLeft{screenName}"):
                        self.clockOnTheLeft = True
                        print(f"🟡 Clock {screenName} on the left (forced)")
                        if not self.getSettings("DisableSystemClockCover"):
                            print("🟠 Showing Cover on the right!")
                            self.shouldCoverWindowsClock = True
                            if self.isCover:
                                self.clockOnTheLeft = False
                else:
                    if self.getSettings(f"SpecificClockOnTheRight{screenName}"):
                        self.clockOnTheLeft = False
                        print(f"🟡 Clock {screenName} on the right (forced)")
                    else:
                        self.shouldCoverWindowsClock = True
                        if self.isCover:
                            self.clockOnTheLeft = False
                
                if self.isSecondary:
                    self.clockOnTheLeft = not self.clockOnTheLeft

                coverX = 0
                coverY = 0
                try:
                    if (registryReadResult[12] == 1 and not self.getSettings("ForceOnBottom")) or (self.getSettings("ForceOnTop") and not self.getSettings(f"SpecificClockOnTheBottom{screenName}")) or self.getSettings(f"SpecificClockOnTheTop{screenName}"):
                        h = self.screenGeometry.y()
                        self.clockOnTop = True
                        print("🟡 Clock on the top")
                    else:
                        h = self.screenGeometry.y()+self.screenGeometry.height()-(self.preferedHeight*dpiy)
                        self.clockOnTop = False
                        print("🟢 Clock on the bottom")
                    if registryReadResult[12] == 1:
                        coverY = self.screenGeometry.y()
                    else:
                        coverY = self.screenGeometry.y()+self.screenGeometry.height()-(self.coverPreferedHeight*dpiy)
                    if h != coverY: # Calculate if clock has been moved vertically and a cover should be applied
                        self.shouldCoverWindowsClock = True
                except Exception as e:
                    report(e)
                    h = self.screenGeometry.y()+self.screenGeometry.height()-(self.preferedHeight*dpiy)
                    coverY = h
                    self.clockOnTop = False
                    self.shouldCoverWindowsClock = False
                    print("🟠 Clock on the bottom (by exception)")
                    
                    
                else:
                    self.showBlurryBackground = False

                if self.clockOnTheLeft:
                    print("🟡 Clock on the left")
                    coverX = self.screenGeometry.x()+self.screenGeometry.width()-((self.coverPreferedWidth)*dpix) # Windows clock position
                    w = self.screenGeometry.x()
                else:
                    print("🟢 Clock on the right")
                    w = self.screenGeometry.x()+self.screenGeometry.width()-((self.preferedwidth)*dpix)
                    coverX = w

                xoff = 0
                yoff = 2

                if self.getSettingsValue("ClockXOffset") != "":
                    print("🟡 X offset being used!")
                    try:
                        xoff = int(self.getSettingsValue("ClockXOffset"))
                    except ValueError as e:
                        report(e)

                if self.getSettingsValue("ClockYOffset") != "":
                    print("🟡 Y offset being used!")
                    try:
                        yoff = int(self.getSettingsValue("ClockYOffset"))
                    except ValueError as e:
                        report(e)

                self.X = int(w) + xoff
                self.Y = int(h) + yoff
                self.coverX = coverX + xoff
                self.coverY = coverY + yoff
                self.dpix = dpix
                self.dpiy = dpiy
                
                if self.isCover:
                    self.move(self.coverX, self.coverY)
                    self.resize(int(self.coverPreferedWidth*dpix), int(self.coverPreferedHeight*dpiy)-2)
                    print("🔵 Clock cover geometry:", self.geometry())
                else:
                    self.move(self.X, self.Y)
                    self.resize(int(self.preferedwidth*dpix), int(self.preferedHeight*dpiy)-2)
                    print("🔵 Clock geometry:", self.geometry())
                
                self.forceDarkTheme = self.getSettings("ForceDarkTheme")
                self.forceLightTheme = self.getSettings("ForceLightTheme")
                self.hideClockWhenClicked = self.getSettings("HideClockWhenClicked")
                self.IS_LOW_CPU_MODE = self.getSettings("EnableLowCpuMode")
                self.DISABLE_AUTOMATIC_TEXT_COLOR = self.getSettings("UseCustomFontColor")
                self.primaryScreen = QGuiApplication.primaryScreen()
                
                self.user32 = windll.user32
                self.user32.SetProcessDPIAware() # optional, makes functions return real pixel numbers instead of scaled values

                self.fullScreenRect = (self.screenGeometry.x(), self.screenGeometry.y(), self.screenGeometry.x()+self.screenGeometry.width(), self.screenGeometry.y()+self.screenGeometry.height())
                print("🔵 Full screen rect: ", self.fullScreenRect)
                globals.previousFullscreenHwnd[self.index] = 0
                
                self.setMouseTracking(True)
                
                if self.shouldAddSecondaryClock:
                    self.shouldCoverWindowsClock = False
                    if not self.isSecondary:
                        self.clockCover = Clock(dpix, dpiy, screen, index, isSecondary=True)
                        globals.clocks.append(self.clockCover)
                elif self.shouldCoverWindowsClock:
                    if not self.isCover:
                        self.clockCover = Clock(dpix, dpiy, screen, index, isCover=True)
                        globals.clocks.append(self.clockCover)
                        
                self.label = Label(timeStr, self, self.isCover, self.settingsEnvironment)
                self.label.move(0, 2)
                self.label.setFixedHeight(self.height())
                self.label.resize(self.width()-8, self.height()-1)
                self.label.show()
                
                if self.getSettings("CenterAlignment"):
                    self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                elif self.clockOnTheLeft:
                    self.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                else:
                    self.label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                       
                # Load clock click actions

                if not self.isCover:
                    self.clickAction = ("win", "n")
                    act = self.getSettingsValue("CustomClockClickAction")
                    if act != "":
                        if len(act.split("+")) > 3 or len(act.split("+")) < 1:
                            print("🟠 Invalid clock custom action")
                        else:
                            r = []
                            for piece in act.split("+"):
                                piece = piece.lower()
                                r.append(piece)     
                            self.clickAction = r
                            print("🟢 Custom valid shortcut specified:", self.clickAction)

                    self.doubleClickAction = ("f20")
                    doubleAction = self.getSettingsValue("CustomClockDoubleClickAction")
                    if doubleAction != "":
                        if len(doubleAction.split("+")) > 3 or len(doubleAction.split("+")) < 1:
                            print("🟠 Invalid double click action piece")
                        else:
                            r = []
                            for piece in doubleAction.split("+"):
                                piece = piece.lower()
                                r.append(piece)
                            self.doubleClickAction = r
                            print("🟢 Custom valid shortcut specified (for double click):", self.doubleClickAction)

                    self.middleClickAction = ("f20")
                    middleAction = self.getSettingsValue("CustomClockMiddleClickAction")
                    if middleAction != "":
                        if len(middleAction.split("+")) > 3 or len(middleAction.split("+")) < 1:
                            print("🟠 Invalid double click action piece")
                        else:
                            r = []
                            for piece in middleAction.split("+"):
                                piece = piece.lower()
                                r.append(piece)
                            self.middleClickAction = r
                            print("🟢 Custom valid shortcut specified (for middle click):", self.middleClickAction)

                    self.label.clicked.connect(lambda: self.singleClickAction())
                    self.label.doubleClicked.connect(lambda: self.doDoubleClickAction())
                    self.label.middleClicked.connect(lambda: self.doMiddleClickAction())

                # Load label styles (only on non-cover clocks)

                if self.isCover:
                    styleSheetString = self.makeLabelStyleSheet(0, 0, 0, 0, f"transparent")
                    self.label.setStyleSheet(styleSheetString)
                else:
                    customFont = self.getSettingsValue("UseCustomFont")
                    if customFont == "":
                        if lang["locale"] == "ko":
                            self.fontfamilies = ["Malgun Gothic", "Segoe UI Variable Text", "sans-serif"]
                        elif lang["locale"] == "zh_TW":
                            self.fontfamilies = ["Microsoft JhengHei UI", "Segoe UI Variable Text", "sans-serif"]
                        elif lang["locale"] == "zh_CN":
                            self.fontfamilies = ["Microsoft YaHei UI", "Segoe UI Variable Text", "sans-serif"]
                        else:
                            self.fontfamilies = ["Segoe UI Variable Display", "sans-serif"]
                        self.font.setPointSizeF(9.3)
                    else:
                        self.fontfamilies = []
                    self.customFont = customFont
                        
                    customSize = self.getSettingsValue("UseCustomFontSize")
                    if customSize == "":
                        self.font.setPointSize(9)
                    else:
                        try:
                            self.font.setPointSize(int(float(customSize)))
                        except ValueError:
                            self.font.setPointSize(9)
                        except Exception as e:
                            self.font.setPointSize(9)
                            report(e)
                    
                    if isTaskbarDark():
                        self.fontfamilies = [element.replace("Segoe UI Variable Display", "Segoe UI Variable Display Semib") for element in self.fontfamilies]
                        if self.fontfamilies != []:
                            self.font.setFamilies(self.fontfamilies)
                            if lang["locale"] in ("zh_TW", "zh_CN", "ko"):
                                self.font.setWeight(QFont.Weight.Normal)
                            else:
                                self.font.setWeight(QFont.Weight.DemiBold)
                        else:
                            self.font.fromString(self.customFont)
                        self.font.setLetterSpacing(QFont.PercentageSpacing, 100)
                        self.label.setFont(self.font)
                        self.label.bgopacity = .1
                    else:
                        self.fontfamilies = [element.replace("Segoe UI Variable Display Semib", "Segoe UI Variable Display") for element in self.fontfamilies]
                        if self.fontfamilies != []:
                            self.font.setFamilies(self.fontfamilies)
                        else:
                            self.font.fromString(self.customFont)
                        self.font.setWeight(QFont.Weight.ExtraLight)
                        self.font.setLetterSpacing(QFont.PercentageSpacing, 110)
                        self.label.setFont(self.font)
                        self.label.bgopacity = .5
                        
                    if self.getSettings("UseCustomFontColor"):
                        print("🟡 Using custom font color:", self.getSettingsValue('UseCustomFontColor'))
                        self.lastTheme = -1
                        styleSheetString = self.makeLabelStyleSheet(0, 3, 9, 5, f"rgb({self.getSettingsValue('UseCustomFontColor')})")
                        self.label.setStyleSheet(styleSheetString)
                    else:
                        print("🔵 Using automatic font color")
                        self.lastTheme = 0 if isTaskbarDark() else 1
                                
                    print(f"🔵 Font families   : {self.fontfamilies}")
                    print(f"🔵 Custom font     : {self.customFont}")
                    print(f"🔵 Font size: {self.font.pointSizeF()}")
                    
                # Load tooltip, desktop button and other widgets
                
                self.colorWidget = QWidget(self)
                self.colorWidget.setStyleSheet("border: 0; margin: 0;")

                self.backgroundTexture = QLabel(self)
                self.backgroundTexture.setAttribute(Qt.WA_TransparentForMouseEvents)
                self.backgroundTexture.setStyleSheet("background-color: transparent; margin: -2px; border: 0;")
                self.backgroundTexture.setContentsMargins(-1, -1, -1, -1)
                if(not self.getSettings("DisableTaskbarBackgroundColor") and not self.getSettings("UseCustomBgColor")) and not self.getSettings("DisableBlurryTexture"):
                    if(isTaskbarDark()):
                        self.showBlurryBackground = True
                        self.backgroundTexture.setPixmap(QPixmap(getPath("taskbarbg_black.png")))
                    else:
                        self.showBlurryBackground = True
                        self.backgroundTexture.setPixmap(QPixmap(getPath("taskbarbg_white.png")))
                        
                self.label.raise_()

                self.tooltip = CustomToolTip(screen, "placeholder", clockId=self.clockId)
                
                self.desktopButton: QHoverButton = None
                
                if (readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "TaskbarSd", 0) == 1 or self.getSettings("ShowDesktopButton")) and not self.isCover:
                    print("🟡 Desktop button enabled")
                    self.desktopButton = QHoverButton(parent=self)
                    self.desktopButton.clicked.connect(lambda: self.showDesktop())
                    self.desktopButton.show()
                    self.desktopButton.setFixedWidth(8)
                    self.desktopButton.setIconSize(QSize(8, 48))
                    hoverIcon = drawVerticalLine(self.desktopButton.iconSize(), 16, 128)
                    pressIcon = drawVerticalLine(self.desktopButton.iconSize(), 16, 70)
                    self.desktopButton.hovered.connect(lambda: self.desktopButton.setIcon(hoverIcon))
                    self.desktopButton.pressed.connect(lambda: self.desktopButton.setIcon(pressIcon))
                    self.desktopButton.unpressed.connect(lambda: self.desktopButton.setIcon(hoverIcon))
                    self.desktopButton.unhovered.connect(lambda: self.desktopButton.setIcon(QIcon()))
                    self.setFixedHeight(self.preferedHeight)
                
                accColors = getColors()

                self.progressbar = QProgressBar(self)
                self.progressbar.setFixedHeight(2)
                self.progressbar.setRange(0, 200)
                self.progressbar.setValue(0)
                self.progressbar.setStyleSheet(f"*{{border: 0;margin:0;padding:0;}}QProgressBar::chunk{{background-color:rgb({accColors[1 if isTaskbarDark() else 4]})}}")
                self.progressbar.hide()

                self.leftSlow = QVariantAnimation()
                self.leftSlow.setStartValue(0)
                self.leftSlow.setEndValue(200)
                self.leftSlow.setDuration(500)
                self.leftSlow.valueChanged.connect(lambda v: self.progressbar.setValue(v))
                self.leftSlow.finished.connect(lambda: (self.rightSlow.start(), self.progressbar.setInvertedAppearance(True)))
                
                self.rightSlow = QVariantAnimation()
                self.rightSlow.setStartValue(200)
                self.rightSlow.setEndValue(0)
                self.rightSlow.setDuration(500)
                self.rightSlow.valueChanged.connect(lambda v: self.progressbar.setValue(v))
                self.rightSlow.finished.connect(lambda: (self.leftFast.start(), self.progressbar.setInvertedAppearance(False)))
                
                self.leftFast = QVariantAnimation()
                self.leftFast.setStartValue(0)
                self.leftFast.setEndValue(200)
                self.leftFast.setDuration(200)
                self.leftFast.valueChanged.connect(lambda v: self.progressbar.setValue(v))
                self.leftFast.finished.connect(lambda: (self.rightFast.start(), self.progressbar.setInvertedAppearance(True)))

                self.rightFast = QVariantAnimation()
                self.rightFast.setStartValue(200)
                self.rightFast.setEndValue(0)
                self.rightFast.setDuration(200)
                self.rightFast.valueChanged.connect(lambda v: self.progressbar.setValue(v))
                self.rightFast.finished.connect(lambda: (self.leftSlow.start(), self.progressbar.setInvertedAppearance(False)))
                
                if not self.isCover:
                    self.leftSlow.start()
                    
                # Final initialize procedure
                    
                self.loadTimeFormat()
                
                self.TextUpdaterLoop = KillableThread(target=self.updateTextLoop, daemon=True, name=f"Clock[{index}]: Time updater loop")
                self.MainLoop = KillableThread(target=self.mainClockLoop, daemon=True, name=f"Clock[{index}]: Main clock loop")
                self.InternetTimeLoop = KillableThread(target=self.loadInternetTimeOffset, daemon=True, name=f"Clock[{index}]: Atomic clock sync thread")
                self.TextUpdaterLoop.start()
                self.MainLoop.start()
                self.InternetTimeLoop.start()
                
                self.show()
                self.raise_()
                self.setFocus()
        
        def loadTimeFormat(self):
            try:
                locale.setlocale(locale.LC_ALL, readRegedit(r"Control Panel\International", "LocaleName", "en_US"))
                if self.getSettingsValue("CustomClockStrings") != "":
                    clockFormat = self.getSettingsValue("CustomClockStrings")
                    print(f"🟡 Custom loaded date time format (clock {self.index}):", clockFormat.replace("\n", "\\n"))
                    self.clockFormat = clockFormat
                else:
                    showSeconds = readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced", "ShowSecondsInSystemClock", 0) or self.getSettings("EnableSeconds")
                    clockFormat = "%HH:%M\n%A\n(W%W) %d/%m/%Y"

                    if self.getSettings("DisableTime"):
                        clockFormat = clockFormat.replace("%HH:%M\n", "")
                    if self.getSettings("DisableDate"):
                        if("\n" in clockFormat):
                            clockFormat = clockFormat.replace("\n(W%W) %d/%m/%Y", "")
                        else:
                            clockFormat = clockFormat.replace("(W%W) %d/%m/%Y", "")
                    elif not self.getSettings("EnableWeekNumber"):
                        clockFormat = clockFormat.replace("(W%W) ", "")
                    else:
                        if not lang["locale"] in ("zh_CN", "zh_TW"):
                            clockFormat = clockFormat.replace("(W%W) ", f"({_('W')}%W) ")
                        else:
                            clockFormat = clockFormat.replace("(W%W) ", f"(第%W{_('W')}) ")
                    if not self.getSettings("EnableWeekDay"):
                        try:
                            clockFormat = clockFormat.replace("%A", "").replace("\n\n", "\n")
                            if clockFormat[-1] == "\n":
                                clockFormat = clockFormat[0:-1]
                            if clockFormat[0] == "\n":
                                clockFormat = clockFormat[1:]
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
                            if not("S" in timeMode) and showSeconds == 1:
                                for separator in ":.-/_":
                                    if(separator in timeMode):
                                        timeMode += f"{separator}%S"
                        else:
                            timeMode += ministr

                    for separator in ":.-/_":
                        timeMode = timeMode.replace(f" %p{separator}%S", f"{separator}%S %p")
                        timeMode = timeMode.replace(f" %p{separator}%#S", f"{separator}%#S %p")

                    clockFormat = clockFormat.replace("%d/%m/%Y", dateMode).replace("%HH:%M", timeMode).replace("%S", "%S ").replace("%#S", "%#S ")
                    
                    try:
                        if self.getSettings("CustomLineHeight") and self.getSettingsValue("CustomLineHeight") != "":
                            customLineHeight = float(self.getSettingsValue("CustomLineHeight"))
                            print("🟢 Loaded date time format:", clockFormat)
                            clockFormat = f"<p style=\"line-height:{customLineHeight}\"><span>"+clockFormat.replace("\n", "<br>").replace(" ", "")+"</span></p>"
                    except Exception as e:
                        report(e)

                    print("🔵 Loaded date time format:", clockFormat.replace("\n", "\\n"), f" (clock {self.index}")
                    self.clockFormat = clockFormat
            except Exception as e:
                report(e)
                self.clockFormat = "%HH:%M\n%A\n(W%W) %d/%m/%Y"

        def makeLabelStyleSheet(self, padding, rightPadding, rightMargin, leftPadding, color):
            accColors = getColors()
            bg = 1 if isTaskbarDark() else 4
            fg = 6 if isTaskbarDark() else 1
            return f"*{{padding: {padding}px;padding-right: {rightPadding}px;margin-right: {rightMargin}px;padding-left: {leftPadding}px; color: {color};background-color: transparent;}}#notifIndicator{{background-color: rgb({accColors[bg]});color:rgb({accColors[fg]});}}"

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
            xPos = self.screen().geometry().x()+self.screen().size().width()-10-self.tooltip.width() if not self.clockOnTheLeft else self.screen().geometry().x()+10
            yPos = self.pos().y()-5-self.tooltip.height() if not self.clockOnTop else self.pos().y()+5+self.height()
            self.tooltip.move(xPos, yPos)

        def get6px(self, i: int) -> int:
            return round(i*self.screen().devicePixelRatio())
        
        def getClockID(self, screen: QScreen = None):
            isSecondary = int(self.isSecondary)
            clockMonitor = (screen if screen else self.screen()).name().replace(" ", "_").replace(".", "_")
            return (f"clock{isSecondary}_mon{clockMonitor}", (isSecondary, clockMonitor))

        def checkAndUpdateBackground(self) -> None:
            try:
                CLOCK_IS_TEMPORARILY_TRANSPARENT = self.tempMakeClockTransparent
                if self.isCover:
                    ENABLE_AUTOMATIC_TEXT_COLOR = False
                    ENABLE_AUTOMATIC_BACKGROUND_COLOR = True
                    FALSE_BLUR_TEXTURE_ENABLED = True
                else:
                    ENABLE_AUTOMATIC_TEXT_COLOR = not self.DISABLE_AUTOMATIC_TEXT_COLOR and self.isVisible()
                    ENABLE_AUTOMATIC_BACKGROUND_COLOR = self.UseTaskbarBackgroundColor and self.isVisible()
                    FALSE_BLUR_TEXTURE_ENABLED = self.showBlurryBackground
                BackgroundIntegerColor = 0
                ForceUpdateBackgroundColor: bool = False
                ContextMenuIsVisible = False
                
                if CLOCK_IS_TEMPORARILY_TRANSPARENT:
                    if self.LastCapturedBackgroundColor > -1 and ENABLE_AUTOMATIC_BACKGROUND_COLOR:
                        ForceUpdateBackgroundColor = True
                    self.LastCapturedBackgroundColor = -1
                    
                if FALSE_BLUR_TEXTURE_ENABLED:
                    if CLOCK_IS_TEMPORARILY_TRANSPARENT or self.AWindowIsInFullScreen:
                        self.callInMainSignal.emit(self.backgroundTexture.hide)
                    else:
                        self.callInMainSignal.emit(self.backgroundTexture.show)

                if ENABLE_AUTOMATIC_BACKGROUND_COLOR or ENABLE_AUTOMATIC_TEXT_COLOR:
                    g = self.screen().geometry()
                    BackgroundIntegerColor = self.screen().grabWindow(0, self.x()-g.x()+self.label.x()+(self.label.width() if self.clockOnTheLeft else 0), self.y()-g.y(), 1, 1).toImage().pixel(0, 0)
                
                
                if globals.trayIcon:
                    ContextMenuIsVisible = globals.trayIcon.contextMenu().isVisible()
                
                if (ENABLE_AUTOMATIC_BACKGROUND_COLOR and not ContextMenuIsVisible and not CLOCK_IS_TEMPORARILY_TRANSPARENT) or ForceUpdateBackgroundColor:
                    try:
                        color = QColor(BackgroundIntegerColor)
                    except OverflowError as e:
                        print("🟣 Invalid BackgroundIntegerColor (background function) (OverflowError)")
                        try:
                            color = QColor(BackgroundIntegerColor-10)
                        except OverflowError:
                            color = QColor(Qt.GlobalColor.white)
                    if BackgroundIntegerColor != self.LastCapturedBackgroundColor:
                        self.LastCapturedBackgroundColor = BackgroundIntegerColor
                        self.styler.emit(self.widgetStyleSheet.replace("bgColor", f"{color.red()}, {color.green()}, {color.blue()}, {0 if CLOCK_IS_TEMPORARILY_TRANSPARENT else 100}"))
                
                if ENABLE_AUTOMATIC_TEXT_COLOR:
                    try:
                        color = QColor(BackgroundIntegerColor)
                    except OverflowError as e:
                        print("🟣 Invalid BackgroundIntegerColor (text function) (OverflowError)")
                        try:
                            color = QColor(BackgroundIntegerColor-10)
                        except OverflowError:
                            color = QColor(Qt.GlobalColor.white)
                    AverageColorValue = color.red()/3 + color.green()/3 + color.blue()/3
                    FinalTextColor = "black" if (AverageColorValue>=127) else "white"
                    if FinalTextColor != self.LastCapturedForegroundColor:
                        self.LastCapturedForegroundColor = FinalTextColor
                        styleSheetString = self.makeLabelStyleSheet(0, 3, 9, 5, FinalTextColor)
                        self.callInMainSignal.emit(partial(self.label.setStyleSheet, styleSheetString))
            except Exception as e:
                report(e)

        def TheresAWindowInFullscreen(self) -> bool:
            try:
                windowStyle = windll.user32.GetWindowLongA(self.currentTaskbarHwnd, -20)
                for otherVal in [134217728, 33554432, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 16384, 8192, 4096, 1024, 512, 256, 128, 64, 32, 16]:
                    if otherVal<=windowStyle:
                        windowStyle -= otherVal
                if windowStyle>=0x8:
                    return False # The taskbar is topmost
                else:
                    return True # The taskbar is a regular window
            except Exception as e:
                report(e)

        def mainClockLoop(self):
            global numOfNotifs
            
            IgnoringMouseClicks = False
            BackgroundUpdatesCounter = 1

            IGNORE_MOUSECLICKS_WHEN_FS = self.getSettings("MouseEventTransparentFS")
            LOW_CPU_MODE = getSettings("EnableLowCpuMode")
            self.WAITLOOPTIME = 0.4 if LOW_CPU_MODE else 0.1

            if not self.isCover:
                ENABLE_HIDE_ON_FULLSCREEN = not self.getSettings("DisableHideOnFullScreen")
                DISABLE_HIDE_WITH_TASKBAR = self.getSettings("DisableHideWithTaskbar")
                SHOW_NOTIFICATIONS = not self.getSettings("DisableNotifications")
                MAKE_CLOCK_TRANSPARENT_WHEN_FULLSCREENED = self.getSettings("TransparentClockWhenInFullscreen")
            else:
                ENABLE_HIDE_ON_FULLSCREEN = True
                DISABLE_HIDE_WITH_TASKBAR = False
                SHOW_NOTIFICATIONS = True
                MAKE_CLOCK_TRANSPARENT_WHEN_FULLSCREENED = False
            
            print(f"🔵 Show/hide loop started with parameters: HideonFS:{ENABLE_HIDE_ON_FULLSCREEN}, NotHideOnTB:{DISABLE_HIDE_WITH_TASKBAR}, DisableNotifications:{SHOW_NOTIFICATIONS}")
            
            while True:
                self.AWindowIsInFullScreen = self.TheresAWindowInFullscreen()
                HideClock = False
                
                if self.clockShouldBeHidden:
                    HideClock = True
                elif not ENABLE_HIDE_ON_FULLSCREEN:
                    HideClock = False
                else:
                    HideClock = self.AWindowIsInFullScreen
                    
                if not HideClock and not DISABLE_HIDE_WITH_TASKBAR and self.TASKBAR_DOES_AUTOHIDE:
                    mousePos = getMousePos()
                    if (mousePos.y() + 1 == self.screenGeometry.y() + self.screenGeometry.height()) and self.screenGeometry.x() < mousePos.x() and self.screenGeometry.x()+self.screenGeometry.width() > mousePos.x():
                        if self.isHidden():
                            time.sleep(0.22)
                        HideClock = False
                    elif (mousePos.y() <= self.screenGeometry.y()+self.screenGeometry.height()-self.preferedHeight):
                        if globals.trayIcon != None:
                            menu = globals.trayIcon.contextMenu()
                            if menu.isVisible():
                                HideClock = False
                            else:
                                HideClock = True
                        else:
                            HideClock = True
                    
                if HideClock:
                    self.hideSignal.emit()
                    BackgroundUpdatesCounter = 0
                else:
                    if SHOW_NOTIFICATIONS:
                        if numOfNotifs > 0:
                            if isFocusAssist:
                                self.callInMainSignal.emit(self.label.enableFocusAssistant)
                            else:
                                self.callInMainSignal.emit(self.label.enableNotifDot)                            
                        else:
                            if isFocusAssist:
                                self.callInMainSignal.emit(self.label.enableFocusAssistant)
                            else:
                                self.callInMainSignal.emit(self.label.disableClockIndicators)
                        
                    if self.AWindowIsInFullScreen:
                        self.tempMakeClockTransparent = MAKE_CLOCK_TRANSPARENT_WHEN_FULLSCREENED
                        
                        if IGNORE_MOUSECLICKS_WHEN_FS:
                            if not IgnoringMouseClicks:
                                IgnoringMouseClicks = True
                                self.callInMainSignal.emit(self.makeclockIngoreMouseClicks)
                        else:
                            if IgnoringMouseClicks:
                                IgnoringMouseClicks = False
                                self.callInMainSignal.emit(self.makeclockRegiesterMouseClicks)
                    else:
                        if IgnoringMouseClicks:
                            IgnoringMouseClicks = False
                            self.callInMainSignal.emit(self.makeclockRegiesterMouseClicks)
                            
                        self.tempMakeClockTransparent = False

                    self.refresh.emit()

                    if BackgroundUpdatesCounter >= 2:
                        self.checkAndUpdateBackground()
                        BackgroundUpdatesCounter = 0
                    else:
                        BackgroundUpdatesCounter += 1

                time.sleep(self.WAITLOOPTIME)

        def makeclockIngoreMouseClicks(self):
            if not self.isIgnoringClicks:
                self.isIgnoringClicks = True
                print("🟠 Start ignoring mouse events")
                for w in (self, self.label, self.desktopButton, self.backgroundTexture):
                    self.callInMainSignal.emit(lambda: w.setAttribute(Qt.WA_TransparentForMouseEvents, True))
                    self.callInMainSignal.emit(lambda: w.setAttribute(Qt.WA_NoSystemBackground, True))
         
        def makeclockRegiesterMouseClicks(self):
            if self.isIgnoringClicks:
                self.isIgnoringClicks = False
                print("🟡 Stop ignoring mouse events")
                for w in (self, self.label, self.desktopButton, self.backgroundTexture):
                    self.callInMainSignal.emit(lambda: w.setAttribute(Qt.WA_TransparentForMouseEvents, False))
            
        def updateTextLoop(self) -> None:
            self.callInMainSignal.emit(lambda: self.label.setText("00:00 AM\n00/00/0000"))
            SHOULD_FIX_SECONDS = not(getSettings("UseCustomFont")) and not(lang["locale"] in ("zh_CN", "zh_TW"))
            HAIRSEC_VAR = " " if SHOULD_FIX_SECONDS else ""
            LOW_CPU_MODE = getSettings("EnableLowCpuMode")            
            if self.isCover:
                return
            
            while True:
                try:
                    timeStr = evaluate_expression_string(datetime.datetime.fromtimestamp(time.time()-self.internetTimeOffset).strftime(self.clockFormat.replace("\u200a", "hairsec")).replace("hairsec", HAIRSEC_VAR))
                    if SHOULD_FIX_SECONDS:
                        try:
                            secs = datetime.datetime.fromtimestamp(time.time()-self.internetTimeOffset).strftime("%S")
                            if secs[-1] == "1" and SHOULD_FIX_SECONDS:
                                timeStr = timeStr.replace(" ", " \u200e")
                            else:
                                timeStr = timeStr.replace(" ", "")
                        except IndexError as e:
                            pass
                except ValueError as e:
                    timeStr = "Invalid time format\nPlease modify it\nin the settings"
                self.callInMainSignal.emit(lambda: self.label.setText(timeStr))
                time.sleep(0.1 if LOW_CPU_MODE else 0.25)

        def singleClickAction(self):
            if not self.isCover:
                self.doClickAction(self.clickAction)
                try:
                    if self.hideClockWhenClicked:
                        print("🟡 Hiding clock because clicked!")
                        self.clockShouldBeHidden = True

                        def showClockOn10s(self: Clock):
                            time.sleep(10)
                            print("🟢 Showing clock because 10s passed!")
                            self.clockShouldBeHidden = False

                        KillableThread(target=showClockOn10s, args=(self,), name=f"Temporary: 10s thread").start()
                except Exception as e:
                    report(e)

        def doDoubleClickAction(self):
            if not self.isCover:
                self.doClickAction(self.doubleClickAction)

        def doMiddleClickAction(self):
            if not self.isCover:
                self.doClickAction(self.middleClickAction)

        def doClickAction(self, actions):
            if self.isIgnoringClicks:
                print("🟡 User is ignoring mouse events")
            else:
                print("Action:", actions)
                try:
                    match len(actions):
                        case 1:
                            if actions[0] == "trashcan":
                                winshell.recycle_bin().empty(confirm=True, show_progress=True, sound=True)
                            elif actions[0] == "trashcan_noconfirm":
                                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                            elif actions[0] == "copy_datetime":
                                textToClipboard(self.label.text())
                            else:
                                keyboard.press_and_release(actions[0].lower().replace("altright", "alt gr"))
                        case 2:
                            keyboard.press_and_release("+".join(actions[0:2]).lower().replace("altright", "alt gr"))

                        case 3:
                            keyboard.press_and_release("+".join(actions[0:3]).lower().replace("altright", "alt gr"))
                except Exception as e:
                    report(e)

        def showDesktop(self):
            keyboard.press_and_release("Win+d")

        def focusOutEvent(self, event: QFocusEvent) -> None:
            self.refresh.emit()

        def refreshAndShow(self):
            if(self.shouldBeVisible):
                self.show()
                self.raise_()
                if not self.isCover:
                    if(self.lastTheme >= 0): # If the color is not customized
                        theme = readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "SystemUsesLightTheme", 1)
                        if(theme != self.lastTheme):
                            self.callInMainSignal.emit(restartClocks)

        def close(self) -> bool:
            self.clockShouldBeHidden = True
            try:
                self.TextUpdaterLoop.kill()
                self.MainLoop.kill()
                self.InternetTimeLoop.kill()
            except AttributeError:
                pass
            try:
                self.rightFast.stop()
                self.rightSlow.stop()
                self.leftFast.stop()
                self.leftSlow.stop()
                for signal in (self.rightFast.finished, self.rightFast.valueChanged, self.rightSlow.finished, self.rightSlow.valueChanged, self.leftFast.finished, self.leftFast.valueChanged, self.leftSlow.finished, self.leftSlow.valueChanged):
                    try:
                        signal.disconnect()
                    except RuntimeError:
                        print("🟠 Can't disconnect signal!")
            except AttributeError:
                pass
            try:
                for widget in (self.clockCover, self.tooltip, self.label):
                    try:
                        widget.setAttribute(Qt.WA_DeleteOnClose, True) 
                        widget.deleteLater()
                        widget.close()
                    except AttributeError:
                        pass
                    except Exception as e:
                        report(e)
            except AttributeError:
                pass
            self.setAttribute(Qt.WA_DeleteOnClose, True) 
            self.deleteLater()
            self.destroy(True, True)
            return super().close()

        def resizeEvent(self, event: QResizeEvent = None):
            try:
                self.progressbar.move(self.label.x(), self.height()-self.progressbar.height()-2)
                self.progressbar.setFixedWidth(self.label.width())
                self.colorWidget.setGeometry(self.label.geometry())
                self.backgroundTexture.setGeometry(self.colorWidget.geometry())
                if self.desktopButton:
                    if self.clockOnTheLeft:
                        self.desktopButton.move(0, 0)
                    else:
                        self.desktopButton.move(self.width()-self.desktopButton.width(), 0)
                    self.desktopButton.setFixedSize(self.desktopButton.width(), self.height())
            except Exception as e:
                report(e)
            if event:
                return super().resizeEvent(event)

        def loadInternetTimeOffset(self):
            while True:
                if self.getSettings("EnableInternetTime"): # This settings value will be cached, so no CPU/HDD overload ;)
                    try:
                        dict = json.loads(urlopen(self.getSettingsValue("AtomicClockURL") if self.getSettingsValue("AtomicClockURL") else "http://worldtimeapi.org/api/ip").read().decode("utf-8"))
                        if "datetime" in dict.keys(): # worldtimeapi.org
                            self.internetTimeOffset = time.time()-datetime.datetime.fromisoformat(f'{"-" if not "+" in dict["datetime"] else "+"}'.join(dict["datetime"].split("-" if not "+" in dict["datetime"] else "+")[0:-1])).timestamp()
                            print("🔵 (worldtimeapi.org) Time offset set to", self.internetTimeOffset)
                        elif "currentDateTime" in dict.keys(): # worldclockapi.com
                            self.internetTimeOffset = time.time()-datetime.datetime.fromisoformat(f'{"-" if not "+" in dict["currentDateTime"] else "+"}'.join(dict["currentDateTime"].split("-" if not "+" in dict["currentDateTime"] else "+")[0:-1])).timestamp()
                            print("🔵 (worldclockapi.com) Time offset set to", self.internetTimeOffset)
                        else:
                            print("🟠 (Failed) Time offset set to", self.internetTimeOffset)
                            showNotif.infoSignal.emit("Invalid Internet clock URL", "Supported internet clock APIs are from worldtimeapi.com and worldclockapi.com")
                    except Exception as e:
                        report(e)
                    for i in range(getint(self.getSettingsValue("AtomicClockSyncInterval"), 3600)):
                        time.sleep(1)
                        if getSettings("ReloadInternetTime"):
                            setSettings("ReloadInternetTime", False, thread=True)
                            break
                else:
                    self.internetTimeOffset = 0
                    time.sleep(5)

        def setSettings(self, s: str, v: bool, r: bool = True, thread = False):
            setSettings(s, v, r, thread, env=self.settingsEnvironment)
            
        def setSettingsValue(self, s: str, v: bool, r: bool = True):
            setSettingsValue(s, v, r, env=self.settingsEnvironment)
            
        def getSettings(self, s: str):
            return getSettings(s, env=self.settingsEnvironment)
        
        def getSettingsValue(self, s: str):
            return getSettingsValue(s, env=self.settingsEnvironment)
        
        def enterEvent(self, event):
            if self.getSettings("HideClockWhenHovered"):
                print("🟡 Hiding clock because clicked!")
                self.clockShouldBeHidden = True

                def showClockOn10s(self: Clock):
                    time.sleep(5)
                    print("🟢 Showing clock because 5s passed!")
                    self.clockShouldBeHidden = False

                KillableThread(target=showClockOn10s, args=(self,), name=f"Temporary: 5s thread").start()

            super().enterEvent(event)
        
        

    class Label(QLabel):
        clicked = Signal()
        doubleClicked = Signal()
        middleClicked = Signal()
        outline = True
        def __init__(self, text, parent, isCover: bool = False, settingsEnvironment: str = ""):
            self.settingsEnvironment = settingsEnvironment
            super().__init__(text, parent=parent)
            self.isCover = isCover
            try:
                self.specifiedMinimumWidth = int(getSettingsValue("ClockFixedWidth", env=self.settingsEnvironment))
            except ValueError:
                self.specifiedMinimumWidth = 0
            except Exception as e:
                self.specifiedMinimumWidth = 0
                report(e)

            self.mouseButtonTimer = QTimer()
            self.mouseButtonTimer.setSingleShot(True)
            self.mouseButtonTimer.setInterval((300 if getSettings("DoubleClickLongerPeriod") else 150) if getSettings("CustomClockDoubleClickAction", env=self.settingsEnvironment) else 0)
            self.mouseButtonTimer.timeout.connect(self.mouseButtonTimeout)

            self.isMouseButtonDouble = False
            self.isMouseButtonReleased = False
            self.isMouseButtonLeftClick = True

            self.setMouseTracking(True)
            self.backgroundwidget = QWidget(self)
            self.color = "255, 255, 255"
            self.sidesColor = "0, 0, 0" if isTaskbarDark() else "200,200,200"
            QGuiApplication.instance().installEventFilter(self)
            self.bgopacity = 0.2
            self.backgroundwidget.setContentsMargins(0, self.window().prefMargins, 0, self.window().prefMargins)
            self.backgroundwidget.setStyleSheet(f"background-color: rgba(127, 127, 127, 0.0);border: 1px solid rgba({self.sidesColor},0);border-top: 1px solid rgba({self.color},0);margin-top: {self.window().prefMargins}px; margin-bottom: {self.window().prefMargins};")
            self.backgroundwidget.show()
            self.showBackground = QVariantAnimation()
            self.showBackground.setStartValue(0)
            self.showBackground.setEndValue(self.bgopacity)
            self.showBackground.setDuration(100)
            self.showBackground.setEasingCurve(QEasingCurve.InOutQuad) # Not strictly required, just for the aesthetics
            self.showBackground.valueChanged.connect(lambda opacity: self.backgroundwidget.setStyleSheet(f"background-color: rgba({self.color}, {opacity/1.5});border: 1px solid rgba({self.sidesColor}, {opacity});border-top: 1px solid rgba({self.color}, {opacity});margin-top: {self.window().prefMargins}px; margin-bottom: {self.window().prefMargins};padding-bottom: 6px;"))
            self.hideBackground = QVariantAnimation()
            self.hideBackground.setStartValue(self.bgopacity)
            self.hideBackground.setEndValue(0)
            self.hideBackground.setDuration(100)
            self.hideBackground.setEasingCurve(QEasingCurve.InOutQuad) # Not strictly required, just for the aesthetics
            self.hideBackground.valueChanged.connect(lambda opacity: self.backgroundwidget.setStyleSheet(f"background-color: rgba({self.color}, {opacity/1.5});border-top: 1px solid rgba({self.color}, {opacity});margin-top: {self.window().prefMargins}px; margin-bottom: {self.window().prefMargins};padding-bottom: 6px;"))
            self.setAutoFillBackground(True)
            self.backgroundwidget.setGeometry(0, 0, self.width(), self.height()-2)

            self.opacity=QGraphicsOpacityEffect(self)
            self.opacity.setOpacity(1.00)
            self.backgroundwidget.setGraphicsEffect(self.opacity)

            self.focusassitant = True
            self.focusAssitantLabel = QPushButton(self)
            self.focusAssitantLabel.move(self.width(), -1)
            self.focusAssitantLabel.setAttribute(Qt.WA_TransparentForMouseEvents)
            self.focusAssitantLabel.setStyleSheet("background: transparent; margin: none; padding: none;")
            self.focusAssitantLabel.resize(30, self.height())
            if winver < 22581:
                self.focusAssitantLabel.setIcon(QIcon(getPath(f"moon_{getTaskbarIconMode()}.png")))
            else:
                if numOfNotifs == 0:
                    self.focusAssitantLabel.setIcon(QIcon(getPath(f"notif_assist_empty_{getTaskbarIconMode()}.png")))
                else:
                    self.focusAssitantLabel.setIcon(QIcon(getPath(f"notif_assist_filled_{getTaskbarIconMode()}.png")))
            self.focusAssitantLabel.setIconSize(QSize(16, 16))

            self.notifdot = True
            self.notifDotLabel = QLabel("", self)
            self.notifDotLabel.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            self.notifDotLabel.setObjectName("notifIndicator")
            self.notifDotLabel.setStyleSheet(f"font-size: 8pt;font-family: \"Segoe UI Variable Display\";border-radius: 8px;padding: 0;padding-bottom: 2px;padding-left: 3px;padding-right: 2px;margin: 0;border:0;")

            self.moonIconBlack = QIcon(getPath("moon_black.png"))
            self.moonIconWhite = QIcon(getPath("moon_white.png"))
            self.emptyBellBlack = QIcon(getPath("notif_assist_empty_black.png"))
            self.emptyBellWhite = QIcon(getPath("notif_assist_empty_white.png"))
            self.filledBellBlack = QIcon(getPath(f"notif_assist_filled_black.png"))
            self.filledBellWhite = QIcon(getPath(f"notif_assist_filled_white.png"))

            self.lastFocusAssistIcon = None

            self.disableClockIndicators()

        def enableFocusAssistant(self):
            if self.notifdot:
                self.disableClockIndicators()
                    
            if self.lastFocusAssistIcon != self.focusAssitantLabel.icon():
                if getSettings("DisableAutomaticTextColor", env=self.settingsEnvironment):
                    if winver < 22581:
                        self.focusAssitantLabel.setIcon(self.moonIconWhite if isTaskbarDark() else self.moonIconBlack)
                    else:
                        if numOfNotifs == 0:
                            self.focusAssitantLabel.setIcon(self.emptyBellWhite if isTaskbarDark() else self.emptyBellBlack)
                        else:
                            self.focusAssitantLabel.setIcon(self.filledBellWhite if isTaskbarDark() else self.filledBellBlack)
                else:
                    if winver < 22581:
                        self.focusAssitantLabel.setIcon(self.moonIconWhite if self.window().LastCapturedForegroundColor == "white" else self.moonIconBlack)
                    else:
                        if self.window().LastCapturedForegroundColor == "black":
                            self.focusAssitantLabel.setIcon(self.emptyBellBlack if numOfNotifs == 0 else self.filledBellBlack)
                        elif self.window().LastCapturedForegroundColor == "white":
                            self.focusAssitantLabel.setIcon(self.emptyBellWhite if numOfNotifs == 0 else self.filledBellWhite)
                        else:
                            self.focusAssitantLabel.setIcon(self.filledBellWhite if isTaskbarDark() else self.filledBellBlack)

            if not self.focusassitant:
                self.focusassitant = True
                self.setContentsMargins(5, 0, (43), 4)
                self.focusAssitantLabel.move(self.width()-self.contentsMargins().right(), -1)
                self.focusAssitantLabel.setFixedWidth(30)
                self.focusAssitantLabel.setFixedHeight(self.height())
                self.focusAssitantLabel.setIconSize(QSize(16, 16))
                if not self.isCover:
                    self.focusAssitantLabel.show()

        def enableNotifDot(self):
            if self.focusassitant:
                self.disableClockIndicators()
                
            self.notifDotLabel.setText(str(numOfNotifs))
            if not self.notifdot:
                self.notifdot = True
                self.setContentsMargins(5, 0, (43), 4)
                topBottomPadding = (self.height()-16)/2 # top-bottom margin
                leftRightPadding = (30-16)/2 # left-right margin
                self.notifDotLabel.move(int(self.width()-self.contentsMargins().right()+leftRightPadding), int(topBottomPadding)+-1)
                self.notifDotLabel.resize(16, 16)
                self.notifDotLabel.setStyleSheet(f"font-size: 8pt;font-family: \"Segoe UI Variable Display\";border-radius: 8px;padding: 0;padding-bottom: 2px;padding-left: 3px;padding-right: 2px;margin: 0;border:0;")
                if not self.isCover:
                    self.notifDotLabel.show()

        def disableClockIndicators(self):
            if self.focusassitant:
                self.focusassitant = False
                self.setContentsMargins(6, 0, 13, 4)
                self.focusAssitantLabel.hide()
            if self.notifdot:
                self.notifdot = False
                self.setContentsMargins(6, 0, 13, 4)
                self.notifDotLabel.hide()

        def get6px(self, i: int) -> int:
            return round(i*self.screen().devicePixelRatio())

        def enterEvent(self, event: QEvent, r=False) -> None:
            if not self.isCover:
                geometry: QRect = self.width()
                self.showBackground.setStartValue(.01)
                self.showBackground.setEndValue(self.bgopacity) # Not 0 to prevent white flashing on the border
                if not self.window().clockOnTheLeft:
                    self.backgroundwidget.move(0, 1)
                    self.backgroundwidget.resize(geometry, self.height()-3)
                else:
                    self.backgroundwidget.move(0, 1)
                    self.backgroundwidget.resize(geometry, self.height()-3)
                self.showBackground.start()
                if not r:
                    self.enterEvent(event, r=True)
                self.window().updateToolTipStatus(True)
                return super().enterEvent(event)

        def leaveEvent(self, event: QEvent) -> None:
            if not self.isCover: 
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

        def eventFilter(self, obj, event):
            if obj == self:
                match event.type():
                    case QEvent.MouseButtonPress:
                        self.isMouseButtonReleased = False
                        self.isMouseButtonLeftClick = False
                        self.isMouseButtonDouble = False
                        if not self.mouseButtonTimer.isActive():
                            self.mouseButtonTimer.start()
                        if event.button() == Qt.LeftButton:
                            self.isMouseButtonLeftClick = True
                    case QEvent.MouseButtonRelease:
                        if not self.isMouseButtonDouble and not self.mouseButtonTimer.isActive():
                            if event.button() == Qt.MiddleButton:
                                self.middleClicked.emit()
                            else:
                                self.mouseButtonTimer.start()
                        self.isMouseButtonReleased = True
                    case QEvent.MouseButtonDblClick:
                        self.isMouseButtonDouble = True
                        return True
            return False

        def mouseButtonTimeout(self):
            if self.isMouseButtonDouble:
                self.doubleClicked.emit()
                self.mouseButtonTimer.stop()
            if self.isMouseButtonReleased:
                if self.isMouseButtonLeftClick:
                    if self.isMouseButtonDouble:
                        pass # The clock was double-clicked
                    else:
                        self.clicked.emit()
                else:
                    i.showMenu(self.window())

        def mousePressEvent(self, ev: QMouseEvent) -> None:
            if not self.isCover:
                self.setWindowOpacity(0.7)
                self.opacity.setOpacity(0.60)
                self.backgroundwidget.setGraphicsEffect(self.opacity)
                return super().mousePressEvent(ev)

        def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
            if not self.isCover:
                self.setWindowOpacity(1)
                self.opacity.setOpacity(1)
                self.backgroundwidget.setGraphicsEffect(self.opacity)
                return super().mouseReleaseEvent(ev)

        def paintEvent(self, event: QPaintEvent) -> None:
            if self.specifiedMinimumWidth > 0:
                w = self.specifiedMinimumWidth
            else:
                w = self.minimumSizeHint().width()
            if w<(self.window().preferedwidth) and not self.window().clockOnTheLeft:
                self.move((self.window().preferedwidth)-w+2, 0)
                self.resize(w, self.height()-1)
            else:
                self.move(6, 0)
                self.resize(w, self.height()-1)
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
    timeOffset = 0

    if "zh" in langName:
        sys.argv.append("-platform")
        sys.argv.append("windows:fontengine=freetype")
    if not QApplication.instance():
        translator = QTranslator()
        translator.load(f"qtbase_{langName}.qm", QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath))
        app = QApplication(sys.argv)
        app.installTranslator(translator)
    else:
        app = QApplication.instance()
    app.setQuitOnLastWindowClosed(False)

    sw: SettingsWindow = None
    i: TaskbarIconTray = None
    st: KillableThread = None # Will be defined on loadClocks
    shouldFixSeconds = not(getSettings("UseCustomFont")) and not(lang["locale"] in ("zh_CN", "zh_TW"))

    KillableThread(target=resetRestartCount, daemon=True, name="Main: Restart counter").start()
    KillableThread(target=screenCheckThread, daemon=True, name="Main [not from start]: Screen listener")

    loadClocks()

    print(f"🟢 Loaded clocks in {time.time()-FirstTime}")

    tdir = tempfile.TemporaryDirectory()
    tempDir = tdir.name
    sw = SettingsWindow() # Declare settings window
    i = TaskbarIconTray(app)
    #mController = MouseController()
    
    if(getSettings("DisableSystemTray") and len(globals.clocks)>0):
        i.hide()
    else:
        i.show()

    app.primaryScreenChanged.connect(lambda: (os.startfile(sys.executable), app.quit()))
    app.screenAdded.connect(lambda: (os.startfile(sys.executable), app.quit()))
    app.screenRemoved.connect(lambda: (os.startfile(sys.executable), app.quit()))
    signal = RestartSignal()
    showNotif = InfoSignal()
    showWarn = InfoSignal()
    killSignal = InfoSignal()
    restartClocksSignal = RestartSignal()
    showNotif.infoSignal.connect(lambda a, b: showMessage(a, b))
    showWarn.infoSignal.connect(lambda a, b: wanrUserAboutUpdates(a, b))
    killSignal.infoSignal.connect(lambda: app.quit())
    signal.restartSignal.connect(lambda: restartClocks("checkLoop"))
    restartClocksSignal.restartSignal.connect(lambda: restartClocks())

    KillableThread(target=updateChecker, daemon=True, name="Main: Updater").start()
    KillableThread(target=isElevenClockRunningThread, daemon=True, name="Main: Instance controller").start()
    if getSettings("PreventSleepFailure"):
        KillableThread(target=checkIfWokeUpThread, daemon=True, name="Main: Sleep listener").start()
    if not getSettings("EnableLowCpuMode"): KillableThread(target=wnfDataThread, daemon=True, name="Main: WNF Data listener").start()
    print("🔵 Low cpu mode is set to", str(getSettings("EnableLowCpuMode"))+". DisableNotifications is set to", getSettings("DisableNotifications"))


    globals.tempDir = tempDir # Register global variables
    globals.old_stdout = old_stdout # Register global variables
    globals.buffer = buffer # Register global variables
    globals.app = app # Register global variables
    globals.sw = sw # Register global variables
    globals.trayIcon = i # Register global variables
    globals.updateIfPossible = updateIfPossible # Register global functions
    globals.restartClocks = restartClocks # Register global functions
    globals.closeClocks = closeClocks  # Register global functions

    if not(getSettings(f"Updated{versionName}Already")) and not(getSettings("EnableSilentUpdates")):
        setSettings(f"Updated{versionName}Already", True, False)
        if versionName == "4.0.1":
            if not getSettings("AtomicClockURL"):
                setSettings("EnableInternetTime", False)
        if getSettings("DefaultPrefsLoaded"):
            showMessage(_("ElevenClock Updater"), _("ElevenClock has updated to version {0} successfully\nPlease see GitHub for the changelog").format(versionName), False)

    showSettings = False
    if "--settings" in sys.argv or showSettings:
        sw.show()

    if getSettings("DefaultPrefsLoaded") and not getSettings("NewWizardLaunchingMechanism"):
        setSettings("AlreadyDoneWelcomeWizard", True)

    if not getSettings("DefaultPrefsLoaded"):
        setSettings("AlreadyInstalled", True)
        setSettings("NewWizardLaunchingMechanism", True)
        setSettings("NewFullScreenMethod", True)
        setSettings("ForceClockOnfirstMonitor", True)
        showMessage("Welcome to ElevenClock", "You can customize ElevenClock from the ElevenClock Settings. You can search them on the start menu or right-clicking on any clock -> ElevenClock Settings", uBtn=False)
        print("🟢 Default settings loaded")
        setSettings("DefaultPrefsLoaded", True)
        
    if not getSettings("AlreadyDoneWelcomeWizard"):
        import welcome
        ww = welcome.WelcomeWindow()
        globals.ww = ww

    showWelcomeWizard = False
    if showWelcomeWizard or "--welcome" in sys.argv:
        import welcome
        ww = welcome.WelcomeWindow()
        globals.ww = ww

    print(f"🟢 Loaded everything in {time.time()-FirstTime}")

    if "--quit-on-loaded" in sys.argv: # This is a testing feature to test if the script can load successfully
        app.quit()
    app.exec()
    app.quit()

except FileNotFoundError as e:
    sys.exit(402)
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
    webbrowser.open(("https://www.marticliment.com/error-report/?appName=ElevenClock&errorBody="+os_info.replace('\n', '{l}').replace(' ', '{s}')+"{l}{l}{l}{l}ElevenClock Log:{l}"+str("\n\n\n\n"+traceback_info).replace('\n', '{l}').replace(' ', '{s}')).replace("#", "|=|"))
    print(traceback_info)

