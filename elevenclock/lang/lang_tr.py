# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_2_9 = {
    "Task Manager": "",
    "Change date and time": "",
    "Notification settings": "",
    "Updates, icon tray, language": "",
    "Hide extended options from the clock right-click menu (needs a restart to be aplied)": "",
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
