# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang2_7_bis = {
    "Use a custom font": "Eine benutzerdefinierte Schriftart verwenden",
    "Use a custom font size": "Verwenden einer benutzerdefinierten Schriftgröße",
    "Enable hide when multi-monitor fullscreen apps are running": "Ausblenden aktivieren, wenn Vollbildanwendungen mit mehreren Monitoren ausgeführt werden",
    "<b>{0}</b> needs to be enabled to change this setting": "<b>{0}</b> muss aktiviert sein, um diese Einstellung zu ändern",
    "<b>{0}</b> needs to be disabled to change this setting": "<b>{0}</b> muss deaktiviert werden, um diese Einstellung zu ändern",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": "Dieses Feature wurde deaktiviert, da es grundsätzlich funktionieren sollte. Ist dies nicht der Fall, bitte erstelle einen Fehlerreport.",
    "ElevenClock's language": "Sprache von ElevenClock"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Über Qt6 (PySide6)",
    "About": "Über",
    "Alternative non-SSL update server (This might help with SSL errors)": "Alternative nicht-SSL-Updateserver",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Lösungen und andere experimentelle Features:",
    "Show week number on the clock": "Zeige Wochenanzahl bei der Uhr",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Uhr ausblenden wenn RDP-Client oder Citrix-Workspace läuft",
    "Clock Appearance:": "Erscheinungsbild der Uhr",
    "Force the clock to have black text": "Schwarzen Text der Uhr erzwingen",
    " - It is required that the Dark Text checkbox is disabled": "Es ist notwendig das die Checkbox für schwarzen Test deaktiviert ist",
    "Debbugging information:": "Debugging Informationen",
    "Open ElevenClock's log": "Öffne Log von ElevenClock",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Uhr auf dem Hauptmonitor anzeigen (Sinnvoll, wenn die Uhr auf der linken Seite ist)",
    "Show weekday on the clock"  :"Wochentag anzeigen",
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
    "Change startup behaviour"                                                          :"Startverhalten ändern",
    "Change"                                                                            :"Ändern",
    "<b>Update to the latest version!</b>"                                             :"<b>Auf die neueste Version aktualisieren!</b>",
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
