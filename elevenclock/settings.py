import platform
import subprocess
import os
import sys
import locale
import time

import psutil
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

import globals

from languages import * 
from tools import *

def _(s): #Translate function
    global lang
    try:
        t = lang.lang[s]
        #return t # Uncomment to debug missing translations
        return t if t else s
    except KeyError:
        return s

class QIconLabel(QWidget):
    def __init__(self, text, icon=None):
        super().__init__()
        self.setObjectName("subtitleLabel")
        self.label = QLabel(text, self)
        if lang == lang_zh_TW or lang == lang_zh_CN:
            self.label.setStyleSheet("font-size: 13pt;background: none;font-family: \"Microsoft JhengHei UI\";")
        else:
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
        return int(original*(self.screen().logicalDotsPerInchX()/96))

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.button.move(self.width()-self.getPx(170), self.getPx(10))
        self.label.move(self.getPx(60), self.getPx(10))
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
        return int(original*(self.screen().logicalDotsPerInchX()/96))

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
        self.label.move(self.getPx(60), self.getPx(10))
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
        if lang == lang_zh_TW or lang == lang_zh_CN:
            title.setStyleSheet("font-size: 25pt;font-family: \"Microsoft JhengHei UI\";font-weight: 450;")
        else:
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
        self.updateButton = QSettingsButton(_("<b>Update to the latest version!</b>"), _("Install update"))
        self.updateButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;border-bottom: 0px;}")
        self.updateButton.clicked.connect(lambda: KillableThread(target=globals.updateIfPossible, args=((True,))).start())
        self.updateButton.hide()
        layout.addWidget(self.updateButton)
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
        layout.addWidget(self.selectedLanguage)
        self.updatesChBx = QSettingsCheckBox(_("Automatically check for updates"))
        self.updatesChBx.setChecked(not getSettings("DisableAutoCheckForUpdates"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("DisableAutoCheckForUpdates", not bool(i), r = False))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Automatically install available updates"))
        self.updatesChBx.setChecked(not getSettings("DisableAutoInstallUpdates"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("DisableAutoInstallUpdates", not bool(i), r = False))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Enable really silent updates"))
        self.updatesChBx.setChecked(getSettings("EnableSilentUpdates"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("EnableSilentUpdates", bool(i), r = False))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"))
        self.updatesChBx.setChecked(getSettings("BypassDomainAuthCheck"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("BypassDomainAuthCheck", bool(i), r = False))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Show ElevenClock on system tray"))
        self.updatesChBx.setChecked(not getSettings("DisableSystemTray"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("DisableSystemTray", not bool(i)))
        layout.addWidget(self.updatesChBx)
        self.startupButton = QSettingsButton(_("Change startup behaviour"), _("Change"))
        self.startupButton.clicked.connect(lambda: os.startfile("ms-settings:startupapps"))
        layout.addWidget(self.startupButton)
        layout.addSpacing(10)

        self.clockSettingsTitle = QIconLabel(_("Clock Settings:"), getPath(f"clock_{self.iconMode}.png"))
        layout.addWidget(self.clockSettingsTitle)
        self.updatesChBx = QSettingsCheckBox(_("Hide the clock in fullscreen mode"))
        self.updatesChBx.setChecked(not getSettings("DisableHideOnFullScreen"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("DisableHideOnFullScreen", not bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Hide the clock when RDP Client or Citrix Workspace are running"))
        self.updatesChBx.setChecked(getSettings("EnableHideOnRDP"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("EnableHideOnRDP", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Show the clock when the taskbar is set to hide automatically"))
        self.updatesChBx.setChecked(getSettings("DisableHideWithTaskbar"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("DisableHideWithTaskbar", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Force the clock to be at the bottom of the screen"))
        self.updatesChBx.setChecked(getSettings("ForceOnBottom"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("ForceOnBottom", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Show the clock at the left of the screen"))
        self.updatesChBx.setChecked(getSettings("ClockOnTheLeft"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("ClockOnTheLeft", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Show the clock on the primary screen (Useful if clock is set on the left)"))
        self.updatesChBx.setStyleSheet(f"QWidget#stChkBg{{border-bottom-left-radius: {self.getPx(6)}px;border-bottom-right-radius: {self.getPx(6)}px;border-bottom: 1px;}}")
        self.updatesChBx.setChecked(getSettings("ForceClockOnFirstMonitor"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("ForceClockOnFirstMonitor", bool(i)))
        layout.addWidget(self.updatesChBx)
        layout.addSpacing(10)

        self.clockAppearanceTitle = QIconLabel(_("Clock Appearance:"), getPath(f"appearance_{self.iconMode}.png"))
        layout.addWidget(self.clockAppearanceTitle)
        self.updatesChBx = QSettingsCheckBox(_("Force the clock to have black text"))
        self.updatesChBx.setChecked(getSettings("ForceLightTheme"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("ForceLightTheme", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Force the clock to have white text")+_(" - It is required that the Dark Text checkbox is disabled"))
        self.updatesChBx.setChecked(getSettings("ForceDarkTheme"))
        self.updatesChBx.setStyleSheet(f"QWidget#stChkBg{{border-bottom-left-radius: {self.getPx(6)}px;border-bottom-right-radius: {self.getPx(6)}px;border-bottom: 1px;}}")
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("ForceDarkTheme", bool(i)))
        layout.addWidget(self.updatesChBx)
        #self.updatesChBx = QSettingsCheckBox(_("Align the clock text to the center"))
        #self.updatesChBx.setChecked(getSettings("CenterAlignment"))
        #self.updatesChBx.setStyleSheet(f"QWidget#stChkBg{{border-bottom-left-radius: {self.getPx(6)}px;border-bottom-right-radius: {self.getPx(6)}px;border-bottom: 1px;}}")
        #self.updatesChBx.stateChanged.connect(lambda i: setSettings("CenterAlignment", bool(i)))
        #layout.addWidget(self.updatesChBx)
        layout.addSpacing(10)

        self.dateTimeTitle = QIconLabel(_("Date & Time Settings:"), getPath(f"datetime_{self.iconMode}.png"))
        layout.addWidget(self.dateTimeTitle)
        self.updatesChBx = QSettingsCheckBox(_("Show seconds on the clock"))
        self.updatesChBx.setChecked(getSettings("EnableSeconds"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("EnableSeconds", bool(i), r = False))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Show date on the clock"))
        self.updatesChBx.setChecked(not getSettings("DisableDate"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("DisableDate", not bool(i), r = False))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Show time on the clock"))
        self.updatesChBx.setChecked(not getSettings("DisableTime"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("DisableTime", not bool(i), r = False))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Show weekday on the clock"))
        self.updatesChBx.setChecked(getSettings("EnableWeekDay"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("EnableWeekDay", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Show week number on the clock"))
        self.updatesChBx.setChecked(getSettings("EnableWeekNumber"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("EnableWeekNumber", bool(i), r = False))
        layout.addWidget(self.updatesChBx)
        self.RegionButton = QSettingsButton(_("Change date and time format (Regional settings)"), _("Regional settings"))
        self.RegionButton.clicked.connect(lambda: os.startfile("intl.cpl"))
        layout.addWidget(self.RegionButton)
        layout.addSpacing(10)
        
        self.experimentalTitle = QIconLabel(_("Fixes and other experimental features: (Use ONLY if something is not working)"), getPath(f"experiment_{self.iconMode}.png"))
        layout.addWidget(self.experimentalTitle)
        self.updatesChBx = QSettingsCheckBox(_("Enable hide when multi-monitor fullscreen apps are running"))
        self.updatesChBx.setChecked(getSettings("NewFullScreenMethod"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("NewFullScreenMethod", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Fix the hyphen/dash showing over the month"))
        self.updatesChBx.setChecked(getSettings("EnableHyphenFix"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("EnableHyphenFix", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Alternative non-SSL update server (This might help with SSL errors)"))
        self.updatesChBx.setChecked(getSettings("AlternativeUpdateServerProvider"))
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("AlternativeUpdateServerProvider", bool(i)))
        layout.addWidget(self.updatesChBx)
        self.updatesChBx = QSettingsCheckBox(_("Alternative clock alignment (may not work)"))
        self.updatesChBx.setChecked(getSettings("EnableWin32API"))
        self.updatesChBx.setStyleSheet(f"QWidget#stChkBg{{border-bottom-left-radius: {self.getPx(6)}px;border-bottom-right-radius: {self.getPx(6)}px;border-bottom: 1px;}}")
        self.updatesChBx.stateChanged.connect(lambda i: setSettings("EnableWin32API", bool(i)))
        layout.addWidget(self.updatesChBx)
        layout.addSpacing(10)

        self.languageSettingsTitle = QIconLabel(_("About the language pack:"), getPath(f"lang_{self.iconMode}.png"))
        layout.addWidget(self.languageSettingsTitle)
        self.PackInfoButton = QSettingsButton(_("Translated to English by martinet101"), "")
        self.PackInfoButton.button.hide()
        self.PackInfoButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;border-bottom: 0px;}")
        layout.addWidget(self.PackInfoButton)
        self.openTranslateButton = QSettingsButton(_("Translate ElevenClock to your language"), _("Get started"))
        self.openTranslateButton.clicked.connect(lambda: os.startfile("https://github.com/martinet101/ElevenClock/blob/main/TRANSLATION.md"))
        layout.addWidget(self.openTranslateButton)
        layout.addSpacing(10)

        self.aboutTitle = QIconLabel(_("About ElevenClock version {0}:").format(versionName), getPath(f"about_{self.iconMode}.png"))
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
        self.QtButton = QSettingsButton(_("About Qt6 (PySide6)").replace("Qt6", "Qt5").replace("PySide6", "PySide2"), _("About"))
        self.QtButton.clicked.connect(lambda: QMessageBox.aboutQt(self, "ElevenClock - About Qt"))
        self.QtButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;border-bottom: 0px;}")
        layout.addWidget(self.QtButton)
        self.closeButton = QSettingsButton(_("Close settings"), _("Close"))
        self.closeButton.clicked.connect(lambda: self.hide())
        layout.addWidget(self.closeButton)
        layout.addSpacing(10)

        self.debbuggingTitle = QIconLabel(_("Debbugging information:"), getPath(f"bug_{self.iconMode}.png"))
        layout.addWidget(self.debbuggingTitle)
        self.logButton = QSettingsButton(_("Open ElevenClock's log"), _("Open"))
        self.logButton.clicked.connect(lambda: self.showDebugInfo())
        self.logButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0px;border-bottom-right-radius: 0px;border-bottom: 0px;}")
        layout.addWidget(self.logButton)
        try:
            self.hiddenButton = QSettingsButton(f"ElevenClock Version: {versionName} {platform.architecture()[0]} (version code {version})\nSystem version: {platform.system()} {str(int(platform.release())+1) if int(platform.version().split('.')[-1])>=22000 else platform.release()} {platform.win32_edition()} {platform.version()}\nSystem architecture: {platform.machine()}\n\nTotal RAM: {psutil.virtual_memory().total/(1000.**3)}\n\nSystem locale: {locale.getdefaultlocale()[0]}\nElevenClock language locale: lang_{langName}", _(""), h=140)
        except Exception as e:
            report(e)
            self.hiddenButton = QSettingsButton(f"ElevenClock Version: {versionName} {platform.architecture()[0]} (version code {version})\nSystem version: {platform.system()} {platform.release()} {platform.win32_edition()} {platform.version()}\nSystem architecture: {platform.machine()}\n\nTotal RAM: {psutil.virtual_memory().total/(1000.**3)}\n\nSystem locale: {locale.getdefaultlocale()[0]}\nElevenClock language locale: lang_{langName}", _(""), h=140)

        self.hiddenButton.button.setVisible(False)
        layout.addWidget(self.hiddenButton)
        layout.addSpacing(15)

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
            self.experimentalTitle.setIcon(getPath(f"experiment_{self.iconMode}.png"))
            self.PichonButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.QtButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
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
            self.setStyleSheet(f"""
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
                                #background,QScrollArea,QMessageBox{{
                                   color: white;
                                   background-color: #212121;
                                }}
                                * {{
                                   color: #dddddd;
                                   font-size: 8pt;
                                }}
                                QPlainTextEdit{{
                                    font-family: "Cascadia Mono";
                                    background-color: #212121;
                                    selection-background-color: rgb({colors[4]});
                                    border: none;
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
                                #stCmbbx {{
                                   width: 100px;
                                   background-color: #363636;
                                   border-radius: {self.getPx(6)}px;
                                   border: {self.getPx(1)}px solid #393939;
                                   height: {self.getPx(25)}px;
                                   padding-left: {self.getPx(10)}px;
                                   border-top: {self.getPx(1)}px solid #404040;
                                }}
                                #stCmbbx:hover {{
                                   background-color: #393939;
                                   border-radius: {self.getPx(6)}px;
                                   border: {self.getPx(1)}px solid #414141;
                                   height: {self.getPx(25)}px;
                                   padding-left: {self.getPx(10)}px;
                                   border-top: {self.getPx(1)}px solid #454545;
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
                                #stCmbbx QAbstractItemView {{
                                    border: {self.getPx(1)}px solid #1c1c1c;
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
            self.experimentalTitle.setIcon(getPath(f"experiment_{self.iconMode}.png"))
            self.languageSettingsTitle.setIcon(getPath(f"lang_{self.iconMode}.png"))
            self.PichonButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
            self.QtButton.setIcon(QIcon(getPath(f"launch_{self.iconMode}.png")))
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
            self.setStyleSheet(f"""
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
                                #stCmbbx {{
                                   width: 100px;
                                   background-color: #ffffff;
                                   border-radius: {self.getPx(6)}px;
                                   border: {self.getPx(1)}px solid #dddddd;
                                   height: {self.getPx(25)}px;
                                   padding-left: {self.getPx(10)}px;
                                   border-bottom: {self.getPx(1)}px solid #cccccc;
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

    def showDebugInfo(self):
        global old_stdout, buffer
        win = QMainWindow(self)
        win.resize(800, 600)
        win.setWindowTitle("ElevenClock's log")
        textEdit = QPlainTextEdit()
        textEdit.setReadOnly(True)

        textEdit.setPlainText(globals.buffer.getvalue())

        win.setCentralWidget(textEdit)
        win.show()

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
        self.raise_()
        return super().show()

    def showEvent(self, event: QShowEvent) -> None:
        self.resizewidget.setMinimumHeight(self.resizewidget.sizeHint().height())
        return super().showEvent(event)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.hide()
        event.ignore()

    def getPx(self, original) -> int:
        return int(original*(self.screen().logicalDotsPerInchX()/96))


if __name__ == "__main__":
    import __init__