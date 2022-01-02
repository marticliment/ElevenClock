import platform
import subprocess
import os
import sys
import locale
import time
from PySide2 import QtGui
from PySide2 import QtCore

import psutil
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

import globals
from pymica import ApplyMica

from languages import * 
from tools import *
from tools import _
import welcome

from external.FramelessWindow import QFramelessWindow, QFramelessDialog

class SettingsWindow(QFramelessWindow):
    def __init__(self):
        super().__init__()
        self.scrollArea = QScrollArea()
        self.vlayout = QVBoxLayout()
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        """
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)"""
        self.vlayout.setMargin(0)
        self.vlayout.setSpacing(0)
        layout = QVBoxLayout()
        self.updateSize = True
        self.scrollArea.setWidgetResizable(True)
        self.setObjectName("backgroundWindow")
        self.settingsWidget = QWidget()
        self.settingsWidget.setObjectName("background")
        self.setWindowIcon(QIcon(getPath("icon.ico")))
        layout.addSpacing(0)
        title = QLabel(_("ElevenClock Settings"))
        title.setObjectName("title")
        if lang == lang_zh_TW or lang == lang_zh_CN:
            title.setStyleSheet("font-size: 25pt;font-family: \"Microsoft JhengHei UI\";font-weight: 450;")
        else:
            title.setStyleSheet("font-size: 25pt;font-family: \"Segoe UI Variable Text\";font-weight: 450;")
        layout.addWidget(title)
        layout.setSpacing(5)
        layout.setContentsMargins(10, 0, 0, 0)
        layout.addSpacing(0)
        self.resize(900, 600)
        self.setMinimumWidth(520)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        if(readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "AppsUseLightTheme", 1)==0):
            self.iconMode = "white"
        else:
            self.iconMode = "black"

        self.generalSettingsTitle = QIconLabel(_("General Settings:"), getPath(f"settings_{self.iconMode}.png"), _("Updates, icon tray, language"))
        layout.addWidget(self.generalSettingsTitle)
        self.updateButton = QSettingsButton(_("<b>Update to the latest version!</b>"), _("Install update"))
        self.updateButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;border-bottom: 0px;}")
        self.updateButton.clicked.connect(lambda: KillableThread(target=globals.updateIfPossible, args=((True,))).start())
        self.updateButton.hide()
        self.generalSettingsTitle.addWidget(self.updateButton)
        self.selectedLanguage = QSettingsComboBox(_("ElevenClock's language")+" (Language)", _("Change")) #The non-translated (Language) string is there to know what the language option is if you accidentaly change the language
        self.selectedLanguage.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;border-bottom: 0px;}")
        try:
            self.selectedLanguage.setItems(list(languageReference.values()), list(languageReference.keys()).index(langName))
        except Exception as e:
            report(e)
            self.selectedLanguage.setItems(list(languageReference.values()), 0)

        def changeLang(text):
            keys = list(languageReference.keys())
            values = list(languageReference.values())
            for i in range(len(values)):
                if(text == values[i]):
                    setSettingsValue("PreferredLanguage", str(keys[i]), r=False)
                    self.selectedLanguage.showRestartButton()

        def restartElevenClockByLangChange():
            subprocess.run(str("start /B \"\" \""+sys.executable)+"\" --settings", shell=True)
            globals.app.quit()

        self.selectedLanguage.restartButton.clicked.connect(restartElevenClockByLangChange)
        self.selectedLanguage.textChanged.connect(changeLang)
        self.generalSettingsTitle.addWidget(self.selectedLanguage)
        self.enableUpdates = QSettingsCheckBox(_("Automatically check for updates"))
        self.enableUpdates.setChecked(not getSettings("DisableAutoCheckForUpdates"))
        self.enableUpdates.stateChanged.connect(lambda i: setSettings("DisableAutoCheckForUpdates", not bool(i), r = False))
        self.generalSettingsTitle.addWidget(self.enableUpdates)
        self.installUpdates = QSettingsCheckBox(_("Automatically install available updates"))
        self.installUpdates.setChecked(not getSettings("DisableAutoInstallUpdates"))
        self.installUpdates.stateChanged.connect(lambda i: setSettings("DisableAutoInstallUpdates", not bool(i), r = False))
        self.generalSettingsTitle.addWidget(self.installUpdates)
        self.silentUpdates = QSettingsCheckBox(_("Enable really silent updates"))
        self.silentUpdates.setChecked(getSettings("EnableSilentUpdates"))
        self.silentUpdates.stateChanged.connect(lambda i: setSettings("EnableSilentUpdates", bool(i), r = False))
        self.generalSettingsTitle.addWidget(self.silentUpdates)
        self.bypassCNAMECheck = QSettingsCheckBox(_("Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"))
        self.bypassCNAMECheck.setChecked(getSettings("BypassDomainAuthCheck"))
        self.bypassCNAMECheck.stateChanged.connect(lambda i: setSettings("BypassDomainAuthCheck", bool(i), r = False))
        self.generalSettingsTitle.addWidget(self.bypassCNAMECheck)
        self.enableSystemTray = QSettingsCheckBox(_("Show ElevenClock on system tray"))
        self.enableSystemTray.setChecked(not getSettings("DisableSystemTray"))
        self.enableSystemTray.stateChanged.connect(lambda i: setSettings("DisableSystemTray", not bool(i)))
        self.generalSettingsTitle.addWidget(self.enableSystemTray)
        self.disableTaskMgr = QSettingsCheckBox(_("Hide extended options from the clock right-click menu (needs a restart to be aplied)"))
        self.disableTaskMgr.setChecked(getSettings("HideTaskManagerButton"))
        self.disableTaskMgr.stateChanged.connect(lambda i: setSettings("HideTaskManagerButton", bool(i)))
        self.generalSettingsTitle.addWidget(self.disableTaskMgr)
        self.startupButton = QSettingsButton(_("Change startup behaviour"), _("Change"))
        self.startupButton.clicked.connect(lambda: os.startfile("ms-settings:startupapps"))
        self.generalSettingsTitle.addWidget(self.startupButton)


        self.clockSettingsTitle = QIconLabel(_("Clock Settings:"), getPath(f"clock_{self.iconMode}.png"), _("Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings"))
        layout.addWidget(self.clockSettingsTitle)
        self.legacyHideOnFullScreen = QSettingsCheckBox(_("Hide the clock in fullscreen mode"))
        self.legacyHideOnFullScreen.setChecked(not getSettings("DisableHideOnFullScreen"))
        self.legacyHideOnFullScreen.stateChanged.connect(lambda i: setSettings("DisableHideOnFullScreen", not bool(i)))
        self.clockSettingsTitle.addWidget(self.legacyHideOnFullScreen)
        self.newFullScreenHide = QSettingsCheckBox(_("Hide the clock when a program occupies all screens"))
        self.newFullScreenHide.setChecked(getSettings("NewFullScreenMethod"))
        self.newFullScreenHide.stateChanged.connect(lambda i: setSettings("NewFullScreenMethod", bool(i)))
        self.clockSettingsTitle.addWidget(self.newFullScreenHide)
        self.legacyRDPHide = QSettingsCheckBox(_("Hide the clock when RDP Client or Citrix Workspace are running")+" (Old method)".replace("RDP", "RDP, VMWare Horizon"))
        self.legacyRDPHide.setChecked(getSettings("EnableHideOnRDP"))
        self.legacyRDPHide.stateChanged.connect(lambda i: setSettings("EnableHideOnRDP", bool(i)))
        self.clockSettingsTitle.addWidget(self.legacyRDPHide)
        self.forceClockToShow = QSettingsCheckBox(_("Show the clock when the taskbar is set to hide automatically"))
        self.forceClockToShow.setChecked(getSettings("DisableHideWithTaskbar"))
        self.forceClockToShow.stateChanged.connect(lambda i: setSettings("DisableHideWithTaskbar", bool(i)))
        self.clockSettingsTitle.addWidget(self.forceClockToShow)
        self.showDesktopButton = QSettingsCheckBox(_("Add the \"Show Desktop\" button on the left corner of every clock"))
        self.showDesktopButton.setChecked(getSettings("ShowDesktopButton"))
        self.showDesktopButton.stateChanged.connect(lambda i: setSettings("ShowDesktopButton", bool(i)))
        self.primaryScreen = QSettingsCheckBox(_("Show the clock on the primary screen"))
        self.primaryScreen.setChecked(getSettings("ForceClockOnFirstMonitor"))
        self.primaryScreen.stateChanged.connect(lambda i: setSettings("ForceClockOnFirstMonitor", bool(i)))
        self.clockSettingsTitle.addWidget(self.primaryScreen)
        self.onlyPrimaryScreen = QSettingsCheckBox(_("Do not show the clock on secondary monitors"))
        self.onlyPrimaryScreen.setChecked(getSettings("HideClockOnSecondaryMonitors"))
        self.onlyPrimaryScreen.stateChanged.connect(lambda i: setSettings("HideClockOnSecondaryMonitors", bool(i)))
        self.clockSettingsTitle.addWidget(self.onlyPrimaryScreen)
        self.hideClockWhenClicked = QSettingsCheckBox(_("Hide the clock during 10 seconds when clicked"))
        self.hideClockWhenClicked.setChecked(getSettings("HideClockWhenClicked"))
        self.hideClockWhenClicked.stateChanged.connect(lambda i: setSettings("HideClockWhenClicked", bool(i)))
        self.clockSettingsTitle.addWidget(self.hideClockWhenClicked)
        self.enableLowCpuMode = QSettingsCheckBoxWithWarning(_("Enable low-cpu mode"), _("You might lose functionalities, like the notification counter or the dynamic background"))
        self.enableLowCpuMode.setStyleSheet(f"QWidget#stChkBg{{border-bottom-left-radius: {self.getPx(6)}px;border-bottom-right-radius: {self.getPx(6)}px;border-bottom: 1px;}}")
        self.enableLowCpuMode.setChecked(getSettings("EnableLowCpuMode"))
        self.enableLowCpuMode.stateChanged.connect(lambda i: setSettings("EnableLowCpuMode", bool(i)))
        self.clockSettingsTitle.addWidget(self.enableLowCpuMode)

        self.clockPosTitle = QIconLabel(_("Clock position and size:"), getPath(f"size_{self.iconMode}.png"), _("Clock size preferences, position offset, clock at the left, etc."))
        layout.addWidget(self.clockPosTitle)
        self.clockPosTitle.addWidget(self.showDesktopButton)
        self.clockAtLeft = QSettingsCheckBox(_("Show the clock at the left of the screen"))
        self.clockAtLeft.setChecked(getSettings("ClockOnTheLeft"))
        self.clockAtLeft.stateChanged.connect(lambda i: setSettings("ClockOnTheLeft", bool(i)))
        self.clockPosTitle.addWidget(self.clockAtLeft)
        self.clockAtBottom = QSettingsCheckBox(_("Force the clock to be at the bottom of the screen"))
        self.clockAtBottom.setChecked(getSettings("ForceOnBottom"))
        self.clockAtBottom.stateChanged.connect(lambda i: setSettings("ForceOnBottom", bool(i)))
        self.clockPosTitle.addWidget(self.clockAtBottom)
        self.clockAtTop = QSettingsCheckBox(_("Force the clock to be at the top of the screen"))
        self.clockAtTop.setChecked(getSettings("ForceOnTop"))
        self.clockAtTop.setStyleSheet(f"QWidget#stChkBg{{border-bottom-left-radius: {self.getPx(6)}px;border-bottom-right-radius: {self.getPx(6)}px;border-bottom: 1px;}}")
        self.clockAtTop.stateChanged.connect(lambda i: setSettings("ForceOnTop", bool(i)))
        self.clockPosTitle.addWidget(self.clockAtTop)

        def unblacklist():
            global msg
            setSettingsValue("BlacklistedMonitors", "")
            globals.restartClocks()
            msg = QFramelessDialog(parent=self, closeOnClick=True)
            msg.setAutoFillBackground(True)
            msg.setStyleSheet(globals.sw.styleSheet())
            msg.setAttribute(Qt.WA_StyledBackground)
            msg.setObjectName("QMessageBox")
            msg.setTitle(_("Success"))
            msg.setText(f"""{_("The monitors were unblacklisted successfully.")}<br>
    {_("Now you should see the clock everywhere")}""")
            msg.addButton(_("Ok"), QDialogButtonBox.ButtonRole.ApplyRole)
            msg.setDefaultButtonRole(QDialogButtonBox.ButtonRole.ApplyRole, self.styleSheet())
            msg.show()

        self.unBlackListButton = QSettingsButton(_("Reset monitor blacklisting status"), _("Reset"))
        self.unBlackListButton.clicked.connect(unblacklist)
        self.clockPosTitle.addWidget(self.unBlackListButton)

        self.clockAppearanceTitle = QIconLabel(_("Clock Appearance:"), getPath(f"appearance_{self.iconMode}.png"), _("Clock's font, font size, font color and background, text alignment"))
        layout.addWidget(self.clockAppearanceTitle)
        self.fontPrefs = QSettingsFontBoxComboBox(_("Use a custom font"))
        self.fontPrefs.setChecked(getSettings("UseCustomFont"))
        if self.fontPrefs.isChecked():
            customFont = getSettingsValue("UseCustomFont")
            if customFont:
                self.fontPrefs.combobox.setCurrentText(customFont)
                self.fontPrefs.combobox.lineEdit().setFont(QFont(customFont))
        else:
            if lang == lang_ko:
                self.fontPrefs.combobox.setCurrentText("Malgun Gothic")
            elif lang == lang_zh_TW or lang == lang_zh_CN:
                self.fontPrefs.combobox.setCurrentText("Microsoft JhengHei UI")
            else:
                self.fontPrefs.combobox.setCurrentText("Segoe UI Variable Display")
        self.fontPrefs.stateChanged.connect(lambda i: setSettings("UseCustomFont", bool(i)))
        self.fontPrefs.valueChanged.connect(lambda v: setSettingsValue("UseCustomFont", v))
        self.clockAppearanceTitle.addWidget(self.fontPrefs)
        
        self.fontSize = QSettingsSizeBoxComboBox(_("Use a custom font size"))
        self.fontSize.setChecked(getSettings("UseCustomFontSize"))
        self.fontSize.loadItems()
        if self.fontSize.isChecked():
            customFontSize = getSettingsValue("UseCustomFontSize")
            if customFontSize:
                self.fontSize.combobox.setCurrentText(customFontSize)
        else:
                self.fontSize.combobox.setCurrentText("9")
        self.fontSize.stateChanged.connect(lambda i: setSettings("UseCustomFontSize", bool(i)))
        self.fontSize.valueChanged.connect(lambda v: setSettingsValue("UseCustomFontSize", v))
        self.clockAppearanceTitle.addWidget(self.fontSize)
        
        self.fontColor = QSettingsSizeBoxColorDialog(_("Use a custom font color"))
        self.fontColor.setChecked(getSettings("UseCustomFontColor"))
        if self.fontColor.isChecked():
            self.fontColor.button.setStyleSheet(f"color: rgb({getSettingsValue('UseCustomFontColor')})")
        self.fontColor.stateChanged.connect(lambda i: setSettings("UseCustomFontColor", bool(i)))
        self.fontColor.valueChanged.connect(lambda v: setSettingsValue("UseCustomFontColor", v))
        self.clockAppearanceTitle.addWidget(self.fontColor)
        self.disableSystemTrayColor = QSettingsCheckBox(_("Disable clock taskbar background color (make clock transparent)"))
        self.disableSystemTrayColor.setChecked(getSettings("DisableTaskbarBackgroundColor"))
        self.disableSystemTrayColor.stateChanged.connect(lambda i: setSettings("DisableTaskbarBackgroundColor", bool(i)))
        self.clockAppearanceTitle.addWidget(self.disableSystemTrayColor)
        self.backgroundcolor = QSettingsBgBoxColorDialog(_("Use a custom background color"))
        self.backgroundcolor.setChecked(getSettings("UseCustomBgColor"))
        self.backgroundcolor.colorDialog.setOption(QColorDialog.ShowAlphaChannel, True)
        if self.backgroundcolor.isChecked():
            self.backgroundcolor.button.setStyleSheet(f"background-color: rgba({getSettingsValue('UseCustomBgColor')})")
        self.backgroundcolor.stateChanged.connect(lambda i: setSettings("UseCustomBgColor", bool(i)))
        self.backgroundcolor.valueChanged.connect(lambda v: setSettingsValue("UseCustomBgColor", v))
        self.clockAppearanceTitle.addWidget(self.backgroundcolor)
        self.centerText = QSettingsCheckBox(_("Align the clock text to the center"))
        self.centerText.setChecked(getSettings("CenterAlignment"))
        self.centerText.setStyleSheet(f"QWidget#stChkBg{{border-bottom-left-radius: {self.getPx(6)}px;border-bottom-right-radius: {self.getPx(6)}px;border-bottom: 1px;}}")
        self.centerText.stateChanged.connect(lambda i: setSettings("CenterAlignment", bool(i)))
        self.clockAppearanceTitle.addWidget(self.centerText)


        self.dateTimeTitle = QIconLabel(_("Date & Time Settings:"), getPath(f"datetime_{self.iconMode}.png"), _("Date format, Time format, seconds,weekday, weeknumber, regional settings"))
        layout.addWidget(self.dateTimeTitle)
        self.showTime = QSettingsCheckBox(_("Show time on the clock"))
        self.showTime.setChecked(not getSettings("DisableTime"))
        self.showTime.stateChanged.connect(lambda i: setSettings("DisableTime", not bool(i), r = False))
        self.dateTimeTitle.addWidget(self.showTime)
        self.showSeconds = QSettingsCheckBox(_("Show seconds on the clock"))
        self.showSeconds.setChecked(getSettings("EnableSeconds"))
        self.showSeconds.stateChanged.connect(lambda i: setSettings("EnableSeconds", bool(i), r = False))
        self.dateTimeTitle.addWidget(self.showSeconds)
        self.showDate = QSettingsCheckBox(_("Show date on the clock"))
        self.showDate.setChecked(not getSettings("DisableDate"))
        self.showDate.stateChanged.connect(lambda i: setSettings("DisableDate", not bool(i), r = False))
        self.dateTimeTitle.addWidget(self.showDate)
        self.showWeekCount = QSettingsCheckBox(_("Show week number on the clock"))
        self.showWeekCount.setChecked(getSettings("EnableWeekNumber"))
        self.showWeekCount.stateChanged.connect(lambda i: setSettings("EnableWeekNumber", bool(i), r = False))
        self.dateTimeTitle.addWidget(self.showWeekCount)
        self.showWeekday = QSettingsCheckBox(_("Show weekday on the clock"))
        self.showWeekday.setChecked(getSettings("EnableWeekDay"))
        self.showWeekday.stateChanged.connect(lambda i: setSettings("EnableWeekDay", bool(i)))
        self.dateTimeTitle.addWidget(self.showWeekday)
        self.RegionButton = QSettingsButton(_("Change date and time format (Regional settings)"), _("Regional settings"))
        self.RegionButton.clicked.connect(lambda: os.startfile("intl.cpl"))
        self.dateTimeTitle.addWidget(self.RegionButton)

        
        self.experimentalTitle = QIconLabel(_("Fixes and other experimental features: (Use ONLY if something is not working)"), getPath(f"experiment_{self.iconMode}.png"), _("Testing features and error-fixing tools"))
        layout.addWidget(self.experimentalTitle)
        self.wizardButton = QSettingsButton(_("Open the welcome wizard")+_(" (ALPHA STAGE, MAY NOT WORK)"), _("Open"))
        
        def ww():
            global welcomewindow
            welcomewindow = welcome.WelcomeWindow()
        
        self.wizardButton.clicked.connect(ww)
        self.wizardButton.button.setObjectName("AccentButton")
        self.wizardButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;border-bottom: 0px;}")
        self.experimentalTitle.addWidget(self.wizardButton)
        self.fixDash = QSettingsCheckBox(_("Fix the hyphen/dash showing over the month"))
        self.fixDash.setChecked(getSettings("EnableHyphenFix"))
        self.fixDash.stateChanged.connect(lambda i: setSettings("EnableHyphenFix", bool(i)))
        self.experimentalTitle.addWidget(self.fixDash)
        self.fixSSL = QSettingsCheckBox(_("Alternative non-SSL update server (This might help with SSL errors)"))
        self.fixSSL.setChecked(getSettings("AlternativeUpdateServerProvider"))
        self.fixSSL.stateChanged.connect(lambda i: setSettings("AlternativeUpdateServerProvider", bool(i)))
        self.experimentalTitle.addWidget(self.fixSSL)
        self.win32alignment = QSettingsCheckBox(_("Alternative clock alignment (may not work)"))
        self.win32alignment.setChecked(getSettings("EnableWin32API"))
        self.win32alignment.setStyleSheet(f"QWidget#stChkBg{{border-bottom-left-radius: {self.getPx(6)}px;border-bottom-right-radius: {self.getPx(6)}px;border-bottom: 1px;}}")
        self.win32alignment.stateChanged.connect(lambda i: setSettings("EnableWin32API", bool(i)))
        self.experimentalTitle.addWidget(self.win32alignment)


        self.languageSettingsTitle = QIconLabel(_("About the language pack:"), getPath(f"lang_{self.iconMode}.png"), _("Language pack author(s), help translating ElevenClock"))
        layout.addWidget(self.languageSettingsTitle)
        self.PackInfoButton = QSettingsButton(_("Translated to English by martinet101"), "")
        self.PackInfoButton.button.hide()
        self.PackInfoButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;border-bottom: 0px;}")
        self.languageSettingsTitle.addWidget(self.PackInfoButton)
        self.openTranslateButton = QSettingsButton(_("Translate ElevenClock to your language"), _("Get started"))
        self.openTranslateButton.clicked.connect(lambda: os.startfile("https://github.com/martinet101/ElevenClock/wiki/Translating-ElevenClock#translating-elevenclock"))
        self.languageSettingsTitle.addWidget(self.openTranslateButton)

        def thirdPartyLicenses():
            msg = QFramelessDialog(parent=self, closeOnClick=False)
            msg.setAutoFillBackground(True)
            msg.setStyleSheet(self.styleSheet())
            msg.setAttribute(Qt.WA_StyledBackground)
            msg.setWindowFlag(Qt.WindowStaysOnTopHint)
            msg.setObjectName("QMessageBox")
            msg.setTitle(_("Third Party Open-Source Software in Elevenclock {0} (And their licenses)").format(versionName))
            colors = getColors()
            msg.setText(f"""
                <p>{_("ElevenClock is an Open-Source application made with the help of other libraries made by the community:")}</p><br>
                <style> a {{color: rgb({colors[3]})}}</style>
                <ul>
                <li> <b>Python 3.9</b>: <a href="https://docs.python.org/3/license.html">PSF License Agreement</a></li>
                <li> <b>PyMica</b> (Also made by me): <a href="https://github.com/martinet101/pymica/blob/master/LICENSE">MIT License</a></li>
                <li> <b>PyWin32</b>: <a href="https://pypi.org/project/pynput/">LGPL-v3</a></li>
                <li> <b>PySide2 (Qt5)</b>: <a href="https://www.qt.io/licensing/open-source-lgpl-obligations">LGPL-v3</a></li>
                <li> <b>Psutil</b>: <a href="https://github.com/giampaolo/psutil/blob/master/LICENSE">BSD 3-Clause</a></li>
                <li> <b>PyInstaller</b>: <a href="https://www.pyinstaller.org/license.html">Custom GPL</a></li>
                <li> <b>PythonBlurBehind</b>: <a href="https://github.com/Peticali/PythonBlurBehind/blob/main/LICENSE">MIT License</a></li>
                <li> <b>Frameless Window</b>: <a href="https://github.com/mustafaahci/FramelessWindow/blob/master/LICENSE">The Unlicense</a></li>
                <li> <b>WNFUN</b>: <a href="https://github.com/ionescu007/wnfun/blob/master/LICENSE">BSD 2-Clause</a></li>
                </ul>    """)
            msg.addButton(_("Ok"), QDialogButtonBox.ButtonRole.ApplyRole, lambda: msg.close())
            msg.addButton(_("More Info"), QDialogButtonBox.ButtonRole.ResetRole, lambda: os.startfile("https://github.com/martinet101/ElevenClock/wiki#third-party-libraries"))
            def closeAndQt():
                msg.close()
                QMessageBox.aboutQt(self, "ElevenClock - "+_("About Qt"))
            msg.addButton(_("About Qt"), QDialogButtonBox.ButtonRole.ResetRole, lambda: closeAndQt())
            msg.setDefaultButtonRole(QDialogButtonBox.ButtonRole.ApplyRole, self.styleSheet())
            msg.show()

        self.aboutTitle = QIconLabel(_("About ElevenClock version {0}:").format(versionName), getPath(f"about_{self.iconMode}.png"), _("Info, report a bug, submit a feature request, donate, about"))
        layout.addWidget(self.aboutTitle)
        self.WebPageButton = QSettingsButton(_("View ElevenClock's homepage"), _("Open"))
        self.WebPageButton.clicked.connect(lambda: os.startfile("https://github.com/martinet101/ElevenClock/"))
        self.WebPageButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;border-bottom: 0px;}")
        self.aboutTitle.addWidget(self.WebPageButton)
        self.ThirdParty = QSettingsButton(_("Third party licenses"), _("View"))
        self.ThirdParty.clicked.connect(lambda: thirdPartyLicenses())
        self.ThirdParty.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;border-bottom: 0px;}")
        self.aboutTitle.addWidget(self.ThirdParty)
        self.IssueButton = QSettingsButton(_("Report an issue/request a feature"), _("Report"))
        self.IssueButton.clicked.connect(lambda: os.startfile("https://github.com/martinet101/ElevenClock/issues/new/choose"))
        self.IssueButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;border-bottom: 0px;}")
        self.aboutTitle.addWidget(self.IssueButton)
        self.CofeeButton = QSettingsButton(_("Support the dev: Give me a coffee☕"), _("Open page"))
        self.CofeeButton.clicked.connect(lambda: os.startfile("https://ko-fi.com/martinet101"))
        self.CofeeButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;border-bottom: 0px;}")
        self.aboutTitle.addWidget(self.CofeeButton)
        self.closeButton = QSettingsButton(_("Close settings"), _("Close"))
        self.closeButton.clicked.connect(lambda: self.hide())
        self.aboutTitle.addWidget(self.closeButton)


        self.debbuggingTitle = QIconLabel(_("Debbugging information:"), getPath(f"bug_{self.iconMode}.png"), _("Log, debugging information"))
        layout.addWidget(self.debbuggingTitle)
        self.logButton = QSettingsButton(_("Open ElevenClock's log"), _("Open"))
        self.logButton.clicked.connect(lambda: self.showDebugInfo())
        self.logButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;border-bottom: 0px;}")
        self.debbuggingTitle.addWidget(self.logButton)
        try:
            self.hiddenButton = QSettingsButton(f"ElevenClock Version: {versionName} {platform.architecture()[0]} (version code {version})\nSystem version: {platform.system()} {str(int(platform.release())+1) if int(platform.version().split('.')[-1])>=22000 else platform.release()} {platform.win32_edition()} {platform.version()}\nSystem architecture: {platform.machine()}\n\nTotal RAM: {psutil.virtual_memory().total/(1000.**3)}\n\nSystem locale: {locale.getdefaultlocale()[0]}\nElevenClock language locale: lang_{langName}", _(""), h=140)
        except Exception as e:
            report(e)
            self.hiddenButton = QSettingsButton(f"ElevenClock Version: {versionName} {platform.architecture()[0]} (version code {version})\nSystem version: {platform.system()} {platform.release()} {platform.win32_edition()} {platform.version()}\nSystem architecture: {platform.machine()}\n\nTotal RAM: {psutil.virtual_memory().total/(1000.**3)}\n\nSystem locale: {locale.getdefaultlocale()[0]}\nElevenClock language locale: lang_{langName}", _(""), h=140)

        self.hiddenButton.button.setVisible(False)
        self.debbuggingTitle.addWidget(self.hiddenButton)
        layout.addSpacing(15)
        layout.addStretch()

        shl = QHBoxLayout()
        shl.setSpacing(0)
        shl.setContentsMargins(0, 0, 0, 0)
        shl.addWidget(QWidget(), stretch=0)
        shl.addLayout(layout, stretch=1)
        shl.addWidget(QWidget(), stretch=0)

        self.settingsWidget.setLayout(shl)
        self.scrollArea.setWidget(self.settingsWidget)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.titlebar = QTitleBarWidget(self)
        self.scrollArea.setStyleSheet(f"QScrollArea{{border-bottom-left-radius: {self.getPx(6)}px;border-bottom-right-radius: {self.getPx(6)}px;}}")
        self.titlebar.setStyleSheet(f"#ControlWidget{{border-top-left-radius: {self.getPx(6)}px;border-top-right-radius: {self.getPx(6)}px;}}#closeButton{{border-top-right-radius: {self.getPx(6)}px;}}")
        self.vlayout.addWidget(self.titlebar)
        self.vlayout.addWidget(self.scrollArea)
        self.setWindowTitle(_("ElevenClock Settings"))
        self.applyStyleSheet()
        self.updateCheckBoxesStatus()
        w = QWidget()
        w.setObjectName("borderBackground")
        w.setLayout(self.vlayout)
        self.setCentralWidget(w)
        self.setMouseTracking(True)
        self.resize(900, 600)
        self.installEventFilter(self)

    def showEvent(self, event: QShowEvent) -> None:
        self.debbuggingTitle.toggleChilds()
        return super().showEvent(event)

    def updateCheckBoxesStatus(self):
        
        # General settings section
        if not self.enableUpdates.isChecked(): # Check if check for updates enabled
            for checkbox in [self.installUpdates, self.silentUpdates, self.bypassCNAMECheck]:
                checkbox.setToolTip(_("<b>{0}</b> needs to be enabled to change this setting").format(_("Automatically check for updates")))
                checkbox.setEnabled(False)
        else:
            for checkbox in [self.installUpdates, self.silentUpdates, self.bypassCNAMECheck]:
                checkbox.setToolTip("")
                checkbox.setEnabled(True)
            if not self.installUpdates.isChecked(): # Check if install updates enabled
                for checkbox in [self.silentUpdates, self.bypassCNAMECheck]:
                    checkbox.setToolTip(_("<b>{0}</b> needs to be enabled to change this setting").format(_("Automatically install available updates")))
                    checkbox.setEnabled(False)
            else:
                for checkbox in [self.silentUpdates, self.bypassCNAMECheck]:
                    checkbox.setToolTip("")
                    checkbox.setEnabled(True)
        
                    
        # Date & time settings
        if not self.showTime.isChecked(): # Check if time is shown
            self.showSeconds.setToolTip(_("<b>{0}</b> needs to be enabled to change this setting").format(_("Show time on the clock")))
            self.showSeconds.setEnabled(False)
        else:
            self.showSeconds.setToolTip("")
            self.showSeconds.setEnabled(True)
            
        if not self.showDate.isChecked(): # Check if date is shown
            self.showWeekCount.setToolTip(_("<b>{0}</b> needs to be enabled to change this setting").format(_("Show date on the clock")))
            self.showWeekCount.setEnabled(False)
        else:
            self.showWeekCount.setToolTip("")
            self.showWeekCount.setEnabled(True)
            
            
        if not self.primaryScreen.isChecked(): # Clock is set to be in primary monitor
            self.onlyPrimaryScreen.setToolTip(_("<b>{0}</b> needs to be enabled to change this setting").format(_("Show the clock on the primary screen")))
            self.onlyPrimaryScreen.setEnabled(False)
            self.onlyPrimaryScreen.setChecked(False)
        else:
            self.onlyPrimaryScreen.setToolTip("")
            self.onlyPrimaryScreen.setEnabled(True)

        if self.enableLowCpuMode.isChecked():
            self.disableSystemTrayColor.setToolTip(_("<b>{0}</b> needs to be disabled to change this setting").format(_("Enable low-cpu mode")))
            self.disableSystemTrayColor.setChecked(True)
            self.disableSystemTrayColor.setEnabled(False)
            self.legacyRDPHide.setToolTip(_("<b>{0}</b> needs to be disabled to change this setting").format(_("Enable low-cpu mode")))
            self.legacyRDPHide.setChecked(False)
            self.legacyRDPHide.setEnabled(False)
        else:
            self.disableSystemTrayColor.setToolTip("")
            self.disableSystemTrayColor.setEnabled(True)
            self.legacyRDPHide.setToolTip("")
            self.legacyRDPHide.setEnabled(True)


    def applyStyleSheet(self):
        colors = getColors()
                            
        self.titlebar.setFixedHeight(self.getPx(32))
        if(readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "AppsUseLightTheme", 1)==0):
            ApplyMica(self.winId(), True)
            self.iconMode = "white"
            self.aboutTitle.setIcon(getPath(f"about_{self.iconMode}.png"))
            self.dateTimeTitle.setIcon(getPath(f"datetime_{self.iconMode}.png"))
            self.clockSettingsTitle.setIcon(getPath(f"clock_{self.iconMode}.png"))
            self.languageSettingsTitle.setIcon(getPath(f"lang_{self.iconMode}.png"))
            self.generalSettingsTitle.setIcon(getPath(f"settings_{self.iconMode}.png"))
            self.experimentalTitle.setIcon(getPath(f"experiment_{self.iconMode}.png"))
            self.clockPosTitle.setIcon(getPath(f"size_{self.iconMode}.png"))
            self.unBlackListButton.setIcon(QIcon(getPath(f"restart_{self.iconMode}.png")))
            self.ThirdParty.setIcon(QIcon(getPath(f"open_{self.iconMode}.png")))
            self.closeButton.setIcon(QIcon(getPath(f"close_{self.iconMode}.png")))
            self.startupButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.RegionButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.IssueButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.IssueButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.WebPageButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.logButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.debbuggingTitle.setIcon(QIcon(getPath(f"bug_{self.iconMode}.png")))
            self.clockAppearanceTitle.setIcon(QIcon(getPath(f"appearance_{self.iconMode}.png")))
            self.CofeeButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.openTranslateButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.titlebar.closeButton.setIconSize(QSize(self.getPx(14), self.getPx(14)))
            self.titlebar.closeButton.setFixedHeight(self.getPx(32))
            self.titlebar.closeButton.setFixedWidth(self.getPx(50))
            self.titlebar.maximizeButton.setFixedHeight(self.getPx(32))
            self.titlebar.maximizeButton.setIconSize(QSize(self.getPx(14), self.getPx(14)))
            self.titlebar.maximizeButton.setFixedWidth(self.getPx(46))
            self.titlebar.minimizeButton.setFixedHeight(self.getPx(32))
            self.titlebar.minimizeButton.setIconSize(QSize(self.getPx(12), self.getPx(12)))
            self.titlebar.minimizeButton.setFixedWidth(self.getPx(46))
            
            self.setStyleSheet(f"""
                               #backgroundWindow {{
                                   
                                   /*background-color: rgba({colors[3]}, 1);*/
                                   background: transparent;
                               }}
                               #titlebarButton {{
                                   border-radius: 0px;
                                   border:none;
                                   background-color: rgba(0, 0, 0, 0.01);
                               }}
                               #titlebarButton:hover {{
                                   border-radius: 0px;
                                   background-color: rgba(80, 80, 80, 25%);
                               }}
                               #closeButton {{
                                   border-radius: 0px;
                                   border:none;
                                   background-color: rgba(0, 0, 0, 0.01);
                               }}
                               #closeButton:hover {{
                                   border-radius: 0px;
                                   background-color: rgba(196, 43, 28, 25%);
                               }}
                                QToolTip {{
                                    border: {self.getPx(1)}px solid #222222;
                                    padding: {self.getPx(4)}px;
                                    border-radius: {self.getPx(6)}px;
                                    background-color: #262626;
                                }}
                                QMenu {{
                                    border: {self.getPx(1)}px solid rgb(60, 60, 60);
                                    padding: {self.getPx(2)}px;
                                    outline: 0px;
                                    color: white;
                                    background: #262626;
                                    border-radius: {self.getPx(8)}px;
                                }}
                                QMenu::separator {{
                                    margin: {self.getPx(2)}px;
                                    height: {self.getPx(1)}px;
                                    background: rgb(60, 60, 60);
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
                                    background: rgba(255, 255, 255, 10%);
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
                                QColorDialog {{
                                    background-color: transparent;
                                    border: none;
                                }}
                                QLineEdit {{
                                    background-color: #1d1d1d;
                                    padding: 5px;
                                    border-radius: {self.getPx(6)}px;
                                    border: 1px solid #262626;
                                }}
                                #background,QMessageBox,QDialog,QSlider,#ControlWidget{{
                                   color: white;
                                   /*background-color: #212121;*/
                                   background: transparent;
                                }}
                                QScrollArea {{
                                   color: white;
                                   /*background-color: #212121;*/
                                   background: transparent;
                                }}
                                QLabel {{
                                    font-family: "Segoe UI Variable Display Semib";
                                    font-weight: medium;
                                }}
                                * {{
                                   color: #dddddd;
                                   font-size: 8pt;
                                }}
                                #greyishLabel {{
                                    color: #aaaaaa;
                                }}
                                #warningLabel {{
                                    color: #bdba00;
                                }}
                                QPlainTextEdit{{
                                    font-family: "Cascadia Mono";
                                    background-color: #212121;
                                    selection-background-color: rgb({colors[4]});
                                    border: none;
                                }}
                                QSpinBox {{
                                   background-color: rgba(81, 81, 81, 25%);
                                   border-radius: {self.getPx(6)}px;
                                   border: {self.getPx(1)}px solid rgba(86, 86, 86, 25%);
                                   height: {self.getPx(25)}px;
                                   border-top: {self.getPx(1)}px solid rgba(99, 99, 99, 25%);
                                }}
                                QPushButton {{
                                   width: 100px;
                                   background-color:rgba(81, 81, 81, 25%);
                                   border-radius: {self.getPx(6)}px;
                                   border: {self.getPx(1)}px solid rgba(86, 86, 86, 25%);
                                   height: {self.getPx(25)}px;
                                   border-top: {self.getPx(1)}px solid rgba(99, 99, 99, 25%);
                                }}
                                QPushButton:hover {{
                                   background-color:rgba(86, 86, 86, 25%);
                                   border-radius: {self.getPx(6)}px;
                                   border: {self.getPx(1)}px solid rgba(100, 100, 100, 25%);
                                   height: {self.getPx(25)}px;
                                   border-top: {self.getPx(1)}px solid rgba(107, 107, 107, 25%);
                                }}
                                #AccentButton{{
                                    background-color: rgb({colors[3]});
                                    border-color: rgb({colors[2]});
                                    border-top-color: rgb({colors[1]});
                                }}
                                #AccentButton:hover{{
                                    background-color: rgb({colors[2]});
                                    border-color: rgb({colors[1]});
                                    border-top-color: rgb({colors[1]});
                                }}
                                #title{{
                                   /*background-color: #303030;
                                   */margin: {self.getPx(2)}px;
                                   margin-bottom: 0px;
                                   padding-left: {self.getPx(20)}px;
                                   padding-top: {self.getPx(15)}px;
                                   padding-bottom: {self.getPx(15)}px;
                                   /*border: {self.getPx(1)}px solid rgba(36, 36, 36, 50%);
                                   border-bottom: 0px;
                                   */font-size: 13pt;
                                   border-radius: {self.getPx(4)}px;
                                }}
                                #subtitleLabel{{
                                   background-color: rgba(71, 71, 71, 25%);
                                   margin: {self.getPx(10)}px;
                                   margin-bottom: 0px;
                                   margin-top: 0px;
                                   padding-left: {self.getPx(20)}px;
                                   padding-top: {self.getPx(15)}px;
                                   padding-bottom: {self.getPx(15)}px;
                                   border: {self.getPx(1)}px solid rgba(36, 36, 36, 50%);
                                   font-size: 13pt;
                                   border-top-left-radius: {self.getPx(6)}px;
                                   border-top-right-radius: {self.getPx(6)}px;
                                }}
                                #subtitleLableHover {{
                                   background-color: rgba(20, 20, 20, 1%);
                                   margin: {self.getPx(10)}px;
                                   margin-top: 0px;
                                   margin-bottom: 0px;
                                   border-radius: {self.getPx(6)}px;
                                   border-top-left-radius: {self.getPx(6)}px;
                                   border-top-right-radius: {self.getPx(6)}px;
                                   border: 1px solid transparent;
                                }}
                                #subtitleLableHover:hover{{
                                   background-color: rgba(255, 255, 255, 4%);
                                   margin: {self.getPx(10)}px;
                                   margin-top: 0px;
                                   margin-bottom: 0px;
                                   padding-left: {self.getPx(20)}px;
                                   padding-top: {self.getPx(15)}px;
                                   padding-bottom: {self.getPx(15)}px;
                                   border: {self.getPx(1)}px solid rgba(36, 36, 36, 50%);
                                   border-bottom: 0px;
                                   font-size: 13pt;
                                   border-top-left-radius: {self.getPx(6)}px;
                                   border-top-right-radius: {self.getPx(6)}px;
                                }}
                                #StLbl{{
                                   padding: 0px;
                                   background-color: rgba(71, 71, 71, 0%);
                                   margin: 0px;
                                   border:none;
                                   font-size: {self.getPx(11)}px;
                                }}
                                #stBtn{{
                                   background-color: rgba(71, 71, 71, 0%);
                                   margin: {self.getPx(10)}px;
                                   margin-bottom: 0px;
                                   margin-top: 0px;
                                   border: {self.getPx(1)}px solid rgba(36, 36, 36, 50%);
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
                                   background-color: rgba(71, 71, 71, 0%);
                                   margin: {self.getPx(10)}px;
                                   margin-bottom: 0px;
                                   margin-top: 0px;
                                   border: {self.getPx(1)}px solid rgba(36, 36, 36, 50%);
                                   border-bottom: 0px;
                                }}
                                #stChk::indicator{{
                                   height: {self.getPx(20)}px;
                                   width: {self.getPx(20)}px;
                                }}
                                #stChk::indicator:unchecked {{
                                    background-color: rgba(30, 30, 30, 25%);
                                    border: {self.getPx(1)}px solid #444444;
                                    border-radius: {self.getPx(6)}px;
                                }}
                                #stChk::indicator:disabled {{
                                    background-color: rgba(71, 71, 71, 0%);
                                    color: #bbbbbb;
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
                                #stChk::indicator:checked:disabled {{
                                    border: {self.getPx(1)}px solid #444444;
                                    background-color: #303030;
                                    color: #bbbbbb;
                                    border-radius: {self.getPx(6)}px;
                                    image: url("{getPath("tick_black.png")}");
                                }}
                                #stChk::indicator:checked:hover {{
                                    border: {self.getPx(1)}px solid #444444;
                                    background-color: rgb({colors[2]});
                                    border-radius: {self.getPx(6)}px;
                                    image: url("{getPath("tick_white.png")}");
                                }}
                                #stCmbbx {{
                                   width: 100px;
                                   background-color:rgba(81, 81, 81, 25%);
                                   border-radius: {self.getPx(6)}px;
                                   border: {self.getPx(1)}px solidrgba(86, 86, 86, 25%);
                                   height: {self.getPx(25)}px;
                                   padding-left: {self.getPx(10)}px;
                                   border-top: {self.getPx(1)}px solidrgba(99, 99, 99, 25%);
                                }}
                                #stCmbbx:disabled {{
                                   width: 100px;
                                   background-color: #303030;
                                   border-radius: {self.getPx(6)}px;
                                   border: {self.getPx(1)}px solidrgba(86, 86, 86, 25%);
                                   height: {self.getPx(25)}px;
                                   padding-left: {self.getPx(10)}px;
                                   border-top: {self.getPx(1)}px solidrgba(86, 86, 86, 25%);
                                }}
                                #stCmbbx:hover {{
                                   background-color:rgba(86, 86, 86, 25%);
                                   border-radius: {self.getPx(6)}px;
                                   border: {self.getPx(1)}px solidrgba(100, 100, 100, 25%);
                                   height: {self.getPx(25)}px;
                                   padding-left: {self.getPx(10)}px;
                                   border-top: {self.getPx(1)}px solid rgba(107, 107, 107, 25%);
                                }}
                                #stCmbbx::drop-down {{
                                    subcontrol-origin: padding;
                                    subcontrol-position: top right;
                                    padding: {self.getPx(5)}px;
                                    border-radius: {self.getPx(6)}px;
                                    border: none;
                                    width: {self.getPx(30)}px;
                                }}
                                #stCmbbx::down-arrow {{
                                    image: url("{getPath(f"down-arrow_{self.iconMode}.png")}");
                                    height: {self.getPx(8)}px;
                                    width: {self.getPx(8)}px;
                                }}
                                #stCmbbx::down-arrow:disabled {{
                                    image: url("{getPath(f"down-arrow_{self.iconMode}.png")}");
                                    height: {self.getPx(2)}px;
                                    width: {self.getPx(2)}px;
                                }}
                                #stCmbbx QAbstractItemView {{
                                    border: {self.getPx(1)}px solid rgba(36, 36, 36, 50%);
                                    padding: {self.getPx(4)}px;
                                    outline: 0px;
                                    padding-right: {self.getPx(0)}px;
                                    background-color: #303030;
                                    border-radius: {self.getPx(8)}px;
                                }}
                                #stCmbbx QAbstractItemView::item{{
                                    height: {self.getPx(30)}px;
                                    border: none;
                                    padding-left: {self.getPx(10)}px;
                                    border-radius: {self.getPx(4)}px;
                                }}
                                #stCmbbx QAbstractItemView::item:selected{{
                                    background-color: #4c4c4c;
                                    height: {self.getPx(30)}px;
                                    outline: none;
                                    border: none;
                                    padding-left: {self.getPx(10)}px;
                                    border-radius: {self.getPx(4)}px;
                                }}
                                QSCrollArea, QVBoxLayout{{
                                    border: none;
                                    margin: none;
                                    padding: none;
                                    outline: none;
                                }}
                                QScrollBar:vertical {{
                                    background: rgba(71, 71, 71, 25%);
                                    margin: {self.getPx(4)}px;
                                    width: {self.getPx(20)}px;
                                    border: none;
                                    border-radius: {self.getPx(5)}px;
                                }}
                                QScrollBar::handle:vertical {{
                                    margin: {self.getPx(3)}px;
                                    min-height: 20px;
                                    border-radius: {self.getPx(3)}px;
                                    background: rgba(80, 80, 80, 25%);
                                }}
                                QScrollBar::handle:vertical:hover {{
                                    margin: {self.getPx(3)}px;
                                    border-radius: {self.getPx(3)}px;
                                    background: rgba(112, 112, 112, 25%);
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
                                #titlebarLabel {{
                                    color: red;
                                    background: transparent;
                                    font-size: 10pt;
                                }}
                                #dialogButtonWidget{{
                                    background-color: #1d1d1d;
                                }}
                               """)
        else:
            ApplyMica(self.winId(), False)
            self.iconMode = "black"
            self.aboutTitle.setIcon(getPath(f"about_{self.iconMode}.png"))
            self.dateTimeTitle.setIcon(getPath(f"datetime_{self.iconMode}.png"))
            self.clockSettingsTitle.setIcon(getPath(f"clock_{self.iconMode}.png"))
            self.generalSettingsTitle.setIcon(getPath(f"settings_{self.iconMode}.png"))
            self.experimentalTitle.setIcon(getPath(f"experiment_{self.iconMode}.png"))
            self.languageSettingsTitle.setIcon(getPath(f"lang_{self.iconMode}.png"))
            self.clockPosTitle.setIcon(getPath(f"size_{self.iconMode}.png"))
            self.unBlackListButton.setIcon(QIcon(getPath(f"restart_{self.iconMode}.png")))
            self.ThirdParty.setIcon(QIcon(getPath(f"restart_{self.iconMode}.png")))
            self.CofeeButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.startupButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.RegionButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.WebPageButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.logButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.debbuggingTitle.setIcon(QIcon(getPath(f"bug_{self.iconMode}.png")))
            self.clockAppearanceTitle.setIcon(QIcon(getPath(f"appearance_{self.iconMode}.png")))
            self.IssueButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.closeButton.setIcon(QIcon(getPath(f"close_{self.iconMode}.png")))
            self.openTranslateButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.titlebar.closeButton.setIconSize(QSize(self.getPx(14), self.getPx(14)))
            self.titlebar.closeButton.setIcon(QIcon(getPath(f"cross_{self.iconMode}.png")))
            self.titlebar.closeButton.setFixedHeight(self.getPx(32))
            self.titlebar.closeButton.setFixedWidth(self.getPx(50))
            self.titlebar.maximizeButton.setFixedHeight(self.getPx(32))
            self.titlebar.maximizeButton.setIconSize(QSize(self.getPx(14), self.getPx(14)))
            self.titlebar.maximizeButton.setIcon(QIcon(getPath(f"maximize_{self.iconMode}.png")))
            self.titlebar.maximizeButton.setFixedWidth(self.getPx(46))
            self.titlebar.minimizeButton.setFixedHeight(self.getPx(32))
            self.titlebar.minimizeButton.setIconSize(QSize(self.getPx(12), self.getPx(12)))
            self.titlebar.minimizeButton.setIcon(QIcon(getPath(f"minimize_{self.iconMode}.png")))
            self.titlebar.minimizeButton.setFixedWidth(self.getPx(46))
            self.setStyleSheet(f"""
                               #backgroundWindow {{
                                   background-color: rgba({colors[4]}, 1);
                               }}
                               #titlebarButton {{
                                   border-radius: 0px;
                                   border:none;
                                   background-color: rgba(0, 0, 0, 0.01);
                               }}
                               #titlebarButton:hover {{
                                   border-radius: 0px;
                                   background-color: rgba({colors[4]}, 1);
                               }}
                               #closeButton {{
                                   border-radius: 0px;
                                   border:none;
                                   background-color: rgba(0, 0, 0, 0.01);
                               }}
                               #closeButton:hover {{
                                   border-radius: 0px;
                                   background-color: rgba(196, 43, 28, 1);
                               }}
                                QToolTip{{
                                    border: {self.getPx(1)}px solid #dddddd;
                                    padding: {self.getPx(4)}px;
                                    border-radius: {self.getPx(6)}px;
                                    background-color: #eeeeee;
                                }}
                                QPlainTextEdit{{
                                    font-family: "Cascadia Mono";
                                    background-color: #ffffff;
                                    selection-background-color: rgb({colors[3]});
                                    border: none;
                                }}
                                QMenu {{
                                    border: {self.getPx(1)}px solid rgb(200, 200, 200);
                                    padding: {self.getPx(2)}px;
                                    outline: 0px;
                                    color: black;
                                    background: #eeeeee;
                                    border-radius: {self.getPx(8)}px;
                                }}
                                QMenu::separator {{
                                    margin: {self.getPx(2)}px;
                                    height: {self.getPx(1)}px;
                                    background: rgb(200, 200, 200);
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
                                QColorDialog {{
                                    background-color: transparent;
                                    border: none;
                                }}
                                #background,QScrollArea,QMessageBox,QDialog,QSlider,#ControlWidget{{
                                   color: white;
                                }}
                                * {{
                                   background-color: #eeeeee;
                                   color: #000000;
                                   font-size: 8pt;
                                }}
                                #warningLabel {{
                                    color: #bd0000;
                                    background-color: transparent;
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
                                #AccentButton{{
                                    background-color: rgb({colors[3]});
                                    border-color: rgb({colors[4]});
                                    border-bottom-color: rgb({colors[5]});
                                    color: white;
                                }}
                                #AccentButton:hover{{
                                    background-color: rgb({colors[2]});
                                    border-color: rgb({colors[3]});
                                    color: white;
                                    border-bottom-color: rgb({colors[3]});
                                }}
                                #title{{
                                   /*background-color: #ffffff;
                                   */margin: {self.getPx(2)}px;
                                   margin-bottom: 0px;
                                   padding-left: {self.getPx(20)}px;
                                   padding-top: {self.getPx(15)}px;
                                   padding-bottom: {self.getPx(15)}px;
                                   /*border: {self.getPx(1)}px solid #dddddd;
                                   border-bottom: 1px;
                                   */font-size: 13pt;
                                   border-radius: {self.getPx(6)}px;
                                }}
                                #subtitleLabel{{
                                   background-color: #ffffff;
                                   margin: {self.getPx(10)}px;
                                   margin-bottom: 0px;
                                   margin-top: 0px;
                                   padding-left: {self.getPx(20)}px;
                                   padding-top: {self.getPx(15)}px;
                                   padding-bottom: {self.getPx(15)}px;
                                   border-radius: {self.getPx(4)}px;
                                   border: {self.getPx(1)}px solid #dddddd;
                                   font-size: 13pt;
                                   border-top-left-radius: {self.getPx(6)}px;
                                   border-top-right-radius: {self.getPx(6)}px;
                                }}
                                #subtitleLableHover {{
                                   background-color: rgba(0, 0, 0, 1%);
                                   margin: {self.getPx(10)}px;
                                   margin-top: 0px;
                                   margin-bottom: 0px;
                                   border-radius: {self.getPx(6)}px;
                                   border-top-left-radius: {self.getPx(6)}px;
                                   border-top-right-radius: {self.getPx(6)}px;
                                   border: 1px solid transparent;
                                }}
                                #subtitleLableHover:hover{{
                                   background-color: rgba(0, 0, 0, 6%);
                                   margin: {self.getPx(10)}px;
                                   margin-top: 0px;
                                   margin-bottom: 0px;
                                   padding-left: {self.getPx(20)}px;
                                   padding-top: {self.getPx(15)}px;
                                   padding-bottom: {self.getPx(15)}px;
                                   border: {self.getPx(1)}px solid #dddddd;
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
                                   border-bottom-left-radius: {self.getPx(0)}px;
                                   border-bottom-right-radius: {self.getPx(0)}px;
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
                                #stChk::indicator:disabled {{
                                    background-color: #eeeeee;
                                    color: #bbbbbb;
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
                                #stChk::indicator:checked:disabled {{
                                    border: {self.getPx(1)}px solid #bbbbbb;
                                    background-color: #eeeeee;
                                    color: #bbbbbb;
                                    border-radius: {self.getPx(6)}px;
                                    image: url("{getPath("tick_white.png")}");
                                }}
                                #stCmbbx {{
                                   width: 100px;
                                   background-color: #ffffff;
                                   border-radius: {self.getPx(6)}px;
                                   border: {self.getPx(1)}px solid #dddddd;
                                   height: {self.getPx(25)}px;
                                   padding-left: {self.getPx(10)}px;
                                   border-bottom: {self.getPx(1)}px solid #cccccc;
                                }}
                                #stCmbbx:disabled {{
                                   width: 100px;
                                   background-color: #eeeeee;
                                   border-radius: {self.getPx(6)}px;
                                   border: {self.getPx(1)}px solid #dddddd;
                                   height: {self.getPx(25)}px;
                                   padding-left: {self.getPx(10)}px;
                                   border-top: {self.getPx(1)}px solid #dddddd;
                                }}
                                #stCmbbx:hover {{
                                   background-color: #f6f6f6;
                                   border-radius: {self.getPx(6)}px;
                                   border: {self.getPx(1)}px solid #dddddd;
                                   height: {self.getPx(25)}px;
                                   padding-left: {self.getPx(10)}px;
                                   border-bottom: {self.getPx(1)}px solid #cccccc;
                                }}
                                #stCmbbx::drop-down {{
                                    subcontrol-origin: padding;
                                    subcontrol-position: top right;
                                    padding: {self.getPx(5)}px;
                                    border-radius: {self.getPx(6)}px;
                                    border: none;
                                    width: {self.getPx(30)}px;
                                }}
                                #stCmbbx::down-arrow {{
                                    image: url("{getPath(f"down-arrow_{self.iconMode}.png")}");
                                    height: {self.getPx(8)}px;
                                    width: {self.getPx(8)}px;
                                }}
                                #stCmbbx::down-arrow:disabled {{
                                    image: url("{getPath(f"down-arrow_{self.iconMode}.png")}");
                                    height: {self.getPx(2)}px;
                                    width: {self.getPx(2)}px;
                                }}
                                #stCmbbx QAbstractItemView {{
                                    border: {self.getPx(1)}px solid #dddddd;
                                    padding: {self.getPx(4)}px;
                                    outline: 0px;
                                    background-color: #ffffff;
                                    border-radius: {self.getPx(8)}px;
                                }}
                                #stCmbbx QAbstractItemView::item{{
                                    height: {self.getPx(30)}px;
                                    border: none;
                                    padding-left: {self.getPx(10)}px;
                                    border-radius: {self.getPx(4)}px;
                                }}
                                #stCmbbx QAbstractItemView::item:selected{{
                                    background-color: #eeeeee;
                                    height: {self.getPx(30)}px;
                                    outline: none;
                                    color: black;
                                    border: none;
                                    padding-left: {self.getPx(10)}px;
                                    border-radius: {self.getPx(4)}px;
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
                                    min-height: 20px;
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
                                #greyishLabel {{
                                    color: #888888;
                                }}
                                #dialogButtonWidget{{
                                    background-color: #eeeeee;
                                }}
                               """)

    def showDebugInfo(self):
        global old_stdout, buffer
        win = QMainWindow(self)
        win.resize(800, 600)
        win.setObjectName("background")
        win.setWindowTitle("ElevenClock's log")
        
        w = QWidget()
        w.setLayout(QVBoxLayout())
        w.layout().setContentsMargins(0, 0, 0, 0)
        
        textEdit = QPlainTextEdit()
        textEdit.setReadOnly(True)

        textEdit.setPlainText(globals.buffer.getvalue())
        
        reloadButton = QPushButton(_("Reload log"))
        reloadButton.clicked.connect(lambda: textEdit.setPlainText(globals.buffer.getvalue()))
        hl = QHBoxLayout()
        hl.setSpacing(0)
        hl.setContentsMargins(3, 3, 3, 0)
        hl.addStretch()
        hl.addWidget(reloadButton)
        
        w.layout().setSpacing(0)
        w.layout().addLayout(hl, stretch=0)
        w.layout().addWidget(textEdit, stretch=1)
        
        win.setCentralWidget(w)
        win.show()

    def moveEvent(self, event: QMoveEvent) -> None:
        if(self.updateSize):
            pass
        else:
            def enableUpdateSize(self: SettingsWindow):
                time.sleep(1)
                self.updateSize = True

            self.updateSize = False
            KillableThread(target=enableUpdateSize, args=(self,)).start()
        super().moveEvent(event)
            
    def mouseReleaseEvent(self, event) -> None:
        if(self.updateSize):
            self.settingsWidget.resize(self.width()-self.getPx(17), self.settingsWidget.height())
            self.applyStyleSheet()
            if not self.isMaximized():
                self.scrollArea.setStyleSheet(f"QScrollArea{{border-bottom-left-radius: {self.getPx(6)}px;border-bottom-right-radius: {self.getPx(6)}px;}}")
                self.titlebar.setStyleSheet(f"#ControlWidget{{border-top-left-radius: {self.getPx(6)}px;border-top-right-radius: {self.getPx(6)}px;}}#closeButton{{border-top-right-radius: {self.getPx(6)}px;}}")
                self.vlayout.setContentsMargins(2, 2, 2, 2)
            self.updateSize = False
        return super().mouseReleaseEvent(event)


    def show(self) -> None:
        self.applyStyleSheet()
        self.raise_()
        self.vlayout.setContentsMargins(2, 2, 2, 2)
        return super().show()
    
    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == event.WindowStateChange:
            if self.isMaximized():
                self.scrollArea.setStyleSheet(f"QScrollArea{{border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;}}")
                self.titlebar.setStyleSheet(f"#ControlWidget{{border-top-left-radius: 0px;border-top-right-radius: 0px;}}#closeButton{{border-top-right-radius: 0px;}}")
                self.vlayout.setContentsMargins(0, 0, 0, 0)
            else:
                self.scrollArea.setStyleSheet(f"QScrollArea{{border-bottom-left-radius: {self.getPx(6)}px;border-bottom-right-radius: {self.getPx(6)}px;}}")
                self.titlebar.setStyleSheet(f"#ControlWidget{{border-top-left-radius: {self.getPx(6)}px;border-top-right-radius: {self.getPx(6)}px;}}#closeButton{{border-top-right-radius: {self.getPx(6)}px;}}")
                self.vlayout.setContentsMargins(2, 2, 2, 2)
        return super().eventFilter(watched, event)

    def showEvent(self, event: QShowEvent) -> None:
        self.showNormal()
        self.resize(self.getPx(900), self.getPx(600))
        return super().showEvent(event)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.hide()
        event.ignore()

    def getPx(self, original) -> int:
        return round(original*(self.screen().logicalDotsPerInch()/96))


class QIconLabel(QWidget):
    def __init__(self, text: str, icon: str, descText: str = "No description provided"):
        if(readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "AppsUseLightTheme", 1)==0):
            self.iconMode = "white"
            semib = "Semib"
        else:
            self.iconMode = "black"
            semib = ""
        super().__init__()
        self.icon = icon
        self.setObjectName("subtitleLabel")
        self.label = QLabel(text, self)
        self.setMaximumWidth(self.getPx(1000))
        self.descLabel = QLabel(descText, self)
        self.descLabel.setObjectName("greyishLabel")
        if lang == lang_zh_TW or lang == lang_zh_CN:
            self.label.setStyleSheet("font-size: 10pt;background: none;font-family: \"Microsoft JhengHei UI\";")
            self.descLabel.setStyleSheet("font-size: 8pt;background: none;font-family: \"Microsoft JhengHei UI\";")

        else:
            self.label.setStyleSheet(f"font-size: 10pt;background: none;font-family: \"Segoe UI Variable Display {semib}\";")
            self.descLabel.setStyleSheet(f"font-size: 8pt;background: none;font-family: \"Segoe UI Variable Display {semib}\";")

        self.image = QLabel(self)
        self.image.setStyleSheet("padding: 3px;background: none;")
        self.setAttribute(Qt.WA_StyledBackground)
        self.compressibleWidget = QWidget(self)
        self.compressibleWidget.show()
        self.childOpacity=QGraphicsOpacityEffect(self)
        self.childOpacity.setOpacity(1.0)
        self.compressibleWidget.setGraphicsEffect(self.childOpacity)
        self.compressibleWidget.setAutoFillBackground(True)
        self.compressibleWidget.setObjectName("compressibleWidget")
        self.compressibleWidget.setStyleSheet("#compressibleWidget{background-color: transparent;}")

        self.showHideButton = QPushButton("", self)
        self.showHideButton.setIcon(QIcon(getPath(f"expand_{self.iconMode}.png")))
        self.showHideButton.setStyleSheet("border: none; background-color:none;")
        self.showHideButton.clicked.connect(self.toggleChilds)
        l = QVBoxLayout()
        l.setSpacing(0)
        l.setContentsMargins(0, 0, 0, 0)
        self.childsVisible = False
        self.compressibleWidget.setLayout(l)

        self.setStyleSheet(f"QWidget#subtitleLabel{{border-bottom-left-radius: {self.getPx(6)}px;border-bottom-right-radius: {self.getPx(6)}px;border-bottom: 1px;}}")

        self.showAnim = QVariantAnimation(self.compressibleWidget)
        self.showAnim.setEasingCurve(QEasingCurve.InOutQuart)
        self.showAnim.setStartValue(0)
        self.showAnim.setEndValue(1000)
        self.showAnim.valueChanged.connect(lambda v: self.setChildFixedHeight(v, v/self.compressibleWidget.sizeHint().height()))
        self.showAnim.setDuration(300)
        self.showAnim.finished.connect(self.invertNotAnimated)
        self.hideAnim = QVariantAnimation(self.compressibleWidget)
        self.hideAnim.setEndValue(0)
        self.hideAnim.setEasingCurve(QEasingCurve.InOutQuart)
        self.hideAnim.valueChanged.connect(lambda v: self.setChildFixedHeight(v, v/self.compressibleWidget.sizeHint().height()))
        self.hideAnim.setDuration(300)
        self.hideAnim.finished.connect(self.invertNotAnimated)
        self.NotAnimated = True

     

        self.button = QPushButton("", self)
        self.button.setObjectName("subtitleLableHover")
        self.button.clicked.connect(self.toggleChilds)
        self.button.setStyleSheet(f"border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;")

        self.setChildFixedHeight(0, 0)
        self.button.setStyleSheet(f"border-bottom-left-radius: {self.getPx(6)}px;border-bottom-right-radius: {self.getPx(6)}px;")

        
    def setChildFixedHeight(self, h: int, o:float = 1.0) -> None:
        self.compressibleWidget.setFixedHeight(h)
        self.setFixedHeight(h+self.getPx(70))
        self.childOpacity.setOpacity((o-(0.5))*2 if (o-(0.5))*2>0 else 0)
        self.compressibleWidget.setGraphicsEffect(self.childOpacity)

    def invertNotAnimated(self):
        self.NotAnimated = not self.NotAnimated

    def toggleChilds(self):
        if(readRegedit(r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", "AppsUseLightTheme", 1)==0):
            self.iconMode = "white"
        else:
            self.iconMode = "black"
        if self.childsVisible:
            self.childsVisible = False
            self.hideAnim.setStartValue(self.compressibleWidget.sizeHint().height())
            self.hideAnim.setEndValue(0)
            self.invertNotAnimated()
            self.showHideButton.setIcon(QIcon(getPath(f"expand_{self.iconMode}.png")))
            self.hideAnim.finished.connect(lambda: self.button.setStyleSheet(f"border-bottom-left-radius: {self.getPx(6)}px;border-bottom-right-radius: {self.getPx(6)}px;"))
            self.hideAnim.start()
        else:
            self.showAnim.setStartValue(0)
            self.showHideButton.setIcon(QIcon(getPath(f"collapse_{self.iconMode}.png")))
            self.showAnim.setEndValue(self.compressibleWidget.sizeHint().height())
            self.button.setStyleSheet(f"border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;")
            self.showAnim.start()
            self.invertNotAnimated()
            self.childsVisible = True
        
    def getPx(self, original) -> int:
        return round(original*(self.screen().logicalDotsPerInchX()/96))

    def setIcon(self, icon: str) -> None:
        self.image.setPixmap(QIcon(icon).pixmap(QSize(24, 24)))

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.image.setPixmap(QIcon(self.icon).pixmap(QSize(self.getPx(24), self.getPx(24))))
        self.showHideButton.setIconSize(QSize(self.getPx(12), self.getPx(12)))
        self.button.move(0, 0)
        self.button.resize(self.width(), self.getPx(70))
        self.showHideButton.setFixedSize(self.getPx(30), self.getPx(30))
        self.showHideButton.move(self.width()-self.getPx(55), self.getPx(20))
        
        self.label.move(self.getPx(70), self.getPx(17))
        self.label.setFixedHeight(self.getPx(20))
        self.descLabel.move(self.getPx(70), self.getPx(37))
        self.descLabel.setFixedHeight(self.getPx(20))

        self.image.move(self.getPx(27), self.getPx(20))
        self.image.setFixedHeight(self.getPx(30))
        if self.childsVisible and self.NotAnimated:
            self.setFixedHeight(self.compressibleWidget.sizeHint().height()+self.getPx(70))
            self.compressibleWidget.setFixedHeight(self.compressibleWidget.sizeHint().height())
        elif self.NotAnimated:
            self.setFixedHeight(self.getPx(70))
        self.compressibleWidget.move(0, self.getPx(70))
        self.compressibleWidget.setFixedWidth(self.width())
        self.image.setFixedHeight(self.getPx(30))
        self.label.setFixedWidth(self.width()-self.getPx(70))
        self.image.setFixedWidth(self.getPx(30))
        return super().resizeEvent(event)
    
    def addWidget(self, widget: QWidget) -> None:
        self.compressibleWidget.layout().addWidget(widget)
        
class QSettingsButton(QWidget):
    clicked = Signal()
    def __init__(self, text="", btntext="", parent=None, h = 30):
        super().__init__(parent)
        self.fh = h
        self.setAttribute(Qt.WA_StyledBackground)
        self.button = QPushButton(btntext+" ", self)
        self.button.setLayoutDirection(Qt.RightToLeft)
        self.setObjectName("stBtn")
        self.label = QLabel(text, self)

        if lang == lang_zh_TW or lang == lang_zh_CN:
            self.label.setStyleSheet("font-size: 10pt;background: none;font-family: \"Microsoft JhengHei UI\";font-weight: 450;")
            self.button.setStyleSheet("font-size: 10pt;font-family: \"Microsoft JhengHei UI\";font-weight: 450;")
            self.label.setObjectName("StLbl")
        else:
            self.label.setStyleSheet("font-size: 9pt;background: none;font-family: \"Segoe UI Variable Text\";font-weight: 450;")
            self.button.setStyleSheet("font-size: 9pt;font-family: \"Segoe UI Variable Text\";font-weight: 450;")
            self.label.setObjectName("StLbl")
        self.button.clicked.connect(self.clicked.emit)

    def getPx(self, original) -> int:
        return round(original*(self.screen().logicalDotsPerInchX()/96))

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.button.move(self.width()-self.getPx(170), self.getPx(10))
        self.label.move(self.getPx(70), self.getPx(10))
        self.label.setFixedWidth(self.width()-self.getPx(230))
        self.label.setFixedHeight(self.getPx(self.fh))
        self.setFixedHeight(self.getPx(50+(self.fh-30)))
        self.button.setFixedHeight(self.getPx(self.fh))
        self.button.setFixedWidth(self.getPx(150))
        return super().resizeEvent(event)

    def setIcon(self, icon: QIcon) -> None:
        self.button.setIcon(icon)

class QSettingsComboBox(QWidget):
    textChanged = Signal(str)
    def __init__(self, text="", btntext="", parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground)
        self.combobox = QComboBox(self)
        self.combobox.setObjectName("stCmbbx")
        self.combobox.setItemDelegate(QStyledItemDelegate(self.combobox))
        self.setObjectName("stBtn")
        self.restartButton = QPushButton("Restart ElevenClock", self)
        self.restartButton.hide()
        self.restartButton.setObjectName("AccentButton")
        self.label = QLabel(text, self)

        if lang == lang_zh_TW or lang == lang_zh_CN:
            self.label.setStyleSheet("font-size: 11pt;background: none;font-family: \"Microsoft JhengHei UI\";font-weight: 450;")
            self.combobox.setStyleSheet("font-size: 11pt;font-family: \"Microsoft JhengHei UI\";font-weight: 450;")
            self.restartButton.setStyleSheet("font-size: 11pt;font-family: \"Microsoft JhengHei UI\";font-weight: 450;")
        else:
            self.label.setStyleSheet("font-size: 9pt;background: none;font-family: \"Segoe UI Variable Text\";font-weight: 450;")
            self.combobox.setStyleSheet("font-size: 9pt;font-family: \"Segoe UI Variable Text\";font-weight: 450;")
            self.restartButton.setStyleSheet("font-size: 9pt;font-family: \"Segoe UI Variable Text\";font-weight: 450;")
        self.label.setObjectName("StLbl")

    def getPx(self, original) -> int:
        return round(original*(self.screen().logicalDotsPerInchX()/96))

    def setItems(self, items: list, index: int) -> None:
        self.combobox.addItems(items)
        try:
            self.combobox.setCurrentIndex(index)
        except Exception as e:
            report(e)
            self.combobox.setCurrentIndex(0)
        self.combobox.currentTextChanged.connect(self.textChanged.emit)

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.combobox.move(self.width()-self.getPx(270), self.getPx(10))
        self.label.move(self.getPx(70), self.getPx(10))
        self.label.setFixedWidth(self.width()-self.getPx(480))
        self.label.setFixedHeight(self.getPx(30))
        self.restartButton.move(self.width()-self.getPx(430), self.getPx(10))
        self.restartButton.setFixedWidth(self.getPx(150))
        self.restartButton.setFixedHeight(self.getPx(30))
        self.setFixedHeight(self.getPx(50))
        self.combobox.setFixedHeight(self.getPx(30))
        self.combobox.setFixedWidth(self.getPx(250))
        return super().resizeEvent(event)

    def setIcon(self, icon: QIcon) -> None:
        pass
        #self.button.setIcon(icon)

    def showRestartButton(self) -> None:
        self.restartButton.show()

class QSettingsCheckBox(QWidget):
    stateChanged = Signal(bool)
    def __init__(self, text="", parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground)
        self.setObjectName("stChkBg")
        self.checkbox = QCheckBox(text, self)
        if lang == lang_zh_TW or lang == lang_zh_CN:
            self.checkbox.setStyleSheet("font-size: 11pt;background: none;font-family: \"Microsoft JhengHei UI\";font-weight: 450;")
        else:
            self.checkbox.setStyleSheet("font-size: 9pt;background: none;font-family: \"Segoe UI Variable Text\";font-weight: 450;")
        self.checkbox.setObjectName("stChk")
        self.checkbox.stateChanged.connect(self.stateChanged.emit)

    def setChecked(self, checked: bool) -> None:
        self.checkbox.setChecked(checked)

    def isChecked(self) -> bool:
        return self.checkbox.isChecked()

    def getPx(self, original) -> int:
        return round(original*(self.screen().logicalDotsPerInchX()/96))

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.checkbox.move(self.getPx(70), self.getPx(10))
        self.checkbox.setFixedHeight(self.getPx(30))
        self.checkbox.setFixedWidth(self.width()-self.getPx(70))
        self.setFixedHeight(self.getPx(50))
        return super().resizeEvent(event)

class QSettingsCheckBoxWithWarning(QSettingsCheckBox):
    def __init__(self, text = "", infotext = "", parent=None):
        super().__init__(text=text, parent=parent)
        self.infolabel = QLabel(infotext, self)
        self.infolabel.setTextFormat(Qt.RichText)
        self.infolabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.infolabel.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.infolabel.setOpenExternalLinks(True)
        self.infolabel.setObjectName("warningLabel")
        self.infolabel.setVisible(self.checkbox.isChecked())
        self.checkbox.stateChanged.connect(self.stateChangedFun)
        
    def stateChangedFun(self, checked: bool) -> bool:
        self.infolabel.setVisible(checked)
        self.stateChanged.emit(checked)
        
    def resizeEvent(self, event: QResizeEvent) -> None:
        self.checkbox.move(self.getPx(70), self.getPx(10))
        self.checkbox.setFixedHeight(self.getPx(30))
        self.checkbox.setFixedWidth(self.width()-self.getPx(70))
        self.infolabel.move(self.getPx(150), self.getPx(10))
        self.infolabel.setFixedHeight(self.getPx(30))
        self.infolabel.setFixedWidth(self.width()-self.getPx(70)-self.getPx(150))
        self.setFixedHeight(self.getPx(50))
        return super().resizeEvent(event)

class QSettingsSizeBoxComboBox(QSettingsCheckBox):
    stateChanged = Signal(bool)
    valueChanged = Signal(str)
    
    def __init__(self, text: str, parent=None):
        super().__init__(text=text, parent=parent)
        self.setAttribute(Qt.WA_StyledBackground)
        self.combobox = QComboBox(self)
        self.combobox.setObjectName("stCmbbx")
        self.combobox.currentIndexChanged.connect(self.valuechangedEvent)
        self.checkbox.stateChanged.connect(self.stateChangedEvent)
        self.stateChangedEvent(self.checkbox.isChecked())
        
    def resizeEvent(self, event: QResizeEvent) -> None:
        self.combobox.move(self.width()-self.getPx(270), self.getPx(10))
        self.checkbox.move(self.getPx(70), self.getPx(10))
        self.checkbox.setFixedWidth(self.width()-self.getPx(280))
        self.checkbox.setFixedHeight(self.getPx(30))
        self.setFixedHeight(self.getPx(50))
        self.combobox.setFixedHeight(self.getPx(30))
        self.combobox.setFixedWidth(self.getPx(250))
        return super().resizeEvent(event)
    
    def valuechangedEvent(self, i: int):
        self.valueChanged.emit(self.combobox.itemText(i))
    
    def stateChangedEvent(self, v: bool):
        self.combobox.setEnabled(self.checkbox.isChecked())
        if not self.checkbox.isChecked():
            self.combobox.setEnabled(False)
            self.combobox.setToolTip(_("<b>{0}</b> needs to be enabled to change this setting").format(_(self.checkbox.text())))
        else:
            self.combobox.setEnabled(True)
            self.combobox.setToolTip("")
            self.valueChanged.emit(self.combobox.currentText())
        self.stateChanged.emit(v)
        
    def loadItems(self):
        self.combobox.clear()
        self.combobox.addItems(str(item) for item in [5, 6, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 13, 14, 16])

class QCustomColorDialog(QColorDialog):
    def __init__(self, parent = ...) -> None:
        super().__init__(parent=parent)
        self.setStyleSheet("*{border-radius: 5px;background: transparent;}  QColorLuminancePicker {background-color: transparent; border: 5px solid black;margin: none; border: none; padding: none;} ")
        self.setAttribute(Qt.WA_NoSystemBackground)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_TranslucentBackground)

class QSettingsSizeBoxColorDialog(QSettingsCheckBox):
    stateChanged = Signal(bool)
    valueChanged = Signal(str)
    
    def __init__(self, text: str, parent=None):
        super().__init__(text=text, parent=parent)
        self.setAttribute(Qt.WA_StyledBackground)
        self.colorDialog = QCustomColorDialog(self)
        self.colorDialog.setOptions(QColorDialog.DontUseNativeDialog)
        self.button = QPushButton(self)
        self.button.setObjectName("stCmbbx")
        self.button.setText(_("Select custom color"))
        self.button.clicked.connect(self.colorDialog.show)
        self.colorDialog.colorSelected.connect(self.valuechangedEvent)
        self.checkbox.stateChanged.connect(self.stateChangedEvent)
        self.stateChangedEvent(self.checkbox.isChecked())
        
    def resizeEvent(self, event: QResizeEvent) -> None:
        self.button.move(self.width()-self.getPx(270), self.getPx(10))
        self.checkbox.move(self.getPx(70), self.getPx(10))
        self.checkbox.setFixedWidth(self.width()-self.getPx(280))
        self.checkbox.setFixedHeight(self.getPx(30))
        self.setFixedHeight(self.getPx(50))
        self.button.setFixedHeight(self.getPx(30))
        self.button.setFixedWidth(self.getPx(250))
        return super().resizeEvent(event)
    
    def valuechangedEvent(self, c: QColor):
        r = c.red()
        g = c.green()
        b = c.blue()
        color = f"{r},{g},{b}"
        self.valueChanged.emit(color)
        self.button.setStyleSheet(f"color: rgb({color})")
    
    def stateChangedEvent(self, v: bool):
        self.button.setEnabled(self.checkbox.isChecked())
        if not self.checkbox.isChecked():
            self.button.setEnabled(False)
            self.button.setStyleSheet("")
            self.button.setToolTip(_("<b>{0}</b> needs to be enabled to change this setting").format(_(self.checkbox.text())))
        else:
            self.button.setEnabled(True)
            self.button.setToolTip("")
        self.stateChanged.emit(v)
        
class QSettingsBgBoxColorDialog(QSettingsSizeBoxColorDialog):
 
    def valuechangedEvent(self, c: QColor):
        r = c.red()
        g = c.green()
        b = c.blue()
        a = c.alpha()
        color = f"{r},{g},{b},{a/255*100}"
        self.valueChanged.emit(color)
        self.button.setStyleSheet(f"background-color: rgba({color})")    

class QSettingsFontBoxComboBox(QSettingsCheckBox):
    stateChanged = Signal(bool)
    valueChanged = Signal(str)
    
    def __init__(self, text: str, parent=None):
        super().__init__(text=text, parent=parent)
        self.setAttribute(Qt.WA_StyledBackground)
        self.combobox = QFontComboBox(self)
        self.combobox.setObjectName("stCmbbx")
        self.combobox.currentIndexChanged.connect(self.valuechangedEvent)
        self.checkbox.stateChanged.connect(self.stateChangedEvent)
        self.stateChangedEvent(self.checkbox.isChecked())
        
    def resizeEvent(self, event: QResizeEvent) -> None:
        self.combobox.move(self.width()-self.getPx(270), self.getPx(10))
        self.checkbox.move(self.getPx(70), self.getPx(10))
        self.checkbox.setFixedWidth(self.width()-self.getPx(280))
        self.checkbox.setFixedHeight(self.getPx(30))
        self.setFixedHeight(self.getPx(50))
        self.combobox.setFixedHeight(self.getPx(30))
        self.combobox.setFixedWidth(self.getPx(250))
        return super().resizeEvent(event)
    
    def valuechangedEvent(self, i: int):
        self.valueChanged.emit(self.combobox.itemText(i))
        self.combobox.lineEdit().setFont(self.combobox.itemText(i))
    
    def stateChangedEvent(self, v: bool):
        self.combobox.setEnabled(self.checkbox.isChecked())
        if not self.checkbox.isChecked():
            self.combobox.setEnabled(False)
            self.combobox.setToolTip(_("<b>{0}</b> needs to be enabled to change this setting").format(_(self.checkbox.text())))
        else:
            self.combobox.setEnabled(True)
            self.combobox.setToolTip("")
            self.valueChanged.emit(self.combobox.currentText())
            self.combobox.lineEdit().setFont(self.combobox.currentText())
        self.stateChanged.emit(v)
        
    def setItems(self, items: list):
        self.combobox.clear()
        self.combobox.addItems(items)

class QTitleBarWidget(QWidget):
    def __init__(self, parent: QMainWindow = ...) -> None:
        super().__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground)
        self.setObjectName("ControlWidget")
        self.oldPos = QPoint(0, 0)
        self.setFixedHeight(parent.getPx(32))
        
        self.iconMode = "white"
        
        self.closeButton = QPushButton()
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setIconSize(QSize(parent.getPx(14), parent.getPx(14)))
        #self.closeButton.setIcon(QIcon(getPath(f"cross_{self.iconMode}.png")))
        self.closeButton.setFixedHeight(parent.getPx(32))
        self.closeButton.setFixedWidth(parent.getPx(50))
        self.closeButton.clicked.connect(parent.close)
        
        self.maximizeButton = QPushButton()
        self.maximizeButton.setObjectName("titlebarButton")
        self.maximizeButton.setFixedHeight(parent.getPx(32))
        self.maximizeButton.setIconSize(QSize(parent.getPx(14), parent.getPx(14)))
        #self.maximizeButton.setIcon(QIcon(getPath(f"maximize_{self.iconMode}.png")))
        self.maximizeButton.setFixedWidth(parent.getPx(46))
        self.maximizeButton.clicked.connect(lambda: parent.showNormal() if parent.isMaximized() else parent.showMaximized())
        
        self.minimizeButton = QPushButton()
        self.minimizeButton.setObjectName("titlebarButton")
        self.minimizeButton.setFixedHeight(parent.getPx(32))
        self.minimizeButton.setIconSize(QSize(parent.getPx(12), parent.getPx(12)))
        #self.minimizeButton.setIcon(QIcon(getPath(f"minimize_{self.iconMode}.png")))
        self.minimizeButton.setFixedWidth(parent.getPx(46))
        self.minimizeButton.clicked.connect(parent.showMinimized)
        
        self.setLayout(QHBoxLayout())
        icon = QLabel()
        icon.setAttribute(Qt.WA_TransparentForMouseEvents)
        icon.setPixmap(QIcon(getPath("icon.png")).pixmap(parent.getPx(16), parent.getPx(16)))
        l = QLabel(_("ElevenClock Settings"), self)
        l.setAttribute(Qt.WA_TransparentForMouseEvents)
        l.setObjectName("#titlebarLabel")
        self.layout().addWidget(icon)
        self.layout().addSpacing(parent.getPx(16))
        self.layout().addWidget(l)
        self.layout().addStretch()
        self.layout().setContentsMargins(parent.getPx(16), 0, 0, 0)
        self.layout().setSpacing(0)
        self.layout().addWidget(self.minimizeButton)
        self.layout().addWidget(self.maximizeButton)
        self.layout().addWidget(self.closeButton)
        
    
if __name__ == "__main__":
    import __init__
