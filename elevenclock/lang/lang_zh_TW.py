# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang2_5 = {
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
    "<b>Update to the lastest version!</b>"                                             :"<b>更新到最新版本！</b>",
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
    "About the language pack:"                  :"關於此語言包",
    "Translated to English by martinet101"      :"由 mmis1000 翻譯為正體中文（台灣）", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
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