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
    "Open online help to troubleshoot problems": "",
    "Reset ElevenClock preferences to defaults": "",
    "Specify a minimum width for the clock": "",
    "Search on the settings": "",
    "No results were found": "",
}

lang_3_2 = lang_3_2_1 | {
    "Use system accent color as background color": "",
    "Check only the focused window on the fullscreen check": "",
    "Clock on monitor {0}": "",
    "Move to the left": "",
    "Show this clock on the left": "",
    "Show this clock on the right": "",
    "Restore clock position": "",
}

lang_3_1 = lang_3_2 | {
    "W": "", # The initial of the word week in your language: W for week, S for setmana, etc.
    "Disable the notification badge": "",
    "Override clock default height": "",
    "Adjust horizontal clock position": "",
    "Adjust vertical clock position": "",
    "Export log as a file": "",
    "Copy log to clipboard": "",
    "Announcements:": "",
    "Fetching latest announcement, please wait...": "",
    "Couldn't load the announcements. Please try again later": "",
    "ElevenClock's log": "",
    "Pick a color": ""
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "",
    "Enable low-cpu mode": "",
    "You might lose functionalities, like the notification counter or the dynamic background": "",
    "Clock position and size:": "",
    "Clock size preferences, position offset, clock at the left, etc.": "",
    "Reset monitor blacklisting status": "",
    "Reset": "",
    "Third party licenses": "",
    "View": "",
    "ElevenClock": "",
    "Monitor tools": "",
    "Blacklist this monitor": "",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "",
    "Ok": "",
    "More Info": "",
    "About Qt": "",
    "Success": "",
    "The monitors were unblacklisted successfully.": "",
    "Now you should see the clock everywhere": "",
    "Ok": "",
    "Blacklist Monitor": "",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "",
    "This action can be reverted from the settings window, under <b>Clock position and size</b>": "",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "",
    "Yes": "",
    "No": "",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "",
    "Do not show the clock on secondary monitors": "",
    "Disable clock taskbar background color (make clock transparent)": "",
    "Open the welcome wizard": "",
    " (ALPHA STAGE, MAY NOT WORK)": "",
    "Welcome to ElevenClock": "",
    "Skip": "",
    "Start": "",
    "Next": "",
    "Finish": "",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "",
    "Change date and time": "",
    "Notification settings": "",
    "Updates, icon tray, language": "",
    "Hide extended options from the clock right-click menu (needs a restart to be applied)": "",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "",
    'Add the "Show Desktop" button on the left corner of every clock': '',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': '',
    "Clock's font, font size, font color and background, text alignment": "",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "",
    "Testing features and error-fixing tools": "",
    "Language pack author(s), help translating ElevenClock": "",
    "Info, report a bug, submit a feature request, donate, about": "",
    "Log, debugging information": "",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen": "",
    "Show the clock on the primary screen": "",
    "Use a custom font color": "",
    "Use a custom background color": "",
    "Align the clock text to the center": "",
    "Select custom color": "",
    "Hide the clock when a program occupies all screens": "",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "",
    "Use a custom font size": "",
    "Enable hide when multi-monitor fullscreen apps are running": "",
    "<b>{0}</b> needs to be enabled to change this setting": "",
    "<b>{0}</b> needs to be disabled to change this setting": "",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": "",
    "ElevenClock's language": ""
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "",
    "About": "",
    "Alternative non-SSL update server (This might help with SSL errors)": "",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "",
    "Show week number on the clock": "",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "RDP Client veya Citrix Çalışma Alanı aktifken saati gizle",
    "Clock Appearance:": "Saat Görünümü",
    "Force the clock to have black text": "Saatin siyah yazı renginde olmasına zorla",
    " - It is required that the Dark Text checkbox is disabled": "- Siyah Metin onay kutusunun devre dışı bırakılması gerekir",
    "Debbugging information:": "- Koyu Metin onay kutusunun devre dışı bırakılması gerekir",
    "Open ElevenClock's log": "ElevenClock kayıtlarını aç",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Saati birincil ekranda göster (Saat solda ayarlanmışsa kullanışlıdır)",
    "Show weekday on the clock"  :"Saatte haftanın gününü göster",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"ElevenClock Ayarlar", # Also settings title
    "Reload Clocks"             :"Saatleri Yenile",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"ElevenClock'u Yeniden Başlat",
    "Hide ElevenClock"          :"ElevenClock'u Gizle",
    "Quit ElevenClock"          :"ElevenClock'tan Çık",
    
    #General settings section
    "General Settings:"                                                                 :"Genel Ayarlar:",
    "Automatically check for updates"                                                   :"Güncelleştirmeleri otomatik kontrol et",
    "Automatically install available updates"                                           :"Mevcut güncellemeleri otomatik yükle",
    "Enable really silent updates"                                                      :"Küçük güncelleştirmeleri aktif et",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Güncelleme sağlayıcı onaylama kontrolünü atla  (TAVSİYE EDİLMEZ, RİSK SİZE AİTTİR)",
    "Show ElevenClock on system tray"                                                   :"ElevenClock'u sistem tepsisinde göster",
    "Alternative clock alignment (may not work)"                                        :"Alternatif saat hizalaması (çalışmayabilir)",
    "Change startup behaviour"                                                          :"Başlangıç davranışını değiştir",
    "Change"                                                                            :"Değiştir",
    "<b>Update to the latest version!</b>"                                             :"<b>Son versiyona güncelle!</b>",
    "Install update"                                                                    :"Güncelleştirmeyi yükle",
    
    #Clock settings
    "Clock Settings:"                                              :"Saat Ayarları:",
    "Hide the clock in fullscreen mode"                            :"Tam ekran modunda saati gize",
    "Hide the clock when RDP client is active"                     :"RDP client aktifken saati gizle",
    "Force the clock to be at the bottom of the screen"            :"Saati ekranın alt tarafında olmasına zorla",
    "Show the clock when the taskbar is set to hide automatically" :"Görev çubuğu otomatik gizlense bile saati göster",
    "Fix the hyphen/dash showing over the month"                   :"Ay için gösterilen kısa çizgiyi/tireyi düzeltin",
    "Force the clock to have white text"                           :"Saati beyaz yazı renginde olmasına zorla",
    "Show the clock at the left of the screen"                     :"Saati ekranın sol tarafında göster",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Tarih & Zaman Ayarları:",
    "Show seconds on the clock"                         :"Saniye bilgisini göster",
    "Show date on the clock"                            :"Tarih bilgisini göster",
    "Show time on the clock"                            :"Zaman bilgisini göster",
    "Change date and time format (Regional settings)"   :"Tarih ve zaman formatını değiştir (Bölgesel ayarlar)",
    "Regional settings"                                 :"Bölgesel ayarlar",
    
    #About the language pack
    "About the language pack:"                  :"Dil paketi hakkında:",
    "Translated to English by martinet101"      :"Türkçeye cotur tarafından çevrildi", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"ElevenClock'u kendi diline çevir",
    "Get started"                               :"Başlarken",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"ElevenClock versiyonu {0}:",
    "View ElevenClock's homepage"               :"ElevenClock anasayfasını göster",
    "Open"                                      :"Aç",
    "Report an issue/request a feature"         :"Geri bildirimde bulun",
    "Report"                                    :"Rapor et",
    "Support the dev: Give me a coffee☕"       :"Destek: Bi kahve ısmarla☕",
    "Open page"                                 :"Sayfayı aç",
    "Icons by Icons8"                           :"Ikonlar: Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Websitesi",
    "Close settings"                            :"Ayarları kapat",
    "Close"                                     :"Kapat",
}

lang = lang2_3
