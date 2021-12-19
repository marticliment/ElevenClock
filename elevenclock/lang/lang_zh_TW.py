# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_2_9 = {
    "Task Manager": "工作管理員",
    "Change date and time": "調整日期和時間",
    "Notification settings": "通知設定",
    "Updates, icon tray, language": "更新、系統匣、語言",
    "Hide extended options from the clock right-click menu (needs a restart to be aplied)": "隱藏右鍵功能表中的延伸選項（需要重新啟動以進行套用）",
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
