# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"

# So it would look like: "ORIGINAL_TEXT" : "TRANSLATED_TEXT",


# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_5_0 = {
    "Tooltip Appearance:": "",
    "Tooltip's font, font size, font color and background": "",
    "Disable tooltip's blurry background": "",
    "Sync time with the internet": "",
    "Internet date and time": "",
    "Select internet time provider, change sync frequency": "",
    "Enable internet time sync": "",
    "Paste a URL from the world clock api or equivalent": "",
    "Help": "",
    "Internet sync frequency": "",
    "10 minutes": "",
    "30 minutes": "",
    "1 hour": "",
    "2 hours": "",
    "4 hours": "",
    "10 hours": "",
    "24 hours": "",
}

lang_3_4_0 = lang_3_5_0 | {
    "Show calendar": "Vis kalender",
    "Disabled": "Deaktivert",
    "Open quick settings": "Åpne hurtiginnstillinger",
    "Show desktop": "Vis skrivebord",
    "Open run dialog": "Åpne Kjør-oppgåva",
    "Open task manager": "Åpne oppgåvebehandling",
    "Open start menu": "Åpne startmenyen",
    "Open search menu": "Åpne søkemenyen",
    "Change task": "Bytt oppgåve",
    "Change the action done when the clock is clicked": "Endre kva som verte gjere når klokka er klikka på",
}

lang_3_3_2 = lang_3_4_0 | {
    "ElevenClock Updater": "ElevenClock oppdaterar",
    "ElevenClock is downloading updates": "ElevenClock lastar ned oppdateringar",
    "ElevenClock has updated to version {0} successfully\nPlease see GitHub for the changelog": "Elevenclock har suksessfullt oppdatert til versjon {0}\nVenlegst sjå GitHub for endringslogg",
    "Customize the clock on Windows 11": "Personaliser klokka på Windows 11",
    "Disable the new instance checker method": "Deaktiver ny oppgave-undersøkingsmetoden",
    "Import settings from a local file": "Importer innstillingar frå ein lokal fil",
    "Export settings to a local file": "Eksporter innstillingar til ein lokal fil",
    "Export": "Eksporter",
    "Import": "Importer",
}

lang_3_3_1 = lang_3_3_2 | {
    "Invalid time format\nPlease follow the\nC 1989 Standards": "Ugyldig tidsformat\nVenlegst følj\nC 1989-standardane",
    "Nothing to preview": "Ingenting å forhandsvise",
    "Invalid time format\nPlease modify it\nin the settings": "Ugyldig tidsformat\nVenlegst modifiser det\ni innstillingane",
    "Disable the tooltip shown when the clock is hovered": "Deaktiver pekerhintet vist når pekaren svevar over klokka"
}
lang_3_3 = lang_3_3_1 | {
    "Custom format rules:": "Personlige formateringsreglar",
    "Any text can be placed here. To place items such as date and time, please use the 1989 C standard. More info on the following link": "Hvilken som helst tekst kan plasserast her. For å plassere dato og tid, venlegst bruk 1989 C-standarden. Mer informasjon på føljende lenke",
    "Python date and time formats": "Pythons dato- og tidsformat",
    "To disable the zero-padding effect, add a # in between the % and the code: non-zero-padded hours would be %#H, and zero-padded hours would be %H": "For å skru av null-padding-effekten, legg inn ein # mellom % og koden: ikke-null-paddede timer er %#H, og null-paddede timer er %H", # Here please don't modify the %H and %#H values
    "Click on Apply to apply and preview the format": "Klikk på Bruk for å bruke og forhandsvise formatet",
    "Apply": "Bruk",
    "If you don't understand what is happening, please uncheck the checkbox over the text area": "Hvis du ikkje forstår kva som skjer, vær så snill og av-avhuk boksen over tekstområdet",
    "Set a custom date and time format": "Sett personleg dato- og tidsformat",
    "(for advanced users only)": "(kun for avanserte brukarar)",
    "Move this clock to the left": "Flytt klokka til venstre",
    "Move this clock to the top": "Flytt klokka til toppen",
    "Move this clock to the right": "Flytt klokka til høgre",
    "Move this clock to the bottom": "Flytt klokka til bunnen",
    "Restore horizontal position": "Gjenopprett horisontal posisjon",
    "Restore vertical position": "Gjenopprett vertikal posisjon",
}

lang_3_2_1 = lang_3_3 | {
    "Open online help to troubleshoot problems": "Åpne hjelp på nettet for å feilsøke problemet",
    "Reset ElevenClock preferences to defaults": "Nullstill ElevenClocks innstillingar til standardinnstillinage",
    "Specify a minimum width for the clock": "Spesifiser ein minimumsvidde for klokka",
    "Search on the settings": "Søk i innstillingane",
    "No results were found": "Ingen resultatar er funnen",
}

lang_3_2 = lang_3_2_1 | {
    "Use system accent color as background color": "Bruk systemfargen som bakgrunnsfarge",
    "Check only the focused window on the fullscreen check": "Bare undersøk det fokuserte vinduet under fullskjermundersøkinga",
    "Clock on monitor {0}": "Klokke på monitor {0}",
    "Move to the left": "Flytt til venstresida",
    "Show this clock on the left": "Vis denne klokka på venstresida",
    "Show this clock on the right": "Vis denne klokka på høgresida",
    "Restore clock position": "Gjenopprett klokkas posisjon",
}

lang_3_1 = lang_3_2 | {
    "W": "V", # The initial of the word week in your language: W for week, S for setmana, etc.
    "Disable the notification badge": "Deaktiver varselmerket",
    "Override clock default height": "Overstyr klokkas standardhøgde",
    "Adjust horizontal clock position": "Juster horisontal klokkeposisjon",
    "Adjust vertical clock position": "Juster vertikal klokkeposisjon",
    "Export log as a file": "Eksporter logg som ei fil",
    "Copy log to clipboard": "Kopier logg til utklippstavle",
    "Announcements:": "Kunngjeringer:",
    "Fetching latest announcement, please wait...": "Henter siste kunngjering, vennlegst vent",
    "Couldn't load the announcements. Please try again later": "Kunne ikkje laste kunngjeringane. Prøv igjen seinare",
    "ElevenClock's log": "Loggen til ElevenClock",
    "Pick a color": "Velj ein farge"
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "Skjul klokka i 10 sekund ved klikk",
    "Enable low-cpu mode": "Aktiver modus for lite bruk av prosessorkraft",
    "You might lose functionalities, like the notification counter or the dynamic background": "Du kan miste funksjoner, som varselteljaren eller dynamisk bakgrunn",
    "Clock position and size:": "Klokkas posisjon og storleik",
    "Clock size preferences, position offset, clock at the left, etc.": "Preferanser for klokkestorleikar, posisjonsforskyving, klokka til venstre, etc.",
    "Reset monitor blacklisting status": "Nullstill svartelistingsstatus for monitorar",
    "Reset": "Nullstill",
    "Third party licenses": "Tredjepartslisensar",
    "View": "Vis",
    "ElevenClock": "ElevenClock",
    "Monitor tools": "Monitorverktøy",
    "Blacklist this monitor": "Svartelist denne monitoren",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "Tredjepartsprogramvare med åpen kjeldekode i ElevenClock {0} (Og deira lisensar)",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "ElevenClock er ein applikasjon med åpen kjeldekode laget med hjelp av andre bibliotek laget av fellesskapet_",
    "Ok": "Ok",
    "More Info": "Meir informasjon",
    "About Qt": "Om Qt",
    "Success": "Suksess",
    "The monitors were unblacklisted successfully.": "Monitorane blei u-svartelista suksessfullt",
    "Now you should see the clock everywhere": "Nå skal du kunne se klokka over alt",
    "Ok": "Ok",
    "Blacklist Monitor": "Svartelist monitor",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "Å svarteliste ein monitor vil skjule klokka frå denne monitoren permanent",
    "This action can be reverted from the settings window, under <b>Clock position and size</b>": "Dette kan bli omgjort frå innstillings-vindauget under <b>Klokkas posisjon og storleik</b>",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "Er du sikker på ad du ynskjer å svareliste monitor \"{0}\"?",
    "Yes": "Ja",
    "No": "Nei",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "Last inn logg på nytt",
    "Do not show the clock on secondary monitors": "Ikkje vis klokka på sekundær-monitorar",
    "Disable clock taskbar background color (make clock transparent)": "Deaktiver klokkens oppgåvelinje-bakgrunnsfarge (gjer klokka gjennomsiktig)",
    "Open the welcome wizard": "Åpne velkomstvegvisaren",
    " (ALPHA STAGE, MAY NOT WORK)": " (ALPHA NIVÅ, FUNGERAR KANSKJE IKKJE)",
    "Welcome to ElevenClock": "Velkommen til ElevenClock",
    "Skip": "Hopp over",
    "Start": "Start",
    "Next": "Neste",
    "Finish": "Fullfør",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "Oppåvebehandling",
    "Change date and time": "Endre dato og tid",
    "Notification settings": "Varslingsinnstillingar",
    "Updates, icon tray, language": "Oppdateringar, ikonområde, språk",
    "Hide extended options from the clock right-click menu (needs a restart to be applied)": "Skjul utvidede alternativ frå klokkas høgreklikk-meny (krever omstart for å brukes)",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "Fullskjermoppførsel, klokkas posisjon, klokka på fyrste monitor, andre diverse innstillinger",
    'Add the "Show Desktop" button on the left corner of every clock': 'Legg til "Vis skrivebord"-knappen på det venstre hjørnet av kvar klokke',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': 'Du må kanskje bestemme ein personleg bakgrunnsfarge for at dette skal virke.&nbsp;Meir informasjon <a href="{0}" style="color:DodgerBlue">HER</a>',
    "Clock's font, font size, font color and background, text alignment": "Klokkas font, fontstorheit, fontfarge og -bakgrunn, tekstinnstillingar",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "Datoformat, tidsformat, sekunder, vekedag, vekenummer, regionale innstillingar",
    "Testing features and error-fixing tools": "Testfunksjonar og feilsøkingsverktøy",
    "Language pack author(s), help translating ElevenClock": "Språkpakkens forfattar(ar), hjelp til med å oversetje ElevenClock",
    "Info, report a bug, submit a feature request, donate, about": "Informasjon, rapporter ein feil, send inn funksjonsforespurnad, doner, om",
    "Log, debugging information": "Logg, informasjon for feilsøking",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen": "Tving klokka til å være på toppen av skjermen",
    "Show the clock on the primary screen": "Vis klokka på primærskjermen",
    "Use a custom font color": "Bruk personleg fontfarge",
    "Use a custom background color": "Bruk personleg bakgrunnsfarge",
    "Align the clock text to the center": "Juster klokketeksten til midten",
    "Select custom color": "Velj personleg farge",
    "Hide the clock when a program occupies all screens": "Skjul klokka når eit program brukar heile skjermen",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "Bruk personleg font",
    "Use a custom font size": "Bruk personleg fontstorleik",
    "Enable hide when multi-monitor fullscreen apps are running": "Skjul når multi-monitor fullskjermapper køyrar",
    "<b>{0}</b> needs to be enabled to change this setting": "<b>{0}</b> må vere på for å endre denne innstillinga",
    "<b>{0}</b> needs to be disabled to change this setting": "<b>{0}</b> må vere av for å endre denne innstillinga",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": " (Denne funksjonen har blitt deaktivert fordi den skal fungere til vanleg. Hvis ikke, vær så snill og rapporter ein feil)",
    "ElevenClock's language": "Språk for ElevenClock"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Om Qt6 (PySide6)",
    "About": "Om",
    "Alternative non-SSL update server (This might help with SSL errors)": "Alternative ikke-SSL oppdateringsserver (dette kan hjelpe med SSL-feil)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Eksperimentelle funksjoner: (BERRE bruk hvis noko ikkje fungerar)",
    "Show week number on the clock": "Vis vekenummer på klokka"
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Skjul klokka når RDP Client eller Citrix Workspace køyrar",
    "Clock Appearance:": "Klokkas utseande",
    "Force the clock to have black text": "Tving klokka til å ha svart tekst",
    " - It is required that the Dark Text checkbox is disabled": " - Det er påkrevt at Mørk Tekst-avkrysningsboksen ikkje er huka av på",
    "Debbugging information:": "Feilsøkingsinformasjon",
    "Open ElevenClock's log": "Åpne ElevenClocks logg",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Vis klokken på primærskjermen (hjelpsamt hvis klokka er satt til venstre)",
    "Show weekday on the clock"  :"Vis vekedag på klokka",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"Innstillingar for ElevenClock", # Also settings title
    "Reload Clocks"             :"Last inn klokker på nytt",
    "ElevenClock v{0}"          :"ElevenClock versjon {0}",
    "Restart ElevenClock"       :"Restart ElevenClock",
    "Hide ElevenClock"          :"Skjul ElevenClock",
    "Quit ElevenClock"          :"Avslutt ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Generelle innstillingar",
    "Automatically check for updates"                                                   :"Sjekk for oppdateringar automatisk",
    "Automatically install available updates"                                           :"Installer oppdateringar automatisk",
    "Enable really silent updates"                                                      :"Aktiver stille oppdateringar",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Unngå oppdateringstjenesteleverandørens autentisitetssjekkk (IKKJE ANBEFALT, PÅ EIGEN RISIKO)",
    "Show ElevenClock on system tray"                                                   :"Vis ElevenClock i ikonboksen på oppgåvelinja (system tray)",
    "Alternative clock alignment (may not work)"                                        :"Alternativ klokkeplassering (fungerer kanskje ikkje)",
    "Change startup behaviour"                                                          :"Endre oppstartsoppførsel",
    "Change"                                                                            :"Endre",
    "<b>Update to the latest version!</b>"                                             :"<b>Oppdater til den siste versjonen!</b>",
    "Install update"                                                                    :"Installer oppdatering",
    
    #Clock settings
    "Clock Settings:"                                              :"Klokkeinnstillingar",
    "Hide the clock in fullscreen mode"                            :"Skjul klokka i fullskjerm",
    "Hide the clock when RDP client is active"                     :"Skjul klokka når RDP-klient er aktiv",
    "Force the clock to be at the bottom of the screen"            :"Tving klokka til å vere på bunnen av skjermen",
    "Show the clock when the taskbar is set to hide automatically" :"Vis klokka når oppgåvelinja er sett til å skjule seg automatisk",
    "Fix the hyphen/dash showing over the month"                   :"Fiks at bindestreken visest over månaden",
    "Force the clock to have white text"                           :"Tving klokka til å ha kvit tekst",
    "Show the clock at the left of the screen"                     :"Vis klokka på venstresiden av skjermen",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Innstillinger for dato og tid",
    "Show seconds on the clock"                         :"Vis sekundar på klokka",
    "Show date on the clock"                            :"Vis dato på klokka",
    "Show time on the clock"                            :"Vis tid på klokka",
    "Change date and time format (Regional settings)"   :"Endre dato- og tidsformat (Regionale innstillingar)",
    "Regional settings"                                 :"Regionale innstillingar",
    
    #About the language pack
    "About the language pack:"                  :"Om språkpakken",
    "Translated to English by martinet101"      :"Oversett til norsk (nynorsk) av norway-yv", # Here, make sure to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Oversett ElevenClock til ditt språk eller hjelp norway-yv med korrekturlesning (han har bokmål som hovudmål)",
    "Get started"                               :"Sett i gang",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Om ElevenClock versjon {0}",
    "View ElevenClock's homepage"               :"Vis heimesiden til ElevenClock",
    "Open"                                      :"Åpne",
    "Report an issue/request a feature"         :"Rapporter ein feil/forespør ein funksjon",
    "Report"                                    :"Rapporter",
    "Support the dev: Give me a coffee☕"       :"Støtt utviklaren: Gi han ein kaffi☕",
    "Open page"                                 :"Åpne side",
    "Icons by Icons8"                           :"Ikoner fra Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Nettside",
    "Close settings"                            :"Lukk innstillingar",
    "Close"                                     :"Lukk",
}

lang = lang2_3
