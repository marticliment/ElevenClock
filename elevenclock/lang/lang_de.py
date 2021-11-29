# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_2_8 = {
    "Force the clock to be at the top of the screen"            : "Uhr immer am oberen Rand des Bildschirms angezeigen",
    "Show the clock on the primary screen"                      : "Uhr auf dem Hauptbildschirm angezeigen",
    "Use a custom font color"                                   : "Eine benutzerdefinierte Schriftfarbe verwenden",
    "Use a custom background color"                             : "Eine benutzerdefinierte Hintergrundfarbe verwenden",
    "Align the clock text to the center"                        : "Ausrichten des Uhrentextes in der Mitte",
    "Select custom color"                                       : "Benutzerdefinierte Farbe auswählen",
    "Hide the clock when a program occupies all screens"        : "Die Uhr ausblenden, wenn ein Programm alle Bildschirme belegt",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font"                                             :"Benutzerdefinierte Schriftart verwenden",
    "Use a custom font size"                                        :"Benutzerdefinierte Schriftgröße verwenden",
    "Enable hide when multi-monitor fullscreen apps are running"    :"Aktiviere das Verstecken, wenn Multi-Monitor-Vollbild-Apps laufen",
    "<b>{0}</b> needs to be enabled to change this setting"         :"<b>{0}</b> muss aktiviert sein, um diese Einstellung zu ändern",
    "<b>{0}</b> needs to be disabled to change this setting"        :"<b>{0}</b> muss deaktiviert sein, um diese Einstellung zu ändern",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)"    :"Dieses Einstellung wurde deaktiviert, da es grundsätzlich funktionieren sollte. Ist dies nicht der Fall, bitte erstelle einen Fehlermeldung.",
    "ElevenClock's language"                                                                                    :"Spracheinstellung",
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)"                                                           :"Über Qt6 (PySide6)",
    "About"                                                                         :"Über",
    "Alternative non-SSL update server (This might help with SSL errors)"           :"Alternative Nicht-SSL-Updateserver",
    "Fixes and other experimental features: (Use ONLY if something is not working)" :"Verbesserungen und andere experimentelle Funktionen:",
    "Show week number on the clock"                                                 :"Anzeige Wochennummern",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running"    :"Uhr ausblenden, sobald RDP-Client oder Citrix-Workspace läuft",
    "Clock Appearance:"                                                 :"Aussehen der Uhr",
    "Force the clock to have black text"                                :"Erzwinge schwarze Schriftart der Uhr",
    " - It is required that the Dark Text checkbox is disabled"         :"Es ist notwendig das die Checkbox für schwarzen Test deaktiviert ist",
    "Debbugging information:"                                           :"Debugging Informationen",
    "Open ElevenClock's log"                                            :"Öffne Log von ElevenClock",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)"     :"Uhr auf dem Hauptmonitor anzeigen (Sinnvoll, wenn die Uhr auf der linken Seite ist)",
    "Show weekday on the clock"                                                     :"Wochentag anzeigen",
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
    "Automatically install available updates"                                           :"Automatisch alle Aktualisierungen installieren",
    "Enable really silent updates"                                                      :"Aktivierung von absolut stillen Updates",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Umgehen der Überprüfung der Authentizität des Update-Anbieters (NICHT EMPFOHLEN, AUF EIGENE GEFAHR)",
    "Show ElevenClock on system tray"                                                   :"ElevenClock im System Tray anzeigen",
    "Alternative clock alignment (may not work)"                                        :"Alternative Ausrichtung der Uhr (funkioniert möglicherweise nicht)",
    "Change startup behaviour"                                                          :"Startverhalten ändern",
    "Change"                                                                            :"Ändern",
    "<b>Update to the latest version!</b>"                                              :"<b>Auf die neueste Version aktualisieren!</b>",
    "Install update"                                                                    :"Update installieren",
    
    #Clock settings
    "Clock Settings:"                                              :"Einstellungen der Uhr:",
    "Hide the clock in fullscreen mode"                            :"Verstecken der Uhr im Vollbildmodus",
    "Hide the clock when RDP client is active"                     :"Verstecken der Uhr, wenn der RDP Client aktiviert ist",
    "Force the clock to be at the bottom of the screen"            :"Uhr immer am unteren Bildschirmrand anzeigen",
    "Show the clock when the taskbar is set to hide automatically" :"Uhr anzeigen, wenn die Taskleiste auf automatisch Ausblenden eingestellt ist",
    "Fix the hyphen/dash showing over the month"                   :"Korrigiert, dass der Bindestrich über dem Monat angezeigt wird",
    "Force the clock to have white text"                           :"Erzwinge weißen Schriftart der Uhr",
    "Show the clock at the left of the screen"                     :"Anzeige der Uhr auf der linken Seite des Bildschirms",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Einstellungen von Datum & Uhrzeit:",
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
    "View ElevenClock's homepage"               :"Internetseite von ElevenClocks",
    "Open"                                      :"Öffnen",
    "Report an issue/request a feature"         :"Ein Problem/Vorschlag melden",
    "Report"                                    :"Melden",
    "Support the dev: Give me a coffee☕"        :"Unterstütze den Entwickler: Spendiere einen Kaffee ☕",
    "Open page"                                 :"Seite öffnen",
    "Icons by Icons8"                           :"Symbole von Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Webseite",
    "Close settings"                            :"Einstellungen schließen",
    "Close"                                     :"Schließen",
}

lang = lang2_3
