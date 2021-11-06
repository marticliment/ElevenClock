# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang2_5 = {
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
    "<b>Update to the lastest version!</b>"                                             :"<b>Pembaharuan ke versi terbaru!</b>",
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