# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"

# So it would look like: "ORIGINAL_TEXT" : "TRANSLATED_TEXT",


# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_2_8 = {
    "Force the clock to be at the top of the screen": "Az óra kényszerítése a képernyő tetejére",
    "Show the clock on the primary screen": "Az óra megjelenítése az elsődleges kijelzőn",
    "Use a custom font color": "Egyedi betűszín használata",
    "Use a custom background color": "Egyedi háttérszín használata",
    "Align the clock text to the center": "Az óra szövegének középre igazítása",
    "Select custom color": "Egyedi szín választása",
    "Hide the clock when a program occupies all screens": "Óra elrejtése amikor egy alkalmazás elfoglalja az összes kijelzőt",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "Egyedi betűtípus használata",
    "Use a custom font size": "Egyedi betűméret használata",
    "Enable hide when multi-monitor fullscreen apps are running": "Elrejtés engedélyezése többkijelzős, teljes képernyős alkalmazások futásakor",
    "<b>{0}</b> needs to be enabled to change this setting": "Ezen beállítás módosításához engedélyezni kell a következőt: <b>{0}</b>",
    "<b>{0}</b> needs to be disabled to change this setting": "Ezen beállítás módosításához le kell tiltani a következőt: <b>{0}</b>",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": " (Ez a funkció letiltásra került, mert alapértelmezetten működnie kellene. Ha mégsem működik kérem jelentse a hibát!)",
    "ElevenClock's language": "Az ElevenClock nyelve"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "A Qt6 (PySide6)-ról",
    "About": "Megnyitás",
    "Alternative non-SSL update server (This might help with SSL errors)": "Alternatív, nem-SSL frissítési szerver (Ez segíthet SSL hibák esetén)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Javítások és egyéb kísérleti funkciók (Csak hibás működés esetén használja)",
    "Show week number on the clock": "A hetek számának mutatása"
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Az óra elrejtése RDP kliens, vagy Citrix Workspace futása esetén",
    "Clock Appearance:": "Az óra megjelenése:",
    "Force the clock to have black text": "Fekete betűszín kényszerítése",
    " - It is required that the Dark Text checkbox is disabled": " - A sötét szöveg letiltása kötelező",
    "Debbugging information:": "Fejlesztői információk:",
    "Open ElevenClock's log": "Az ElevenClock eseménynaplója",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Óra megjelenítése az elsődleges képernyőn (Hasznos, ha az óra a bal oldalon jelenik meg)",
    "Show weekday on the clock"  :"A hét napjának mutatása",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"ElevenClock beállításai", # Also settings title
    "Reload Clocks"             :"Órák újratöltése",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"ElevenClock újraindítása",
    "Hide ElevenClock"          :"ElevenClock elrejtése",
    "Quit ElevenClock"          :"Kilépés az ElevenClock-ból",
    
    #General settings section
    "General Settings:"                                                                 :"Általános beállítások:",
    "Automatically check for updates"                                                   :"Frissítések automatikus keresése",
    "Automatically install available updates"                                           :"Elérhető frissítések automatikus telepítése",
    "Enable really silent updates"                                                      :"Csendes frissítések engedélyezése",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Ne ellenőrizze a frissítő szolgáltatás hitelességét (NEM JAVASOLT! HASZNÁLAT CSAK SAJÁT FELELŐSSÉGRE!)",
    "Show ElevenClock on system tray"                                                   :"Az ElevenClock megjelenítése a tálcán",
    "Alternative clock alignment (may not work)"                                        :"Alternatív óra elrendezés (nem mindig működik)",
    "Change startup behaviour"                                                          :"Indítás a rendszerrel",
    "Change"                                                                            :"Módosítás",
    "<b>Update to the latest version!</b>"                                             :"<b>Frissíts a legújabb verzióra!</b>",
    "Install update"                                                                    :"Frissítés telepítése",
    
    #Clock settings
    "Clock Settings:"                                              :"Óra beállításai:",
    "Hide the clock in fullscreen mode"                            :"Óra elrejtése teljes képernyős módban",
    "Hide the clock when RDP client is active"                     :"Óra elrejtése, amikor az RDP kliens aktív",
    "Force the clock to be at the bottom of the screen"            :"Az óra kényszerítése a képernyő aljára",
    "Show the clock when the taskbar is set to hide automatically" :"Az óra megjelenítése a tálca automatikus elrejtésekor",
    "Fix the hyphen/dash showing over the month"                   :"A per/kötőjel megjavítása, ha a hónap felett jelenik meg",
    "Force the clock to have white text"                           :"Fehér betűszín kényszerítése",
    "Show the clock at the left of the screen"                     :"Az óra megjelenítése a képernyő bal oldalán",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Idő és dátum beállításai:",
    "Show seconds on the clock"                         :"Másodpercek megjelenítése",
    "Show date on the clock"                            :"Dátum megjelenítése",
    "Show time on the clock"                            :"Idő megjelenítése",
    "Change date and time format (Regional settings)"   :"Dátum és idő formátumának módosítása (Területi beállítások)",
    "Regional settings"                                 :"Területi beállítások",
    
    #About the language pack
    "About the language pack:"                  :"A nyelvi csomagról:",
    "Translated to English by martinet101"      :"Magyarra fordította: morbydance", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Az ElevenClock fordítása a nyelvedre",
    "Get started"                               :"Kezdés",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Az ElevenClock version {0}-ról:",
    "View ElevenClock's homepage"               :"Az ElevenClock honlapjának megtekintése",
    "Open"                                      :"Megnyitás",
    "Report an issue/request a feature"         :"Hiba jelentése, javaslat küldése",
    "Report"                                    :"Jelentés",
    "Support the dev: Give me a coffee☕"       :"A fejlesztő támogatása: Vegyél nekem egy kávét ☕",
    "Open page"                                 :"Megnyitás",
    "Icons by Icons8"                           :"Ikonok: Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Honlap",
    "Close settings"                            :"Beállítások bezárása",
    "Close"                                     :"Bezárás",
}

lang = lang2_3
