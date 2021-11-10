# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"

# So it would look like: "ORIGINAL_TEXT" : "TRANSLATED_TEXT",


# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang2_7 = {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": " (Ova opcija je isključena jer bi trebala da radi u većini slučajeva. Ako ne radi, molimo prijavite grešku)",
    "ElevenClock's language": "Jezik programa ElevenClock"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "O Qt6 (PySide6)",
    "About": "O",
    "Alternative non-SSL update server (This might help with SSL errors)": "Alternativni server za ažuriranje bez SSL-a (Ovo može pomoći ako se pojavljuju SSL greške)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Popravke i ostale eksperimentalne funkcije: (Koristiti SAMO u slučaju da nešto ne radi kako treba)",
    "Show week number on the clock": "Prikazuj redni broj nedelje u okviru sata"
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Sakrij sat kada je RDP klijent ili Citrix Workspace pokrenut",
    "Clock Appearance:": "Izgled Sata",
    "Force the clock to have black text": "Forsiraj crnu boju teksta sata",
    " - It is required that the Dark Text checkbox is disabled": " - Ova funkcija zahteva da opcija Crni Boja teksta sata bude isključena",
    "Debbugging information:": "Otklanjanje grešaka:",
    "Open ElevenClock's log": "Otvori ElevenClock log fajl",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Prikazuj sat na primarnom ekranu (Korisno ako je podešeno da se sat prikazuje uz levu ivicu ekrana)",
    "Show weekday on the clock"  :"Prikazuj dan u nedelji u okviru sata",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"Podešavanja programa ElevenClock", # Also settings title
    "Reload Clocks"             :"Osveži satove",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"Ponovo pokreni ElevenClock",
    "Hide ElevenClock"          :"Sakrij ElevenClock",
    "Quit ElevenClock"          :"Zatvori ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Opšta Podešavanja",
    "Automatically check for updates"                                                   :"Automatski proveri da li postoji nova verzija",
    "Automatically install available updates"                                           :"Automatski instaliraj nove verzije",
    "Enable really silent updates"                                                      :"Uključi neprimetna ažuriranja",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Zaobiđi proveru autentičnosti provajdera ažuriranja (NIJE PREPORUČLJIVO, NA SOPSTVENU ODGOVORNOST)",
    "Show ElevenClock on system tray"                                                   :"Prikaži ElevenClock u sistemskoj traci",
    "Alternative clock alignment (may not work)"                                        :"Alternativni metod za pozicioniranje sata (možda neće raditi)",
    "Change startup behaviour"                                                          :"Podesi pokretanje sa sistemom",
    "Change"                                                                            :"Izmeni",
    "<b>Update to the latest version!</b>"                                             :"<b>Ažuriraj na najnoviju verziju!</b>",
    "Install update"                                                                    :"Instaliraj novu verziju",
    
    #Clock settings
    "Clock Settings:"                                              :"Podešavanje Sata:",
    "Hide the clock in fullscreen mode"                            :"Sakrij sat u režimu punog ekrana (Fullscreen)",
    "Hide the clock when RDP client is active"                     :"Sakrij sat kada je RDP klijent aktivan",
    "Force the clock to be at the bottom of the screen"            :"Forsiraj sat na dno ekrana",
    "Show the clock when the taskbar is set to hide automatically" :"Prikazuj sat i kada je traka zadataka podešena da se sakrije automatski",
    "Fix the hyphen/dash showing over the month"                   :"Uključiti ovu opciju ako se pojavljuje crtica preko naziva meseca",
    "Force the clock to have white text"                           :"Forsiraj belu boju teksta sata",
    "Show the clock at the left of the screen"                     :"Prikazuj sat uz levu ivicu ekrana",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Podešavanje Datuma i Vremena:",
    "Show seconds on the clock"                         :"Prikazuj sekunde u okviru sata",
    "Show date on the clock"                            :"Prikazuj datum u okviru sata",
    "Show time on the clock"                            :"Prikazuj sat i minut",
    "Change date and time format (Regional settings)"   :"Promeni format datuma i vremena (Regionalni format)",
    "Regional settings"                                 :"Opcije regionalnog formata",
    
    #About the language pack
    "About the language pack:"                  :"O prevodu ovog programa:",
    "Translated to English by martinet101"      :"Preveli na srpski jezik: Stefan Marjanov", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Prevedi ElevenClock na tvoj jezik",
    "Get started"                               :"Započni",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"O programu ElevenClock verzija {0}:",
    "View ElevenClock's homepage"               :"Otvori zvanični ElevenClock sajt",
    "Open"                                      :"Otvori",
    "Report an issue/request a feature"         :"Prijavi grešku/zahtevaj novu opciju",
    "Report"                                    :"Prijavi",
    "Support the dev: Give me a coffee☕"       :"Podrži developera: Kupi mi kafu☕",
    "Open page"                                 :"Doniraj",
    "Icons by Icons8"                           :"Ikonice: Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Sajt",
    "Close settings"                            :"Zatvori podešavanja",
    "Close"                                     :"Zatvori",
}

lang = lang2_3
