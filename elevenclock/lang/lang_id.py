# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_2_1 = {
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
    "This action can be reverted from the settings window. under <b>Clock position and size</b>": "",
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
    "Hide the clock when RDP Client or Citrix Workspace are running": "Sembunyikan jam ketika Klien RDP atau Citrix Workspace sedang berjalan",
    "Clock Appearance:": "Tampilan jam:",
    "Force the clock to have black text": "Paksakan tulisan pada jam berwarna hitam",
    " - It is required that the Dark Text checkbox is disabled": " - Dark Text diharuskan untuk tidak dicentang",
    "Debbugging information:": "Informasi Debug:",
    "Open ElevenClock's log": "Buka log ElevenClock",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Tampilkan jam pada monitor utama (Berguna jika jam ditampilkan pada bagian kiri)",
    "Show weekday on the clock"  :"Tampilkan hari pada jam",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"Pengaturan ElevenClock", # Also settings title
    "Reload Clocks"             :"Muat ulang jam",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"Mulai ulang ElevenClock",
    "Hide ElevenClock"          :"Sembunyikan ElevenClock",
    "Quit ElevenClock"          :"Keluar dari ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Pengaturan umum:",
    "Automatically check for updates"                                                   :"Otomatisasikan pengecekan pembaharuan",
    "Automatically install available updates"                                           :"Otomatisasikan pemasangan pembaharuan jika tersedia",
    "Enable really silent updates"                                                      :"Nyalakan pembaharuan secara diam-diam",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Lewati pembaharuan pengecekan autentik oleh provider (SANGAT TIDAK DISARANKAN, LAKUKAN DENGAN RESIKO SENDIRI)",
    "Show ElevenClock on system tray"                                                   :"Tampilkan ElevenClock pada system tray",
    "Alternative clock alignment (may not work)"                                        :"Posisi alternatif jam (ada kemungkinan tidak bekerja)",
    "Change startup behaviour"                                                          :"Ganti perilaku startup",
    "Change"                                                                            :"Ganti",
    "<b>Update to the latest version!</b>"                                             :"<b>Pembaharuan ke versi terbaru!</b>",
    "Install update"                                                                    :"Pasang pembaharuan",
    
    #Clock settings
    "Clock Settings:"                                              :"Pengaturan jam:",
    "Hide the clock in fullscreen mode"                            :"Sembunyikan jam ketika berada pada mode layar penuh",
    "Hide the clock when RDP client is active"                     :"Sembunyikan jam saat klien RDP sedang aktif",
    "Force the clock to be at the bottom of the screen"            :"Paksa jam untuk berada pada bagian bawah layar",
    "Show the clock when the taskbar is set to hide automatically" :"Tampilkan jam ketika taskbar diatur ke sembunyikan otomatis",
    "Fix the hyphen/dash showing over the month"                   :"Perbaiki tanda penghubung/garis setrip yang ditunjukkan di atas bulan",
    "Force the clock to have white text"                           :"Paksa tulisan pada jam berwarna putih",
    "Show the clock at the left of the screen"                     :"Tampilkan jam pada bagian kiri layar",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Pengaturan tanggal & waktu:",
    "Show seconds on the clock"                         :"Tampilkan detik pada jam",
    "Show date on the clock"                            :"Tampilkan tanggal pada jam",
    "Show time on the clock"                            :"Tampilkan waktu pada jam",
    "Change date and time format (Regional settings)"   :"Ganti format tanggal dan waktu (Pengaturan regional)",
    "Regional settings"                                 :"Pengaturan regional",
    
    #About the language pack
    "About the language pack:"                  :"Tentang kemasan bahasa:",
    "Translated to English by martinet101"      :"Terjemahan oleh FahrulID | ig:@fahrulrputra", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Terjemahkan ElevenClock ke bahasamu",
    "Get started"                               :"Memulai",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Tentang versi ElevenClock {0}:",
    "View ElevenClock's homepage"               :"Lihat halaman utama ElevenClock",
    "Open"                                      :"Buka",
    "Report an issue/request a feature"         :"Laporkan isu/permintaan pada fitur",
    "Report"                                    :"Laporkan",
    "Support the dev: Give me a coffee☕"       :"Bantu developer dengan: Membeli secangkir kopi☕",
    "Open page"                                 :"Buka halaman",
    "Icons by Icons8"                           :"Ikon oleh Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Halaman web",
    "Close settings"                            :"Tutup pengaturan",
    "Close"                                     :"Tutup",
}

lang = lang2_3
