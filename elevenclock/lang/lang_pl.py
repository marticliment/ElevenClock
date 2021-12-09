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
    "About Qt6 (PySide6)": "O Qt6 (PySide6)",
    "About": "Więcej o",
    "Alternative non-SSL update server (This might help with SSL errors)": "Alternatywny serwer aktualizacji bez SSL (Może pomóc z problemem SSL)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "",
    "Show week number on the clock": "Pokaż numery dni tygodnia na zegarze",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Ukryj zegar, gdy działa klient RDP lub Citrix Workspace",
    "Clock Appearance:": "Wygląd zegara",
    "Force the clock to have black text": "Wymuś czarny kolor tekstu zegara",
    " - It is required that the Dark Text checkbox is disabled": " - Wymagane jest odznaczenie opcji czarnego koloru tekstu zegara",
    "Debbugging information:": "Informacje debugowania:",
    "Open ElevenClock's log": "Otwórz plik logów ElevenClock",
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
    "<b>Update to the latest version!</b>"                                             :"Zaktualizuj do najnowszej wersji!",
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
    "Support the dev: Give me a coffee☕"       :"Wsparcie dla dewelopera: Kup mi kawę☕",
    "Open page"                                 :"Otwórz stronę",
    "Icons by Icons8"                           :"Ikony z Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Strona internetowa",
    "Close settings"                            :"Zamknij ustawienia",
    "Close"                                     :"Zamknij",
}

lang = lang2_3
