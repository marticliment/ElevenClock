# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang2_5 = {
    "Hide the clock when RDP Client or Citrix Workspace are running": "",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "",
    "Show weekday on the clock"  :"",
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
    "<b>Update to the lastest version!</b>"                                             :"<b>Son versiyona güncelle!</b>",
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