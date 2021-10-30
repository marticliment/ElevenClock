# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang2_5 = {
    "Hide the clock when RDP Client or Citrix Workspace are running": "",
    "Clock Appearance:": "",
    "Force the clock to have black text": "",
    " - It is required that the Dark Text checkbox is disabled": "",
    "Debbugging information:": "",
    "Open ElevenClock's log": "",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Afficher l'horloge sur l'écran principal",
    "Show weekday on the clock"  :"Afficher le jour de la semaine sur l'horloge",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"Paramètre de ElevenClock", # Also settings title
    "Reload Clocks"             :"Recharger ElevenClock",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"Redémarrer ElevenClock",
    "Hide ElevenClock"          :"Cacher ElevenClock",
    "Quit ElevenClock"          :"Quitter ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Paramètre généraux :",
    "Automatically check for updates"                                                   :"Rechercher automatiquement les mises à jour",
    "Automatically install available updates"                                           :"Installer automatiquement les mises à jour",
    "Enable really silent updates"                                                      :"Activer les mises à jour silencieuses",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Passer l'authentification du programme de mise à jour (NON RECOMMANDÉ, À VOS RISQUES ET PÉRILS)",
    "Show ElevenClock on system tray"                                                   :"Afficher ElevenClock dans la barre d'état",
    "Alternative clock alignment (may not work)"                                        :"Alignement alternatif de l'horloge (peut ne pas fonctionner)",
    "Change startup behaviour"                                                          :"Changer le comportement du démarrage", # not sure what this is
    "Change"                                                                            :"Changer",
    "<b>Update to the lastest version!</b>"                                             :"<b>Mettre à jour vers la dernière version !</b>",
    "Install update"                                                                    :"Installer la mise à jour",
    
    #Clock settings
    "Clock Settings:"                                              :"Paramètre de l'horloge :",
    "Hide the clock in fullscreen mode"                            :"Cacher l'horloge en pleine écran",
    "Hide the clock when RDP client is active"                     :"Cacher l'horloge quand un client RDP est actif",
    "Force the clock to be at the bottom of the screen"            :"Forcer l'alignement de l'horloge en bas de l'écran",
    "Show the clock when the taskbar is set to hide automatically" :"Afficher l'horloge lorsque la barre des tâches est masquée automatiquement",
    "Fix the hyphen/dash showing over the month"                   :"Corriger le trait d'union affiché au-dessus du mois",
    "Force the clock to have white text"                           :"Forcer le texte de l'horloge en blanc",
    "Show the clock at the left of the screen"                     :"Afficher l'horloge à gauche de l'écran",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Paramètre de la date & heure",
    "Show seconds on the clock"                         :"Afficher les secondes sur l'horloge",
    "Show date on the clock"                            :"Afficher la date sur l'horloge",
    "Show time on the clock"                            :"Afficher l'heure sur l'horloge",
    "Change date and time format (Regional settings)"   :"Changer le format de la date & heure (paramètre régionaux)",
    "Regional settings"                                 :"Paramètre régionaux",
    
    #About the language pack
    "About the language pack:"                  :"À propos du pack de langue",
    "Translated to English by martinet101"      :"Traduis en français par Lilobast", # Here, make sure to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Traduire ElevenClock dans votre langue",
    "Get started"                               :"Commencer",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"À propos de ElevenClock {0} :",
    "View ElevenClock's homepage"               :"Page d'accueil d'ElevenClock",
    "Open"                                      :"Ouvrir",
    "Report an issue/request a feature"         :"Signaler un bug / Suggérer une fonctionnalité",
    "Report"                                    :"Signaler",
    "Support the dev: Give me a coffee☕"       :"Supporter le développeur",
    "Open page"                                 :"Ouvrir la page",
    "Icons by Icons8"                           :"Icônes faites par Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Page web",
    "Close settings"                            :"Fermer les paramètres",
    "Close"                                     :"Fermer",
}

lang = lang2_3