# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang2_4 = {
    # Added text in version 2.4
    "Show weekday on the clock"  :"",
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
    "<b>Update to the lastest version!</b>"                                             :"Zaktualizuj do najnowszej wersji!",
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
    "Show seconds on the clock"                         :"Pokaż sekundy ",
    "Show date on the clock"                            :"Pokaż datę",
    "Show time on the clock"                            :"Pokaż godzinę",
    "Change date and time format (Regional settings)"   :"Zmień format daty i czasu (ustawienia regionalne)",
    "Regional settings"                                 :"Ust. regionalne",
    
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
    "Support the dev: Give me a coffee☕"       :"Wsparcie dla dewelopera",
    "Open page"                                 :"Otwórz stronę",
    "Icons by Icons8"                           :"Ikony z Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Strona internetowa",
    "Close settings"                            :"Zamknij ustawienia",
    "Close"                                     :"Zamknij",
}

lang = lang2_3