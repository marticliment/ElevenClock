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
    "ElevenClock Settings"      :"ElevenClock Einstellungen", # Also settings title
    "Reload Clocks"             :"Uhren neu laden",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"ElevenClock neu starten",
    "Hide ElevenClock"          :"ElevenClock verstecken",
    "Quit ElevenClock"          :"ElevenClock beenden",
    
    #General settings section
    "General Settings:"                                                                 :"Allgemeine Einstellungen:",
    "Automatically check for updates"                                                   :"Automatisch nach Aktualisierungen suchen",
    "Automatically install available updates"                                           :"Automatisch verfügbare Aktualisierungen installieren",
    "Enable really silent updates"                                                      :"Sehr stille Updates aktivieren",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Authentizitätsprüfung des Aktualisierungs-Anbieters umgehen (NICHT EMPFOHLEN, AUF EIGENE GEFAHR)",
    "Show ElevenClock on system tray"                                                   :"ElevenClock im System Tray anzeigen",
    "Alternative clock alignment (may not work)"                                        :"Alternative Uhr Ausrichtung (funkioniert möglicherweise nicht)",
    "Change startup behaviour"                                                          :"Start-Verhalten ändern",
    "Change"                                                                            :"Ändern",
    "<b>Update to the lastest version!</b>"                                             :"<b>Auf die neueste Version aktualisieren!</b>",
    "Install update"                                                                    :"Update installieren",
    
    #Clock settings
    "Clock Settings:"                                              :"Uhr Einstellungen:",
    "Hide the clock in fullscreen mode"                            :"Uhr im Vollbildmodus verstecken",
    "Hide the clock when RDP client is active"                     :"Uhr verstecken, wenn der RDP Client aktiviert ist",
    "Force the clock to be at the bottom of the screen"            :"Uhr immer am unteren Bildschirmrand anzeigen",
    "Show the clock when the taskbar is set to hide automatically" :"Uhr zeigen, wenn die Taskleiste auf automatisch Ausblenden eingestellt ist",
    "Fix the hyphen/dash showing over the month"                   :"Korrigieren, dass der Bindestrich über dem Monat angezeigt wird",
    "Force the clock to have white text"                           :"Weißen Text der Uhr erzwingen",
    "Show the clock at the left of the screen"                     :"Uhr auf der linken Seite des Bildschirms anzeigen",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Datum & Uhrzeit Einstellungen:",
    "Show seconds on the clock"                         :"Sekunden anzeigen",
    "Show date on the clock"                            :"Datum anzeigen",
    "Show time on the clock"                            :"Uhrzeit anzeigen",
    "Change date and time format (Regional settings)"   :"Datums- und Uhrzeitsformat ändern (Regionale Einstellungen)",
    "Regional settings"                                 :"Regionale Einstellungen",
    
    #About the language pack
    "About the language pack:"                  :"Über das Sprachpaket:",
    "Translated to English by martinet101"      :"Auf Deutsch übersetzt von Seeloewen", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"ElevenClock auf deine Sprache übersetzen",
    "Get started"                               :"Loslegen",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Über ElevenClock Version {0}:",
    "View ElevenClock's homepage"               :"ElevenClocks Internetseite besuchen",
    "Open"                                      :"Öffnen",
    "Report an issue/request a feature"         :"Ein Problem/Vorschlag einreichen",
    "Report"                                    :"Einreichen",
    "Support the dev: Give me a coffee☕"       :"Unterstütze den Entwickler: Gib mir einen Kaffee☕",
    "Open page"                                 :"Seite öffnen",
    "Icons by Icons8"                           :"Symbole von Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Webseite",
    "Close settings"                            :"Einstellungen schließen",
    "Close"                                     :"Schließen",
}

lang = lang2_3
