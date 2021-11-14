# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang2_7_bis = {
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
    "Hide the clock when RDP Client or Citrix Workspace are running": "Piilota kello, kun RDP-asiakasohjelma tai Citrix Workspace on käynnissä",
    "Clock Appearance:": "Kellon ulkonäkö:",
    "Force the clock to have black text": "Pakota kellon fontti mustaksi",
    " - It is required that the Dark Text checkbox is disabled": " - Tumma teksti -valintaruudun on oltava pois käytöstä.",
    "Debbugging information:": "Tietoja virheenkorjauksesta:",
    "Open ElevenClock's log": "Avaa ElevenClokin logi",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Näytä kello ensisijaisessa näytössä (Hyödyllinen, jos kello on asetettu vasemmalle).",
    "Show weekday on the clock"  :"Näytä viikonpäivä kellossa",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"ElevenClock-asetukset", # Also settings title
    "Reload Clocks"             :"Päivitä kellot",
    "ElevenClock v{0}"          :"Versio: ElevenClock v{0}",
    "Restart ElevenClock"       :"Käynnistä ElevenClock uudelleen",
    "Hide ElevenClock"          :"Piilota ElevenClock",
    "Quit ElevenClock"          :"Sulje ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Yleiset asetukset",
    "Automatically check for updates"                                                   :"Tarkista päivitykset automaattisesti",
    "Automatically install available updates"                                           :"Asenna saatavilla olevat päivitykset automaattisesti",
    "Enable really silent updates"                                                      :"Ota käyttöön hiljaiset päivitykset",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Ohita päivityksen tarjoajan aitoustarkastus (EI SUOSITELLA, OMALLA VASTUULLA)",
    "Show ElevenClock on system tray"                                                   :"Näytä ElevenClock-kuvake tehtäväpalkissa",
    "Alternative clock alignment (may not work)"                                        :"Vaihtoehtoinen kellon tasaus (ei välttämättä toimi)",
    "Change startup behaviour"                                                          :"Muuta käyttäytymistä käynnistäessä",
    "Change"                                                                            :"Muuta",
    "<b>Update to the latest version!</b>"                                             :"<b>Päivitä viimeisinpään versioon!</b>",
    "Install update"                                                                    :"Asenna päivitys",
    
    #Clock settings
    "Clock Settings:"                                              :"Kellon asetukset:",
    "Hide the clock in fullscreen mode"                            :"Piilota kello koko näytön tilassa",
    "Hide the clock when RDP client is active"                     :"Piilota kello, kun RDP-asiakasohjelma on käynnissä",
    "Force the clock to be at the bottom of the screen"            :"Pakota kello näytön alareunaan",
    "Show the clock when the taskbar is set to hide automatically" :"Näytä kello, kun tehtäväpalkki on asetettu piilotettavaksi automaattisesti",
    "Fix the hyphen/dash showing over the month"                   :"Korjaa viiva kuukauden kohdalla",
    "Force the clock to have white text"                           :"Pakota kellon fontti valkoiseksi",
    "Show the clock at the left of the screen"                     :"Näytä kello ruudun vasemmassa reunassa",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Päivämäärän ja Kellonajan Asetukset:",
    "Show seconds on the clock"                         :"Näytä sekunnit kellossa",
    "Show date on the clock"                            :"Näytä päivämäärä kellossa",
    "Show time on the clock"                            :"Näytä kellonaika kellossa",
    "Change date and time format (Regional settings)"   :"Vaihda päivämäärän ja kellonajan formaattia (Alueelliset asetukset)",
    "Regional settings"                                 :"Alueelliset asetukset",
    
    #About the language pack
    "About the language pack:"                  :"Tietoja kielipaketista:",
    "Translated to English by martinet101"      :"Suomentanut: npsand", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Käännä ElevenClock omalle kielellesi",
    "Get started"                               :"Aloita",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Tietoja ElevenClock-verisosta {0}:",
    "View ElevenClock's homepage"               :"Näytä ElevenClokin kotisivu",
    "Open"                                      :"Avaa",
    "Report an issue/request a feature"         :"Ilmoita ongelmasta tai pyydä ominaisuutta",
    "Report"                                    :"Ilmoita",
    "Support the dev: Give me a coffee☕"       :"Tue kehittäjää: Tarjoa minulle kahvi☕",
    "Open page"                                 :"Avaa sivu",
    "Icons by Icons8"                           :"Kuvakkeet Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Verkkosivu",
    "Close settings"                            :"Sulje asetukset",
    "Close"                                     :"Sulje",
}

lang = lang2_3
