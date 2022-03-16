# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_3_2 = {
    "ElevenClock Updater": "",
    "ElevenClock is downloading updates": "",
    "ElevenClock has updated to version {0} successfully\nPlease see GitHub for the changelog": "",
    "Customize the clock on Windows 11": "",
    "Disable the new instance checker method": "",
    "Import settings from a local file": "",
    "Export settings to a local file": "",
    "Export": "",
    "Import": "",
}

lang_3_3_1 = lang_3_3_2 | {
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
    "Use system accent color as background color": "Bruk systemfarge som bakgrunnsfarge",
    "Check only the focused window on the fullscreen check": "Bare undersøk vinduet i fokus på fullskjermundersøkelsen",
    "Clock on monitor {0}": "Klokke på monitor {0}",
    "Move to the left": "Flytt til venstre",
    "Show this clock on the left": "Vis denne klokken på venstresiden",
    "Show this clock on the right": "Vis denne klokken på høyresiden",
    "Restore clock position": "Gjenopprett klokkens posisjon",
}

lang_3_1 = lang_3_2 | {
    "W": "U", # The initial of the word week in your language: W for week, S for setmana, etc.
    "Disable the notification badge": "Deaktiver varslingsmerket",
    "Override clock default height": "Overstyr standardhøyde for klokken",
    "Adjust horizontal clock position": "Juster klokkens horisontale posisjon",
    "Adjust vertical clock position": "Juster klokkens vertikale posisjon",
    "Export log as a file": "Eksporter logg som fil",
    "Copy log to clipboard": "Kopier logg til utklippstavlen",
    "Announcements:": "Kunngjøringer:",
    "Fetching latest announcement, please wait...": "Henter siste kunngjøring, vennligst vent...",
    "Couldn't load the announcements. Please try again later": "Kunne ikke laste kunngjøringene. Vennligst prøv igjen senere",
    "ElevenClock's log": "Logg for ElevenClock",
    "Pick a color": "Velg en farge"
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "Skjul klokken i 10 sekunder når den trykkes på",
    "Enable low-cpu mode": "Slå på modus for lite prosessorbruk",
    "You might lose functionalities, like the notification counter or the dynamic background": "Du kan miste funksjonalitet, som varseltelleren eller dynamisk bakgrunn",
    "Clock position and size:": "Klokkens posisjon og størrelse",
    "Clock size preferences, position offset, clock at the left, etc.": "Innstillinger for klokkestørrelse, plassering, klokken til venstre, etc.",
    "Reset monitor blacklisting status": "Nullstill status for svartelisting av skjerm",
    "Reset": "Nullstill",
    "Third party licenses": "Tredjepartslisenser",
    "View": "Vis",
    "ElevenClock": "ElevenClock",
    "Monitor tools": "Skjermverktøy",
    "Blacklist this monitor": "Svartelist denne skjermen",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "Tredjeparts programvare med åpen kildekode i ElevenClock {0} (og lisensene deres)",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "ElevenClock er en app med åpen kildekode laget med hjelp fra andre biblioteker laget av brukerfellesskapet",
    "Ok": "Ok",
    "More Info": "Mer Info",
    "About Qt": "Om Qt",
    "Success": "Suksessfullt",
    "The monitors were unblacklisted successfully.": "Skjermene ble u-svartelistet suksessfullt.",
    "Now you should see the clock everywhere": "Nå skal du kunne se klokken overalt",
    "Ok": "Ok",
    "Blacklist Monitor": "Svartelist skjerm",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "Å svarteliste en skjerm vil skjule klokken på denne skjermen permanent.",
    "This action can be reverted from the settings window, under <b>Clock position and size</b>": "Denne handlingen kan bli omgjort fra innstillingsvinduet under <b>Klokkens posisjon og størrelse<b>",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "Er du sikker på at du vil svarteliste denne skjermen? \"{0}\"?",
    "Yes": "Ja",
    "No": "Nei",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "Last inn logg på nytt",
    "Do not show the clock on secondary monitors": "Ikke vil klokken på sekundærskjermer",
    "Disable clock taskbar background color (make clock transparent)": "Skru av oppgavelinjeklokkens bakgrunnsfarge (gjør klokken gjennomsiktig)",
    "Open the welcome wizard": "Åpne veiviseren for installasjon",
    " (ALPHA STAGE, MAY NOT WORK)": " (ALFA-STADIUM, VIRKER KANSKJE IKKE",
    "Welcome to ElevenClock": "Velkommen til ElevenClock",
    "Skip": "Hopp over",
    "Start": "Start",
    "Next": "Neste",
    "Finish": "Fullfør",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "Oppgavebehandling",
    "Change date and time": "Endre dato og klokkeslett",
    "Notification settings": "Varslingsinnstillinger",
    "Updates, icon tray, language": "Oppdateringer, ikonboks, språk",
    "Hide extended options from the clock right-click menu (needs a restart to be applied)": "Skjul avanserte innsillinger fra høyreklikkmenyen for klokken (trenger omstart av programmet for å brukes)",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "Fullskjermoppførsel, klokkens posisjon, klokke på hovedskjerm, diverse andre innstillinger",
    'Add the "Show Desktop" button on the left corner of every clock': 'Legg til "Vis skrivebord"-knappen på venstre side av alle klokker',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': 'Det kan hende at du må bestemme en egen bakgrunnsfarge for at dette skal fungere.&nbsp;Mer informasjon <a href="{0}" style="color:DodgerBlue">HER</a>',
    "Clock's font, font size, font color and background, text alignment": "Klokkens font, fontstørrelse, fontfarge og -bakgrunn, tekststilling",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "Datoformat, tidsformat, sekunder, ukedag, ukenummer, regionale innstillinger",
    "Testing features and error-fixing tools": "Testfunksjoner og feilløsningsverktøy",
    "Language pack author(s), help translating ElevenClock": "Språkpakkens forfatter(e), hjelp til med å oversette ElevenClock",
    "Info, report a bug, submit a feature request, donate, about": "Informasjon, rapporter en feil, send forslag til ny funksjon, doner, om",
    "Log, debugging information": "Logg, informasjon for feilsøking",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen": "Tving klokken til å være på toppen av skjermen",
    "Show the clock on the primary screen": "Vis klokken på hovedskjermen",
    "Use a custom font color": "Bruk en annen skriftfarge",
    "Use a custom background color": "Bruk en annen bakgrunnsfarge",
    "Align the clock text to the center": "Sentrer klokketeksten",
    "Select custom color": "Bruk en annen farge",
    "Hide the clock when a program occupies all screens": "Skjul klokken når et program bruker alle skjermer",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "Bruk en annen font",
    "Use a custom font size": "Bruk en annen skriftstørrelse",
    "Enable hide when multi-monitor fullscreen apps are running": "Skjul klokken når apper som bruker fullskjerm over flere skjermer kjører",
    "<b>{0}</b> needs to be enabled to change this setting": "<b>{0}</b> må være aktivert for å endre denne innstillingen",
    "<b>{0}</b> needs to be disabled to change this setting": "<b>{0}</b> må være deaktivert for å endre denne innstillingen",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": " (Denne funksjonen har blitt deaktivert fordi den skal virke som standard. Hvis den ikke virker, vær så snill og rapporter en 'bug' (feil))",
    "ElevenClock's language": "Valgt språk"
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
    "Clock Appearance:": "Klokkens utseende:",
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
    "ElevenClock Settings"      :"Innstillinger for ElevenClock", # Also settings title
    "Reload Clocks"             :"Last inn klokker på nytt",
    "ElevenClock v{0}"          :"ElevenClock versjon {0}",
    "Restart ElevenClock"       :"Start ElevenClock på nytt",
    "Hide ElevenClock"          :"Skjul ElevenClock",
    "Quit ElevenClock"          :"Avslutt ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Generelle innstillinger",
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
    "Translated to English by martinet101"      :"Oversatt til Norsk (Bokmål) av SkebbZ og norway-yv", # Here, make sure to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
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
