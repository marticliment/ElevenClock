# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_5_0 = {
    "Tooltip Appearance:": "",
    "Tooltip's font, font size, font color and background": "",
    "Disable tooltip's blurry background": "",
    "Sync time with the internet": "",
    "Internet date and time": "",
    "Select internet time provider, change sync frequency": "",
    "Enable atomic clock-based internet time": "",
    "Paste a URL from the world clock api or equivalent": "",
    "Help": "",
    "Internet sync frequency": "",
    "10 minutes": "",
    "30 minutes": "",
    "1 hour": "",
    "2 hours": "",
    "4 hours": "",
    "10 hours": "",
    "24 hours": "",
}

lang_3_4_0 = lang_3_5_0 | {
    "Show calendar": "",
    "Disabled": "",
    "Open quick settings": "",
    "Show desktop": "",
    "Open run dialog": "",
    "Open task manager": "",
    "Open start menu": "",
    "Open search menu": "",
    "Change task": "",
    "Change the action done when the clock is clicked": "",
}

lang_3_3_2 = lang_3_4_0 | {
    "ElevenClock Updater": "",
    "ElevenClock is downloading updates": "",
    "ElevenClock has updated to version {0} successfully\nPlease see GitHub for the changelog": "",
    "Customize the clock on Windows 11": "",
    "Disable the new instance checker method": "",
    "Import settings from a local file": "",
    "Export settings to a local file": "",
    "Export": "",
    "Import": "",
}

lang_3_3_1 = lang_3_3_2 | {
    "Invalid time format\nPlease follow the\nC 1989 Standards": "",
    "Nothing to preview": "",
    "Invalid time format\nPlease modify it\nin the settings": "",
    "Disable the tooltip shown when the clock is hovered": ""
}
lang_3_3 = lang_3_3_1 | {
    "Custom format rules:": "",
    "Any text can be placed here. To place items such as date and time, please use the 1989 C standard. More info on the following link": "",
    "Python date and time formats": "",
    "To disable the zero-padding effect, add a # in between the % and the code: non-zero-padded hours would be %#H, and zero-padded hours would be %H": "", # Here please don't modify the %H and %#H values
    "Click on Apply to apply and preview the format": "",
    "Apply": "",
    "If you don't understand what is happening, please uncheck the checkbox over the text area": "",
    "Set a custom date and time format": "",
    "(for advanced users only)": "",
    "Move this clock to the left": "",
    "Move this clock to the top": "",
    "Move this clock to the right": "",
    "Move this clock to the bottom": "",
    "Restore horizontal position": "",
    "Restore vertical position": "",
}

lang_3_2_1 = lang_3_3 | {
    "Open online help to troubleshoot problems": "打開線上說明以疑難排解問題",
    "Reset ElevenClock preferences to defaults": "重設 ElevenClock 的偏好設定至預設值",
    "Specify a minimum width for the clock": "指定時鐘的最小寬度",
    "Search on the settings": "在設定中搜尋",
    "No results were found": "找不到任何結果",
}

lang_3_2 = lang_3_2_1 | {
    "Use system accent color as background color": "使用系統輔色作為背景色",
    "Check only the focused window on the fullscreen check": "只對已設定焦點的視窗進行全螢幕判斷",
    "Clock on monitor {0}": "螢幕 {0} 上的時鐘",
    "Move to the left": "移到左邊",
    "Show this clock on the left": "將這個時鐘顯示在左邊",
    "Show this clock on the right": "將這個時鐘顯示在右邊",
    "Restore clock position": "還原時鐘位置",
}

lang_3_1 = lang_3_2 | {
    "W": "周", # The initial of the word week in your language: W for week, S for setmana, etc.
    "Disable the notification badge": "停用通知徽章",
    "Override clock default height": "覆寫時鐘預設高度",
    "Adjust horizontal clock position": "調整時鐘水平位置",
    "Adjust vertical clock position": "調整時鐘垂直位置",
    "Export log as a file": "將日誌匯出為檔案",
    "Copy log to clipboard": "複製日誌到剪貼簿",
    "Announcements:": "公告",
    "Fetching latest announcement, please wait...": "讀取最新公告中，請稍後...",
    "Couldn't load the announcements. Please try again later": "無法讀取公告，清稍後重試",
    "ElevenClock's log": "ElevenClock 的日誌",
    "Pick a color": "請選擇顏色"
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "在被點擊後 10 秒內隱藏時鐘",
    "Enable low-cpu mode": "啟用低 CPU 資源用量模式",
    "You might lose functionalities, like the notification counter or the dynamic background": "你可能會失去一些功能，例如通知數量顯示或是動態背景",
    "Clock position and size:": "時鐘位置以及大小",
    "Clock size preferences, position offset, clock at the left, etc.": "時鐘尺寸偏好設定、位移、左側時鐘以及其他",
    "Reset monitor blacklisting status": "重設螢幕黑名單",
    "Reset": "重設",
    "Third party licenses": "第三方使用條款",
    "View": "檢視",
    "ElevenClock": "ElevenClock",
    "Monitor tools": "螢幕工具",
    "Blacklist this monitor": "將這個螢幕加入黑名單",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "Elevenclock {0} 中的協力廠商開放原始碼軟體（以及它們的條款）",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "ElevenClock 是一個在其他社群維護的程式庫幫助下建立的開放原始碼軟體",
    "Ok": "確定",
    "More Info": "更多資訊",
    "About Qt": "關於 Qt",
    "Success": "成功",
    "The monitors were unblacklisted successfully.": "成功將所有螢幕自黑名單中移除",
    "Now you should see the clock everywhere": "你現在應該能在每個螢幕上看到時鐘了",
    "Ok": "確定",
    "Blacklist Monitor": "黑名單螢幕",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "黑名單此螢幕將會將時鐘自此螢幕永久移除",
    "This action can be reverted from the settings window, under <b>Clock position and size</b>": "這個動作可以在設定頁中恢復。對應的選項位於 <b>時鐘位置以及大小</b> 中",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "你確定要黑名單這個螢幕 \"{0}\"？",
    "Yes": "是",
    "No": "否",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "重新讀取記錄檔",
    "Do not show the clock on secondary monitors": "不要在第二螢幕上顯示時鐘",
    "Disable clock taskbar background color (make clock transparent)": "停用工具列時鐘背景（使時鐘變成透明的）",
    "Open the welcome wizard": "開啟歡迎畫面",
    " (ALPHA STAGE, MAY NOT WORK)": "（Alpha 版本，可能無法正常運作）",
    "Welcome to ElevenClock": "歡迎使用 ElevenClock",
    "Skip": "略過",
    "Start": "開始",
    "Next": "下一步",
    "Finish": "完成",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "工作管理員",
    "Change date and time": "調整日期和時間",
    "Notification settings": "通知設定",
    "Updates, icon tray, language": "更新、系統匣、語言",
    "Hide extended options from the clock right-click menu (needs a restart to be applied)": "隱藏右鍵功能表中的延伸選項（需要重新啟動以進行套用）",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "全螢幕行為、時鐘位置、主要螢幕時鐘、其他雜項設定",
    'Add the "Show Desktop" button on the left corner of every clock': '新增「顯示桌面」的按鈕到每個時鐘角落',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': '為使本功能正常運作，你可能需要設定自訂背景顏色。&nbsp;更多資訊見 <a href="{0}" style="color:DodgerBlue">這裡</a>',
    "Clock's font, font size, font color and background, text alignment": "時鐘字型、字型大小、字型色彩、文字背景、文字對齊",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "日期格式、時間格式、秒數顯示、星期幾、週數、地區設定",
    "Testing features and error-fixing tools": "實驗性功能、錯誤修正工具",
    "Language pack author(s), help translating ElevenClock": "語言套件作者（翻譯協助者）",
    "Info, report a bug, submit a feature request, donate, about": "資訊、錯誤回報、功能請求、贊助、關於",
    "Log, debugging information": "日誌、除錯資訊",
    "Do not show the clock on secondary monitors": "不要在第二螢幕上顯示時鐘",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen": "強制將時鐘放置於螢幕最上方",
    "Show the clock on the primary screen": "在主要螢幕上顯示時鐘",
    "Use a custom font color": "使用自訂字型顏色",
    "Use a custom background color": "使用自訂背景顏色",
    "Align the clock text to the center": "將時鐘文字與中心對齊",
    "Select custom color": "選擇自訂顏色",
    "Hide the clock when a program occupies all screens": "當程式佔用所有顯示器時隱藏時鐘",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "使用自訂字型",
    "Use a custom font size": "使用自訂字型大小",
    "Enable hide when multi-monitor fullscreen apps are running": "在多螢幕全螢幕應用程式執行時隱藏時鐘",
    "<b>{0}</b> needs to be enabled to change this setting": "你需要啟用 <b>{0}</b> 以使用此選項",
    "<b>{0}</b> needs to be disabled to change this setting": "你需要停用 <b>{0}</b> 以使用此選項",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": "（這個功能因為預設情況下就能正確運作所以被停用了，如果它實際上不能正確運作，請回報錯誤）",
    "ElevenClock's language": "ElevenClock 語言"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "關於 Qt6 (PySide6)",
    "About": "關於",
    "Alternative non-SSL update server (This might help with SSL errors)": "選用的無 SSL 更新伺服器（可能對 SSL 錯誤的情況有用）",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "錯誤修正以及其他實驗性更新（請「只」在有東西無法正常運作時使用）",
    "Show week number on the clock": "顯示週數",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "在使用 RDP 用戶端或是 Citrix Workspace 時隱藏時鐘",
    "Clock Appearance:": "時鐘外觀",
    "Force the clock to have black text": "強制時鐘使用黑色文字",
    " - It is required that the Dark Text checkbox is disabled": " - 必須關閉「強制時鐘使用黑色文字」",
    "Debbugging information:": "除錯資訊",
    "Open ElevenClock's log": "打開 ElevenClock 的日誌",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "將時鐘顯示於主螢幕上（在你希望把時鐘顯示在左邊時很有用）",
    "Show weekday on the clock"  :"將星期幾顯示於時鐘上",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"ElevenClock 設定", # Also settings title
    "Reload Clocks"             :"重新整理時鐘",
    "ElevenClock v{0}"          :"ElevenClock 版本 {0}",
    "Restart ElevenClock"       :"重新啟動 ElevenClock",
    "Hide ElevenClock"          :"隱藏 ElevenClock",
    "Quit ElevenClock"          :"關閉 ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"一般設定",
    "Automatically check for updates"                                                   :"自動檢查更新",
    "Automatically install available updates"                                           :"自動安裝更新",
    "Enable really silent updates"                                                      :"啟用靜默更新",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"跳過更新來源驗證（不推薦，請自行考慮風險）",
    "Show ElevenClock on system tray"                                                   :"在系統匣顯示 ElevenClock",
    "Alternative clock alignment (may not work)"                                        :"替代的時鐘對齊方式（可能不能正常運作）",
    "Change startup behaviour"                                                          :"修改開機自動啟動行為",
    "Change"                                                                            :"修改",
    "<b>Update to the latest version!</b>"                                             :"<b>更新到最新版本！</b>",
    "Install update"                                                                    :"安裝更新",
    
    #Clock settings
    "Clock Settings:"                                              :"時鐘設定",
    "Hide the clock in fullscreen mode"                            :"在全螢幕模式下隱藏時鐘",
    "Hide the clock when RDP client is active"                     :"在使用 RDP 用戶端時隱藏時鐘",
    "Force the clock to be at the bottom of the screen"            :"強制將時鐘置於螢幕底部",
    "Show the clock when the taskbar is set to hide automatically" :"在使用「自動隱藏工作列」時顯示時鐘",
    "Fix the hyphen/dash showing over the month"                   :"修正連字符以及底線會壓住月份的問題",
    "Force the clock to have white text"                           :"強制時鐘使用白色文字",
    "Show the clock at the left of the screen"                     :"將時鐘顯示於螢幕左邊",
    
    #Date & time settings
    "Date & Time Settings:"                             :"日期以及時間設定",
    "Show seconds on the clock"                         :"顯示秒數",
    "Show date on the clock"                            :"顯示日期",
    "Show time on the clock"                            :"顯示時間",
    "Change date and time format (Regional settings)"   :"修改時間以及日期格式（地區設定）",
    "Regional settings"                                 :"地區設定",
    
    #About the language pack
    "About the language pack:"                  :"關於此語言套件",
    "Translated to English by martinet101"      :"由 mmis1000、BoyceLig 翻譯為正體中文（台灣）", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"將 ElevenClock 翻譯成你的語言",
    "Get started"                               :"立刻開始",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"關於 ElevenClock 版本 {0}",
    "View ElevenClock's homepage"               :"檢視 ElevenClock 專案首頁",
    "Open"                                      :"打開",
    "Report an issue/request a feature"         :"回報錯誤/提出新的功能請求",
    "Report"                                    :"回報",
    "Support the dev: Give me a coffee☕"       :"支援開發者：給我一杯咖啡☕",
    "Open page"                                 :"打開",
    "Icons by Icons8"                           :"圖標由 Icons8 提供", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"網站",
    "Close settings"                            :"關閉設定",
    "Close"                                     :"關閉",
}

lang = lang2_3
