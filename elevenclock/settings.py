from ctypes import c_int, windll
windll.shcore.SetProcessDpiAwareness(c_int(2))

import datetime
import glob
import platform
import subprocess
import os
import sys
import locale
import time
from urllib.request import urlopen
from PySide6 import QtGui
from PySide6 import QtCore

try:
    import psutil
    from psutil._common import bytes2human
except ImportError as e:
    print(e)
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
#from PySide6.QtCore import pyqtSignal as Signal


import globals
from win32mica import ApplyMica, MICAMODE

from languages import *
from lang.translated_percentage import *
from tools import *
from tools import _
import tools

import win32gui

from win32con import GWL_STYLE, WS_BORDER, WS_THICKFRAME, WS_CAPTION, WS_SYSMENU, WS_POPUP

from external.FramelessWindow import QFramelessWindow, QFramelessDialog
from external.blurwindow import ExtendFrameIntoClientArea, GlobalBlur

class SettingsWindow(QMainWindow):
    callInMain = Signal(object)
    lastTheme: int = -1
    def __init__(self):
        super().__init__()
        self.callInMain.connect(lambda f: f())
        self.scrollArea = SmoothScrollArea()
        sp = QScrollerProperties()
        sp.setScrollMetric( QScrollerProperties.DragVelocitySmoothingFactor,   1 )
        sp.setScrollMetric( QScrollerProperties.ScrollingCurve, QEasingCurve.InOutCubic )
        qs  = QScroller.scroller( self.scrollArea )
        qs.setScrollerProperties( sp )
        self.vlayout = QVBoxLayout()
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.vlayout.setSpacing(0)
        layout = QVBoxLayout()
        self.mainLayout = layout
        self.updateSize = True
        self.scrollArea.setWidgetResizable(True)
        self.setObjectName("backgroundWindow")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.settingsWidget = QWidget()
        self.settingsWidget.setObjectName("background")
        self.setWindowIcon(QIcon(getPath("icon.ico")))
        layout.addSpacing(0)
        self.title = QLabel(_("ElevenClock Settings"))
        self.title.setObjectName("title")
        if lang["locale"] == "zh_TW":
            self.title.setStyleSheet("font-size: 20pt;font-family: \"Microsoft JhengHei UI\";font-weight: 600;")
        elif lang["locale"] == "zh_CN":
            self.title.setStyleSheet("font-size: 20pt;font-family: \"Microsoft YaHei UI\";font-weight: 600;")
        else:
            self.title.setStyleSheet("font-size: 20pt;font-family: \"Segoe UI Variable Text\";font-weight: 700;")
        layout.setSpacing(5)
        layout.setContentsMargins(10, 0, 10, 0)
        layout.addSpacing(0)
        self.resize(900, 600)
        self.setMinimumWidth(540)
        self.iconMode = getAppIconMode()

        self.announcements = QAnnouncements()
        layout.addWidget(self.announcements)
        
        self.MessageLabel = QLabel()
        self.MessageLabel.setObjectName("greyishLabel")
        self.MessageLabel.setStyleSheet("font-size: 22pt;")
        layout.addWidget(self.MessageLabel)
        self.MessageLabel.hide()


        self.updateButton = QSettingsButton(_("<b>Update to the latest version!</b>"), _("Install update"))
        self.updateButton.setStyleSheet("")
        self.updateButton.clicked.connect(lambda: KillableThread(target=globals.updateIfPossible, args=((True,))).start())
        self.updateButton.setStyleSheet(f"QWidget#stBtn{{border-radius: 8px;}}")

        self.updateButton.hide()
        layout.addWidget(self.updateButton)

        self.generalSettingsTitle = QSettingsTitle(_("General Settings:"), getPath(f"settings_{self.iconMode}.png"), _("Updates, icon tray, language"))
        layout.addWidget(self.generalSettingsTitle)
        self.selectedLanguage = QSettingsComboBox(_("ElevenClock's language")+" (Language)", _("Change")) # The non-translated (Language) string is there to let people know what the language option is if you accidentaly change the language
        self.selectedLanguage.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0;border-bottom-right-radius: 0;border-bottom: 0;}")

        langListWithPercentage = []
        langDictWithPercentage = {}
        invertedLangDict = {}
        for key, value in languageReference.items():
            if (key in untranslatedPercentage):
                perc = untranslatedPercentage[key]
                if (perc == "0%"): continue
                if not key in lang["locale"]:
                    langListWithPercentage.append(f"{value} ({perc})")
                    langDictWithPercentage[key] = f"{value} ({perc})"
                    invertedLangDict[f"{value} ({perc})"] = key
                else:
                    k = len(lang.keys())
                    v = len([val for val in lang.values() if val != None])
                    perc = f"{int(v/k*100)}%"
                    langListWithPercentage.append(f"{value} ({perc})")
                    langDictWithPercentage[key] = f"{value} ({perc})"
                    invertedLangDict[f"{value} ({perc})"] = key
            else:
                invertedLangDict[value] = key
                langDictWithPercentage[key] = value
                langListWithPercentage.append(value)
        try:
            self.selectedLanguage.setItems(langListWithPercentage, langListWithPercentage.index(langDictWithPercentage[langName]))
        except Exception as e:
            report(e)
            self.selectedLanguage.setItems(langListWithPercentage, 0)

        def changeLang():
            self.selectedLanguage.restartButton.setVisible(True)
            i = self.selectedLanguage.combobox.currentIndex()
            selectedLang = invertedLangDict[self.selectedLanguage.combobox.currentText()] # list(languageReference.keys())[i]
            self.selectedLanguage.toggleRestartButton(selectedLang != langName)
            self.setSettingsValue("PreferredLanguage", selectedLang, r=False)

        def restartElevenClockByLangChange():
            subprocess.run(str("start /B \"\" \""+sys.executable)+"\" --settings", shell=True)
            globals.app.quit()

        self.selectedLanguage.restartButton.clicked.connect(restartElevenClockByLangChange)
        self.selectedLanguage.textChanged.connect(changeLang)
        self.generalSettingsTitle.addWidget(self.selectedLanguage)
        self.wizardButton = QSettingsButton(_("Open the welcome wizard"), _("Open"))

        def ww():
            subprocess.run(str("start /B \"\" \""+sys.executable)+"\" --welcome", shell=True)
            globals.app.quit()
            
        self.wizardButton.clicked.connect(ww)
        self.wizardButton.button.setObjectName("AccentButton")
        self.wizardButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0;border-bottom-right-radius: 0;border-bottom: 0;}")
        self.generalSettingsTitle.addWidget(self.wizardButton)
        self.enableUpdates = QSettingsCheckBox(_("Automatically check for updates"))
        self.enableUpdates.setChecked(not self.getSettings("DisableAutoCheckForUpdates"))
        self.enableUpdates.stateChanged.connect(lambda i: self.setSettings("DisableAutoCheckForUpdates", not bool(i), r = False))
        self.generalSettingsTitle.addWidget(self.enableUpdates)
        self.installUpdates = QSettingsCheckBox(_("Automatically install available updates"))
        self.installUpdates.setChecked(not self.getSettings("DisableAutoInstallUpdates"))
        self.installUpdates.stateChanged.connect(lambda i: self.setSettings("DisableAutoInstallUpdates", not bool(i), r = False))
        self.generalSettingsTitle.addWidget(self.installUpdates)
        self.installUpdates.setStyleSheet("border-top: 0px solid transparent;")
        self.silentUpdates = QSettingsCheckBox(_("Enable really silent updates"))
        self.silentUpdates.setChecked(self.getSettings("EnableSilentUpdates"))
        self.silentUpdates.stateChanged.connect(lambda i: self.setSettings("EnableSilentUpdates", bool(i), r = False))
        self.silentUpdates.setStyleSheet("border-top: 0px solid transparent;")
        self.generalSettingsTitle.addWidget(self.silentUpdates)
        self.enableSystemTray = QSettingsCheckBox(_("Show ElevenClock on system tray"))
        self.enableSystemTray.setChecked(not self.getSettings("DisableSystemTray"))
        self.enableSystemTray.stateChanged.connect(lambda i: self.setSettings("DisableSystemTray", not bool(i)))
        self.generalSettingsTitle.addWidget(self.enableSystemTray)
        self.startupButton = QSettingsButton(_("Change startup behaviour"), _("Change"))
        self.startupButton.clicked.connect(lambda: os.startfile("ms-settings:startupapps"))
        self.generalSettingsTitle.addWidget(self.startupButton)


        self.clockSettingsTitle = QSettingsTitle(_("Clock Settings:"), getPath(f"clock_{self.iconMode}.png"), _("Fullscreen behaviour, low cpu mode, other miscellaneous preferences"))
        layout.addWidget(self.clockSettingsTitle)
        self.addSecondClock = QSettingsCheckBox(_("Show a second clock on the other end of the taskbar"))
        self.addSecondClock.setChecked(self.getSettings("EnableSecondClock"))
        self.addSecondClock.stateChanged.connect(lambda i: self.setSettings("EnableSecondClock", bool(i)))
        self.clockSettingsTitle.addWidget(self.addSecondClock)
        self.legacyHideOnFullScreen = QSettingsCheckBox(_("Hide the clock in fullscreen mode"))
        self.legacyHideOnFullScreen.setChecked(not self.getSettings("DisableHideOnFullScreen"))
        self.legacyHideOnFullScreen.stateChanged.connect(lambda i: (self.setSettings("DisableHideOnFullScreen", not bool(i)), self.updateCheckBoxesStatus()))
        self.clockSettingsTitle.addWidget(self.legacyHideOnFullScreen)
        self.TransparentClockWhenInFullscreen = QSettingsCheckBox(_("Force the clock to be transparent if any window shows in fullscreen"))
        self.TransparentClockWhenInFullscreen.setChecked(self.getSettings("TransparentClockWhenInFullscreen"))
        self.TransparentClockWhenInFullscreen.stateChanged.connect(lambda i: self.setSettings("TransparentClockWhenInFullscreen", bool(i)))
        self.TransparentClockWhenInFullscreen.setStyleSheet("border-top: 0px solid transparent;")
        self.clockSettingsTitle.addWidget(self.TransparentClockWhenInFullscreen)
        self.transparentclickEventFS = QSettingsCheckBox(_("Ignore mouse clicks when on fullscreen"))
        self.transparentclickEventFS.setChecked(self.getSettings("MouseEventTransparentFS"))
        self.transparentclickEventFS.stateChanged.connect(lambda i: self.setSettings("MouseEventTransparentFS", bool(i)))
        self.transparentclickEventFS.setStyleSheet("border-top: 0px solid transparent;")
        self.clockSettingsTitle.addWidget(self.transparentclickEventFS)
        self.forceClockToShow = QSettingsCheckBox(_("Show the clock when the taskbar is set to hide automatically"))
        self.forceClockToShow.setChecked(self.getSettings("DisableHideWithTaskbar"))
        self.forceClockToShow.stateChanged.connect(lambda i: self.setSettings("DisableHideWithTaskbar", bool(i)))
        self.clockSettingsTitle.addWidget(self.forceClockToShow)
        self.hideClockWhenClicked = QSettingsCheckBox(_("Hide the clock during 10 seconds when clicked"))
        self.hideClockWhenClicked.setChecked(self.getSettings("HideClockWhenClicked"))
        self.hideClockWhenClicked.stateChanged.connect(lambda i: self.setSettings("HideClockWhenClicked", bool(i)))
        self.clockSettingsTitle.addWidget(self.hideClockWhenClicked)
        self.hideClockWhenHovered = QSettingsCheckBox(_("Hide the clock during 5 seconds when hoveredwith the mouse"))
        self.hideClockWhenHovered.setChecked(self.getSettings("HideClockWhenHovered"))
        self.hideClockWhenHovered.stateChanged.connect(lambda i: self.setSettings("HideClockWhenHovered", bool(i)))
        self.hideClockWhenHovered.setStyleSheet("border-top: 0px solid transparent;")
        self.clockSettingsTitle.addWidget(self.hideClockWhenHovered)
        self.autoreloadclocks = QSettingsCheckBox(_("Reload clocks automatically every 5 minutes"))
        self.autoreloadclocks.setChecked(self.getSettings("AutoReloadClocks"))
        self.autoreloadclocks.stateChanged.connect(lambda i: self.setSettings("AutoReloadClocks", bool(i)))
        self.clockSettingsTitle.addWidget(self.autoreloadclocks)
        self.enableLowCpuMode = QSettingsCheckBoxWithWarning(_("Enable low-cpu mode"), _("You might lose functionalities, like the notification counter or the dynamic background"))
        self.enableLowCpuMode.setStyleSheet(f"QWidget#stChkBg{{border-bottom-left-radius: 8px;border-bottom-right-radius: 8px;border-bottom: 1px;}}")
        self.enableLowCpuMode.setChecked(self.getSettings("EnableLowCpuMode"))
        self.enableLowCpuMode.stateChanged.connect(lambda i: self.setSettings("EnableLowCpuMode", bool(i)))
        self.clockSettingsTitle.addWidget(self.enableLowCpuMode)

        self.clockFeaturesTitle = QSettingsTitle(_("Clock features:"), getPath(f"plugin_{self.iconMode}.png"), _("Notification badge, clicked action, show desktop button, etc."))
        layout.addWidget(self.clockFeaturesTitle)
        self.disableNotificationBadge = QSettingsCheckBox(_("Disable the notification badge"))
        self.disableNotificationBadge.setChecked(self.getSettings("DisableNotifications"))
        self.disableNotificationBadge.stateChanged.connect(lambda i: self.setSettings("DisableNotifications", bool(i)))
        self.clockFeaturesTitle.addWidget(self.disableNotificationBadge)
        self.disableTooltip = QSettingsCheckBox(_("Disable the tooltip shown when the clock is hovered"))
        self.disableTooltip.setChecked(self.getSettings("DisableToolTip"))
        self.disableTooltip.stateChanged.connect(lambda i: self.setSettings("DisableToolTip", bool(i)))
        self.clockFeaturesTitle.addWidget(self.disableTooltip)
        self.showDesktopButton = QSettingsCheckBox(_("Add the \"Show Desktop\" button on the left corner of every clock"))
        self.showDesktopButton.setChecked(self.getSettings("ShowDesktopButton"))
        self.showDesktopButton.stateChanged.connect(lambda i: self.setSettings("ShowDesktopButton", bool(i)))
        self.clockFeaturesTitle.addWidget(self.showDesktopButton)
        self.customClockAction = QSettingsSizeBoxComboBox(_("Change the action done when the clock is clicked"))
        clkactions = {
            _("Show calendar"): "Win+N",
            _("Copy date/time"): "copy_datetime",
            _("Disabled"): "f20",
            _("Open quick settings"): "Win+A",
            _("Show desktop"): "Win+d",
            _("Open run dialog"): "Win+R",
            _("Open task manager"): "Ctrl+Shift+Esc",
            _("Open start menu"): "Win",
            _("Open search menu"): "Win+S",
            _("Change task"): "AltRight+Tab",
        }
        self.customClockAction.loadItems(clkactions.keys())
        self.customClockAction.setChecked(self.getSettings("CustomClockClickAction"))
        try:
            self.customClockAction.combobox.setCurrentIndex(list(clkactions.values()).index(self.getSettingsValue("CustomClockClickAction")))
        except ValueError:
            pass
        self.customClockAction.stateChanged.connect(lambda i: self.setSettings("CustomClockClickAction", bool(i)))
        self.customClockAction.valueChanged.connect(lambda v: (self.setSettingsValue("CustomClockClickAction", clkactions[str(v)])))
        self.clockFeaturesTitle.addWidget(self.customClockAction)
        self.customDoubleClickAction = QSettingsSizeBoxComboBox(_("Change the action done when the clock is double-clicked"))
        self.customDoubleClickAction.setStyleSheet("border-top: 0px solid transparent;")
        dblactions = {
            _("Show calendar"): "Win+N",
            _("Copy date/time"): "copy_datetime",
            _("Empty the recycle bin"): "trashcan",
            _("Empty the recycle bin (Without confirmation)"): "trashcan_noconfirm",
            _("Disabled"): "f20",
            _("Open quick settings"): "Win+A",
            _("Show desktop"): "Win+d",
            _("Open run dialog"): "Win+R",
            _("Open task manager"): "Ctrl+Shift+Esc",
            _("Open start menu"): "Win",
            _("Open search menu"): "Win+S",
            _("Change task"): "AltRight+Tab",
        }
        self.customDoubleClickAction.loadItems(dblactions.keys())
        self.customDoubleClickAction.setChecked(self.getSettings("CustomClockDoubleClickAction"))
        try:
            self.customDoubleClickAction.combobox.setCurrentIndex(list(dblactions.values()).index(self.getSettingsValue("CustomClockDoubleClickAction")))
        except ValueError:
            pass
        self.customDoubleClickAction.stateChanged.connect(lambda i: self.setSettings("CustomClockDoubleClickAction", bool(i)))
        self.customDoubleClickAction.valueChanged.connect(lambda v: self.setSettingsValue("CustomClockDoubleClickAction", dblactions[v]))
        self.clockFeaturesTitle.addWidget(self.customDoubleClickAction)
        self.customDoubleClickAction = QSettingsSizeBoxComboBox(_("Change the action done when the clock is middle-clicked"))
        self.customDoubleClickAction.setStyleSheet("border-top: 0px solid transparent;")
        dblactions = {
            _("Show calendar"): "Win+N",
            _("Copy date/time"): "copy_datetime",
            _("Empty the recycle bin"): "trashcan",
            _("Empty the recycle bin (Without confirmation)"): "trashcan_noconfirm",
            _("Disabled"): "f20",
            _("Open quick settings"): "Win+A",
            _("Show desktop"): "Win+d",
            _("Open run dialog"): "Win+R",
            _("Open task manager"): "Ctrl+Shift+Esc",
            _("Open start menu"): "Win",
            _("Open search menu"): "Win+S",
            _("Change task"): "AltRight+Tab",
        }
        self.customDoubleClickAction.loadItems(dblactions.keys())
        self.customDoubleClickAction.setChecked(self.getSettings("CustomClockMiddleClickAction"))
        try:
            self.customDoubleClickAction.combobox.setCurrentIndex(list(dblactions.values()).index(self.getSettingsValue("CustomClockMiddleClickAction")))
        except ValueError:
            pass
        self.customDoubleClickAction.stateChanged.connect(lambda i: self.setSettings("CustomClockMiddleClickAction", bool(i)))
        self.customDoubleClickAction.valueChanged.connect(lambda v: self.setSettingsValue("CustomClockMiddleClickAction", dblactions[v]))
        self.clockFeaturesTitle.addWidget(self.customDoubleClickAction)


        self.clockPosTitle = QSettingsTitle(_("Clock position and size:"), getPath(f"size_{self.iconMode}.png"), _("Clock size preferences, position offset, clock at the left, etc."))
        layout.addWidget(self.clockPosTitle)
        self.clockAtLeft = QSettingsCheckBox(_("Show the clock at the left of the screen"))
        self.clockAtLeft.setChecked(self.getSettings("ClockOnTheLeft"))
        self.clockAtLeft.stateChanged.connect(lambda i: self.setSettings("ClockOnTheLeft", bool(i)))
        self.clockPosTitle.addWidget(self.clockAtLeft)
        self.clockAtBottom = QSettingsCheckBox(_("Force the clock to be at the bottom of the screen"))
        self.clockAtBottom.setChecked(self.getSettings("ForceOnBottom"))
        self.clockAtBottom.stateChanged.connect(lambda i: self.setSettings("ForceOnBottom", bool(i)))
        self.clockPosTitle.addWidget(self.clockAtBottom)
        self.clockAtTop = QSettingsCheckBox(_("Force the clock to be at the top of the screen"))
        self.clockAtTop.setChecked(self.getSettings("ForceOnTop"))
        self.clockAtTop.stateChanged.connect(lambda i: self.setSettings("ForceOnTop", bool(i)))
        self.clockPosTitle.addWidget(self.clockAtTop)
        self.clockAtTop.setStyleSheet("border-top: 0px solid transparent;")
        self.PinClockToDesktop = QSettingsCheckBox(_("Pin the clock to the desktop"))
        self.PinClockToDesktop.setChecked(self.getSettings("PinClockToTheDesktop"))
        self.PinClockToDesktop.stateChanged.connect(lambda i: self.setSettings("PinClockToTheDesktop", bool(i)))
        self.clockPosTitle.addWidget(self.PinClockToDesktop)
        self.clockFixedHeight = QSettingsSliderWithCheckBox(_("Change the height of the clock"), self, 20, 105, 48)
        self.clockFixedHeight.setChecked(self.getSettings("ClockFixedHeight"))
        if self.clockFixedHeight.isChecked():
            try:
                self.clockFixedHeight.slider.setValue(int(self.getSettingsValue("ClockFixedHeight")))
            except ValueError:
                print("🟠 Unable to parse int from ClockFixedHeight settings value")
        self.clockFixedHeight.stateChanged.connect(lambda v: self.setSettings("ClockFixedHeight", bool(v)))
        self.clockFixedHeight.valueChanged.connect(lambda v: self.setSettingsValue("ClockFixedHeight", str(v)))
        self.clockPosTitle.addWidget(self.clockFixedHeight)
        self.ClockFixedWidth = QSettingsSliderWithCheckBox(_("Change the width of the clock"), self, 30, 200, 48)
        self.ClockFixedWidth.setStyleSheet("border-top: 0px solid transparent;")
        self.ClockFixedWidth.setChecked(self.getSettings("ClockFixedWidth"))
        if self.ClockFixedWidth.isChecked():
            try:
                self.ClockFixedWidth.slider.setValue(int(self.getSettingsValue("ClockFixedWidth")))
            except ValueError:
                print("🟠 Unable to parse int from ClockFixedWidth settings value")
        self.ClockFixedWidth.stateChanged.connect(lambda v: self.setSettings("ClockFixedWidth", bool(v)))
        self.ClockFixedWidth.valueChanged.connect(lambda v: self.setSettingsValue("ClockFixedWidth", str(v)))
        self.clockPosTitle.addWidget(self.ClockFixedWidth)

        self.clockXOffset = QSettingsSliderWithCheckBox(_("Adjust horizontal clock position"), self, -200, 200, 0)
        self.clockXOffset.setChecked(self.getSettings("ClockXOffset"))
        if self.clockXOffset.isChecked():
            try:
                self.clockXOffset.slider.setValue(int(self.getSettingsValue("ClockXOffset")))
            except ValueError:
                print("🟠 Unable to parse int from ClockXOffset settings value")
        self.clockXOffset.stateChanged.connect(lambda v: self.setSettings("ClockXOffset", bool(v)))
        self.clockXOffset.valueChanged.connect(lambda v: self.setSettingsValue("ClockXOffset", str(v)))
        self.clockPosTitle.addWidget(self.clockXOffset)

        self.clockYOffset = QSettingsSliderWithCheckBox(_("Adjust vertical clock position"), self, -200, 200, 0)
        self.clockYOffset.setStyleSheet("border-top: 0px solid transparent;")
        self.clockYOffset.setChecked(self.getSettings("ClockYOffset"))
        if self.clockYOffset.isChecked():
            try:
                self.clockYOffset.slider.setValue(int(self.getSettingsValue("ClockYOffset")))
            except ValueError:
                print("🟠 Unable to parse int from clockYOffset settings value")
        self.clockYOffset.stateChanged.connect(lambda v: self.setSettings("ClockYOffset", bool(v)))
        self.clockYOffset.valueChanged.connect(lambda v: self.setSettingsValue("ClockYOffset", str(v)))
        self.clockPosTitle.addWidget(self.clockYOffset)
        def unblacklist():
            global msg
            self.setSettingsValue("BlacklistedMonitors", "")
            globals.restartClocks()
            msg = QFramelessDialog(parent=self, closeOnClick=True)
            msg.setAutoFillBackground(True)
            msg.setStyleSheet(globals.sw.styleSheet())
            msg.setAttribute(Qt.WA_StyledBackground)
            msg.setObjectName("QMessageBox")
            msg.setTitle(_("Success")+"!")
            msg.setText(f"""{_("The monitors were unblacklisted successfully.")}<br>
    {_("Now you should see the clock everywhere")}""")
            msg.addButton(_("Ok"), QDialogButtonBox.ButtonRole.ApplyRole)
            msg.setDefaultButtonRole(QDialogButtonBox.ButtonRole.ApplyRole, self.styleSheet())
            msg.show()

        self.unBlackListButton = QSettingsButton(_("Reset monitor blacklisting status"), _("Reset"))
        self.unBlackListButton.clicked.connect(unblacklist)
        self.clockPosTitle.addWidget(self.unBlackListButton)

        self.clockAppearanceTitle = QSettingsTitle(_("Clock Appearance:"), getPath(f"appearance_{self.iconMode}.png"), _("Clock's font, font size, font color and background, text alignment"))
        layout.addWidget(self.clockAppearanceTitle)
        self.fontPrefs = QSettingsFontBoxComboBox(_("Use a custom font"))
        self.fontPrefs.setChecked(self.getSettings("UseCustomFont"))
        if self.fontPrefs.isChecked():
            customFont = self.getSettingsValue("UseCustomFont")
            if customFont:
                f = QFont()
                f.fromString(self.getSettingsValue("UseCustomFont"))
                self.fontPrefs.fontPicker.setCurrentFont(f)
                self.fontPrefs.button.setFont(f)
        self.fontPrefs.stateChanged.connect(lambda i: self.setSettings("UseCustomFont", bool(i)))
        self.fontPrefs.valueChanged.connect(lambda v: self.setSettingsValue("UseCustomFont", v))
        self.clockAppearanceTitle.addWidget(self.fontPrefs)

        self.fontSize = QSettingsSizeBoxComboBox(_("Use a custom font size"))
        self.fontSize.setStyleSheet("border-top: 0px solid transparent;")
        self.fontSize.setChecked(self.getSettings("UseCustomFontSize"))
        self.fontSize.loadItems()
        if self.fontSize.isChecked():
            customFontSize = self.getSettingsValue("UseCustomFontSize")
            if customFontSize:
                self.fontSize.combobox.setCurrentText(customFontSize)
        else:
                self.fontSize.combobox.setCurrentText("9")
        self.fontSize.stateChanged.connect(lambda i: self.setSettings("UseCustomFontSize", bool(i)))
        
        def setCustomFont(v):
            self.setSettingsValue("UseCustomFontSize", v, r=not(self.fontPrefs.isChecked()))
            if self.fontPrefs.isChecked():
                f = self.fontPrefs.fontPicker.currentFont()
                f.setPointSizeF(float(v))
                self.fontPrefs.fontPicker.setCurrentFont(f)
                self.fontPrefs.valuechangedEvent(f)
                self.fontPrefs.button.setFont(f)
                
        self.fontSize.valueChanged.connect(lambda v: setCustomFont(v))
        self.clockAppearanceTitle.addWidget(self.fontSize)
    
        self.fontColor = QSettingsCheckboxColorDialog(_("Use a custom font color"))
        self.fontColor.setStyleSheet("border-top: 0px solid transparent;")
        self.fontColor.setChecked(self.getSettings("UseCustomFontColor"))
        if self.fontColor.isChecked():
            self.fontColor.button.setStyleSheet(f"color: rgb({self.getSettingsValue('UseCustomFontColor')})")
        self.fontColor.stateChanged.connect(lambda i: (self.setSettings("UseCustomFontColor", bool(i))))
        self.fontColor.valueChanged.connect(lambda v: self.setSettingsValue("UseCustomFontColor", v))
        self.clockAppearanceTitle.addWidget(self.fontColor)
        
        self.lineHeight = QSettingsSizeBoxComboBox(_("Use a custom line height"))
        self.lineHeight.setChecked(self.getSettings("CustomLineHeight"))
        self.lineHeight.loadItems([i/100 for i in range(5, 300, 5)])
        if self.lineHeight.isChecked():
            try:
                customlineHeight = self.getSettingsValue("CustomLineHeight")
                if customlineHeight == "":
                    customlineHeight = "1"
            except Exception as e:
                customlineHeight = "1"
            self.lineHeight.combobox.setCurrentText(customlineHeight)
        else:
            self.lineHeight.combobox.setCurrentText("1")
        self.lineHeight.stateChanged.connect(lambda i: self.setSettings("CustomLineHeight", bool(i)))
        self.lineHeight.valueChanged.connect(lambda v: self.setSettingsValue("CustomLineHeight", v))
        self.centerText = QSettingsCheckBox(_("Align the clock text to the center"))
        self.centerText.setChecked(self.getSettings("CenterAlignment"))
        self.centerText.stateChanged.connect(lambda i: self.setSettings("CenterAlignment", bool(i)))
        self.clockAppearanceTitle.addWidget(self.centerText)
        self.clockAppearanceTitle.addWidget(self.lineHeight)
        self.backgroundcolor = QSettingsBgBoxColorDialog(_("Use a custom background color"))
        self.backgroundcolor.setChecked(self.getSettings("UseCustomBgColor"))
        self.backgroundcolor.colorDialog.setOption(QColorDialog.ShowAlphaChannel, True)
        if self.backgroundcolor.isChecked():
            self.backgroundcolor.button.setStyleSheet(f"background-color: rgba({self.getSettingsValue('UseCustomBgColor')})")
        self.backgroundcolor.stateChanged.connect(lambda i: self.setSettings("UseCustomBgColor", bool(i)))
        self.backgroundcolor.valueChanged.connect(lambda v: self.setSettingsValue("UseCustomBgColor", v))
        self.clockAppearanceTitle.addWidget(self.backgroundcolor)        
        self.disableClocckBlurryBackgound = QSettingsCheckBox(_("Disable clock blurry texture"))
        self.disableClocckBlurryBackgound.setStyleSheet("border-top: 0px solid transparent;")
        self.disableClocckBlurryBackgound.setChecked(self.getSettings("DisableBlurryTexture"))
        self.disableClocckBlurryBackgound.stateChanged.connect(lambda i: self.setSettings("DisableBlurryTexture", bool(i)))
        self.disableClocckBlurryBackgound.setStyleSheet(f"QWidget#stChkBg{{border-bottom-left-radius: 8px;border-bottom-right-radius: 8px;border-bottom: 1px;}}")
        self.clockAppearanceTitle.addWidget(self.disableClocckBlurryBackgound)


        self.dateTimeTitle = QSettingsTitle(_("Date & Time Settings:"), getPath(f"datetime_{self.iconMode}.png"), _("Date format, Time format, seconds,weekday, weeknumber, regional settings"))
        layout.addWidget(self.dateTimeTitle)
        rulesText = f"""<b>{_("Custom format rules:")}</b>
        <ul>
        <li>{_("Any text can be placed here. To place items such as date and time, please use the 1989 C standard. Check the format codes on the following link:")} <a href="https://strftime.org" style="color:{f"rgb({getColors()[2 if isWindowDark() else 4]})"}">{_("Python date and time formats")}</a>
        <li>{_("To disable the zero-padding effect, add a # in between the % and the code: non-zero-padded hours would be %#H, and zero-padded hours would be %H")}</li>
        <li>{_("Click on Apply to apply and preview the format")}</li></ul>
        {_("If you don't understand what is happening, please uncheck the checkbox over the text area")}
        """
        self.customDateTimeFormat = QSettingsLineEditCheckBox(_("Set a custom date and time format")+" "+_("(for advanced users only)"))
        self.customDateTimeFormat.edit.setPlainText(self.getSettingsValue("CustomClockStrings"))
        self.customDateTimeFormat.setChecked(self.getSettings("CustomClockStrings"))
        self.customDateTimeFormat.setLabelText(rulesText)
        self.customDateTimeFormat.stateChanged.connect(lambda i: (self.setSettings("CustomClockStrings", bool(i)), self.dateTimeTitle.resizeEvent()))
        self.customDateTimeFormat.valueChanged.connect(lambda v: self.setSettingsValue("CustomClockStrings", v))
        self.dateTimeTitle.addWidget(self.customDateTimeFormat)
        self.showTime = QSettingsCheckBox(_("Show time on the clock"))
        self.showTime.setChecked(not self.getSettings("DisableTime"))
        self.showTime.stateChanged.connect(lambda i: self.setSettings("DisableTime", not bool(i)))
        self.dateTimeTitle.addWidget(self.showTime)
        self.showSeconds = QSettingsCheckBox(_("Show seconds on the clock"))
        self.showSeconds.setChecked(self.getSettings("EnableSeconds"))
        self.showSeconds.stateChanged.connect(lambda i: self.setSettings("EnableSeconds", bool(i)))
        self.dateTimeTitle.addWidget(self.showSeconds)
        self.showDate = QSettingsCheckBox(_("Show date on the clock"))
        self.showDate.setChecked(not self.getSettings("DisableDate"))
        self.showDate.stateChanged.connect(lambda i: self.setSettings("DisableDate", not bool(i)))
        self.dateTimeTitle.addWidget(self.showDate)
        self.showWeekCount = QSettingsCheckBox(_("Show week number on the clock"))
        self.showWeekCount.setChecked(self.getSettings("EnableWeekNumber"))
        self.showWeekCount.stateChanged.connect(lambda i: self.setSettings("EnableWeekNumber", bool(i)))
        self.dateTimeTitle.addWidget(self.showWeekCount)
        self.showWeekday = QSettingsCheckBox(_("Show weekday on the clock"))
        self.showWeekday.setChecked(self.getSettings("EnableWeekDay"))
        self.showWeekday.stateChanged.connect(lambda i: self.setSettings("EnableWeekDay", bool(i)))
        self.dateTimeTitle.addWidget(self.showWeekday)
        self.RegionButton = QSettingsButton(_("Change date and time format (Regional settings)"), _("Regional settings"))
        self.RegionButton.clicked.connect(lambda: os.startfile("intl.cpl"))
        self.dateTimeTitle.addWidget(self.RegionButton)


        self.internetTimeTitle = QSettingsTitle(_("Internet date and time"), getPath(f"internet_{self.iconMode}.png"), _("Select internet time provider, change sync frequency"))
        layout.addWidget(self.internetTimeTitle)

        self.internetTime = QSettingsCheckBox(_("Enable internet time sync"), None)
        self.internetTime.setChecked(self.getSettings("EnableInternetTime"))
        self.internetTime.stateChanged.connect(lambda e: self.setSettings("EnableInternetTime", e))
        self.internetTimeTitle.addWidget(self.internetTime)

        self.internetTimeURL = QSettingsCheckBoxTextBox(_("Set a custom network time provider"), None, f"<a style='color:rgb({getColors()[2 if isWindowDark() else 4]})' href=\"https://www.marticliment.com/redirect?ECNetworkTime\">{_('Help')}</a>")
        self.internetTimeURL.setPlaceholderText(_("Paste a URL from the world clock api or equivalent"))
        self.internetTimeURL.setText(self.getSettingsValue("AtomicClockURL"))
        self.internetTimeURL.setChecked(self.getSettings("AtomicClockURL"))
        self.internetTimeURL.stateChanged.connect(lambda e: self.setSettings("AtomicClockURL", e))
        self.internetTimeURL.valueChanged.connect(lambda v: (self.setSettingsValue("AtomicClockURL", v, r=False), self.setSettings("ReloadInternetTime", True)))
        self.internetTimeTitle.addWidget(self.internetTimeURL)

        self.internetSyncTime = QSettingsComboBox(_("Internet sync frequency"))
        actions = {
            _("10 minutes"): "600",
            _("30 minutes"): "1800",
            _("1 hour"): "3600",
            _("2 hours"): "7200",
            _("4 hours"): "14400",
            _("10 hours"): "36000",
            _("24 hours"): "86400",
        }
        self.internetSyncTime.loadItems(actions.keys())
        self.internetSyncTime.setEnabled(True)
        try:
            self.internetSyncTime.combobox.setCurrentIndex(list(actions.values()).index(self.getSettingsValue("AtomicClockSyncInterval")))
        except ValueError:
            pass
        self.internetSyncTime.valueChanged.connect(lambda v: (self.setSettingsValue("AtomicClockSyncInterval", actions[v]), self.setSettings("ReloadInternetTime", True)))
        self.internetTimeTitle.addWidget(self.internetSyncTime)

        self.toolTipAppearanceTitle = QSettingsTitle(_("Tooltip Appearance:"), getPath(f"tooltip_{self.iconMode}.png"), _("Tooltip's font, font size, font color and background"))
        layout.addWidget(self.toolTipAppearanceTitle)
        self.toolTipFontPrefs = QSettingsNewFontBoxComboBox(_("Use a custom font"))
        self.toolTipFontPrefs.setChecked(self.getSettings("TooltipUseCustomFont"))
        if self.toolTipFontPrefs.isChecked():
            customFont = self.getSettingsValue("TooltipUseCustomFont")
            if customFont:
                f = QFont()
                f.fromString(self.getSettingsValue("TooltipUseCustomFont"))
                self.fontPrefs.fontPicker.setCurrentFont(f)
                self.fontPrefs.button.setFont(f)
        self.toolTipFontPrefs.stateChanged.connect(lambda i: self.setSettings("TooltipUseCustomFont", bool(i)))
        self.toolTipFontPrefs.valueChanged.connect(lambda v: self.setSettingsValue("TooltipUseCustomFont", v))
        self.toolTipAppearanceTitle.addWidget(self.toolTipFontPrefs)

        self.toolTipFontSize = QSettingsSizeBoxComboBox(_("Use a custom font size"))
        self.toolTipFontSize.setStyleSheet("border-top: 0px solid transparent;")
        self.toolTipFontSize.setChecked(self.getSettings("TooltipUseCustomFontSize"))
        self.toolTipFontSize.loadItems()
        if self.toolTipFontSize.isChecked():
            customFontSize = self.getSettingsValue("TooltipUseCustomFontSize")
            if customFontSize:
                self.toolTipFontSize.combobox.setCurrentText(customFontSize)
        else:
                self.toolTipFontSize.combobox.setCurrentText("9")
        self.toolTipFontSize.stateChanged.connect(lambda i: self.setSettings("TooltipUseCustomFontSize", bool(i)))
        self.toolTipFontSize.valueChanged.connect(lambda v: self.setSettingsValue("TooltipUseCustomFontSize", v))
        self.toolTipAppearanceTitle.addWidget(self.toolTipFontSize)

        self.toolTipFontColor = QSettingsCheckboxColorDialog(_("Use a custom font color"))
        self.toolTipFontColor.setStyleSheet("border-top: 0px solid transparent;")
        self.toolTipFontColor.setChecked(self.getSettings("TooltipUseCustomFontColor"))
        if self.toolTipFontColor.isChecked():
            self.toolTipFontColor.button.setStyleSheet(f"color: rgb({self.getSettingsValue('TooltipUseCustomFontColor')})")
        self.toolTipFontColor.stateChanged.connect(lambda i: self.setSettings("TooltipUseCustomFontColor", bool(i)))
        self.toolTipFontColor.valueChanged.connect(lambda v: self.setSettingsValue("TooltipUseCustomFontColor", v))
        self.toolTipAppearanceTitle.addWidget(self.toolTipFontColor)
        self.disableBlurryBackground = QSettingsCheckBox(_("Disable tooltip's blurry background"))
        self.disableBlurryBackground.setChecked(self.getSettings("TooltipDisableTaskbarBackgroundColor"))
        self.disableBlurryBackground.stateChanged.connect(lambda i: self.setSettings("TooltipDisableTaskbarBackgroundColor", bool(i)))
        self.toolTipAppearanceTitle.addWidget(self.disableBlurryBackground)
        self.toolTipBackgroundColor = QSettingsBgBoxColorDialog(_("Use a custom background color"))
        self.toolTipBackgroundColor.setChecked(self.getSettings("TooltipUseCustomBgColor"))
        self.toolTipBackgroundColor.colorDialog.setOption(QColorDialog.ShowAlphaChannel, True)
        if self.toolTipBackgroundColor.isChecked():
            self.toolTipBackgroundColor.button.setStyleSheet(f"background-color: rgba({self.getSettingsValue('TooltipUseCustomBgColor')})")
        self.toolTipBackgroundColor.stateChanged.connect(lambda i: self.setSettings("TooltipUseCustomBgColor", bool(i)))
        self.toolTipBackgroundColor.valueChanged.connect(lambda v: self.setSettingsValue("TooltipUseCustomBgColor", v))
        self.toolTipBackgroundColor.setStyleSheet(f"QWidget#stChkBg{{border-bottom-left-radius: 8px;border-bottom-right-radius: 8px;border-bottom: 1px;}}")
        self.toolTipAppearanceTitle.addWidget(self.toolTipBackgroundColor)
        self.toolTipBackgroundColor.setStyleSheet("border-top: 0px solid transparent;")


        self.experimentalTitle = QSettingsTitle(_("Fixes and other experimental features: (Use ONLY if something is not working)"), getPath(f"experiment_{self.iconMode}.png"), _("Testing features and error-fixing tools"))
        layout.addWidget(self.experimentalTitle)
        self.bypassCNAMECheck = QSettingsCheckBox(_("Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"))
        self.bypassCNAMECheck.setChecked(self.getSettings("BypassDomainAuthCheck"))
        self.bypassCNAMECheck.stateChanged.connect(lambda i: self.setSettings("BypassDomainAuthCheck", bool(i), r = False))
        self.experimentalTitle.addWidget(self.bypassCNAMECheck)
        self.fixDash = QSettingsCheckBox(_("Reload clocks right after exiting from sleep"))
        self.fixDash.setChecked(self.getSettings("PreventSleepFailure"))
        self.fixDash.stateChanged.connect(lambda i: self.setSettings("PreventSleepFailure", bool(i)))
        self.experimentalTitle.addWidget(self.fixDash)
        self.disableLang = QSettingsCheckBox(_("Do NOT update the language files dynamically"))
        self.disableLang.setChecked(self.getSettings("DisableLangAutoUpdater"))
        self.disableLang.stateChanged.connect(lambda i: self.setSettings("DisableLangAutoUpdater", bool(i)))
        self.experimentalTitle.addWidget(self.disableLang)
        self.longerDoubleClickPeriod = QSettingsCheckBox(_("Increase the length of the double-click period"))
        self.longerDoubleClickPeriod.setChecked(self.getSettings("DoubleClickLongerPeriod"))
        self.longerDoubleClickPeriod.stateChanged.connect(lambda i: self.setSettings("DoubleClickLongerPeriod", bool(i)))
        self.experimentalTitle.addWidget(self.longerDoubleClickPeriod)
        self.disableClockCover = QSettingsCheckBox(_("Disable hiding the default windows clock"))
        self.disableClockCover.setChecked(self.getSettings("DisableSystemClockCover"))
        self.disableClockCover.stateChanged.connect(lambda i: self.setSettings("DisableSystemClockCover", bool(i)))
        self.disableClockCover.setStyleSheet(f"QWidget#stChkBg{{border-bottom-left-radius: 8px;border-bottom-right-radius: 8px;border-bottom: 1px;}}")
        self.experimentalTitle.addWidget(self.disableClockCover)

        self.languageSettingsTitle = QSettingsTitle(_("About the language pack:"), getPath(f"lang_{self.iconMode}.png"), _("Language pack author(s), help translating ElevenClock"))
        layout.addWidget(self.languageSettingsTitle)
        self.PackInfoButton = QSettingsButton(_("Translated to English by martinet101"), "")
        self.PackInfoButton.button.hide()
        self.PackInfoButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0;border-bottom-right-radius: 0;border-bottom: 0;}")
        self.languageSettingsTitle.addWidget(self.PackInfoButton)
        self.openTranslateButton = QSettingsButton(_("Translate ElevenClock to your language"), _("Get started"))
        self.openTranslateButton.clicked.connect(lambda: os.startfile("https://github.com/marticliment/ElevenClock/wiki/#translating-elevenclock"))
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
                <style> a {{color: rgb({colors[2 if isWindowDark() else 4]})}}</style>
                <ul>
                <li> <b>Dateutil</b>: <a href="https://github.com/dateutil/dateutil/blob/master/LICENSE">Apache 2 License</a></li>
                <li> <b>Frameless Window</b>: <a href="https://github.com/mustafaahci/FramelessWindow/blob/master/LICENSE">The Unlicense</a></li>
                <li> <b>Keyboard</b>: <a href="https://github.com/boppreh/keyboard/blob/master/LICENSE.txt">MIT License</a></li>
                <li> <b>Psutil</b>: <a href="https://github.com/giampaolo/psutil/blob/master/LICENSE">BSD 3-Clause</a></li>
                <li> <b>PyAutoGui</b>: <a href="https://github.com/asweigart/pyautogui/">BSD-3 Clause New</a></li>
                <li> <b>PyInstaller</b>: <a href="https://www.pyinstaller.org/license.html">Custom GPL</a></li>
                <li> <b>PySide6 (Qt6)</b>: <a href="https://www.qt.io/download-open-source">GPL-v3</a></li>
                <li> <b>PyWin32</b>: <a href="https://pypi.org/project/pywin32/">PSF-2.0</a></li>
                <li> <b>Python 3</b>: <a href="https://docs.python.org/3/license.html">PSF License Agreement</a></li>
                <li> <b>TzLocal</b>: <a href="https://github.com/regebro/tzlocal/blob/master/LICENSE.txt">MIT License</a></li>
                <li> <b>WNFUN</b>: <a href="https://github.com/ionescu007/wnfun/blob/master/LICENSE">BSD 2-Clause</a></li>
                <li> <b>Win32mica</b> (Also made by me): <a href="https://github.com/marticliment/pymica/blob/master/LICENSE">MIT License</a></li>
                <li> <b>WinShell</b>: <a href="https://github.com/tjguk/winshell/blob/master/LICENSE.txt">MIT License</a></li>
                </ul>    """)
            msg.addButton(_("Ok"), QDialogButtonBox.ButtonRole.ApplyRole, lambda: msg.close())
            msg.addButton(_("More Info"), QDialogButtonBox.ButtonRole.ResetRole, lambda: os.startfile("https://github.com/marticliment/ElevenClock/wiki#third-party-libraries"))
            def closeAndQt():
                msg.close()
                QMessageBox.aboutQt(self, "ElevenClock - "+_("About Qt"))
            msg.addButton(_("About Qt"), QDialogButtonBox.ButtonRole.ResetRole, lambda: closeAndQt())
            msg.setDefaultButtonRole(QDialogButtonBox.ButtonRole.ApplyRole, self.styleSheet())
            msg.show()

        def exportSettings():
            nonlocal self
            try:
                rawstr = ""
                for file in glob.glob(os.path.join(os.path.expanduser("~"), ".elevenclock/*")):
                    if not "Running" in file and not "png" in file and not "PreferredLanguage" in file:
                        sName = file.replace("\\", "/").split("/")[-1]
                        rawstr += sName+"|@|"+getSettingsValue(sName)+"|~|"
                fileName = QFileDialog.getSaveFileName(self, _("Export settings to a local file"), os.path.expanduser("~"), "ElevenClock Settings File (*.esf);;All Files (*.*)")
                if fileName[0] != "":
                    oFile =  open(fileName[0], "w")
                    oFile.write(rawstr)
                    oFile.close()
                    subprocess.run("explorer /select,\""+fileName[0].replace('/', '\\')+"\"", shell=True)
            except Exception as e:
                report(e)

        def importSettings():
            nonlocal self
            try:
                fileName = QFileDialog.getOpenFileName(self, _("Import settings from a local file"), os.path.expanduser("~"), "ElevenClock Settings File (*.esf);;All Files (*.*)")
                if fileName:
                    iFile = open(fileName[0], "r")
                    rawstr = iFile.read()
                    iFile.close()
                    resetSettings()
                    for element in rawstr.split("|~|"):
                        pairValue = element.split("|@|")
                        if len(pairValue) == 2:
                            setSettings(pairValue[0], True, r=False)
                            if pairValue[1] != "":
                                setSettingsValue(pairValue[0], pairValue[1], r=False)
                    os.startfile(sys.executable)
                    globals.app.quit()
            except Exception as e:
                report(e)

        def resetSettings():
            for file in glob.glob(os.path.join(os.path.expanduser("~"), ".elevenclock/*")):
                if not "Running" in file:
                    try:
                        os.remove(file)
                    except:
                        pass

        def getAppVersion():
            return f"{versionName} {platform.architecture()[0]} (version code {version})"

        def getSystemInfo():
            release = platform.release()
            try:
                if int(platform.version().split('.')[-1]) >= 22000:
                    release = "11"
            except Exception as e:
                report(e)
            return f"{platform.system()} {release} {platform.win32_edition()} {platform.version()}"

        def getTotalRAM():
            try:
                total_ram = bytes2human(psutil.virtual_memory().total)
                if total_ram[-1] != "B":
                    total_ram += "B"
                return total_ram
            except Exception as e:
                report(e)
                return "Unknown"

        self.aboutTitle = QSettingsTitle(_("About ElevenClock version {0}:").format(versionName), getPath(f"about_{self.iconMode}.png"), _("Info, report a bug, submit a feature request, donate, about"))
        layout.addWidget(self.aboutTitle)
        self.WebPageButton = QSettingsButton(_("View ElevenClock's homepage"), _("Open"))
        self.WebPageButton.clicked.connect(lambda: os.startfile("https://marticliment.com/elevenclock/"))
        self.WebPageButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0;border-bottom-right-radius: 0;border-bottom: 0;}")
        self.aboutTitle.addWidget(self.WebPageButton)
        self.ThirdParty = QSettingsButton(_("Third party licenses"), _("View"))
        self.ThirdParty.clicked.connect(lambda: thirdPartyLicenses())
        self.ThirdParty.setStyleSheet("QWidget#stBtn{border-top: 0px solid transparent;border-bottom-left-radius: 0;border-bottom-right-radius: 0;border-bottom: 0;}")
        self.aboutTitle.addWidget(self.ThirdParty)
        self.IssueButton = QSettingsButton(_("Report an issue/request a feature"), _("Report"))
        self.IssueButton.clicked.connect(lambda: os.startfile("https://github.com/marticliment/ElevenClock/issues/new/choose"))
        self.IssueButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0;border-bottom-right-radius: 0;border-bottom: 0;}")
        self.aboutTitle.addWidget(self.IssueButton)
        self.CofeeButton = QSettingsButton(_("Support the dev: Give me a coffee☕"), _("Open page"))
        self.CofeeButton.clicked.connect(lambda: os.startfile("https://ko-fi.com/martinet101"))
        self.CofeeButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0;border-bottom-right-radius: 0;border-bottom: 0;}")
        self.aboutTitle.addWidget(self.CofeeButton)
        self.importSettings = QSettingsButton(_("Import settings from a local file"), _("Import"))
        self.importSettings.clicked.connect(lambda: importSettings())
        self.importSettings.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0;border-bottom-right-radius: 0;border-bottom: 0;}")
        self.aboutTitle.addWidget(self.importSettings)
        self.exportSettings = QSettingsButton(_("Export settings to a local file"), _("Export"))
        self.exportSettings.clicked.connect(lambda: exportSettings())
        self.exportSettings.setStyleSheet("QWidget#stBtn{border-top: 0px solid transparent;border-bottom-left-radius: 0;border-bottom-right-radius: 0;border-bottom: 0;}")
        self.aboutTitle.addWidget(self.exportSettings)
        self.resetButton = QSettingsButton(_("Reset ElevenClock preferences to defaults"), _("Reset"))
        self.resetButton.setStyleSheet("QWidget#stBtn{border-top: 0px solid transparent;border-bottom-left-radius: 0;border-bottom-right-radius: 0;border-bottom: 0;}")
        self.resetButton.clicked.connect(lambda: (resetSettings(), os.startfile(sys.executable), globals.app.quit()))
        self.aboutTitle.addWidget(self.resetButton)
        self.closeButton = QSettingsButton(_("Close settings"), _("Close"))
        self.closeButton.clicked.connect(lambda: self.hide())
        self.aboutTitle.addWidget(self.closeButton)


        self.debbuggingTitle = QSettingsTitle(_("Debbugging information:"), getPath(f"bug_{self.iconMode}.png"), _("Log, debugging information"))
        layout.addWidget(self.debbuggingTitle)
        self.helpButton = QSettingsButton(_("Open online help to troubleshoot problems"), _("Open"))
        self.helpButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0;border-bottom-right-radius: 0;border-bottom: 0;}")
        self.helpButton.clicked.connect(lambda: os.startfile("https://github.com/marticliment/ElevenClock/wiki#Troubleshooting"))
        self.debbuggingTitle.addWidget(self.helpButton)
        self.logButton = QSettingsButton(_("Open ElevenClock's log"), _("Open"))
        self.logButton.clicked.connect(lambda: self.openLogWindow())
        self.logButton.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0;border-bottom-right-radius: 0;border-bottom: 0;}")
        self.debbuggingTitle.addWidget(self.logButton)
        hiddenButtonList = [
            _("ElevenClock version:") + " " + getAppVersion(),
            _("System version:") + " " + getSystemInfo(),
            _("System architecture:") + " " + platform.machine(),
            "",
            _("Total RAM:") + " " + getTotalRAM(),
            "",
            _("System locale:") + " " + locale.getdefaultlocale()[0],
            _("ElevenClock language locale:") + f" lang_{langName}",
        ]
        self.hiddenButton = QSettingsButton("\n".join(hiddenButtonList), "", h=len(hiddenButtonList)*17.5)
        self.hiddenButton.button.setVisible(False)
        self.debbuggingTitle.addWidget(self.hiddenButton)

        self.notFoundLabel = QLabel(_("No results were found"))
        if isWindowDark():
            self.notFoundLabel.setStyleSheet(f"padding-top: 30px;font-size: 16pt; font-weight: bold; color: rgba(255, 255, 255, 50%)")
        else:
            self.notFoundLabel.setStyleSheet(f"padding-top: 30px;font-size: 16pt; font-weight: bold; color: rgba(0, 0, 0, 50%)")

        self.notFoundLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.notFoundLabel)
        self.notFoundLabel.hide()

        layout.addSpacing(15)
        layout.addStretch()


        class QStaticWidget(QWidget):
            def __init__(self) -> None:
                super().__init__()
                self.setFixedHeight(1)


        self.settingsWidget.setLayout(layout)
        self.scrollArea.setWidget(self.settingsWidget)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setStyleSheet(f"QScrollArea{{border-bottom-left-radius: 8px;border-bottom-right-radius: 8px;}}")

        self.searchBox = QLineEdit()
        self.searchBox.setClearButtonEnabled(True)
        self.searchBox.setPlaceholderText(_("Search on the settings"))
        self.searchBox.setContentsMargins(0, 0, 25, 0)
        self.searchBox.textChanged.connect(self.filter)

        titleLayout = QHBoxLayout()
        titleLayout.setContentsMargins(0, 0, 0, 0)
        titleLayout.setSpacing(0)
        titleLayout.addWidget(self.title, stretch=1)
        titleLayout.addWidget(self.searchBox)

        svl = QVBoxLayout()
        svl.setSpacing(0)
        svl.setContentsMargins(0, 0, 0, 0)
        svl.addLayout(titleLayout, stretch=0)
        svl.addWidget(self.scrollArea, stretch=1)

        self.staticVerticalWidget = QWidget()
        self.staticVerticalWidget.setMaximumWidth(1000)
        self.staticVerticalWidget.setLayout(svl)

        self.scrollbar = QScrollBar()
        self.scrollArea.setVerticalScrollBar(self.scrollbar)

        shl = QHBoxLayout()
        shl.setSpacing(0)
        shl.setContentsMargins(0, 0, 0, 0)
        shl.addSpacing(16)
        shl.addWidget(QStaticWidget(), stretch=0)
        shl.addWidget(self.staticVerticalWidget, stretch=1)
        shl.addWidget(QStaticWidget(), stretch=0)
        shl.addWidget(self.scrollbar, stretch=0)


        self.vlayout.addLayout(shl)

        self.setWindowTitle(_("ElevenClock Settings"))
        self.applyStyleSheet()
        self.updateCheckBoxesStatus()
        w = QWidget()
        w.setObjectName("borderBackground")
        w.setLayout(self.vlayout)
        self.setCentralWidget(w)
        self.setMouseTracking(True)
        self.resize((1100), (700))
        self.hwnd = self.winId().__int__()
        
        ExtendFrameIntoClientArea(self.winId().__int__())
        self.installEventFilter(self)
        if winver < 22581:
            self.setWindowTitle("")
            pixmap = QPixmap(32, 32)
            pixmap.fill(Qt.transparent)
            self.setWindowIcon(QIcon(pixmap))
        else:
            self.setWindowTitle(""+_("ElevenClock Settings"))
            self.setWindowIcon(QIcon(getPath("icon.ico")))

    def filter(self, query: str):
        widgets: list[QSettingsTitle] = (
            self.generalSettingsTitle,
            self.clockSettingsTitle,
            self.clockFeaturesTitle,
            self.clockPosTitle,
            self.clockAppearanceTitle,
            self.dateTimeTitle,
            self.experimentalTitle,
            self.languageSettingsTitle,
            self.toolTipAppearanceTitle,
            self.internetTimeTitle,
            self.aboutTitle,
            self.debbuggingTitle
        )
        if query != "":
            self.announcements.hide()
            found = False
            for w in widgets:
                for item in w.getChildren():
                    if query.lower() in item.text().lower():
                        item.show()
                        w.childrenOpacity.setOpacity(1)
                        found = True
                    else:
                        item.hide()
                w.searchMode = True
                w.resizeEvent(QResizeEvent(w.size(), w.size()))
                if not found:
                    self.notFoundLabel.show()
                else:
                    self.notFoundLabel.hide()
        else:
            self.announcements.show()
            for w in widgets:
                w.childrenOpacity.setOpacity(0)
                for item in w.getChildren():
                        item.show()
                w.searchMode = False
                self.notFoundLabel.hide()
                w.resizeEvent(QResizeEvent(w.size(), w.size()))
                if w.childsVisible:
                    w.toggleChilds()

    def showEvent(self, event: QShowEvent) -> None:
        self.applyStyleSheet()
        Thread(target=self.announcements.loadAnnouncements, daemon=True, name="Settings: Announce loader").start()
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
        if not self.customDateTimeFormat.isChecked():
            for item in (self.showTime, self.showSeconds, self.showDate, self.showWeekCount, self.showWeekday):
                item: QSettingsCheckBox
                item.setVisible(True)

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
        else:
            for item in (self.showTime, self.showSeconds, self.showDate, self.showWeekCount, self.showWeekday):
                item: QSettingsCheckBox
                item.setVisible(False)
        self.dateTimeTitle.resizeEvent()

        if not self.legacyHideOnFullScreen.isChecked():
            self.TransparentClockWhenInFullscreen.setEnabled(True)
            self.TransparentClockWhenInFullscreen.setToolTip("")
        else:
            self.TransparentClockWhenInFullscreen.setEnabled(False)
            self.TransparentClockWhenInFullscreen.setToolTip(_("<b>{0}</b> needs to be enabled to change this setting").format(_("Hide the clock in fullscreen mode")))

        if self.enableLowCpuMode.isChecked():
            self.disableNotificationBadge.setToolTip(_("<b>{0}</b> needs to be disabled to change this setting").format(_("Enable low-cpu mode")))
            self.disableNotificationBadge.setEnabled(False)
        else:
            self.disableNotificationBadge.setToolTip("")
            self.disableNotificationBadge.setEnabled(True)

        if self.internetTime.isChecked():
            self.internetSyncTime.setEnabled(True)
            self.internetSyncTime.setToolTip("")
            self.internetTimeURL.setEnabled(True)
            self.internetTimeURL.setToolTip("")
        else:
            self.internetSyncTime.setEnabled(False)
            self.internetSyncTime.setToolTip(_("<b>{0}</b> needs to be enabled to change this setting").format(_("Sync time with the internet")))
            self.internetTimeURL.setEnabled(False)
            self.internetTimeURL.setToolTip(_("<b>{0}</b> needs to be enabled to change this setting").format(_("Sync time with the internet")))



    def applyStyleSheet(self):
        self.staticVerticalWidget.setMaximumWidth(1000)
        colors = getColors()
        self.iconMode = getAppIconMode()
        if isWindowDark():
            micar = ApplyMica(self.winId().__int__(), MICAMODE.DARK)
            if self.lastTheme != 0:
                self.lastTheme = 0
                self.aboutTitle.setIcon(getPath(f"about_{self.iconMode}.png"))
                self.dateTimeTitle.setIcon(getPath(f"datetime_{self.iconMode}.png"))
                self.clockSettingsTitle.setIcon(getPath(f"clock_{self.iconMode}.png"))
                self.clockFeaturesTitle.setIcon(getPath(f"plugin_{self.iconMode}.png"))
                self.languageSettingsTitle.setIcon(getPath(f"lang_{self.iconMode}.png"))
                self.generalSettingsTitle.setIcon(getPath(f"settings_{self.iconMode}.png"))
                self.experimentalTitle.setIcon(getPath(f"experiment_{self.iconMode}.png"))
                self.clockPosTitle.setIcon(getPath(f"size_{self.iconMode}.png"))
                self.debbuggingTitle.setIcon(QIcon(getPath(f"bug_{self.iconMode}.png")))
                self.toolTipAppearanceTitle.setIcon(QIcon(getPath(f"tooltip_{self.iconMode}.png")))
                self.internetTimeTitle.setIcon(QIcon(getPath(f"internet_{self.iconMode}.png")))
                self.clockAppearanceTitle.setIcon(QIcon(getPath(f"appearance_{self.iconMode}.png")))
                self.setStyleSheet(f"""
                    *::disabled {{
                        color: grey;
                    }}
                    #backgroundWindow {{

                        background-color: {"transparent" if micar == 0x0 else "#262626"};
                    }}
                    #titlebarButton {{
                        border-radius: 0;
                        border:none;
                        background-color: rgba(0, 0, 0, 0.01);
                    }}
                    #titlebarButton:hover {{
                        border-radius: 0;
                        background-color: rgba(80, 80, 80, 25%);
                    }}
                    #closeButton {{
                        border-radius: 0;
                        border:none;
                        background-color: rgba(0, 0, 0, 0.01);
                    }}
                    #closeButton:hover {{
                        border-radius: 0;
                        background-color: rgba(196, 43, 28, 25%);
                    }}
                    QSlider {{
                        background: transparent;
                        height: 20px;
                        margin-left: 10px;
                        margin-right: 10px;
                        border-radius: 2px;
                    }}
                    QSlider::groove {{
                        height: 4px;
                        border: 1px solid #212121;
                        background: #212121;
                        border-radius: 2px;
                    }}
                    QSlider::handle {{
                        border: 4px solid #404040;
                        margin: -8px -10px;
                        height: 8px;
                        border-radius: 9px;
                        background: rgb({colors[0]});
                    }}
                    QSlider::handle:hover {{
                        border: 3px solid #404040;
                        margin: -8px -10px;
                        height: 7px;
                        border-radius: 9px;
                        background: rgb({colors[0]});
                    }}
                    QSlider::handle:disabled {{
                        border: 4px solid #404040;
                        margin: -8px -10px;
                        height: 8px;
                        border-radius: 9px;
                        background: #212121;
                    }}
                    QSlider::add-page {{
                        border-radius: 3px;
                        background: #303030;
                    }}
                    QSlider::sub-page {{
                        border-radius: 3px;
                        background: rgb({colors[0]});
                    }}
                    QSlider::add-page:disabled {{
                        border-radius: 2px;
                        background: #212121;
                    }}
                    QSlider::sub-page:disabled {{
                        border-radius: 2px;
                        background: #212121;
                    }}
                    QToolTip {{
                        border: 1px solid #222222;
                        padding: 4px;
                        border-radius: 8px;
                        background-color: #262626;
                    }}
                    QMenu {{
                        border: 1px solid rgb(60, 60, 60);
                        padding: 2px;
                        outline: 0;
                        color: white;
                        background: #262626;
                        border-radius: 8px;
                    }}
                    QMenu::separator {{
                        margin: 2px;
                        height: 1px;
                        background: rgb(60, 60, 60);
                    }}
                    QMenu::icon{{
                        padding-left: 10px;
                    }}
                    QMenu::item{{
                        height: 30px;
                        border: none;
                        background: transparent;
                        padding-right: 10px;
                        padding-left: 10px;
                        border-radius: 4px;
                        margin: 2px;
                    }}
                    QMenu::item:selected{{
                        background: rgba(255, 255, 255, 10%);
                        height: 30px;
                        outline: none;
                        border: none;
                        padding-right: 10px;
                        padding-left: 10px;
                        border-radius: 4px;
                    }}
                    QMenu::item:selected:disabled{{
                        background: transparent;
                        height: 30px;
                        outline: none;
                        border: none;
                        padding-right: 10px;
                        padding-left: 10px;
                        border-radius: 4px;
                    }}
                    QColorDialog {{
                        background-color: transparent;
                        border: none;
                    }}
                    QLineEdit {{
                        background-color: #212121;
                        font-family: "Segoe UI Variable Text";
                        selection-background-color: rgb({colors[4]});
                        font-size: 9pt;
                        width: 300px;
                        padding: 5px;
                        margin-bottom: 5px;
                        border-radius: 8px;
                        border: 0.6px solid #262626;
                        border-bottom: 2px solid rgb({colors[1]});
                    }}
                    QLineEdit:disabled {{
                        background-color: #303030;
                        font-family: "Segoe UI Variable Text";
                        font-size: 9pt;
                        width: 300px;
                        padding: 5px;
                        border-radius: 8px;
                        border: 0.6px solid #262626;
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
                        font-weight: medium;
                    }}
                    * {{
                        color: white;
                        font-size: 9pt;
                        font-family: "Segoe UI Variable Text";
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
                        border-radius: 6px;
                        border: 1px solid #161616;
                        selection-background-color: rgb({colors[4]});
                    }}
                    QSpinBox {{
                        background-color: rgba(81, 81, 81, 25%);
                        border-radius: 8px;
                        border: 1px solid rgba(86, 86, 86, 25%);
                        height: 25px;
                        border-top: 1px solid rgba(99, 99, 99, 25%);
                    }}
                    QPushButton,#FocusLabel {{
                        width: 200px;
                        background-color:rgba(81, 81, 81, 25%);
                        border-radius: 8px;
                        border: 1px solid rgba(86, 86, 86, 25%);
                        height: 30px;
                        border-top: 1px solid rgba(99, 99, 99, 25%);
                    }}
                    QPushButton:hover {{
                        background-color:rgba(86, 86, 86, 25%);
                        border-radius: 8px;
                        border: 1px solid rgba(100, 100, 100, 25%);
                        height: 30px;
                        border-top: 1px solid rgba(107, 107, 107, 25%);
                    }}
                    QPushButton:disabled {{
                        background-color:rgba(86, 86, 86, 10%);
                        border-radius: 8px;
                        border: 1px solid rgba(100, 100, 100, 10%);
                        height: 30px;
                    }}
                    #AccentButton{{
                        color: black;
                        background-color: rgb({colors[1]});
                        border-color: rgb({colors[1]});
                        border-bottom-color: rgb({colors[2]});
                    }}
                    #AccentButton:disabled{{
                        color: lightgrey;
                        background-color: #303030;
                        border-color: #222222;
                    }}
                    #AccentButton:hover{{
                        background-color: rgba({colors[1]}, 80%);
                        border-color: rgb({colors[2]});
                        border-bottom-color: rgb({colors[2]});
                    }}
                    #AccentButton:pressed{{
                        color: #555555;
                        background-color: rgba({colors[1]}, 80%);
                        border-color: rgb({colors[2]});
                        border-bottom-color: rgb({colors[2]});
                    }}
                    #title{{
                        margin: 2px;
                        margin-bottom: 0;
                        padding-left: 20px;
                        padding-right: 20px;
                        padding-top: 15px;
                        padding-bottom: 15px;
                        font-size: 13pt;
                        border-radius: 4px;
                        font-family: "Segoe UI Variable Display";
                        font-weight: bold;
                    }}
                    #subtitleLabelHover {{
                        background-color: rgba(20, 20, 20, 0.01);
                        margin: 10px;
                        margin-top: 0;
                        margin-bottom: 0;
                        border-radius: 4px;
                        border-top-left-radius: 8px;
                        border-top-right-radius: 8px;
                        border: 1px solid transparent;
                    }}
                    #subtitleLabelHover:hover{{
                        background-color: rgba(255, 255, 255, 3%);
                        margin: 10px;
                        margin-top: 0;
                        margin-bottom: 0;
                        padding-left: 20px;
                        padding-top: 0;
                        padding-bottom: 0;
                        border: 1px solid rgba(255, 255, 255, 7%);
                        font-size: 13pt;
                        border-top-left-radius: 8px;
                        border-top-right-radius: 8px;
                    }}
                    #subtitleLabelHover:pressed{{
                        background-color: rgba(0, 0, 0, 12%);
                        margin: 10px;
                        margin-top: 0;
                        margin-bottom: 0;
                        padding-left: 20px;
                        padding-right: 20px;
                        padding-top: 0;
                        padding-bottom: 0;
                        border: 1px solid rgba(255, 255, 255, 7%);
                        font-size: 13pt;
                        border-top-left-radius: 8px;
                        border-top-right-radius: 8px;
                    }}
                    #micaRegularBackground {{
                        border: 0 solid transparent;
                        margin: 1px;
                        background-color: rgba(255, 255, 255, 5%);
                        border-radius: 8px;
                    }}
                    #subtitleLabel{{
                        margin: 10px;
                        margin-bottom: 0;
                        margin-top: 0;
                        padding-left: 20px;
                        padding-right: 20px;
                        padding-top: 15px;
                        padding-bottom: 15px;
                        border: 1px solid rgba(25, 25, 25, 50%);
                        font-size: 13pt;
                        border-top-left-radius: 8px;
                        border-top-right-radius: 8px;
                    }}
                    #StLbl{{
                        padding: 0;
                        background-color: rgba(71, 71, 71, 0%);
                        margin: 0;
                        border:none;
                        font-size: 11px;
                    }}
                    #stBtn{{
                        background-color: rgba(255, 255, 255, 5%);
                        margin: 10px;
                        margin-bottom: 0;
                        margin-top: 0;
                        border: 1px solid rgba(25, 25, 25, 50%);
                        border-bottom-left-radius: 8px;
                        border-bottom-right-radius: 8px;
                    }}
                    #lastWidget{{
                        border-bottom-left-radius: 4px;
                        border-bottom-right-radius: 4px;
                    }}
                    #stChkBg{{
                        padding: 15px;
                        padding-left: 45px;
                        padding-right: 45px;
                        background-color: rgba(255, 255, 255, 5%);
                        margin: 10px;
                        margin-bottom: 0;
                        margin-top: 0;
                        border: 1px solid rgba(25, 25, 25, 50%);
                        border-bottom: 0;
                    }}
                    QCheckBox::indicator{{
                        height: 20px;
                        width: 20px;
                    }}
                    QCheckBox::indicator:unchecked {{
                        background-color: rgba(30, 30, 30, 25%);
                        border: 1px solid #444444;
                        border-radius: 6px;
                    }}
                    QCheckBox::indicator:disabled {{
                        background-color: rgba(71, 71, 71, 0%);
                        color: #bbbbbb;
                        border: 1px solid #444444;
                        border-radius: 6px;
                    }}
                    QCheckBox::indicator:unchecked:hover {{
                        background-color: #2a2a2a;
                        border: 1px solid #444444;
                        border-radius: 6px;
                    }}
                    QCheckBox::indicator:checked {{
                        border: 1px solid #444444;
                        background-color: rgb({colors[1]});
                        border-radius: 6px;
                        image: url("{getPath("tick_white.png")}");
                    }}
                    QCheckBox::indicator:checked:disabled {{
                        border: 1px solid #444444;
                        background-color: #303030;
                        color: #bbbbbb;
                        border-radius: 6px;
                        image: url("{getPath("tick_black.png")}");
                    }}
                    QCheckBox::indicator:checked:hover {{
                        border: 1px solid #444444;
                        background-color: rgb({colors[2]});
                        border-radius: 6px;
                        image: url("{getPath("tick_white.png")}");
                    }}
                    QComboBox {{
                        width: 200px;
                        background-color:rgba(81, 81, 81, 15%);
                        border-radius: 8px;
                        border: 1px solid rgba(86, 86, 86, 15%);
                        height: 30px;
                        border-top: 1px solid rgba(99, 99, 99, 15%);
                        padding-left: 10px;
                        padding-right: 10px;
                    }}
                    QComboBox:hover {{
                        background-color:rgba(86, 86, 86, 25%);
                        border-radius: 8px;
                        border: 1px solid rgba(100, 100, 100, 15%);
                        height: 30px;
                        border-top: 1px solid rgba(107, 107, 107, 15%);
                    }}
                    QComboBox:disabled {{
                        background-color:rgba(86, 86, 86, 10%);
                        border-radius: 8px;
                        border: 1px solid rgba(100, 100, 100, 10%);
                        height: 30px;
                    }}
                    QComboBox::drop-down {{
                        subcontrol-origin: padding;
                        subcontrol-position: top right;
                        padding: 5px;
                        border-radius: 8px;
                        border: none;
                        width: 30px;
                    }}
                    QComboBox::down-arrow {{
                        image: url("{getPath(f"down-arrow_{self.iconMode}.png")}");
                        height: 8px;
                        width: 8px;
                    }}
                    QComboBox::down-arrow:disabled {{
                        image: url("{getPath(f"down-arrow_{self.iconMode}.png")}");
                        height: 8px;
                        width: 8px;
                    }}
                    QAbstractItemView {{
                        border: 1px solid rgba(90, 90, 90, 25%);
                        padding: 4px;
                        outline: 0;
                        padding-right: 0;
                        background-color: rgba(71, 71, 71, 25%);
                        border-radius: 8px;
                    }}
                    QAbstractItemView::item{{
                        height: 30px;
                        border: none;
                        padding-left: 10px;
                        border-radius: 4px;
                    }}
                    QAbstractItemView::item:selected{{
                        background: rgba(255, 255, 255, 6%);
                        color: white;
                        height: 30px;
                        outline: none;
                        border: none;
                        padding-left: 10px;
                        border-radius: 4px;
                    }}
                    QAbstractItemView::item:focus{{
                        background: rgba(255, 255, 255, 6%);
                        color: rgb({colors[2]});
                        height: 30px;
                        outline: none;
                        border: none;
                        padding-left: 10px;
                        border-radius: 4px;
                    }}
                    QSCrollArea, QVBoxLayout{{
                        border: none;
                        margin: none;
                        padding: none;
                        outline: none;
                    }}
                    QScrollBar {{
                        background: transparent;
                        margin: 4px;
                        margin-left: 0;
                        width: 16px;
                        height: 20px;
                        border: none;
                        border-radius: 5px;
                    }}
                    QScrollBar:horizontal {{
                        margin-bottom: 0;
                        padding-bottom: 0;
                        height: 12px;
                    }}
                    QScrollBar::handle {{
                        margin: 3px;
                        min-height: 20px;
                        min-width: 20px;
                        border-radius: 3px;
                        background: rgba(80, 80, 80, 40%);
                    }}
                    QScrollBar::handle:hover {{
                        margin: 3px;
                        border-radius: 3px;
                        background: rgba(112, 112, 112, 35%);
                    }}
                    QScrollBar::add-line {{
                        height: 0;
                        width: 0;
                        subcontrol-position: bottom;
                        subcontrol-origin: margin;
                    }}
                    QScrollBar::sub-line {{
                        height: 0;
                        width: 0;
                        subcontrol-position: top;
                        subcontrol-origin: margin;
                    }}
                    QScrollBar::up-arrow, QScrollBar::down-arrow {{
                        background: none;
                    }}
                    QScrollBar::add-page, QScrollBar::sub-page {{
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
                    QGroupBox {{
                        background-color: rgba(80, 80, 80, 25%);
                        border-radius: 8px;
                        border: 1px solid rgba(196, 196, 196, 25%);
                        border-bottom: 1px solid rgba(204, 204, 204, 25%);
                        padding-top: 20px;
                    }}
                    QGroupBox::title {{
                        subcontrol-origin: margin;
                        padding: 5px;
                        border: none;
                    }}
                    """)
        else:
            micar = ApplyMica(self.winId().__int__(), MICAMODE.LIGHT)
            if self.lastTheme != 1:
                self.lastTheme = 1
                self.aboutTitle.setIcon(getPath(f"about_{self.iconMode}.png"))
                self.dateTimeTitle.setIcon(getPath(f"datetime_{self.iconMode}.png"))
                self.clockSettingsTitle.setIcon(getPath(f"clock_{self.iconMode}.png"))
                self.clockFeaturesTitle.setIcon(getPath(f"plugin_{self.iconMode}.png"))
                self.languageSettingsTitle.setIcon(getPath(f"lang_{self.iconMode}.png"))
                self.generalSettingsTitle.setIcon(getPath(f"settings_{self.iconMode}.png"))
                self.experimentalTitle.setIcon(getPath(f"experiment_{self.iconMode}.png"))
                self.clockPosTitle.setIcon(getPath(f"size_{self.iconMode}.png"))
                self.debbuggingTitle.setIcon(QIcon(getPath(f"bug_{self.iconMode}.png")))
                self.toolTipAppearanceTitle.setIcon(QIcon(getPath(f"tooltip_{self.iconMode}.png")))
                self.internetTimeTitle.setIcon(QIcon(getPath(f"internet_{self.iconMode}.png")))
                self.clockAppearanceTitle.setIcon(QIcon(getPath(f"appearance_{self.iconMode}.png")))
                self.setStyleSheet(f"""
                    *::disabled {{
                        color: grey;
                    }}
                    #backgroundWindow {{
                        background-color: {"transparent" if micar == 0x0 else "#ffffff"};
                    }}
                    #titlebarButton {{
                        border-radius: 0;
                        border:none;
                        background-color: rgba(0, 0, 0, 0.01);
                    }}
                    #micaRegularBackground {{
                        border: 0 solid #dddddd;
                        margin: 1px;
                        background-color: rgba(0, 0, 0, 0%);
                        border-radius: 8px;
                    }}
                    #titlebarButton:hover {{
                        border-radius: 0;
                        background-color: rgba({colors[4]}, 1);
                    }}
                    #closeButton {{
                        border-radius: 0;
                        border:none;
                        background-color: rgba(0, 0, 0, 0.01);
                    }}
                    #closeButton:hover {{
                        border-radius: 0;
                        background-color: rgba(196, 43, 28, 1);
                    }}
                    QSlider {{
                        background-color: transparent;
                        height: 20px;
                        margin-left: 10px;
                        margin-right: 10px;
                        border-radius: 2px;
                    }}
                    QSlider::groove {{
                        height: 4px;
                        border-radius: 2px;
                        border: 1px solid rgba(150, 150, 150, 100%);
                        background: transparent;
                    }}
                    QSlider::groove:disabled {{
                        height: 4px;
                        border-radius: 2px;
                        background: transparent;
                    }} 
                    QSlider::handle {{
                        border: 4px solid #cccccc;
                        margin: -8px -10px;
                        height: 8px;
                        border-radius: 9px;
                        background: rgb({colors[3]});
                    }}
                    QSlider::handle:hover {{
                        border: 3px solid #cccccc;
                        margin: -8px -10px;
                        height: 8px;
                        border-radius: 9px;
                        background: rgb({colors[3]});
                    }}
                    QSlider::handle:disabled {{
                        border: 4px solid #cccccc;
                        margin: -8px -10px;
                        height: 8px;
                        border-radius: 9px;
                        background: rgba(106, 106, 106, 100%);
                    }}
                    QSlider::add-page {{
                        border-radius: 3px;
                        background: #eeeeee;
                    }}
                    QSlider::sub-page {{
                        border-radius: 3px;
                        background: rgb({colors[4]});
                    }}
                    QSlider::add-page:disabled {{
                        border-radius: 3px;
                        background: #eeeeee;
                    }}
                    QSlider::sub-page:disabled {{
                        border-radius: 3px;
                        background: #eeeeee;
                    }}
                    QToolTip{{
                        border: 1px solid rgba(196, 196, 196, 25%);
                        padding: 4px;
                        border-radius: 8px;
                        background-color: #eeeeee;
                    }}
                    QPlainTextEdit{{
                        font-family: "Cascadia Mono";
                        background-color: rgba(255, 255, 255, 100%);
                        border-radius: 6px;
                        border: 1px solid #dddddd;
                        selection-background-color: rgb({colors[3]});
                    }}
                    QMenu {{
                        border: 1px solid rgb(200, 200, 200);
                        padding: 2px;
                        outline: 0;
                        color: black;
                        background: #eeeeee;
                        border-radius: 8px;
                    }}
                    QMenu::separator {{
                        margin: 2px;
                        height: 1px;
                        background: rgb(200, 200, 200);
                    }}
                    QMenu::icon{{
                        padding-left: 10px;
                    }}
                    QMenu::item{{
                        height: 30px;
                        border: none;
                        background: transparent;
                        padding-right: 10px;
                        padding-left: 10px;
                        border-radius: 4px;
                        margin: 2px;
                    }}
                    QMenu::item:selected{{
                        background: rgba(0, 0, 0, 10%);
                        height: 30px;
                        outline: none;
                        border: none;
                        padding-right: 10px;
                        padding-left: 10px;
                        border-radius: 4px;
                    }}
                    QMenu::item:selected:disabled{{
                        background: transparent;
                        height: 30px;
                        outline: none;
                        border: none;
                        padding-right: 10px;
                        padding-left: 10px;
                        border-radius: 4px;
                    }}
                    QColorDialog {{
                        background-color: transparent;
                        border: none;
                    }}
                    QLineEdit {{
                        background-color: #fefefe;
                        font-family: "Segoe UI Variable Text";
                        font-size: 9pt;
                        width: 300px;
                        padding: 5px;
                        border-radius: 8px;
                        border: 0.6px solid #eeeeee;
                        border-bottom: 2px solid rgb({colors[4]});
                    }}
                    QLineEdit:disabled {{
                        background-color: #f5f5f5;
                        font-family: "Segoe UI Variable Text";
                        font-size: 9pt;
                        width: 300px;
                        padding: 5px;
                        border-radius: 8px;
                        border: 0.6px solid #eeeeee;
                        /*border-bottom: 2px solid rgb({colors[4]});*/
                    }}
                    #background,QScrollArea,QMessageBox,QDialog,QSlider,#ControlWidget{{
                        color: white;
                        background-color: transparent;
                    }}
                    * {{
                        background-color: transparent;
                        color: black;
                        font-size: 9pt;
                        font-family: "Segoe UI Variable Text";
                    }}
                    #warningLabel {{
                        color: #bd0000;
                        background-color: transparent;
                    }}
                    QPushButton,#FocusLabel {{
                        width: 200px;
                        background-color: rgba(255, 255, 255, 70%);
                        border-radius: 8px;
                        border: 1px solid rgba(196, 196, 196, 25%);
                        height: 30px;
                        border-bottom: 1px solid rgba(204, 204, 204, 25%);
                    }}
                    QPushButton:hover {{
                        background-color: rgba(238, 238, 238, 100%);
                        border-radius: 8px;
                        border: 1px solid rgba(196, 196, 196, 25%);
                        height: 30px;
                        border-bottom: 1px solid rgba(204, 204, 204, 25%);
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
                        margin: 2px;
                        margin-bottom: 0;
                        padding-left: 20px;
                        padding-top: 15px;
                        padding-bottom: 15px;
                        font-family: "Segoe UI Variable Display semib";
                        font-size: 13pt;
                        border-radius: 8px;
                    }}
                    #subtitleLabel{{
                        background-color: rgba(255, 255, 255, 50%);
                        margin: 10px;
                        margin-bottom: 0;
                        margin-top: 0;
                        padding-left: 20px;
                        padding-top: 15px;
                        padding-bottom: 15px;
                        border-radius: 8px;
                        border: 1px solid rgba(220, 220, 220, 50%);
                        font-size: 13pt;
                        border-top-left-radius: 8px;
                        border-top-right-radius: 8px;
                    }}
                    #subtitleLabelHover {{
                        background-color: rgba(255, 255, 255, 1%);
                        margin: 10px;
                        margin-top: 0;
                        margin-bottom: 0;
                        border-radius: 8px;
                        border-top-left-radius: 8px;
                        border-top-right-radius: 8px;
                        border: 1px solid transparent;
                    }}
                    #subtitleLabelHover:hover{{
                        background-color: rgba(0, 0, 0, 2%);
                        margin: 10px;
                        margin-top: 0;
                        margin-bottom: 0;
                        padding-left: 20px;
                        padding-top: 15px;
                        padding-bottom: 15px;
                        border: 1px solid rgba(220, 220, 220, 50%);
                        border-bottom: 1px solid rgba(200, 200, 200, 50%);
                        font-size: 13pt;
                        border-top-left-radius: 8px;
                        border-top-right-radius: 8px;
                    }}
                    #StLbl{{
                        padding: 0;
                        background-color: rgba(255, 255, 255,0%);
                        margin: 0;
                        border:none;
                        font-size: 11px;
                    }}
                    #stBtn{{
                        background-color: rgba(255, 255, 255, 0%);
                        margin: 10px;
                        margin-bottom: 0;
                        margin-top: 0;
                        border: 1px solid rgba(196, 196, 196, 15%);
                        border-bottom: 0;
                        border-bottom-left-radius: 0;
                        border-bottom-right-radius: 0;
                    }}
                    #lastWidget{{
                        border-bottom-left-radius: 4px;
                        border-bottom-right-radius: 4px;
                        border-bottom: 1px;
                    }}
                    #stChkBg{{
                        padding: 15px;
                        padding-left: 45px;
                        background-color: rgba(255, 255, 255, 0%);
                        margin: 10px;
                        margin-bottom: 0;
                        margin-top: 0;
                        border: 1px solid rgba(196, 196, 196, 15%);
                        border-bottom: 0;
                    }}
                    QCheckBox::indicator{{
                        height: 20px;
                        width: 20px;
                    }}
                    QCheckBox::indicator:unchecked {{
                        background-color: rgba(255, 255, 255, 10%);
                        border: 1px solid rgba(136, 136, 136, 25%);
                        border-radius: 6px;
                    }}
                    QCheckBox::indicator:disabled {{
                        background-color: #eeeeee;
                        color: rgba(136, 136, 136, 25%);
                        border: 1px solid rgba(136, 136, 136, 25%);
                        border-radius: 6px;
                    }}
                    QCheckBox::indicator:unchecked:hover {{
                        background-color: #eeeeee;
                        border: 1px solid rgba(136, 136, 136, 25%);
                        border-radius: 6px;
                    }}
                    QCheckBox::indicator:checked {{
                        border: 0 solid rgba(136, 136, 136, 25%);
                        background-color: rgb({colors[3]});
                        border-radius: 5px;
                        image: url("{getPath("tick_black.png")}");
                    }}
                    QCheckBox::indicator:checked:hover {{
                        border: 0 solid rgba(136, 136, 136, 25%);
                        background-color: rgb({colors[2]});
                        border-radius: 5px;
                        image: url("{getPath("tick_black.png")}");
                    }}
                    QCheckBox::indicator:checked:disabled {{
                        border: 1px solid rgba(136, 136, 136, 25%);
                        background-color: #eeeeee;
                        color: rgba(136, 136, 136, 25%);
                        border-radius: 6px;
                        image: url("{getPath("tick_white.png")}");
                    }}
                    QComboBox {{
                        width: 100px;
                        background-color: rgba(255, 255, 255, 10%);
                        border-radius: 8px;
                        border: 1px solid rgba(196, 196, 196, 25%);
                        height: 25px;
                        padding-left: 10px;
                        padding-right: 10px;
                        border-bottom: 1px solid rgba(204, 204, 204, 25%);
                    }}
                    QComboBox:disabled {{
                        width: 100px;
                        background-color: #eeeeee;
                        border-radius: 8px;
                        border: 1px solid rgba(196, 196, 196, 25%);
                        height: 30px;
                        padding-left: 10px;
                        border-top: 1px solid rgba(196, 196, 196, 25%);
                    }}
                    QComboBox:hover {{
                        background-color: rgba(238, 238, 238, 25%);
                        border-radius: 8px;
                        border: 1px solid rgba(196, 196, 196, 25%);
                        height: 30px;
                        padding-left: 10px;
                        border-bottom: 1px solid rgba(204, 204, 204, 25%);
                    }}
                    QComboBox::drop-down {{
                        subcontrol-origin: padding;
                        subcontrol-position: top right;
                        padding: 5px;
                        border-radius: 8px;
                        border: none;
                        width: 30px;
                    }}
                    QComboBox::down-arrow {{
                        image: url("{getPath(f"down-arrow_{self.iconMode}.png")}");
                        height: 8px;
                        width: 8px;
                    }}
                    QComboBox::down-arrow:disabled {{
                        image: url("{getPath(f"down-arrow_{self.iconMode}.png")}");
                        height: 8px;
                        width: 8px;
                    }}
                    QAbstractItemView {{
                        border: 1px solid rgba(196, 196, 196, 25%);
                        padding: 4px;
                        outline: 0px;
                        background-color: rgba(255, 255, 255, 100%);
                        border-radius: 8px;
                    }}
                    QAbstractItemView::item{{
                        height: 30px;
                        border: none;
                        padding-left: 10px;
                        border-radius: 4px;
                    }}
                    QAbstractItemView::item:selected{{
                        background: rgba(240, 240, 240, 90%);
                        height: 30px;
                        outline: none;
                        color: black;
                        border: none;
                        padding-left: 10px;
                        border-radius: 4px;
                    }}
                    QAbstractItemView::item:focus{{
                        background: rgba(240, 240, 240, 80%);
                        color: rgb({colors[4]});
                        height: 30px;
                        outline: none;
                        border: none;
                        padding-left: 10px;
                        border-radius: 4px;
                    }}

                    QSCrollArea,QVBoxLayout{{
                        border: none;
                        margin: none;
                        padding: none;
                        outline: none;
                    }}
                    QScrollBar:vertical {{
                        background: rgba(255, 255, 255, 0%);
                        margin: 4px;
                        width: 20px;
                        border: none;
                        border-radius: 5px;
                    }}
                    QScrollBar::handle:vertical {{
                        margin: 3px;
                        border-radius: 3px;
                        min-height: 20px;
                        background: rgba(90, 90, 90, 25%);
                    }}
                    QScrollBar::handle:vertical:hover {{
                        margin: 3px;
                        border-radius: 3px;
                        background: rgba(90, 90, 90, 35%);
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

    def openLogWindow(self):
        global old_stdout, buffer

        class QPlainTextEditWithFluentMenu(QPlainTextEdit):
            def __init__(self):
                super().__init__()

            def contextMenuEvent(self, e: QtGui.QContextMenuEvent) -> None:
                menu = self.createStandardContextMenu()
                menu.addSeparator()

                a = QAction()
                a.setText(_("Reload log"))
                a.triggered.connect(lambda: textEdit.setPlainText(globals.buffer.getvalue()))
                menu.addAction(a)

                a4 = QAction()
                a4.setText(_("Show missing translation strings"))
                a4.triggered.connect(lambda: self.setPlainText('\n'.join(missingTranslationList)))
                menu.addAction(a4)

                a2 = QAction()
                a2.setText(_("Export log as a file"))
                a2.triggered.connect(lambda: saveLog())
                menu.addAction(a2)

                a3 = QAction()
                a3.setText(_("Copy log to clipboard"))
                a3.triggered.connect(lambda: copyLog())
                menu.addAction(a3)

                ApplyMenuBlur(menu.winId().__int__(), menu)
                menu.exec(e.globalPos())

        win = QMainWindow(self)
        win.resize((900), (600))
        win.setObjectName("background")

        w = QWidget()
        w.setLayout(QVBoxLayout())
        w.setContentsMargins(0, 0, 0, 0)

        textEdit = QPlainTextEditWithFluentMenu()
        textEdit.setReadOnly(True)
        if isWindowDark():
            textEdit.setStyleSheet(f"QPlainTextEdit{{margin: 10px;border-radius: 6px;border: 1px solid #161616;}}")
        else:
            textEdit.setStyleSheet(f"QPlainTextEdit{{margin: 10px;border-radius: 6px;border: 1px solid #dddddd;}}")

        textEdit.setPlainText(globals.buffer.getvalue())

        reloadButton = QPushButton(_("Reload log"))
        reloadButton.setFixedWidth(200)
        reloadButton.clicked.connect(lambda: textEdit.setPlainText(globals.buffer.getvalue()))

        def saveLog():
            try:
                print("🔵 Saving log...")
                f = QFileDialog.getSaveFileName(win, "Save log", os.path.expanduser("~"), "Text file (.txt)")
                if f[0]:
                    fpath = f[0]
                    if not ".txt" in fpath.lower():
                        fpath += ".txt"
                    with open(fpath, "wb") as fobj:
                        fobj.write(globals.buffer.getvalue().encode("utf-8"))
                        fobj.close()
                    os.startfile(fpath)
                    print("🟢 log saved successfully")
                    textEdit.setPlainText(globals.buffer.getvalue())
                else:
                    print("🟡 log save cancelled!")
                    textEdit.setPlainText(globals.buffer.getvalue())
            except Exception as e:
                report(e)
                textEdit.setPlainText(globals.buffer.getvalue())

        exportButtom = QPushButton(_("Export log as a file"))
        exportButtom.setFixedWidth(200)
        exportButtom.clicked.connect(lambda: saveLog())

        def copyLog():
            try:
                print("🔵 Copying log to the clipboard...")
                textToClipboard(globals.buffer.getvalue())
                print("🟢 Log copied to the clipboard successfully!")
                textEdit.setPlainText(globals.buffer.getvalue())
            except Exception as e:
                report(e)
                textEdit.setPlainText(globals.buffer.getvalue())

        copyButton = QPushButton(_("Copy log to clipboard"))
        copyButton.setFixedWidth(200)
        copyButton.clicked.connect(lambda: copyLog())

        hl = QHBoxLayout()
        hl.setSpacing(5)
        hl.setContentsMargins(10, 10, 10, 0)
        hl.addWidget(exportButtom)
        hl.addWidget(copyButton)
        hl.addStretch()
        hl.addWidget(reloadButton)

        w.layout().setSpacing(0)
        w.layout().setContentsMargins(5, 5, 5, 5)
        w.layout().addLayout(hl, stretch=0)
        w.layout().addWidget(textEdit, stretch=1)

        win.setCentralWidget(w)
        win.hwnd = win.winId().__int__()
        win.setAutoFillBackground(True)

        win.hwnd = win.winId().__int__()
        window_style = win32gui.GetWindowLong(win.hwnd, GWL_STYLE)
        win32gui.SetWindowLong(win.hwnd, GWL_STYLE, window_style | WS_POPUP | WS_THICKFRAME | WS_CAPTION | WS_SYSMENU)

        
        ExtendFrameIntoClientArea(self.winId().__int__())


        if ApplyMica(win.hwnd, isWindowDark()) != 0:
            if isWindowDark():
                GlobalBlur(win.winId().__int__(), Dark=True, Acrylic=True, hexColor="#333333ff")
            else:
                GlobalBlur(win.winId().__int__(), Dark=False, Acrylic=True, hexColor="#ffffffdd")

        win.show()
        win.setWindowTitle(_("ElevenClock's log"))
        """
        pixmap = QPixmap(32, 32)
        pixmap.fill(Qt.transparent)
        """
        win.setWindowIcon(QIcon(getPath("icon.png")))

    def moveEvent(self, event: QMoveEvent) -> None:
        self.updateSize = True
        super().moveEvent(event)

    def mouseReleaseEvent(self, event) -> None:
        if(self.updateSize):
            self.settingsWidget.resize(self.width()-(17), self.settingsWidget.height())
            if not self.isMaximized():
                self.scrollArea.setStyleSheet(f"QScrollArea{{border-bottom-left-radius: 4px;border-bottom-right-radius: 4px;}}")
            self.updateSize = False
        return super().mouseReleaseEvent(event)


    def show(self) -> None:
        self.raise_()
        self.applyStyleSheet()
        self.activateWindow()
        return super().show()

    

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QWindowStateChangeEvent:
            if self.isMaximized():
                self.scrollArea.setStyleSheet(f"QScrollArea{{border-bottom-left-radius: 0;border-bottom-right-radius: 0;}}")
            else:
                self.scrollArea.setStyleSheet(f"QScrollArea{{border-bottom-left-radius: 4px;border-bottom-right-radius: 4px;}}")
        return super().eventFilter(watched, event)


    def closeEvent(self, event: QCloseEvent) -> None:
        self.hide()
        event.ignore()

    def get6px(self, i: int) -> int:
        return round(i*self.screen().devicePixelRatio())
    
    def setSettings(self, s: str, v: bool, r: bool = True, thread = False):
        setSettings(s, v, r, thread, env = "")
        
    def setSettingsValue(self, s: str, v: bool, r: bool = True):
        setSettingsValue(s, v, r, env = "")
        
    def getSettings(self, s: str):
        return getSettings(s, env = "")
    
    def getSettingsValue(self, s: str):
        return getSettingsValue(s, env = "")



class QSettingsTitle(QWidget):
    oldScrollValue = 0
    showing = False
    searchMode = False
    childrenw = []
    callInMain = Signal(object)
    def __init__(self, text: str, icon: str, descText: str = "No description provided", dummy: bool = False):
        self.dummy = dummy
        if isWindowDark():
            self.iconMode = "white"
        else:
            self.iconMode = "black"
        super().__init__()
        self.callInMain.connect(lambda f: f())
        self.icon = icon
        self.setObjectName("subtitleLabel")
        self.label = QLabel(text, self)
        self.label.setAlignment(Qt.AlignLeft)
        self.setMaximumWidth(1000)
        self.descLabel = QLabel(descText, self)
        self.bg70 = QWidget(self)
        self.bg70.setObjectName("micaRegularBackground")
        self.descLabel.setObjectName("greyishLabel")
        if lang["locale"] == "zh_TW":
            self.label.setStyleSheet("font-size: 10pt;background: none;font-family: \"Microsoft JhengHei UI\";")
            self.descLabel.setStyleSheet("font-size: 8pt;background: none;font-family: \"Microsoft JhengHei UI\";")
        elif lang["locale"] == "zh_CN":
            self.label.setStyleSheet("font-size: 10pt;background: none;font-family: \"Microsoft YaHei UI\";")
            self.descLabel.setStyleSheet("font-size: 8pt;background: none;font-family: \"Microsoft YaHei UI\";")
        else:
            self.label.setStyleSheet(f"font-size: 10pt;background: none;font-family: \"Segoe UI Variable Display Semib\";")
            self.descLabel.setStyleSheet(f"font-size: 8pt;background: none;font-family: \"Segoe UI Variable Text\";")

        self.image = QLabel(self)
        self.image.setStyleSheet(f"padding: 1px;background: transparent;")
        self.setAttribute(Qt.WA_StyledBackground)
        self.compressibleWidget = QWidget(self)
        self.compressibleWidget.show()
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

        self.setStyleSheet(f"QWidget#subtitleLabel{{border-bottom-left-radius: 8px;border-bottom-right-radius: 8px;}}")
        self.bg70.setStyleSheet(f"QWidget#subtitleLabel{{border-bottom-left-radius: 8px;border-bottom-right-radius: 8px;}}")


        self.showAnim = QVariantAnimation(self.compressibleWidget)
        self.showAnim.setEasingCurve(QEasingCurve.InOutCubic)
        self.showAnim.setStartValue(0)
        self.showAnim.setEndValue(1000)
        self.showAnim.valueChanged.connect(lambda v: self.setChildFixedHeight(v))
        self.showAnim.setDuration(300)
        self.showAnim.finished.connect(self.invertNotAnimated)
        self.hideAnim = QVariantAnimation(self.compressibleWidget)
        self.hideAnim.setEndValue(0)
        self.hideAnim.setEasingCurve(QEasingCurve.InOutCubic)
        self.hideAnim.valueChanged.connect(lambda v: self.setChildFixedHeight(v))
        self.hideAnim.setDuration(300)
        self.hideAnim.finished.connect(self.invertNotAnimated)
        self.scrollAnim = QVariantAnimation(self)
        self.scrollAnim.setEasingCurve(QEasingCurve.InOutCubic)
        self.scrollAnim.valueChanged.connect(lambda i: self.window().scrollArea.verticalScrollBar().setValue(i))
        self.scrollAnim.setDuration(200)
        self.NotAnimated = True

        self.button = QPushButton("", self)
        self.button.setObjectName("subtitleLabelHover")
        self.button.clicked.connect(self.toggleChilds)
        self.button.setStyleSheet(f"border-bottom-left-radius: 0;border-bottom-right-radius: 0;")
        self.button.setStyleSheet(f"border-bottom-left-radius: 8px;border-bottom-right-radius: 8px;")
        self.setChildFixedHeight(0)

        self.newShowAnim = QVariantAnimation(self)
        self.newShowAnim.setEasingCurve(QEasingCurve.OutQuart)
        self.newShowAnim.setStartValue(50)
        self.newShowAnim.setEndValue(70)
        self.newShowAnim.setDuration(200)
        self.newShowAnim.valueChanged.connect(lambda i: (self.compressibleWidget.move(0, i),self.childrenOpacity.setOpacity((i-50)/20)))

        self.newHideAnim = QVariantAnimation(self)
        self.newHideAnim.setEasingCurve(QEasingCurve.InQuart)
        self.newHideAnim.setStartValue(70)
        self.newHideAnim.setEndValue(50)
        self.newHideAnim.setDuration(200)
        self.newHideAnim.valueChanged.connect(lambda i: (self.compressibleWidget.move(0, i),self.childrenOpacity.setOpacity((i-50)/20)))
        self.newHideAnim.finished.connect(lambda: (self.compressibleWidget.hide(),self.setChildFixedHeight(70)))

        self.childrenOpacity = QGraphicsOpacityEffect(self.compressibleWidget)
        self.childrenOpacity.setOpacity(0)
        self.compressibleWidget.setGraphicsEffect(self.childrenOpacity)

        self.compressibleWidget.move((-1500),(-1500))

    def showHideChildren(self):
        self.hideChildren()
        self.showChildren()

    def hideChildren(self) -> None:
        self.callInMain.emit(lambda: self.compressibleWidget.show())
        self.callInMain.emit(lambda: self.setChildFixedHeight(self.compressibleWidget.sizeHint().height()))
        self.callInMain.emit(self.newHideAnim.start)
        time.sleep(0.2)
        self.callInMain.emit(lambda: self.compressibleWidget.move((-1500), (-1500)))
        self.callInMain.emit(lambda: self.setChildFixedHeight(70))

    def showChildren(self) -> None:
        self.callInMain.emit(lambda: self.compressibleWidget.move(0, (50)))
        self.callInMain.emit(lambda: self.setChildFixedHeight(self.compressibleWidget.sizeHint().height()))
        self.callInMain.emit(lambda: self.compressibleWidget.show())
        self.callInMain.emit(self.newShowAnim.start)
        time.sleep(0.2)

    def setChildFixedHeight(self, h: int) -> None:
        self.compressibleWidget.setFixedHeight(h)
        self.setFixedHeight(h+(70))

    def invertNotAnimated(self):
        self.NotAnimated = not self.NotAnimated

    def toggleChilds(self):
        self.iconMode = getAppIconMode()
        if self.childsVisible and not self.dummy:
            self.childsVisible = False
            self.invertNotAnimated()
            self.showHideButton.setIcon(QIcon(getPath(f"expand_{getAppIconMode()}.png")))
            Thread(target=lambda: (time.sleep(0.2),self.button.setStyleSheet(f"border-bottom-left-radius: 8px;border-bottom-right-radius: 8px;"),self.bg70.setStyleSheet(f"border-bottom-left-radius: 8px;border-bottom-right-radius: 8px;")), daemon=True).start()
            Thread(target=self.hideChildren).start()
        else:
            self.showHideButton.setIcon(QIcon(getPath(f"collapse_{getAppIconMode()}.png")))
            self.button.setStyleSheet(f"border-bottom-left-radius: 0;border-bottom-right-radius: 0;")
            self.bg70.setStyleSheet(f"border-bottom-left-radius: 0;border-bottom-right-radius: 0;")
            self.invertNotAnimated()
            self.childsVisible = True
            Thread(target=self.showChildren).start()

    def window(self) -> 'SettingsWindow':
        return super().window()

    def get6px(self, i: int) -> int:
        return round(i*self.screen().devicePixelRatio())

    def setIcon(self, icon: str) -> None:
        self.image.setPixmap(QIcon(icon).pixmap(QSize((24), (24))))

    def resizeEvent(self, event: QResizeEvent = None) -> None:
        if not self.searchMode and not self.dummy:
            self.image.show()
            self.showHideButton.show()
            self.button.show()
            self.label.show()
            self.descLabel.show()
            self.button.move(0, 0)
            self.button.resize(self.width(), (70))
            self.showHideButton.setIconSize(QSize((12), (12)))
            self.showHideButton.setFixedSize(30, 30)
            self.showHideButton.move(self.width()-(55), (20))

            self.label.move((70), (17))
            self.label.setFixedHeight(20)
            self.descLabel.move((70), (37))
            self.descLabel.setFixedHeight(20)
            self.descLabel.setFixedWidth(self.width()-(70)-(70))

            self.image.move((27), (20))
            self.image.setFixedHeight(30)
            if self.childsVisible and self.NotAnimated:
                self.setFixedHeight(self.compressibleWidget.sizeHint().height()+(70))
                self.compressibleWidget.setFixedHeight(self.compressibleWidget.sizeHint().height())
            elif self.NotAnimated:
                self.setFixedHeight(70)
            self.compressibleWidget.move(0, (70))
            self.compressibleWidget.setFixedWidth(self.width())
            self.image.setFixedHeight(30)
            self.label.setFixedWidth(self.width()-(140))
            self.image.setFixedWidth(30)
            self.bg70.show()
            self.bg70.move(10, 0)
            self.bg70.resize(self.width()-(20), (70))
        else:
            self.bg70.hide()
            self.image.hide()
            self.showHideButton.hide()
            self.button.hide()
            self.image.hide()
            self.label.hide()
            self.descLabel.hide()

            self.setFixedHeight(self.compressibleWidget.sizeHint().height())
            self.compressibleWidget.setFixedHeight(self.compressibleWidget.sizeHint().height())
            self.compressibleWidget.move(0, 0)
            self.compressibleWidget.setFixedWidth(self.width())
        if event:
            return super().resizeEvent(event)

    def addWidget(self, widget: QWidget) -> None:
        self.compressibleWidget.layout().addWidget(widget)
        self.childrenw.append(widget)

    def getChildren(self) -> list:
        return self.childrenw

    def showEvent(self, event) -> None:
        if isWindowDark():
            self.setIcon(self.icon.replace("black", "white"))
        else:
            self.setIcon(self.icon.replace("white", "black"))
        if self.childsVisible:
            self.showHideButton.setIcon(QIcon(getPath(f"collapse_{getAppIconMode()}.png")))
        else:
            self.showHideButton.setIcon(QIcon(getPath(f"expand_{getAppIconMode()}.png")))
        return super().showEvent(event)

class QSettingsButton(QWidget):
    clicked = Signal()
    def __init__(self, text="", btntext="", parent=None, h = 30):
        super().__init__(parent)
        self.fh = h
        self.setAttribute(Qt.WA_StyledBackground)
        self.button = QPushButton(btntext+" ", self)
        self.setObjectName("stBtn")
        self.label = QLabel(text, self)
        if lang["locale"] == "zh_TW":
            self.label.setStyleSheet("font-size: 10pt;background: none;font-family: \"Microsoft JhengHei UI\";font-weight: 450;")
            self.button.setStyleSheet("font-size: 10pt;font-family: \"Microsoft JhengHei UI\";font-weight: 450;")
        elif lang["locale"] == "zh_CN":
            self.label.setStyleSheet("font-size: 10pt;background: none;font-family: \"Microsoft YaHei UI\";font-weight: 450;")
            self.button.setStyleSheet("font-size: 10pt;font-family: \"Microsoft YaHei UI\";font-weight: 450;")
        else:
            self.label.setStyleSheet("font-size: 9pt;background: none;font-family: \"Segoe UI Variable Text\";font-weight: 450;")
            self.button.setStyleSheet("font-size: 9pt;font-family: \"Segoe UI Variable Text\";font-weight: 450;")
        self.label.setObjectName("StLbl")
        self.button.clicked.connect(self.clicked.emit)
        self.label.move((70), 10)
        self.label.setFixedHeight((self.fh))
        self.setFixedHeight((50+(self.fh-30)))
        self.button.setFixedHeight((self.fh))
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.label)
        self.layout().addStretch()
        self.layout().addWidget(self.button)
        self.layout().setContentsMargins(70, 0, 20, 0)

    def get6px(self, i: int) -> int:
        return round(i*self.screen().devicePixelRatio())

    def setIcon(self, icon: QIcon) -> None:
        self.button.setIcon(icon)

    def text(self) -> str:
        return self.label.text() + " " + self.button.text()

class QSettingsComboBox(QWidget):
    textChanged = Signal(str)
    valueChanged = Signal(str)
    def __init__(self, text="", unusedArgument="", parent=None, buttonEnabled: bool = True):
        super().__init__(parent)
        self.buttonOn = buttonEnabled

        class QComboBoxWithFluentMenu(QComboBox):
            def __init__(self, parent) -> None:
                super().__init__(parent)
                v = self.view().window()
                ApplyMenuBlur(v.winId().__int__(), v)

        self.setAttribute(Qt.WA_StyledBackground)
        self.combobox = QComboBoxWithFluentMenu(self)
        self.combobox.setItemDelegate(QStyledItemDelegate(self.combobox))
        self.setObjectName("stBtn")
        self.restartButton = QPushButton("Restart ElevenClock", self)
        self.restartButton.hide()
        self.restartButton.setObjectName("AccentButton")
        self.label = QLabel(text, self)

        if lang["locale"] == "zh_TW":
            self.label.setStyleSheet("font-size: 11pt;background: none;font-family: \"Microsoft JhengHei UI\";font-weight: 450;")
            self.combobox.setStyleSheet("font-size: 11pt;font-family: \"Microsoft JhengHei UI\";font-weight: 450;")
            self.restartButton.setStyleSheet("font-size: 11pt;font-family: \"Microsoft JhengHei UI\";font-weight: 450;")
        elif lang["locale"] == "zh_CN":
            self.label.setStyleSheet("font-size: 11pt;background: none;font-family: \"Microsoft YaHei UI\";font-weight: 450;")
            self.combobox.setStyleSheet("font-size: 11pt;font-family: \"Microsoft YaHei UI\";font-weight: 450;")
            self.restartButton.setStyleSheet("font-size: 11pt;font-family: \"Microsoft YaHei UI\";font-weight: 450;")
        else:
            self.label.setStyleSheet("font-size: 9pt;background: none;font-family: \"Segoe UI Variable Text\";font-weight: 450;")
            self.combobox.setStyleSheet("font-size: 9pt;font-family: \"Segoe UI Variable Text\";font-weight: 450;")
            self.restartButton.setStyleSheet("font-size: 9pt;font-family: \"Segoe UI Variable Text\";font-weight: 450;")
        self.label.setObjectName("StLbl")
        self.label.move((70), 10)
        self.label.setFixedHeight(30)
        self.restartButton.setFixedHeight(30)
        self.setFixedHeight(50)
        self.combobox.setFixedHeight(30)
        
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.label)
        self.layout().addStretch()
        self.layout().addWidget(self.restartButton)
        self.layout().addWidget(self.combobox)
        self.layout().setContentsMargins(70, 0, 20, 0)

    def get6px(self, i: int) -> int:
        return round(i*self.screen().devicePixelRatio())

    def loadItems(self, items: list, index: int = -1) -> None:
        return self.setItems(items, index)

    def setItems(self, items: list, index: int = -1) -> None:
        self.combobox.addItems(items)
        try:
            if index >= 0:
                self.combobox.setCurrentIndex(index)
        except Exception as e:
            report(e)
            self.combobox.setCurrentIndex(0)
        self.combobox.currentTextChanged.connect(self.textChanged.emit)
        self.combobox.currentTextChanged.connect(self.valueChanged.emit)

    def setIcon(self, icon: QIcon) -> None:
        pass
        #self.button.setIcon(icon)

    def toggleRestartButton(self, force = None) -> None:
        if self.buttonOn:
            if (force == None):
                force = self.restartButton.isHidden
            if (force == True):
                self.restartButton.show()
            else:
                self.restartButton.hide()

    def text(self) -> str:
        return self.label.text() + " " + self.combobox.currentText()

class QSettingsCheckBox(QWidget):
    stateChanged = Signal(bool)
    def __init__(self, text="", parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground)
        self.setObjectName("stChkBg")
        self.checkbox = QCheckBox(text, self)
        if lang["locale"] == "zh_TW":
            self.checkbox.setStyleSheet("font-size: 11pt;background: none;font-family: \"Microsoft JhengHei UI\";font-weight: 450;")
        elif lang["locale"] == "zh_CN":
            self.checkbox.setStyleSheet("font-size: 11pt;background: none;font-family: \"Microsoft YaHei UI\";font-weight: 450;")
        else:
            self.checkbox.setStyleSheet("font-size: 9pt;background: none;font-family: \"Segoe UI Variable Text\";font-weight: 450;")
        self.checkbox.setObjectName("stChk")
        self.checkbox.stateChanged.connect(self.stateChanged.emit)
        self.checkbox.move((70), 10)
        self.checkbox.setFixedHeight(30)
        self.setFixedHeight(50)
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.checkbox)
        self.layout().setContentsMargins(70, 0, 20, 0)

    def setChecked(self, checked: bool) -> None:
        self.checkbox.setChecked(checked)

    def isChecked(self) -> bool:
        return self.checkbox.isChecked()

    def get6px(self, i: int) -> int:
        return round(i*self.screen().devicePixelRatio())

    def text(self) -> str:
        return self.checkbox.text()

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
        self.checkbox.move((70), 10)
        self.checkbox.setFixedHeight(30)
        self.infolabel.move((150), 10)
        self.infolabel.setFixedHeight(30)
        self.setFixedHeight(50)
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.checkbox)
        self.layout().addStretch()
        self.layout().addWidget(self.infolabel)
        self.layout().setContentsMargins(70, 0, 20, 0)

    def stateChangedFun(self, checked: bool) -> bool:
        self.infolabel.setVisible(checked)
        self.stateChanged.emit(checked)


class QSettingsCheckBoxTextBox(QSettingsCheckBox):
    stateChanged = Signal(bool)
    valueChanged = Signal(str)

    def __init__(self, text: str, parent=None, helpLabel: str = ""):

        class QLineEditWithFluentMenu(QLineEdit):
            def __init__(self, parent) -> None:
                super().__init__(parent)
            def contextMenuEvent(self, e: QtGui.QContextMenuEvent) -> None:
                menu = self.createStandardContextMenu()
                ApplyMenuBlur(menu.winId().__int__(), menu)
                menu.exec(e.globalPos())

        super().__init__(text=text, parent=parent)
        self.setAttribute(Qt.WA_StyledBackground)
        self.lineedit = QLineEditWithFluentMenu(self)
        self.oldtext = ""
        self.lineedit.setObjectName("")
        self.lineedit.textChanged.connect(self.valuechangedEvent)
        self.checkbox.stateChanged.connect(self.stateChangedEvent)
        self.helplabel = QLabel(helpLabel, self)
        self.helplabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.helplabel.setOpenExternalLinks(True)
        self.stateChangedEvent(self.checkbox.isChecked())
        self.checkbox.move((70), 10)
        self.checkbox.setFixedHeight(30)
        self.setFixedHeight(50)
        self.lineedit.setFixedHeight(30)
        self.helplabel.setFixedHeight(30)
        
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.checkbox)
        self.layout().addStretch()
        self.layout().addWidget(self.helplabel)
        self.layout().addWidget(self.lineedit)
        self.layout().setContentsMargins(70, 0, 20, 0)

    def valuechangedEvent(self, text: str):
        self.valueChanged.emit(text)

    def setPlaceholderText(self, text: str):
        self.lineedit.setPlaceholderText(text)
        self.oldtext = text

    def setText(self, text: str):
        self.lineedit.setText(text)

    def stateChangedEvent(self, v: bool):
        self.lineedit.setEnabled(self.checkbox.isChecked())
        if not self.checkbox.isChecked():
            self.lineedit.setEnabled(False)
            self.oldtext = self.lineedit.placeholderText()
            self.lineedit.setToolTip(_("<b>{0}</b> needs to be enabled to change this setting").format(self.checkbox.text()))
            self.lineedit.setPlaceholderText(_("<b>{0}</b> needs to be enabled to change this setting").format(self.checkbox.text()).replace("<b>", "\"").replace("</b>", "\""))
            self.stateChanged.emit(v)
        else:
            self.stateChanged.emit(v)
            self.lineedit.setEnabled(True)
            self.lineedit.setToolTip("")
            self.lineedit.setPlaceholderText(self.oldtext)
            self.valueChanged.emit(self.lineedit.text())


class QSettingsSizeBoxComboBox(QSettingsCheckBox):
    stateChanged = Signal(bool)
    valueChanged = Signal(str)

    def __init__(self, text: str, parent=None):
        super().__init__(text=text, parent=parent)

        class QComboBoxWithFluentMenu(QComboBox):
            def __init__(self, parent) -> None:
                super().__init__(parent)
                self.setAutoFillBackground(True)
                self.setAttribute(Qt.WA_StyledBackground)
                v = self.view().window()
                ApplyMenuBlur(v.winId().__int__(), v)

        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_StyledBackground)
        self.combobox = QComboBoxWithFluentMenu(self)
        self.combobox.setItemDelegate(QStyledItemDelegate(self.combobox))
        self.combobox.currentIndexChanged.connect(self.valuechangedEvent)
        self.checkbox.stateChanged.connect(self.stateChangedEvent)
        self.stateChangedEvent(self.checkbox.isChecked())
        self.setFixedHeight(50)
        self.combobox.setFixedHeight(30)
        self.checkbox.move((70), 10)
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.checkbox)
        self.layout().addStretch()
        self.layout().addWidget(self.combobox)
        self.layout().setContentsMargins(70, 0, 20, 0)

    def valuechangedEvent(self, i: int):
        self.valueChanged.emit(self.combobox.itemText(i))

    def stateChangedEvent(self, v: bool):
        self.combobox.setEnabled(self.checkbox.isChecked())
        if not self.checkbox.isChecked():
            self.combobox.setEnabled(False)
            self.combobox.setToolTip(_("<b>{0}</b> needs to be enabled to change this setting").format(self.checkbox.text()))
            self.stateChanged.emit(v)
        else:
            self.stateChanged.emit(v)
            self.combobox.setEnabled(True)
            self.combobox.setToolTip("")
            self.valueChanged.emit(self.combobox.currentText())

    def loadItems(self, items: list = None):
        self.combobox.clear()
        if items:
            self.combobox.addItems(str(item) for item in items)

        else:
            self.combobox.addItems(str(item) for item in [2, 3, 4, 5, 6, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 13, 14, 16, 18, 20, 22, 24, 26, 28, 30, 34, 37, 40, 44, 47, 50, 55, 60, 70, 95, 100])

class QSettingsSliderWithCheckBox(QSettingsCheckBox):
    stateChanged = Signal(bool)
    valueChanged = Signal(int)

    def __init__(self, text: str, parent=None, min: int = 10, max: int = 100, value: int = 0):
        super().__init__(text=text, parent=parent)
        self.setAttribute(Qt.WA_StyledBackground)
        self.slider = QSlider(self)
        self.slider.setRange(min, max)
        self.slider.setValue(value)
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.slider.sliderReleased.connect(self.valuechangedEvent)
        self.slider.valueChanged.connect(lambda: self.intLabel.setText(str(self.slider.value())))
        self.checkbox.stateChanged.connect(self.stateChangedEvent)
        self.stateChangedEvent(self.checkbox.isChecked())
        self.intLabel = QLabel(self)
        self.intLabel.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        self.intLabel.setFixedSize(QSize(30, 30))
        self.checkbox.setFixedHeight(30)
        self.setFixedHeight(50)
        self.slider.setFixedHeight(30)
        self.intLabel.setText(str(self.slider.value()))
        self.checkbox.move(70, 10)
        
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.checkbox)
        self.layout().addStretch()
        self.layout().addWidget(self.slider)
        self.layout().addWidget(self.intLabel)
        self.layout().setContentsMargins(70, 0, 20, 0)

    def valuechangedEvent(self):
        self.intLabel.setText(str(self.slider.value()))
        self.valueChanged.emit(self.slider.value())

    def stateChangedEvent(self, v: bool):
        self.slider.setEnabled(self.checkbox.isChecked())
        if not self.checkbox.isChecked():
            self.slider.setEnabled(False)
            self.slider.setToolTip(_("<b>{0}</b> needs to be enabled to change this setting").format(self.checkbox.text()))
            self.stateChanged.emit(v)
        else:
            self.stateChanged.emit(v)
            self.slider.setEnabled(True)
            self.slider.setToolTip("")
            self.valueChanged.emit(self.slider.value())

class QCustomColorDialog(QColorDialog):
    def __init__(self, parent = ...) -> None:
        super().__init__(parent=parent)
        self.setWindowModality(Qt.WindowModality.WindowModal)
        self.setStyleSheet(f"*{{border-radius: 8px;}}  QColorLuminancePicker {{background-color: transparent; border: 4px solid black;margin: none; border: none; padding: none;}} ")
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAutoFillBackground(True)
        self.setWindowTitle("")
        pixmap = QPixmap(32, 32)
        pixmap.fill(Qt.transparent)
        self.setWindowIcon(QIcon(pixmap))
        self.hwnd = self.winId().__int__()

        window_style = win32gui.GetWindowLong(self.hwnd, GWL_STYLE)
        win32gui.SetWindowLong(self.hwnd, GWL_STYLE, window_style | WS_POPUP | WS_THICKFRAME | WS_CAPTION | WS_SYSMENU)
        self.setWindowTitle(_("Pick a color"))

    def showEvent(self, arg__1: QShowEvent) -> None:
        ExtendFrameIntoClientArea(self.winId().__int__())
        self.setWindowIcon(globals.sw.windowIcon())
        self.hwnd = self.winId().__int__()
        if ApplyMica(self.hwnd, isWindowDark()) != 0x0:
            if isWindowDark():
                GlobalBlur(self.hwnd, Dark=True, Acrylic=True, hexColor="#333333ff")
            else:
                GlobalBlur(self.hwnd, Dark=False, Acrylic=True, hexColor="#ffffffdd")
        return super().showEvent(arg__1)

    def get6px(self, i: int) -> int:
        return round(i*self.screen().devicePixelRatio())
    
class QSettingsCheckboxColorDialog(QSettingsCheckBox):
    stateChanged = Signal(bool)
    valueChanged = Signal(str)
    color = "0,0,0"

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
        self.checkbox.setFixedHeight(30)
        self.button.setFixedHeight(30)
        self.setFixedHeight(50)
        self.checkbox.move((70), 10)
        
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.checkbox)
        self.layout().addStretch()
        self.layout().addWidget(self.button)
        self.layout().setContentsMargins(70, 0, 20, 0)

    def valuechangedEvent(self, c: QColor):
        r = c.red()
        g = c.green()
        b = c.blue()
        self.color = f"{r},{g},{b}"
        self.valueChanged.emit(self.color)
        self.button.setStyleSheet(f"color: rgb({self.color})")

    def stateChangedEvent(self, v: bool):
        self.button.setEnabled(self.checkbox.isChecked())
        if not self.checkbox.isChecked():
            self.button.setEnabled(False)
            self.button.setStyleSheet("")
            self.stateChanged.emit(v)
            self.button.setToolTip(_("<b>{0}</b> needs to be enabled to change this setting").format(self.checkbox.text()))
        else:
            self.stateChanged.emit(v)
            self.button.setEnabled(True)
            self.button.setToolTip("")
            self.valueChanged.emit(self.color)
            self.button.setStyleSheet(f"color: rgb({self.color})")

class QSettingsBgBoxColorDialog(QSettingsCheckboxColorDialog):
    color = "0, 0, 0, 100"

    def valuechangedEvent(self, c: QColor):
        r = c.red()
        g = c.green()
        b = c.blue()
        a = c.alpha()
        self.color = f"{r},{g},{b},{a/255*100}"
        self.valueChanged.emit(self.color)
        self.button.setStyleSheet(f"background-color: rgba({self.color})")

    def stateChangedEvent(self, v: bool):
        self.button.setEnabled(self.checkbox.isChecked())
        if not self.checkbox.isChecked():
            self.button.setEnabled(False)
            self.button.setStyleSheet("")
            self.stateChanged.emit(v)
            self.button.setToolTip(_("<b>{0}</b> needs to be enabled to change this setting").format(self.checkbox.text()))
        else:
            self.stateChanged.emit(v)
            self.button.setEnabled(True)
            self.button.setToolTip("")
            self.valueChanged.emit(self.color)
            self.button.setStyleSheet(f"background-color: rgba({self.color})")

class QSettingsFontBoxComboBox(QSettingsCheckBox):
    stateChanged = Signal(bool)
    valueChanged = Signal(str)

    def __init__(self, text: str, parent=None):
        super().__init__(text=text, parent=parent)
        self.setAttribute(Qt.WA_StyledBackground)

        class QFluentFontDialog(QFontDialog):
            def __init__(self, parent) -> None:
                super().__init__(parent)
                self.setAutoFillBackground(False)

            def showEvent(self, arg__1: QShowEvent) -> None:
                ApplyMica(self.winId().__int__(), isWindowDark())
                return super().showEvent(arg__1)

        self.fontPicker = QFluentFontDialog(self)
        self.fontPicker.setWindowTitle(_("Select font"))
        self.fontPicker.setObjectName("stCmbbx")
        self.fontPicker.fontSelected.connect(self.valuechangedEvent)
        self.button = QPushButton(self)
        self.button.setObjectName("stCmbbx")
        self.button.setText(_("Select custom font"))
        self.button.clicked.connect(self.fontPicker.show)
        self.checkbox.stateChanged.connect(self.stateChangedEvent)
        self.stateChangedEvent(self.checkbox.isChecked())
        self.checkbox.setFixedHeight(30)
        self.setFixedHeight(50)
        self.button.setFixedHeight(30)
        self.checkbox.move((70), 10)
        
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.checkbox)
        self.layout().addStretch()
        self.layout().addWidget(self.button)
        self.layout().setContentsMargins(70, 0, 20, 0)

    def valuechangedEvent(self, font: QFont):
        self.valueChanged.emit(font.key())
        self.button.setFont(font)

    def stateChangedEvent(self, v: bool):
        self.button.setEnabled(self.checkbox.isChecked())
        if not self.checkbox.isChecked():
            self.button.setEnabled(False)
            self.button.setToolTip(_("<b>{0}</b> needs to be enabled to change this setting").format(self.checkbox.text()))
            self.stateChanged.emit(v)
        else:
            self.stateChanged.emit(v)
            self.button.setEnabled(True)
            self.button.setToolTip("")
            self.valueChanged.emit(str(self.fontPicker.currentFont()))
            #self.combobox.lineEdit().setFont(QFont(self.combobox.currentText()))

    def setItems(self, items: list):
        pass
        #self.combobox.clear()
        #self.combobox.addItems(items)

class QSettingsNewFontBoxComboBox(QSettingsFontBoxComboBox):

    def valuechangedEvent(self, font: QFont):
        self.valueChanged.emit(font.toString())
        self.button.setFont(font)

class QSettingsLineEditCheckBox(QSettingsCheckBox):
    valueChanged = Signal(str)

    def __init__(self, text="", parent=None):

        class QPlainTextEditWithFluentMenu(QPlainTextEdit):
                def __init__(self, parent=None):
                    super().__init__(parent=parent)
                def contextMenuEvent(self, e: QtGui.QContextMenuEvent) -> None:
                    menu = self.createStandardContextMenu()
                    ApplyMenuBlur(menu.winId().__int__(), menu)
                    menu.exec(e.globalPos())

        super().__init__(text, parent)
        self.button = QPushButton(_("Apply"), self)
        self.edit = QPlainTextEditWithFluentMenu(self)
        self.edit.setEnabled(True)
        self.edit.setPlaceholderText(globals.dateTimeFormat)
        self.edit.setStyleSheet("QPlainTextEdit{font-size: 13pt;}")
        self.edit.textChanged.connect(self.updateText)
        self.preview = QLabel(_("Nothing to preview"), self)
        self.preview.setOpenExternalLinks(False)
        self.preview.setObjectName("FocusLabel")
        self.rulesLabel = QLabel(self)
        self.rulesLabel.setOpenExternalLinks(True)
        self.rulesLabel.setWordWrap(True)
        self.stateChanged.connect(self.resizeEvent)
        self.button.clicked.connect(lambda: self.valueChanged.emit(self.edit.toPlainText().strip()))
        self.checkbox.setFixedHeight(30)
        self.button.setFixedHeight(30)
        self.button.setFixedWidth(150)
        self.edit.setFixedHeight(80)
        self.checkbox.move(70, 10)
        self.preview.setFixedHeight(80)
        self.preview.setFixedWidth(150)
        self.rulesLabel.setFixedHeight(100)
        self.layout().removeWidget(self.checkbox)


    def resizeEvent(self, event: QResizeEvent = None) -> None:
        if not self.isChecked():
            self.button.hide()
            self.rulesLabel.hide()
            self.edit.setEnabled(True)
            self.edit.hide()
            self.preview.hide()
            self.checkbox.setFixedWidth(self.width()-(70))
            self.setFixedHeight(50)
        else:
            if not event:
                self.valueChanged.emit(self.edit.toPlainText().strip())
            self.edit.setPlaceholderText(globals.dateTimeFormat)
            self.button.show()
            self.edit.setEnabled(True)
            self.rulesLabel.show()
            self.edit.show()
            self.preview.show()
            self.checkbox.setFixedWidth(self.width()-(250))
            self.setFixedHeight(300)
            self.button.move(self.width()-(170), 10)
            self.edit.setFixedWidth(self.width()-(90)-(160))
            self.edit.move((70), (50))
            self.preview.move(self.width()-(170), (50))
            self.rulesLabel.move((70), (130))
            self.rulesLabel.setFixedWidth(self.width()-(90))

    def setLabelText(self, s: str) -> None:
        self.rulesLabel.setText(s)

    def updateText(self) -> None:
        if self.edit.toPlainText() == "":
            self.preview.setText(_("Nothing to preview"))
        else:
            try:
                currtext = self.edit.toPlainText()
                self.preview.setText(datetime.datetime.now().strftime(currtext.replace("\u200a", "hairsec")).replace("hairsec", "\u200a"))
            except Exception as e:
                self.preview.setText(_("Invalid time format\nPlease follow the\nC 1989 Standards"))
                report(e)

class SmoothScrollArea(QScrollArea):
    missingScroll = 0
    buttonVisible = False
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self.smoothScrollAnimation = QVariantAnimation(self)
        self.smoothScrollAnimation.setDuration(300)
        self.smoothScrollAnimation.setEasingCurve(QEasingCurve.OutQuart)
        self.smoothScrollAnimation.valueChanged.connect(lambda v: self.verticalScrollBar().setValue(v))
        self.goTopButton = QPushButton(self)
        self.goTopButton.setIcon(QIcon(getPath(f"gotop_{getAppIconMode()}.png")))
        self.goTopButton.setToolTip(_("Return to top"))
        self.goTopButton.setAccessibleDescription(_("Return to top"))
        self.goTopButton.setFixedSize(24, 32)
        self.buttonOpacity = QGraphicsOpacityEffect()
        self.goTopButton.clicked.connect(lambda: (self.smoothScrollAnimation.setStartValue(self.verticalScrollBar().value()), self.smoothScrollAnimation.setEndValue(0), self.smoothScrollAnimation.start(), self.hideTopButton()))
        self.goTopButton.setGraphicsEffect(self.buttonOpacity)
        self.buttonOpacity.setOpacity(0)
        self.buttonAnimation = QVariantAnimation(self)
        self.buttonAnimation.setDuration(100)
        self.buttonAnimation.valueChanged.connect(lambda v: self.buttonOpacity.setOpacity(v/100))
        self.verticalScrollBar().setFixedWidth(15)
        
    def wheelEvent(self, e: QWheelEvent) -> None:
        currentPos = self.verticalScrollBar().value()
        finalPos = currentPos - e.angleDelta().y()
        self.doSmoothScroll(currentPos, finalPos)
        e.ignore()
        
    def doSmoothScroll(self, currentPos: int, finalPos: int):
        if self.smoothScrollAnimation.state() == QAbstractAnimation.Running:
            self.smoothScrollAnimation.stop()
            self.missingScroll = self.smoothScrollAnimation.endValue() - self.smoothScrollAnimation.currentValue()
        else:
            self.missingScroll = 0
        finalPos += self.missingScroll
        self.showTopButton() if finalPos>20 else self.hideTopButton()
        if finalPos < 0:
            finalPos = 0
        elif finalPos > self.verticalScrollBar().maximum():
            finalPos = self.verticalScrollBar().maximum()
        self.smoothScrollAnimation.setStartValue(currentPos)
        self.smoothScrollAnimation.setEndValue(finalPos)
        self.smoothScrollAnimation.start()
        
    def keyPressEvent(self, event: QKeyEvent) -> None:
        match event.key():
            case Qt.Key.Key_PageDown:
                currentPos = self.verticalScrollBar().value()
                finalPos = self.verticalScrollBar().value() + self.height()
                self.doSmoothScroll(currentPos, finalPos)
                event.ignore()
                return
            case Qt.Key.Key_PageUp:
                currentPos = self.verticalScrollBar().value()
                finalPos = self.verticalScrollBar().value() - self.height()
                self.doSmoothScroll(currentPos, finalPos)
                event.ignore()
                return
            case Qt.Key.Key_End:
                currentPos = self.verticalScrollBar().value()
                finalPos = self.verticalScrollBar().maximum()
                self.doSmoothScroll(currentPos, finalPos)
                event.ignore()
                return
            case Qt.Key.Key_Home:
                currentPos = self.verticalScrollBar().value()
                finalPos = 0
                self.doSmoothScroll(currentPos, finalPos)
                event.ignore()
                return
        return super().keyPressEvent(event)
    
    def showTopButton(self):
        if not self.buttonVisible:
            self.buttonVisible = True
            self.goTopButton.raise_()
            self.buttonAnimation.setStartValue(int(self.buttonOpacity.opacity()*100))
            self.buttonAnimation.setEndValue(100)
            self.buttonAnimation.start()
        
    def hideTopButton(self):
        if self.buttonVisible:
            self.buttonVisible = False
            self.buttonAnimation.setStartValue(int(self.buttonOpacity.opacity()*100))
            self.buttonAnimation.setEndValue(0)
            self.buttonAnimation.start()
            
    def resizeEvent(self, event: QResizeEvent) -> None:
        self.goTopButton.move(self.width()-48, self.height()-48)
        return super().resizeEvent(event)


class QAnnouncements(QLabel):
    callInMain = Signal(object)

    def __init__(self):
        super().__init__()
        self.area = SmoothScrollArea()
        self.setMaximumWidth(1000)
        self.callInMain.connect(lambda f: f())
        self.setFixedHeight(110)
        self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setStyleSheet(f"#subtitleLabel{{border-bottom-left-radius: 4px;border-bottom-right-radius: 4px;border-bottom: 1px;font-size: 12pt;}}*{{padding: 3px;}}")
        self.setTtext(_("Fetching latest announcement, please wait..."))
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.pictureLabel = QLabel()
        self.pictureLabel.setContentsMargins(0, 0, 0, 0)
        self.pictureLabel.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.textLabel = QLabel()
        self.textLabel.setOpenExternalLinks(True)
        self.textLabel.setContentsMargins(10, 0, 10, 0)
        self.textLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.addStretch()
        layout.addWidget(self.textLabel, stretch=0)
        layout.addWidget(self.pictureLabel, stretch=0)
        layout.addStretch()
        self.w = QWidget()
        self.w.setObjectName("backgroundWindow")
        self.w.setLayout(layout)
        self.w.setContentsMargins(0, 0, 0, 0)
        self.area.setWidget(self.w)
        l = QVBoxLayout()
        l.setSpacing(0)
        l.setContentsMargins(0, 5, 0, 5)
        l.addWidget(self.area, stretch=1)
        self.area.setWidgetResizable(True)
        self.area.setContentsMargins(0, 0, 0, 0)
        self.area.setObjectName("backgroundWindow")
        self.area.setStyleSheet("border: 0 solid black; padding: 0; margin: 0;")
        self.area.setFrameShape(QFrame.NoFrame)
        self.area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pictureLabel.setFixedHeight(self.area.height())
        self.textLabel.setFixedHeight(self.area.height())
        self.setLayout(l)



    def loadAnnouncements(self, useHttps: bool = True):
        try:
            response = urlopen(f"http{'s' if useHttps else ''}://www.marticliment.com/resources/elevenclock.announcement")
            print("🔵 Announcement URL:", response.url)
            response = response.read().decode("utf8")
            self.callInMain.emit(lambda: self.setTtext(""))
            rawbody = str(response.split("////")[0]).strip()
            rawbody = '\n'.join([_(line) for line in rawbody.replace("\r", "").split("\n")])
            announcement_body = rawbody.replace("http://", "ignore:").replace("https://", "ignoreSecure:").replace("linkId", "http://marticliment.com/redirect/").replace("linkColor", f"rgb({getColors()[2 if isWindowDark() else 4]})")
            self.callInMain.emit(lambda: self.textLabel.setText(announcement_body))
            self.callInMain.emit(lambda: self.pictureLabel.setText("Loading media..."))
            announcement_image_url = response.split("////")[1].strip()
            try:
                response = urlopen(announcement_image_url)
                print("🔵 Image URL:", response.url)
                response = response.read()
                self.file =  open(os.path.join(os.path.join(os.path.join(os.path.expanduser("~"), ".elevenclock")), "announcement.png"), "wb")
                self.file.write(response)
                self.callInMain.emit(lambda: self.pictureLabel.setText(""))
                self.file.close()
                h = self.area.height()
                self.callInMain.emit(lambda: self.pictureLabel.setFixedHeight(h))
                self.callInMain.emit(lambda: self.textLabel.setFixedHeight(h))
                self.callInMain.emit(lambda: self.pictureLabel.setPixmap(QPixmap(self.file.name).scaledToHeight(h-8, Qt.SmoothTransformation)))
            except Exception as ex:
                s = _("Couldn't load the announcement image")+"\n\n"+str(ex)
                self.callInMain.emit(lambda: self.pictureLabel.setText(s))
                print("🟠 Unable to retrieve announcement image")
                report(ex)
        except Exception as e:
            if useHttps:
                self.loadAnnouncements(useHttps=False)
            else:
                s = _("Couldn't load the announcements. Please try again later")+"\n\n"+str(e)
                self.callInMain.emit(lambda: self.setTtext(s))
                print("🟠 Unable to retrieve latest announcement")
                report(e)

    def showEvent(self, a0: QShowEvent) -> None:
        return super().showEvent(a0)

    def get6px(self, i: int) -> int:
        return round(i*self.screen().devicePixelRatio())

    def setTtext(self, a0: str) -> None:
        return super().setText(a0)

    def setText(self, a: str) -> None:
        raise Exception("This member should not be used under any circumstances")
    
    
class CustomSettings(SettingsWindow):
    def __init__(self, id, data):
        self.data = data
        self.clockId = id
        super().__init__()
        print(f"🔵 Loading settings window with ID={self.clockId}")
        self.title.setText(_("Modifying Clock {0} on the monitor {1}").format(data[0], data[1]))
        self.setWindowTitle(_("Settings for clock {0} on the monitor {1} - ElevenClock Settings").format(data[0], data[1]))
        self.generalSettingsTitle.hide()
        self.aboutTitle.hide()
        self.languageSettingsTitle.hide()
        self.debbuggingTitle.hide()
        self.dummyTitle = QSettingsTitle("", "", "")
        self.mainLayout.insertWidget(3, self.dummyTitle)
        self.MessageLabel.setText("\n"+_("You need to enable the checkbox above\nin order to change those settings")+"\n")
        self.MessageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.enableCustomStyle = QSettingsCheckBox(_("Set clock {0} on monitor {1} to have a different style that the other clocks.").format(data[0], data[1]))
        self.enableCustomStyle.setChecked(getSettings(f"Individualize{id}"))
        self.enableCustomStyle.stateChanged.connect(lambda v: (setSettings(f"Individualize{id}", v), self.changeState()))
        self.enableCustomStyle.setStyleSheet(f"QWidget#stChkBg{{border-top-left-radius: 8px;border-top-right-radius: 8px;border-width: 1px;}}"+("border-color: #000000" if isWindowDark() else ""))
        self.dummyTitle.addWidget(self.enableCustomStyle)
        self.openGeneralSettings = QSettingsButton(_("Do you want to open the global settings instead?"), _("Open global settings"))
        self.openGeneralSettings.button.setObjectName("AccentButton")
        self.openGeneralSettings.clicked.connect(lambda: (globals.sw.setGeometry(self.geometry()), self.hide(), globals.sw.show()))

        self.importPrefs = QSettingsComboBox(_("Clone style from another clock"))
        self.importPrefs.restartButton.setText(_("Import"))
        self.importPrefs.setStyleSheet("QWidget#stBtn{border-bottom-left-radius: 0;border-bottom-right-radius: 0;border-bottom: 0;}")
        self.dummyTitle.addWidget(self.importPrefs)
        
        def importPreferences():
            nonlocal self
            oldenv = self.clocks[self.importPrefs.combobox.currentText()]
            newenv = self.clockId
            for setting in globals.settingsList:
                setSettings(setting, getSettings(setting, env=oldenv), env=newenv, r=False)
                if getSettingsValue(setting, env=oldenv) != "":
                    setSettingsValue(setting, getSettingsValue(setting, env=oldenv), env=newenv, r=False)
            globals.restartClocks()
            self.close()
            tools.specificSettings[id] = globals.CustomSettings(id, data)
            tools.specificSettings[id].show()

                
            
            
        self.importPrefs.restartButton.clicked.connect(importPreferences)
        self.importPrefs.restartButton.show()
        
        self.changeState()
        self.dummyTitle.addWidget(self.openGeneralSettings)
        
    def showEvent(self, event: QShowEvent) -> None:
        self.dummyTitle.searchMode = True
        self.dummyTitle.resizeEvent(QResizeEvent(self.dummyTitle.size(), self.dummyTitle.size()))
        self.dummyTitle.childrenOpacity.setOpacity(1)
        
        self.clocks = {
            "Global preferences": "",
        }
        for clock in globals.clocks:
            cprint(clock.clockId)
            if clock.isCustomClock and clock.clockId != self.clockId:
                self.clocks[clock.clockName] = clock.clockId
        for i in range(self.importPrefs.combobox.count()):
            self.importPrefs.combobox.removeItem(0)
        self.importPrefs.combobox.addItems(self.clocks.keys())
        
        return super().showEvent(event)

    def changeState(self):
        v = self.enableCustomStyle.isChecked()
        self.clockSettingsTitle.setEnabled(v)
        self.clockFeaturesTitle.setEnabled(v)
        self.clockPosTitle.setEnabled(v)
        self.clockAppearanceTitle.setEnabled(v)
        self.dateTimeTitle.setEnabled(v)
        self.internetTimeTitle.setEnabled(v)
        self.toolTipAppearanceTitle.setEnabled(v)
        self.experimentalTitle.setEnabled(v)
        self.importPrefs.setEnabled(v)
        self.MessageLabel.setVisible(not v)
        
    def setSettings(self, s: str, v: bool, r: bool = True, thread = False):
        setSettings(s, v, r, thread, env = self.clockId)
        
    def setSettingsValue(self, s: str, v: bool, r: bool = True):
        setSettingsValue(s, v, r, env = self.clockId)
        
    def getSettings(self, s: str):
        return getSettings(s, env = self.clockId)
    
    def getSettingsValue(self, s: str):
        return getSettingsValue(s, env = self.clockId)
        
        
globals.CustomSettings = CustomSettings


if __name__ == "__main__":
    from ctypes import c_int, windll
    windll.shcore.SetProcessDpiAwareness(c_int(2))
    import __init__
