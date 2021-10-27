# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang2_5 = {
    "Hide the clock when RDP Client or Citrix Workspace are running": "",
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
    "<b>Update to the lastest version!</b>"                                             :"<b>Update naar de nieuwste versie!</b>",
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
