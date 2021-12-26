# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_2_9_2 = {
    "Reload log": "",
    "Do not show the clock on secondary monitors": "",
    "Disable clock taskbar background color (make clock transparent)": "",
    "Open the welcome wizard": "",
    " (ALPHA STAGE, MAY NOT WORK)": "",
    "Welcome to ElevenClock": "",
    "Skip": "",
    "Start": "",
    "Next": "",
    "Finish": "",
}

lang_2_9 = lang_2_9_2 | {
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
    "About Qt6 (PySide6)": "",
    "About": "",
    "Alternative non-SSL update server (This might help with SSL errors)": "",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "",
    "Show week number on the clock": "",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "",
    "Clock Appearance:": "",
    "Force the clock to have black text": "",
    " - It is required that the Dark Text checkbox is disabled": "",
    "Debbugging information:": "",
    "Open ElevenClock's log": "",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "",
    "Show weekday on the clock"  :"",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"Instellingen ElevenClock", # Also settings title
    "Reload Clocks"             :"Herlaad Klokken",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"ElevenClock opnieuw opstarten",
    "Hide ElevenClock"          :"Verberg ElevenClock",
    "Quit ElevenClock"          :"Afsluiten ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Algemene Instellingen:",
    "Automatically check for updates"                                                   :"Controlleer automatisch voor updates",
    "Automatically install available updates"                                           :"Installeer automatisch beschikbare updates",
    "Enable really silent updates"                                                      :"Schakel hele stille updates in",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Omzeil update provider autenticatie check (NIET AANBEVOLEN, GEBRUIK OP EIGEN RISICO)",
    "Show ElevenClock on system tray"                                                   :"Laat ElevenClock in systeemvak zien",
    "Alternative clock alignment (may not work)"                                        :"Alternatieve klok uitlijning (werkt mogelijk niet)",
    "Change startup behaviour"                                                          :"Verander automatisch starten gedrag",
    "Change"                                                                            :"Verander",
    "<b>Update to the latest version!</b>"                                             :"<b>Update naar de nieuwste versie!</b>",
    "Install update"                                                                    :"Installeer update",
    
    #Clock settings
    "Clock Settings:"                                              :"Klok instellingen:",
    "Hide the clock in fullscreen mode"                            :"Verberg de klok in volledigscherm applicaties",
    "Hide the clock when RDP client is active"                     :"Verberg de klok wanneer RDP client actief is",
    "Force the clock to be at the bottom of the screen"            :"Forceer de klok om onderaan het scherm te staan",
    "Show the clock when the taskbar is set to hide automatically" :"Klok weergeven als de taakbalk is ingesteld om automatisch te verbergen",
    "Fix the hyphen/dash showing over the month"                   :"Corrigeer het koppelteken/streepje dat gedurende de maand wordt weergegeven",
    "Force the clock to have white text"                           :"Forceer de klok om witte tekst te hebben",
    "Show the clock at the left of the screen"                     :"Toon de klok aan de linkerkant van het scherm ",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Datum & Tijd instellingen:",
    "Show seconds on the clock"                         :"Toon seconden op de klok",
    "Show date on the clock"                            :"Toon de datum op de klok",
    "Show time on the clock"                            :"Toon de tijd op de klok",
    "Change date and time format (Regional settings)"   :"Datum en Tijd aanpassen (regionale instellingen)",
    "Regional settings"                                 :"Regionale instellingen",
    
    #About the language pack
    "About the language pack:"                  :"Over het taalpakket:",
    "Translated to English by martinet101"      :"Vertaald naar het Nederlands door Bugs", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Vertaal ElevenClock naar jou taal",
    "Get started"                               :"Begin",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Over ElevenClock versie {0}:",
    "View ElevenClock's homepage"               :"Website van ElevenClock",
    "Open"                                      :"Open",
    "Report an issue/request a feature"         :"Rapporteer een probleem/vraag een feature aan",
    "Report"                                    :"Rapporteer",
    "Support the dev: Give me a coffee☕"       :"Steun de ontwikkelaar: Geef mij een kopje koffie☕",
    "Open page"                                 :"Open pagina",
    "Icons by Icons8"                           :"Iconen door Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Webpagina",
    "Close settings"                            :"Instellingen sluiten",
    "Close"                                     :"Sluiten",
}

lang = lang2_3
