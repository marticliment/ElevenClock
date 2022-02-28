# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.


lang_3_3 = {
    "Custom format rules:": "Règles de format personnalisé",
    "Any text can be placed here. To place items such as date and time, please use the 1989 C standard. More info on the following link": "N'importe quel texte peut être placé ici. Pour placer des éléments tels que la date et l'heure, veuillez utiliser la norme 1989 C. Plus d'infos sur le lien suivant",
    "Python Date and time values": "Valeurs de date et heure de python",
    "To disable the zero-padding effect, add a # in bethwwn the % and the code: non-zero-padded hours would be %#H, and zero-padded hours would be %H": "Pour désactiver l'effet zéro-marge, ajoutez un # entre le % et le code : une heure avec marge doit être %#H, une heure sans marge doit être %H", # Here please don't modify the %H and %#H values
    "Click on Apply to apply and preview the format": "Cliquez sur Appliquer pour appliquer et prévisualiser le format",
    "Apply": "Appliquer",
    "If you don't understand what is happening, please uncheck the checkbox over the text area": "Si vous n'êtes pas sûr de ce qu'il se passe, veuillez décocher la case au-dessus de la zone de texte",
    "Set a custom date and time format": "Définir un format de date et heure personnalisé",
    "(for advanced users only)": "(utilisateurs avancés uniquement)",
    "Move this clock to the left": "Déplacer cette horloge vers la gauche",
    "Move this clock to the top": "Déplacer cette horloge vers en haut",
    "Move this clock to the right": "Déplacer cette horloge vers la droite",
    "Move this clock to the bottom": "Déplacer cette horloge vers le bas",
    "Restore horizontal position": "Restaurer la position horizontale",
    "Restore vertical position": "Restaurer la position verticale",
}

lang_3_2_1 = lang_3_3 | {
    "Open online help to troubleshoot problems": "Ouvrir l'aide en ligne pour résoudre les problèmes",
    "Reset ElevenClock preferences to defaults": "Restaurer les paramètres par défaut d'ElevenClock",
    "Specify a minimum width for the clock": "Entrer une largeur minimale pour l'horloge",
    "Search on the settings": "Rechercher un paramètre",
    "No results were found": "Aucun résultat trouvé",
}

lang_3_2 = lang_3_2_1 | {
    "Use system accent color as background color": "Utiliser la couleur d'accentuation en tant que couleur d'arrière-plan",
    "Check only the focused window on the fullscreen check": "N'afficher l'horloge que si une fenêtre active est en plein écran",
    "Clock on monitor {0}": "Horloge sur l'écran {0}",
    "Move to the left": "Déplacer vers la gauche",
    "Show this clock on the left": "Afficher cette horloge à gauche",
    "Show this clock on the right": "Afficher cette horloge à droite",
    "Restore clock position": "Restaurer la position de l'horloge",
}

lang_3_1 = lang_3_2 | {
    "W": "S", # The initial of the word week in your language: W for week, S for setmana, etc.
    "Disable the notification badge": "Désactiver le badge de notification",
    "Override clock default height": "Modifier la hauteur par défaut de l'horloge",
    "Adjust horizontal clock position": "Modifier la position horizontale de l'horloge",
    "Adjust vertical clock position": "Modifier la position verticale de l'horloge",
    "Export log as a file": "Exporter les logs dans un fichier",
    "Copy log to clipboard": "Copier les logs dans le presse-papiers",
    "Announcements:": "Annonces :",
    "Fetching latest announcement, please wait...": "Récupération des dernières annonces, veuillez patienter...",
    "Couldn't load the announcements. Please try again later": "Impossible de charger les annonces. Réessayer ultérieurement",
    "ElevenClock's log": "Logs de ElevenClock",
    "Pick a color": "Choisissez une couleur"
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "Cacher l'horloge pendant 10s lorsqu'elle est cliquée",
    "Enable low-cpu mode": "Activer le mode basse-consommation cpu",
    "You might lose functionalities, like the notification counter or the dynamic background": "Vous pouvez perdre des fonctionnalités, comme les badges de notifications ou l'arrière-plan dynamique",
    "Clock position and size:": "Taille et position de l'horloge",
    "Clock size preferences, position offset, clock at the left, etc.": "Paramètres de la position, de la taille, de la marge, etc.",
    "Reset monitor blacklisting status": "Réinitialiser la liste des écrans ignorés",
    "Reset": "Réinitialiser",
    "Third party licenses": "Licences tierces",
    "View": "Ouvrir",
    "ElevenClock": "ElevenClock",
    "Monitor tools": "Gestion des écrans",
    "Blacklist this monitor": "Ne pas afficher sur cet écran",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "Applications open-source tierces utilisées dans ElevenClock {0} (et leurs licences)",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "ElevenClock est une application open-source créer à l'aide d'autres librairies communautaire",
    "Ok": "OK",
    "More Info": "Plus d'informations",
    "About Qt": "À propos de Qt",
    "Success": "Succès",
    "The monitors were unblacklisted successfully.": "La liste des écrans ignorés a été vidée.",
    "Now you should see the clock everywhere": "Vous devriez maintenant voir l'horloge sur tous les écrans",
    "Ok": "OK",
    "Blacklist Monitor": "Ne pas afficher sur cet écran",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "En continuant, l'écran sera ignoré et l'horloge ne sera plus affichée sur cet écran de manière permanente.",
    "This action can be reverted from the settings window. under <b>Clock position and size</b>": "Cette action peut être annulée via les paramètres, sous <b>Taille et position de l'horloge</b>",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "Êtes-vous sûr de ne plus vouloir afficher l'horloge sur cet écran ?",
    "Yes": "Oui",
    "No": "Non",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "Recharger les logs",
    "Do not show the clock on secondary monitors": "Ne pas afficher l'horloge sur l'écran secondaire",
    "Disable clock taskbar background color (make clock transparent)": "Désactiver l'arrière-plan de l'horloge (rend l'horloge transparente)",
    "Open the welcome wizard": "Ouvrir l'assistant de bienvenue",
    " (ALPHA STAGE, MAY NOT WORK)": " (STADE D'ALPHA, PEUT NE PAS FONCTIONNER",
    "Welcome to ElevenClock": "Bienvenue sur ElevenClock",
    "Skip": "Passer",
    "Start": "Démarrer",
    "Next": "Suivant",
    "Finish": "Terminer",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "Gestionnaire des tâches",
    "Change date and time": "Régler la date et l'heure",
    "Notification settings": "Paramètres des notifications",
    "Updates, icon tray, language": "Mise à jour, icône de l'angle de la barre des tâches, langue",
    "Hide extended options from the clock right-click menu (needs a restart to be aplied)": "Cacher les options avancées du menu clic droit (nécessite un redémarrage)",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "Comportement en plein écran, position de l'horloge, horloge sur l'écran principal, autres paramètres",
    'Add the "Show Desktop" button on the left corner of every clock': 'Ajouter le bouton "Afficher le bureau" à gauche de toutes les horloges',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': 'Vous devrez peut-être sélectionner un fond d\'écran personnalisé pour que cela fonctionne.&nbsp;Plus d\'informations <a href="{0}" style="color:DodgerBlue">ICI</a>',
    "Clock's font, font size, font color and background, text alignment": "Police de l'horloge, taille de la police, couleur et arrière-plan, position du texte",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "Format de la date & heure, affichage des secondes, jour de la semaine, numéro de la semaine et paramètres régionaux",
    "Testing features and error-fixing tools": "Fonctions expérimentales et outil de débogage",
    "Language pack author(s), help translating ElevenClock": "Auteur(s) du pack de langue aidant à traduire ElevenClock",
    "Info, report a bug, submit a feature request, donate, about": "Informations, signaler un bug, proposer une fonctionnalité, faire un don, à propos",
    "Log, debugging information": "Logs, informations de débogage",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen": "Forcer l'affichage de l'horloge en haut de l'écran",
    "Show the clock on the primary screen": "Afficher l'horloge sur l'écran principal",
    "Use a custom font color": "Utiliser une couleur de police personnalisée",
    "Use a custom background color": "Utiliser une couleur de fond personnalisée",
    "Align the clock text to the center": "Aligner le texte de l'horloge au centre",
    "Select custom color": "Sélectionner la couleur",
    "Hide the clock when a program occupies all screens": "Cacher l'horloge lorsqu'une application utilise tous les écrans",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "Utiliser une police personnalisée",
    "Use a custom font size": "Utiliser une taille de police personnalisée",
    "Enable hide when multi-monitor fullscreen apps are running": "Cacher l'horloge lorsqu'une application multi-écran en plein écran est active",
    "<b>{0}</b> needs to be enabled to change this setting": "<b>{0}</b> doit être activé pour changer ce paramètre",
    "<b>{0}</b> needs to be disabled to change this setting": "<b>{0}</b> doit être désactivé pour changer ce paramètre",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": " (Cette fonctionnalité a été désactivée car elle devrait fonctionner par défaut)",
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
    "Hide the clock when RDP Client or Citrix Workspace are running": "Cacher l'horloge quand un client RDP ou Citrix Workspace est actif",
    "Clock Appearance:": "Apparence de l'horloge",
    "Force the clock to have black text": "Forcer le texte de l'horloge en noir",
    " - It is required that the Dark Text checkbox is disabled": " - Forcer le texte de l'horloge en noir doit être désactivé",
    "Debbugging information:": "Informations de débogage",
    "Open ElevenClock's log": "Ouvrir les logs de ElevenClock",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Afficher l'horloge sur l'écran principal",
    "Show weekday on the clock"  :"Afficher le jour de la semaine sur l'horloge",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"Paramètres de ElevenClock", # Also settings title
    "Reload Clocks"             :"Recharger ElevenClock",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"Redémarrer ElevenClock",
    "Hide ElevenClock"          :"Cacher ElevenClock",
    "Quit ElevenClock"          :"Quitter ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Paramètres généraux",
    "Automatically check for updates"                                                   :"Rechercher automatiquement les mises à jour",
    "Automatically install available updates"                                           :"Installer automatiquement les mises à jour",
    "Enable really silent updates"                                                      :"Activer les mises à jour silencieuses",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Passer l'authentification du programme de mise à jour (NON RECOMMANDÉ, À VOS RISQUES ET PÉRILS)",
    "Show ElevenClock on system tray"                                                   :"Afficher ElevenClock dans l'angle de la barre des tâches",
    "Alternative clock alignment (may not work)"                                        :"Alignement alternatif de l'horloge (peut ne pas fonctionner)",
    "Change startup behaviour"                                                          :"Changer le comportement au démarrage de Windows", # not sure what this is
    "Change"                                                                            :"Changer",
    "<b>Update to the latest version!</b>"                                             :"<b>Mettre à jour vers la dernière version !</b>",
    "Install update"                                                                    :"Installer la mise à jour",
    
    #Clock settings
    "Clock Settings:"                                              :"Paramètre de l'horloge",
    "Hide the clock in fullscreen mode"                            :"Cacher l'horloge en mode plein écran",
    "Hide the clock when RDP client is active"                     :"Cacher l'horloge quand un client RDP est actif",
    "Force the clock to be at the bottom of the screen"            :"Forcer l'affichage de l'horloge en bas de l'écran",
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
    "Translated to English by martinet101"      :"Traduit en français par Lilobast et scrocquesel", # Here, make sure to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Traduire ElevenClock dans votre langue",
    "Get started"                               :"Commencer",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"À propos de ElevenClock {0}",
    "View ElevenClock's homepage"               :"Page d'accueil d'ElevenClock",
    "Open"                                      :"Ouvrir",
    "Report an issue/request a feature"         :"Signaler un bug / proposer une fonctionnalité",
    "Report"                                    :"Signaler",
    "Support the dev: Give me a coffee☕"       :"Soutenir le développeur: Offrez-moi un café☕",
    "Open page"                                 :"Soutenir",
    "Icons by Icons8"                           :"Icônes réalisées par Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Page web",
    "Close settings"                            :"Fermer les paramètres",
    "Close"                                     :"Fermer",
}

lang = lang2_3
