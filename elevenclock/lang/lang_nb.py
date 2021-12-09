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
    "Force the clock to be at the top of the screen": "Tving klokken til å være på toppen av skjermen",
    "Show the clock on the primary screen": "Vis klokken på hovedskjermen",
    "Use a custom font color": "Bruk en annen skriftfarge",
    "Use a custom background color": "Bruk en annen bakgrunnsfarge",
    "Align the clock text to the center": "Sentrer klokketeksten",
    "Select custom color": "Bruk en annen farge",
    "Hide the clock when a program occupies all screens": "Skjul klokken når et program bruker alle skjermene",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "Bruk en annen skrifttype (font)",
    "Use a custom font size": "Bruk en annen skriftstørrelse",
    "Enable hide when multi-monitor fullscreen apps are running": "Skjul klokken når apper som bruker fullskjerm over flere skjermer kjører",
    "<b>{0}</b> needs to be enabled to change this setting": "<b>{0}</b> må være aktivert for å endre denne innstillingen",
    "<b>{0}</b> needs to be disabled to change this setting": "<b>{0}</b> må være deaktivert for å endre denne innstillingen",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": " (Denne funksjonen har blitt deaktivert fordi den skal virke som standard. Hvis den ikke virker, kan du sende en feilrapport)",
    "ElevenClock's language": "Valgt språk:"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Om Qt6 (PySide6)",
    "About": "Om",
    "Alternative non-SSL update server (This might help with SSL errors)": "Alternativ oppdateringsserver uten SSL (kan hjelpe ved SSL-feilmeldinger)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Diverse fikser og eksperimentelle funksjoner: (Bare aktiver hvis det er noe som ikke fungerer)",
    "Show week number on the clock": "Vis ukenummer på klokken",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Skjul klokken når RDP Klient eller Citrix Workspace kjører",
    "Clock Appearance:": "Klokken sitt utseende:",
    "Force the clock to have black text": "Tving klokken til å bruke svart tekst",
    " - It is required that the Dark Text checkbox is disabled": " - Krever at 'svart tekst' er deaktivert",
    "Debbugging information:": "Feilsøkingsinformasjon:",
    "Open ElevenClock's log": "Åpne ElevenClock sin loggfil",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Vis klokken på hovedskjermen (Nyttig hvis klokken er satt på venstre side)",
    "Show weekday on the clock"  :"Vis ukedag på klokken",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"ElevenClock Innstillinger", # Also settings title
    "Reload Clocks"             :"Last inn klokker på nytt",
    "ElevenClock v{0}"          :"ElevenClock versjon {0}",
    "Restart ElevenClock"       :"Start ElevenClock på nytt",
    "Hide ElevenClock"          :"Skjul ElevenClock",
    "Quit ElevenClock"          :"Avslutt ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Generelle Innstillinger",
    "Automatically check for updates"                                                   :"Se etter oppdateringer automatisk",
    "Automatically install available updates"                                           :"Installer tilgjengelige oppdateringer automatisk",
    "Enable really silent updates"                                                      :"Aktiver stille oppdateringer",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Hopp over verifikasjon av oppdateringstilbyder (IKKE ANBEFALT, PÅ EGEN RISIKO) ",
    "Show ElevenClock on system tray"                                                   :"Vis ElevenClock i systemfeltet",
    "Alternative clock alignment (may not work)"                                        :"Alternativ klokkeplassering (fungerer ikke nødvendigvis)",
    "Change startup behaviour"                                                          :"Endre oppstartsoppførsel",
    "Change"                                                                            :"Endre",
    "<b>Update to the latest version!</b>"                                             :"<b>Oppdater til nyeste versjon!</b>",
    "Install update"                                                                    :"Installer oppdatering",
    
    #Clock settings
    "Clock Settings:"                                              :"Klokkeinnstillinger",
    "Hide the clock in fullscreen mode"                            :"Skjul klokken i fullskjermmodus",
    "Hide the clock when RDP client is active"                     :"Skjul klokken når RDP-klienten er aktiv",
    "Force the clock to be at the bottom of the screen"            :"Tving klokken til bunnen av skjermen",
    "Show the clock when the taskbar is set to hide automatically" :"Vis klokken selv om oppgavelinjen er satt til å skjules automatisk",
    "Fix the hyphen/dash showing over the month"                   :"Fjern eventuell bindestrek som vises over månedsnummer",
    "Force the clock to have white text"                           :"Tving klokken til å ha hvit tekst",
    "Show the clock at the left of the screen"                     :"Vis klokken på venstre siden av skjermen",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Innstillinger for Tid og Dato",
    "Show seconds on the clock"                         :"Vis sekundteller på klokken",
    "Show date on the clock"                            :"Vis dato på klokken",
    "Show time on the clock"                            :"Vis tiden på klokken",
    "Change date and time format (Regional settings)"   :"Endre tid og dato (Regionale innstillinger)",
    "Regional settings"                                 :"Regionale innstillinger",
    
    #About the language pack
    "About the language pack:"                  :"Om språkpakken:",
    "Translated to English by martinet101"      :"Oversatt til Norsk (Bokmål) av SkebbZ", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Oversett ElevenClock til ditt språk",
    "Get started"                               :"Sett i gang",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Om ElevenClock versjon {0}:",
    "View ElevenClock's homepage"               :"Åpne ElevenClock sin hjemmeside",
    "Open"                                      :"Åpne",
    "Report an issue/request a feature"         :"Rapporter et problem/be om en ny funksjon",
    "Report"                                    :"Rapporter",
    "Support the dev: Give me a coffee☕"       :"Støtt utvikleren: Spander en kopp kaffe ☕",
    "Open page"                                 :"Åpne side",
    "Icons by Icons8"                           :"Ikoner laget av Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Nettside",
    "Close settings"                            :"Lukk innstillinger",
    "Close"                                     :"Lukk",
}

lang = lang2_3
