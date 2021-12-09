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
    "Force the clock to be at the top of the screen": "Forcer l'horloge à être en haut de l'écran",
    "Show the clock on the primary screen": "Afficher l'horloge sur l'écran principal",
    "Use a custom font color": "Utiliser une couleur de police personnalisée",
    "Use a custom background color": "Utiliser un couleur de fond personnalisée",
    "Align the clock text to the center": "Aligner le texte de l'horloge au centre",
    "Select custom color": "Sélectionner la couleur",
    "Hide the clock when a program occupies all screens": "Cacher l'horloge lorsqu'une application utilise l'écran complet",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "Utiliser une police personnalisée",
    "Use a custom font size": "Utiliser une taille de police personnalisée",
    "Enable hide when multi-monitor fullscreen apps are running": "Cacher l'horloge quand une application multi-écran en plein écran est active",
    "<b>{0}</b> needs to be enabled to change this setting": "<b>{0}</b> a besoin d'être activer pour changer ce paramètre",
    "<b>{0}</b> needs to be disabled to change this setting": "<b>{0}</b> a besoin d'être désactiver pour changer ce paramètre",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": " (Cette fonctionnalité a été désactivé car elle devrait fonctionner par défaut)",
    "ElevenClock's language": "Langue de ElevenClock"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "À propos de Qt6 (PySide6)",
    "About": "À propos",
    "Alternative non-SSL update server (This might help with SSL errors)": "Serveur de mise à jour alternatif non-SSL (Peux aider à résoudre les erreurs de SSL)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Corrections et autres fonctions expérimentales (Utiliser SEULEMENT si quelque chose ne fonctionne pas)",
    "Show week number on the clock": "Afficher le numéro de la semaine sur l'horloge",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Cacher l'horloge quand un client RDP ou Citrix est actif",
    "Clock Appearance:": "Apparence de l'horloge",
    "Force the clock to have black text": "Forcer le texte de l'horloge en noir",
    " - It is required that the Dark Text checkbox is disabled": " - Forcer le texte de l'horloge en noir doit être désactivé",
    "Debbugging information:": "Information de déboggage",
    "Open ElevenClock's log": "Ouvrir les logs de ElevenClock",
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
    "<b>Update to the latest version!</b>"                                             :"<b>Mettre à jour vers la dernière version !</b>",
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
    "Open page"                                 :"Supporter",
    "Icons by Icons8"                           :"Icônes faites par Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Page web",
    "Close settings"                            :"Fermer les paramètres",
    "Close"                                     :"Fermer",
}

lang = lang2_3
