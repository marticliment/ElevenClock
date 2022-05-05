# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_5_0 = {
    "Tooltip Appearance:"                                   : "Wygląd okna podpowiedzi",
    "Tooltip's font, font size, font color and background"  : "Czcionka, wielkość i kolor czcionki, tło okna podpowiedzi",
    "Disable tooltip's blurry background"                   : "Wyłącz rozmyte tło okna podpowiedzi",
    "Sync time with the internet"                           : "Synchronizuj czas z internetem",
    "Internet date and time"                                : "Czas i data z internetu",
    "Select internet time provider, change sync frequency"  : "Wybierz dostawcę czasu z internetu, zmień częstotliwość synchronizacji",
    "Enable internet time sync"                             : "Włącz synchronizację czasu z internetem",
    "Paste a URL from the world clock api or equivalent"    : "Wklej URL zgodny z World Clock API lub podobnym",
    "Help"                                                  : "Pomoc",
    "Internet sync frequency"                               : "Częstotliwość synchronizacji z internetem",
    "10 minutes"                                            : "10 minut",
    "30 minutes"                                            : "30 minut",
    "1 hour"                                                : "1 godzina",
    "2 hours"                                               : "2 godziny",
    "4 hours"                                               : "4 godziny",
    "10 hours"                                              : "10 godzin",
    "24 hours"                                              : "24 godziny",
}

lang_3_4_0 = lang_3_5_0 | {
    "Show calendar"                                         : "Pokaż kalendarz",
    "Disabled"                                              : "Wyłączony",
    "Open quick settings"                                   : "Otwórz szybkie ustawienia",
    "Show desktop"                                          : "Pokaż pulpit",
    "Open run dialog"                                       : "Otwórz `Uruchom`",
    "Open task manager"                                     : "Otwórz menedżer zadań",
    "Open start menu"                                       : "Otwórz menu start",
    "Open search menu"                                      : "Otwórz menu wyszukiwania",
    "Change task"                                           : "Zmień zadanie",
    "Change the action done when the clock is clicked"      : "Zmień akcję wykonywaną po kliknięciu w zegar",
}

lang_3_3_2 = lang_3_4_0 | {
    "ElevenClock Updater"                                   : "Aktualizator ElevenClock",
    "ElevenClock is downloading updates"                    : "ElevenClock pobiera aktualizacje",
    "ElevenClock has updated to version {0} successfully\nPlease see GitHub for the changelog": "ElevenClock został pomyślnie zaktualizowany do wersji {0}\nSprawdź GitHub, aby zobaczyć listę zmian",
    "Customize the clock on Windows 11"                     : "Dostosuj zegar w Windowsie 11",
    "Disable the new instance checker method"               : "Wyłącz nową metodę sprawdzania instancji",
    "Import settings from a local file"                     : "Importuj ustawienia z pliku",
    "Export settings to a local file"                       : "Eksportuj ustawienia do pliku",
    "Export"                                                : "Eksport",
    "Import"                                                : "Import",
}

lang_3_3_1 = lang_3_3_2 | {
    "Invalid time format\nPlease follow the\nC 1989 Standards": "Niewłaściwy format daty\nWprowadź ją zgodnie ze standardem\nC 1989 Standards",
    "Nothing to preview"                                    : "Brak podglądu",
    "Invalid time format\nPlease modify it\nin the settings": "Niewłaściwy format daty\nZmień go\nwustawieniach",
    "Disable the tooltip shown when the clock is hovered"   : "Wyłącz okno podpowiedzi pokazywane gdy kursor najeżdża nad ikonę zegara"
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
    "Enable hide when multi-monitor fullscreen apps are running"    : "",
    "<b>{0}</b> needs to be enabled to change this setting"         : "<b>{0}</b> musi zostać włączone aby zmienić to ustawienie",
    "<b>{0}</b> needs to be disabled to change this setting"        : "<b>{0}</b> musi zostać wyłączone aby zmienić to ustawienie",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)"    : " (Ta funkcja została wyłączona, bo powinna zawsze działać. Jeśli tak nie jest, zgłoś błąd)",
    "ElevenClock's language"                                                                                    : "Język ElevenClock"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)"                                                               : "O Qt6 (PySide6)",
    "About"                                                                             : "Więcej o",
    "Alternative non-SSL update server (This might help with SSL errors)"               : "Alternatywny serwer aktualizacji bez SSL (Może pomóc z problemem SSL)",
    "Fixes and other experimental features: (Use ONLY if something is not working)"     : "Poprawki i inne funkcje eksperymentalne: (korzystaj TYLKO jeśli coś nie działa)",
    "Show week number on the clock"                                                     : "Pokaż numery dni tygodnia na zegarze",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running"    : "Ukryj zegar, gdy działa klient RDP lub Citrix Workspace",
    "Clock Appearance:"                                                 : "Wygląd zegara",
    "Force the clock to have black text"                                : "Wymuś czarny kolor tekstu zegara",
    " - It is required that the Dark Text checkbox is disabled"         : " - Wymagane jest odznaczenie opcji czarnego koloru tekstu zegara",
    "Debbugging information:"                                           : "Informacje debugowania:",
    "Open ElevenClock's log"                                            : "Otwórz plik logów ElevenClock",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Pokaż zegar na głównym ekranie (Przydatne, jeśli zegar jest ustawiony po lewej stronie)",
    "Show weekday on the clock"  :"Pokaż dzień tygodnia na zegarze",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"Ustawienia ElevenClock", # Also settings title
    "Reload Clocks"             :"Zresetuj zegar",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"Zrestartuj ElevenClock",
    "Hide ElevenClock"          :"Ukryj ElevenClock",
    "Quit ElevenClock"          :"Zamknij ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Ustawienia ogólne:",
    "Automatically check for updates"                                                   :"Automatycznie sprawdzaj aktualizacje",
    "Automatically install available updates"                                           :"Automatycznie instaluj dostępne aktualizacje",
    "Enable really silent updates"                                                      :"Włącz ciche aktualizacje",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Nie sprawdzaj autentyczności dostawcy aktualizacji (NIE ZALECANE, NA WŁASNE RYZYKO)",
    "Show ElevenClock on system tray"                                                   :"Pokaż ElevenClock na pasku zadań",
    "Alternative clock alignment (may not work)"                                        :"Zsynchronizuj zegar z alternatywnym serwerem (może nie działać)",
    "Change startup behaviour"                                                          :"Zmień zachowanie przy uruchamianiu",
    "Change"                                                                            :"Zmień",
    "<b>Update to the latest version!</b>"                                              :"<b>Zaktualizuj do najnowszej wersji!</b>",
    "Install update"                                                                    :"Zainstaluj aktualizację",
    
    #Clock settings
    "Clock Settings:"                                              :"Ustawienia zegara:",
    "Hide the clock in fullscreen mode"                            :"Ukryj zegar w trybie pełnoekranowym",
    "Hide the clock when RDP client is active"                     :"Ukryj zegar, gdy klient RDP jest aktywny",
    "Force the clock to be at the bottom of the screen"            :"Ustaw zegar na dole ekranu",
    "Show the clock when the taskbar is set to hide automatically" :"Pokaż zegar, gdy pasek zadań jest ustawiony na automatyczne ukrywanie",
    "Fix the hyphen/dash showing over the month"                   :"Zmień myślnik / kreskę przy wyświetlaniu miesiąca",
    "Force the clock to have white text"                           :"Wymuś, aby zegar miał biały tekst",
    "Show the clock at the left of the screen"                     :"Pokaż zegar po lewej stronie ekranu",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Ustawienia daty i czasu:",
    "Show seconds on the clock"                         :"Pokaż sekundy",
    "Show date on the clock"                            :"Pokaż datę",
    "Show time on the clock"                            :"Pokaż godzinę",
    "Change date and time format (Regional settings)"   :"Zmień format daty i czasu (ustawienia regionalne)",
    "Regional settings"                                 :"Ustawienia regionalne",
    
    #About the language pack
    "About the language pack:"                  :"O pakiecie językowym:",
    "Translated to English by martinet101"      :"Przetłumaczone na polski przez kinr0k", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Przetłumacz ElevenClock na swój język",
    "Get started"                               :"Rozpocznij",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"O ElevenClock w wersji {0}:",
    "View ElevenClock's homepage"               :"Wyświetl stronę główną ElevenClock",
    "Open"                                      :"Otwórz",
    "Report an issue/request a feature"         :"Zgłoś problem/prośbę o funkcję",
    "Report"                                    :"Zgłoś",
    "Support the dev: Give me a coffee☕"        :"Wsparcie dla dewelopera: Kup mi kawę ☕",
    "Open page"                                 :"Otwórz stronę",
    "Icons by Icons8"                           :"Ikony z Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Strona internetowa",
    "Close settings"                            :"Zamknij ustawienia",
    "Close"                                     :"Zamknij",
}

lang = lang2_3
