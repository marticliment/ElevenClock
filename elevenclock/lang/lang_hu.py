# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"

# So it would look like: "ORIGINAL_TEXT" : "TRANSLATED_TEXT",


# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_3_1 = {
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
    "Hide the clock during 10 seconds when clicked": "Kattintás után az óra elrejtése 10 másodpercre",
    "Enable low-cpu mode": "Alacsony CPU-használat",
    "You might lose functionalities, like the notification counter or the dynamic background": "Olyan funkciókat veszíthet el, mint pl. az értesítések számlálója vagy a dinamikus háttér",
    "Clock position and size:": "Óra helye és mérete",
    "Clock size preferences, position offset, clock at the left, etc.": "Óra mérete, helye, óra a bal oldalon, stb.",
    "Reset monitor blacklisting status": "Monitor tiltási állapotának megszüntetése",
    "Reset": "Visszaállítás",
    "Third party licenses": "Harmadik fél licencei",
    "View": "Nézet",
    "ElevenClock": "ElevenClock",
    "Monitor tools": "Monitoreszközök",
    "Blacklist this monitor": "Jelenlegi monitor tiltása",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "Harmadik fél által készített nyílt forráskódú szoftverek (ElevenClock {0}) (és licenceik)",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "Az ElevenClock nyílt forráskódú alkalmazás, amely más, a közösség által készített könyvtárak segítségével készült.",
    "Ok": "Ok",
    "More Info": "További információk",
    "About Qt": "Qt névjegye",
    "Success": "Sikerült",
    "The monitors were unblacklisted successfully.": "A monitorok tiltási állapotának megszüntetése sikeres volt.",
    "Now you should see the clock everywhere": "Most már mindenhol látható az óra",
    "Ok": "Ok",
    "Blacklist Monitor": "Monitor tiltása",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "Monitor tiltása véglegesen elrejti az órát ezen a monitoron",
    "This action can be reverted from the settings window, under <b>Clock position and size</b>": "Ezt a műveletet a a Beállításoknál, az <b>Óra helye és mérete</b> alatt lehet visszavonni",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "Biztosan letiltja a következő monitort: \"{0}\"?",
    "Yes": "Igen",
    "No": "Nem",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "Napló újratöltése",
    "Do not show the clock on secondary monitors": "Ne jelentítse meg az órát a másodlagos monitoron",
    "Disable clock taskbar background color (make clock transparent)": "Az óra háttérszínének letiltása a tálcán",
    "Open the welcome wizard": "Az Üdvözlővarázsló megnyitása",
    " (ALPHA STAGE, MAY NOT WORK)": " (ALFAÁLLAPOTÚ, LEHET, HOGY NEM MŰKÖDIK)",
    "Welcome to ElevenClock": "Üdvözli az ElevenClock",
    "Skip": "Kihagyás",
    "Start": "Indítás",
    "Next": "Tovább",
    "Finish": "Befejezés",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "Feladatkezelő",
    "Change date and time": "A dátum és az idő beállítása",
    "Notification settings": "Értesítési beállítások",
    "Updates, icon tray, language": "Frissítések, tálca ikonja, nyelv",
    "Hide extended options from the clock right-click menu (needs a restart to be applied)": "Kiterjesztett beállítások elrejtése az óra helyi menüjében",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "Teljes képernyős működés, óra helye, első monitor órája, egyéb beállítások",
    'Add the "Show Desktop" button on the left corner of every clock': 'Az "Asztal mutatása" gomb hozzáadása az összes óra bal sarkában',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': 'Egyedi háttérszínre lehet szükséges ennek a funkciónak a használatához.&nbsp;További információkat <a href="{0}" style="color:DodgerBlue">ITT</a> talál.',
    "Clock's font, font size, font color and background, text alignment": "Óra betűtípusa, betűk mérete, betűk színe és háttere, szövegigazítás",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "Dátumformátum, időformátum, másodpercek, hét száma, területi beállítások",
    "Testing features and error-fixing tools": "Tesztelési funkciók és hibajavításra használt eszközök",
    "Language pack author(s), help translating ElevenClock": "Nyelvi csomagok készítői, segítségnyújtás az ElevenClock fordításában",
    "Info, report a bug, submit a feature request, donate, about": "Információk, hibajelentés, új funkció kérelmezése, anyagi támogatás, névjegy",
    "Log, debugging information": "Eseménynapló, hibakeresési információ",
}

lang_2_8 = lang_2_9 | {
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
    "Translated to English by martinet101"      :"Magyarra fordította: morbydance, viktak.com (2.9 - 3.0)", # Here, make sure to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
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
