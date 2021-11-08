# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang2_7 = {
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
