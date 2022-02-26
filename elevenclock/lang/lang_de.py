# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_3 = {
    "Custom format rules:": "",
    "Any text can be placed here. To place items such as date and time, please use the 1989 C standard. More info on the following link": "",
    "Python Date and time values": "",
    "To disable the zero-padding effect, add a # in bethwwn the % and the code: non-zero-padded hours would be %#H, and zero-padded hours would be %H": "", # Here please don't modify the %H and %#H values
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
    "Open online help to troubleshoot problems": "Online-Hilfe öffnen, um Probleme zu beheben",
    "Reset ElevenClock preferences to defaults": "ElevenClock-Einstellungen auf Standardwerte zurücksetzen",
    "Specify a minimum width for the clock": "Mindestbreite der Uhr festlegen",
    "Search on the settings": "Einstellungen durchsuchen",
    "No results were found": "Es wurden keine Ergebnisse gefunden",
}

lang_3_2 = lang_3_2_1 | {
    "Use system accent color as background color": "Akzentfarbe des System als Hintergrundfarbe benutzen",
    "Check only the focused window on the fullscreen check": "Nur das fokussierte Fenster bei der Vollbildprüfung prüfen",
    "Clock on monitor {0}": "Uhr auf Monitor {0}",
    "Move to the left": "Nach links verschieben",
    "Show this clock on the left": "Diese Uhr links anzeigen",
    "Show this clock on the right": "Diese Uhr rechts anzeigen",
    "Restore clock position": "Position der Uhr wiederherstellen",
}

lang_3_1 = lang_3_2 | {
    "W": "W", # The initial of the word week in your language: W for week, S for setmana, etc.
    "Disable the notification badge"                           : "Anzeige für Benachrichtigungen deaktiveren",
    "Override clock default height"                            : "Standart-Höhe der Uhr überschreiben",
    "Adjust horizontal clock position"                         : "Horizontale Position der Uhr anpassen",
    "Adjust vertical clock position"                           : "Vertikale Position der Uhr anpassen",
    "Export log as a file"                                     : "Log als Datei exportieren",
    "Copy log to clipboard"                                    : "Log in die Zwischenablage kopieren",
    "Announcements:"                                           : "Ankündigungen",
    "Fetching latest announcement, please wait..."             : "Neueste Ankündigungen werden abgerufen, bitte warten...",
    "Couldn't load the announcements. Please try again later"  : "Ankündigungen konnten nicht geladen werden. Bitte versuche es später erneut",
    "ElevenClock's log"                                        : "ElevenClocks Log",
    "Pick a color"                                             : "Wähle eine Farbe"
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked"                                                           : "Verstecke die Uhr für 10 Sekunden beim Anklicken",
    "Enable low-cpu mode"                                                                                     : "Niedrigen CPU-Auslastungs Modus aktivieren",
    "You might lose functionalities, like the notification counter or the dynamic background"                 : "Du könntest Funktionen, wie den Benachrichtigungs-Zähler oder den dynamischen Hintergrund, verlieren.",
    "Clock position and size:"                                                                                : "Position und Größe der Uhr",
    "Clock size preferences, position offset, clock at the left, etc."                                        : "Bevorzugte Uhr Größe, Positionsversatz, Uhr links, etc.",
    "Reset monitor blacklisting status"                                                                       : "Monitor Blacklist-Status zurücksetzen",
    "Reset"                                                                                                   : "Zurücksetzen",
    "Third party licenses"                                                                                    : "Drittanbieter-Lizenzen",
    "View"                                                                                                    : "Anschauen",
    "ElevenClock"                                                                                             : "ElevenClock",
    "Monitor tools"                                                                                           : "Monitor Tools",
    "Blacklist this monitor"                                                                                  : "Diesen Monitor blacklisten",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)"                                : "Quelloffene Drittanbieter-Software in ElevenClock {0} (Und ihre Lizenzen)",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:"  : "ElevenClock ist eine quelloffene Software, die mit Hilfe von anderen Tools der Community entstanden ist.",
    "Ok"                                                                                                      : "Ok",
    "More Info"                                                                                               : "Mehr Informationen",
    "About Qt"                                                                                                : "Über Qt",
    "Success"                                                                                                 : "Erfolgreich",
    "The monitors were unblacklisted successfully."                                                           : "Die Monitore wurden erfolgreich von der Blacklist entfernt.",
    "Now you should see the clock everywhere"                                                                 : "Nun solltest du die Uhr überall sehen.",
    "Ok"                                                                                                      : "Ok",
    "Blacklist Monitor"                                                                                       : "Monitor blacklisten",
    "Blacklisting a monitor will hide the clock on this monitor permanently."                                 : "Durch das Blacklisten eines Monitor wird auf diesem die Uhr permanent versteckt.",
    "This action can be reverted from the settings window. under <b>Clock position and size</b>"              : "Diese Aktion kann über das Einstellungen-Fenster unter <b>Position and Größe der Uhr</b> rückgängig gemacht werden.",
    "Are you sure do you want to blacklist the monitor \"{0}\"?"                                              : "Bist du sicher, dass du Monitor \"{0}\" blacklisten möchtest?",
    "Yes"                                                                                                     : "Ja",
    "No"                                                                                                      : "Nein",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "Log neuladen",
    "Do not show the clock on secondary monitors"                      : "Uhr nicht auf sekundären Bildschirmen anzeigen",
    "Disable clock taskbar background color (make clock transparent)"  : "Deaktiviere Uhr Taskenleisten Hintergrund Farbe (Uhr transparent machen)",
    "Open the welcome wizard"                                          : "Öffne den Willkommensassistenten",
    " (ALPHA STAGE, MAY NOT WORK)"                                     : "(ALPHA PHASE, KÖNNTE NICHT FUNKTIONIEREN)",
    "Welcome to ElevenClock"                                           : "Willkommen zu ElevenClock",
    "Skip"                                                             : "Überspringen",
    "Start"                                                            : "Start",
    "Next"                                                             : "Weiter",
    "Finish"                                                           : "Beenden",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager"                                                                                                                      : "Task-Manager",
    "Change date and time"                                                                                                              : "Datum und Zeit ändern",
    "Notification settings"                                                                                                             : "Benachrichtigungseinstellungen",
    "Updates, icon tray, language"                                                                                                      : "Updates, Tray-Icon, Sprache",
    "Hide extended options from the clock right-click menu (needs a restart to be aplied)"                                              : "Verstecke erweiterte Optionen im Rechts-Klick-Menü der Uhr (erfordert Neustart)",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings"                                             : "Verhalten im Vollbildmodus, Position der Uhr, Uhr auf dem Hauptbildschirm, weitere Einstelleungen",
    'Add the "Show Desktop" button on the left corner of every clock'                                                                   : 'Füge die Schaltfläche "Desktop anzeigen" in der linken Ecke jeder Uhr hinzu',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>'  : 'Möglicherweise müssen Sie eine benutzerdefinierte Hintergrundfarbe festlegen, damit dies funktioniert.&nbsp;Weitere Informationen <a href="{0}" style="color:DodgerBlue">HIER</a>',
    "Clock's font, font size, font color and background, text alignment"                                                                : "Schriftart, Schriftgröße, Schriftfarbe, Hintergrund und Textausrichtung der Uhr",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings"                                                          : "Format für Datum und Zeit, Sekunden, Wochentag, Kalenderwoche und regionale Einstellungen",
    "Testing features and error-fixing tools"                                                                                           : "Funktionen testen und Tools zur Fehlerbehebung",
    "Language pack author(s), help translating ElevenClock"                                                                             : "Autor(en) des Sprachpakets, Hilf beim Übersetzen von ElevenClock",
    "Info, report a bug, submit a feature request, donate, about"                                                                       : "Infos, Fehler melden, Vorschlag für eine Funktion einreichen, Spenden, Über",
    "Log, debugging information"                                                                                                        : "Protokoll, Debugging-Informationen",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen"            : "Uhr immer am oberen Rand des Bildschirms anzeigen",
    "Show the clock on the primary screen"                      : "Uhr auf dem Hauptbildschirm anzeigen",
    "Use a custom font color"                                   : "Eine benutzerdefinierte Schriftfarbe verwenden",
    "Use a custom background color"                             : "Eine benutzerdefinierte Hintergrundfarbe verwenden",
    "Align the clock text to the center"                        : "Uhrzeit mittig ausrichten",
    "Select custom color"                                       : "Benutzerdefinierte Farbe auswählen",
    "Hide the clock when a program occupies all screens"        : "Die Uhr ausblenden, wenn ein Programm alle Bildschirme belegt",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font"                                             :"Benutzerdefinierte Schriftart verwenden",
    "Use a custom font size"                                        :"Benutzerdefinierte Schriftgröße verwenden",
    "Enable hide when multi-monitor fullscreen apps are running"    :"Ausblenden aktivieren, wenn Multi-Monitor-Vollbild-Apps laufen",
    "<b>{0}</b> needs to be enabled to change this setting"         :"<b>{0}</b> muss aktiviert sein, um diese Einstellung zu ändern",
    "<b>{0}</b> needs to be disabled to change this setting"        :"<b>{0}</b> muss deaktiviert sein, um diese Einstellung zu ändern",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)"    :"Dieses Einstellung wurde deaktiviert, da es grundsätzlich funktionieren sollte. Sollte dies nicht der Fall sein, erstelle bitte eine Fehlermeldung.",
    "ElevenClock's language"                                                                                    :"Spracheinstellung",
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)"                                                           :"Über Qt6 (PySide6)",
    "About"                                                                         :"Über",
    "Alternative non-SSL update server (This might help with SSL errors)"           :"Alternative Nicht-SSL-Updateserver (Hilft eventuell nicht bei SSL-Fehlern)",
    "Fixes and other experimental features: (Use ONLY if something is not working)" :"Verbesserungen und andere experimentelle Funktionen: (NUR benutzen, wenn etwas nicht funktioniert)",
    "Show week number on the clock"                                                 :"Kaldenderwoche anzeigen",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running"    :"Uhr ausblenden, sobald RDP-Client oder Citrix-Workspace läuft",
    "Clock Appearance:"                                                 :"Aussehen der Uhr",
    "Force the clock to have black text"                                :"Erzwinge, dass die Uhr schwarzen Text hat",
    " - It is required that the Dark Text checkbox is disabled"         :" - Es ist erforderlich, dass die Checkbox für schwarzen Text deaktiviert ist",
    "Debbugging information:"                                           :"Debugging-Informationen",
    "Open ElevenClock's log"                                            :"Öffne Protokoll von ElevenClock",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)"     :"Uhr auf dem Hauptbildschirm anzeigen (Sinnvoll, wenn die Uhr auf der linken Seite ist)",
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
    "Show ElevenClock on system tray"                                                   :"Tray-Icon von ElevenClock anzeigen",
    "Alternative clock alignment (may not work)"                                        :"Alternative Ausrichtung der Uhr (funkioniert möglicherweise nicht)",
    "Change startup behaviour"                                                          :"Startverhalten ändern",
    "Change"                                                                            :"Ändern",
    "<b>Update to the latest version!</b>"                                              :"<b>Auf die neueste Version aktualisieren!</b>",
    "Install update"                                                                    :"Update installieren",
    
    #Clock settings
    "Clock Settings:"                                              :"Uhreinstellungen:",
    "Hide the clock in fullscreen mode"                            :"Uhr im Vollbildmodus ausblenden",
    "Hide the clock when RDP client is active"                     :"Uhr ausblenden, wenn der RDP Client aktiviert ist",
    "Force the clock to be at the bottom of the screen"            :"Uhr immer am unteren Bildschirmrand anzeigen",
    "Show the clock when the taskbar is set to hide automatically" :"Uhr anzeigen, wenn die Taskleiste auf automatisches Ausblenden eingestellt ist",
    "Fix the hyphen/dash showing over the month"                   :"Korrigiert, dass der Bindestrich über dem Monat angezeigt wird",
    "Force the clock to have white text"                           :"Erzwinge weiße Schriftart der Uhr",
    "Show the clock at the left of the screen"                     :"Uhr auf der linken Seite des Bildschirms anzeigen",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Datums- und Uhrzeiteinstellungen:",
    "Show seconds on the clock"                         :"Sekunden anzeigen",
    "Show date on the clock"                            :"Datum anzeigen",
    "Show time on the clock"                            :"Uhrzeit anzeigen",
    "Change date and time format (Regional settings)"   :"Datums- und Uhrzeitsformat ändern (Regionale Einstellungen)",
    "Regional settings"                                 :"Regionale Einstellungen",
    
    #About the language pack
    "About the language pack:"                  :"Über das Sprachpaket:",
    "Translated to English by martinet101"      :"Auf Deutsch übersetzt von Seeloewen und Bikholf", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"ElevenClock in deine Sprache übersetzen",
    "Get started"                               :"Loslegen",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Über ElevenClock Version {0}:",
    "View ElevenClock's homepage"               :"Internetseite von ElevenClocks",
    "Open"                                      :"Öffnen",
    "Report an issue/request a feature"         :"Ein Problem/Vorschlag melden",
    "Report"                                    :"Melden",
    "Support the dev: Give me a coffee☕"       :"Unterstütze den Entwickler: Spendiere einen Kaffee☕",
    "Open page"                                 :"Seite öffnen",
    "Icons by Icons8"                           :"Symbole von Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Webseite",
    "Close settings"                            :"Einstellungen schließen",
    "Close"                                     :"Schließen",
}

lang = lang2_3
