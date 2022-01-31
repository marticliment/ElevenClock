# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_2 = {
    "Use system accent color as background color": "",
    "Check only the focused window on the fullscreen check": "",
    "Clock on monitor {0}": "",
    "Move to the left": "",
    "Show this clock on the left": "",
    "Show this clock on the right": "",
    "Restore clock position": "",
}

lang_3_1 = lang_3_2 | {
    "W": "", # The initial of the word week in your language: W for week, S for setmana, etc.
    "Disable the notification badge": "Verberg de meldingsbadge",
    "Override clock default height": "Overschrijf standaard klok hoogte",
    "Adjust horizontal clock position": "Pas de horizontale klok positie aan",
    "Adjust vertical clock position": "Pas de verticale klok positie aan",
    "Export log as a file": "Exporteer log als bestand",
    "Copy log to clipboard": "Kopieer log naar klembord",
    "Announcements:": "Aankondigingen:",
    "Fetching latest announcement, please wait...": "Laatste aankondiging ophalen, wacht alsjeblieft...",
    "Couldn't load the announcements. Please try again later": "Kon de aankondigingen niet laden. Probeer het later opnieuw",
    "ElevenClock's log": "",
    "Pick a color": "Kies een kleur"
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "Verberg de klok gedurende 10 seconden wanneer erop wordt geklikt",
    "Enable low-cpu mode": "Lage cpu-modus inschakelen",
    "You might lose functionalities, like the notification counter or the dynamic background": "Mogelijk verliest u functionaliteiten, zoals de notificatieteller of de dynamische achtergrond",
    "Clock position and size:": "Klokpositie en -grootte:",
    "Clock size preferences, position offset, clock at the left, etc.": "Klokgrootte voorkeuren, positie-offset, klok aan de linkerkant, etc.",
    "Reset monitor blacklisting status": "",
    "Reset": "",
    "Third party licenses": "Licenties van derden ",
    "View": "Toon",
    "ElevenClock": "",
    "Monitor tools": "",
    "Blacklist this monitor": "Blacklist deze monitor",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "Open source-software van derden in Elevenclock {0} (En hun licenties)",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "ElevenClock is een Open-Source applicatie die is gemaakt met de hulp van andere bibliotheken die door de gemeenschap zijn gemaakt:", # iffy translation, might need to be looked at
    "Ok": "",
    "More Info": "Meer Info",
    "About Qt": "Over Qt",
    "Success": "Succes",
    "The monitors were unblacklisted successfully.": "De monitoren zijn met succes van de blacklist gehaald.",
    "Now you should see the clock everywhere": "Nu zou je de klok overal moeten zien",
    "Ok": "",
    "Blacklist Monitor": "",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "Als u een monitor op de blacklist zet, wordt de klok op deze monitor permanent verborgen.",
    "This action can be reverted from the settings window. under <b>Clock position and size</b>": "Deze actie kan worden teruggedraaid vanuit het instellingenvenster. Onder <b>Klokpositie en -grootte</b>",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "Weet u zeker dat u de monitor \"{0}\" op de blacklist wilt zetten?",
    "Yes": "Ja",
    "No": "Nee",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "Log opnieuw laden",
    "Do not show the clock on secondary monitors": "Toon de klok niet op secundaire monitoren",
    "Disable clock taskbar background color (make clock transparent)": "Taakbalkachtergrondkleur klok uitschakelen (klok transparant maken)",
    "Open the welcome wizard": "Open de welkomstwizard",
    " (ALPHA STAGE, MAY NOT WORK)": " (ALFA FASE, WERKT MOGELIJK NIET)",
    "Welcome to ElevenClock": "Welkom bij ElevenClock",
    "Skip": "",
    "Start": "",
    "Next": "Volgende",
    "Finish": "",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "Taakbeheer",
    "Change date and time": "Datum en tijd wijzigen",
    "Notification settings": "Melding instellingen",
    "Updates, icon tray, language": "Updates, icoon lade, taal",
    "Hide extended options from the clock right-click menu (needs a restart to be aplied)": "Verberg uitgebreide opties in het rechtsklikmenu van de klok (hiervoor is een herstart nodig)",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "Volledig scherm gedrag, klokpositie, 1e monitor klok, overige instellingen",
    'Add the "Show Desktop" button on the left corner of every clock': 'Voeg de "Bureaublad weergeven" knop toe in de linkerhoek van elke klok',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': 'Mogelijk moet u een aangepaste achtergrondkleur instellen om dit te laten werken.&nbsp;Meer info <a href="{0}" style="color:DodgerBlue">HIER</a>',
    "Clock's font, font size, font color and background, text alignment": "Lettertype van de klok, lettergrootte, letterkleur en -achtergrond, tekstuitlijning",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "Datumformaat, Tijdformaat, seconden, weekdag, weeknummer, regionale instellingen",
    "Testing features and error-fixing tools": "Functies testen en hulpprogramma's voor het oplossen van fouten",
    "Language pack author(s), help translating ElevenClock": "Auteur(s) van het taalpakket, help het vertalen van ElevenClock",
    "Info, report a bug, submit a feature request, donate, about": "Info, een bug melden, een functieverzoek indienen, doneren, over",
    "Log, debugging information": "Log, foutopsporingsinformatie",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen": "Forceer de klok om bovenaan het scherm te staan",
    "Show the clock on the primary screen": "Toon de klok op het primaire scherm",
    "Use a custom font color": "Gebruik een aangepaste letterkleur",
    "Use a custom background color": "Gebruik een aangepaste achtergrondkleur",
    "Align the clock text to the center": "Lijn de kloktekst uit met het midden",
    "Select custom color": "Selecteer aangepaste kleur",
    "Hide the clock when a program occupies all screens": "Verberg de klok wanneer een programma alle schermen gebruikt",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "Gebruik een aangepast lettertype",
    "Use a custom font size": "Gebruik een aangepaste lettergrootte",
    "Enable hide when multi-monitor fullscreen apps are running": "Verberg wanneer apps op volledig scherm met meerdere monitoren actief zijn",
    "<b>{0}</b> needs to be enabled to change this setting": "<b>{0}</b> moet zijn ingeschakeld om deze instelling te wijzigen",
    "<b>{0}</b> needs to be disabled to change this setting": "<b>{0}</b> moet zijn uitgeschakeld om deze instelling te wijzigen",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": " (Deze functie is uitgeschakeld omdat deze standaard zou moeten werken. Als dit niet het geval is, meldt u een bug)",
    "ElevenClock's language": "ElevenClock zijn taal"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Over Qt6 (PySide6)",
    "About": "Over",
    "Alternative non-SSL update server (This might help with SSL errors)": "Alternatieve niet-SSL-updateserver (dit kan helpen bij SSL-fouten)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Oplossingen en andere experimentele functies: (ALLEEN gebruiken als iets niet werkt)",
    "Show week number on the clock": "Toon weeknummer op de klok",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Verberg de klok wanneer RDP Client of Citrix Workspace actief zijn",
    "Clock Appearance:": "Klok Uiterlijk",
    "Force the clock to have black text": "Forceer de klok om zwarte tekst te hebben",
    " - It is required that the Dark Text checkbox is disabled": "- Het is vereist dat het selectievakje Donkere tekst is uitgeschakeld",
    "Debbugging information:": "Foutopsporingsinformatie",
    "Open ElevenClock's log": "Open de log van ElevenClock",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Toon de klok op het primaire scherm (handig als de klok aan de linkerkant is ingesteld)",
    "Show weekday on the clock"  :"Toon weekdag op de klok",
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
    "Translated to English by martinet101"      :"Vertaald naar het Nederlands door Bugs en joosthoi1", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
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
