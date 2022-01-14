# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.
lang_3_1 = {
    "W": "S", # The initial of the word week in your language: W for week, S for setmana, etc.
    "Disable the notification badge": "Desactiva la icona de notificació",
    "Override clock default height": "Sobreescriu l'altura per defecte del rellotge",
    "Adjust horizontal clock position": "Ajusta la posició horitzontal del rellotge",
    "Adjust vertical clock position": "Ajusta la posició vertical del rellotge",
    "Export log as a file": "Exporta el registre com a fitxer",
    "Copy log to clipboard": "Copia el registre al porta-retalls",
    "Announcements:": "Taulell d'anuncis:",
    "Fetching latest announcement, please wait...": "Carregant l'últim anunci, espereu-vos si us plau...",
    "Couldn't load the announcements. Please try again later": "No hem pogut carregar els anuncis. Proveu-ho més tard",
    "ElevenClock's log": "Registre de l'ElevenClock",
    "Pick a color": "Selecciona un color"
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "Amaga el rellotge durant 10 segons quant es cliqui",
    "Enable low-cpu mode": "Activa el mode de baix consum de CPU",
    "You might lose functionalities, like the notification counter or the dynamic background": "Podeu perdre funcionalitats, com el comptador de notificacions o el fons dinàmic",
    "Clock position and size:": "Posició i mida del rellotge:",
    "Clock size preferences, position offset, clock at the left, etc.": "Preferències de mida del rellotge, desplaçament, rellotge a l'esquerra, etc.",
    "Reset monitor blacklisting status": "Reinicialitza la llista negra de pantalles",
    "Reset": "Reinicialitza",
    "Third party licenses": "Llicències de tercers",
    "View": "Mostra",
    "ElevenClock": "ElevenClock",
    "Monitor tools": "Eines de la pantalla",
    "Blacklist this monitor": "Afegeix la pantalla a la llista negra",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "Software de tercers de codi obert a l'ElevenClock {0} (I les seves llicències)",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "L'ElevenClock és una aplicació de codi obert feta amb l'ajuda d'altres llibreries fetes per la comunitat",
    "Ok": "D'acord",
    "More Info": "Més informació",
    "About Qt": "Sobre Qt",
    "Success": "Enhorabona",
    "The monitors were unblacklisted successfully.": "Les pantalles han sigut tretes de la llista negra satisfactòriament",
    "Now you should see the clock everywhere": "Ara hauríeu de veure el rellotge a tot arreu",
    "Ok": "D'acord",
    "Blacklist Monitor": "Afegir a la llista negra",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "Si afegiu una pantalla a la llista negra, el rellotge no es mostrarà allà",
    "This action can be reverted from the settings window. under <b>Clock position and size</b>": "Aquesta acció es pot revertir des de la Configuració, sota <b>Posició i mida del rellotge</b>",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "Esteu segurs de que voleu afegir la pantalla {0} a la llista negra?",
    "Yes": "Sí",
    "No": "No",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "Recarrega el registre",
    "Do not show the clock on secondary monitors": "No mostris el rellotge a les pantalles secundàries",
    "Disable clock taskbar background color (make clock transparent)": "Desactiva el color de fons automàtic del rellotge (fes el rellotge transparent)",
    "Open the welcome wizard": "Obre l'assistent de benvinguda",
    " (ALPHA STAGE, MAY NOT WORK)": " (EN ESTAT ALFA, POT NO FUNCIONAR)",
    "Welcome to ElevenClock": "Benvingut/da a l'ElevenClock",
    "Skip": "Omet",
    "Start": "Comença",
    "Next": "Següent",
    "Finish": "Finalitzar",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "Administrador de tasques",
    "Change date and time": "Ajusta la data i l'hora",
    "Notification settings": "Configuració de les notificacions",
    "Updates, icon tray, language": "Actualitzacions, safata del sistema, idioma",
    "Hide extended options from the clock right-click menu (needs a restart to be aplied)": "Amaga les funcions extres del menú de clic dret del rellotge (Es necessita un reinici per a aplicar)",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "Comportament de pantalla completa, posició del rellotge, rellotge de la pantalla principal, altres paràmetres miscel·lanis",
    'Add the "Show Desktop" button on the left corner of every clock': 'Afegeix el botó de "Mostrar l\'escriptori" a la cantonada dreta de cada rellotge',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': 'Pot ser que necessiteu establir un color de fons concret.&nbsp;Més informació <a href="{0}" style="color:DodgerBlue">AQUÍ</a>',
    "Clock's font, font size, font color and background, text alignment": "Tipus i mida de font, color de text i de fons, alineació del text del rellotge",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "Format de data i hora, segons, dia de la setmana i setmana de l'any, configuració regional",
    "Testing features and error-fixing tools": "Característiques experimentals i altres configuracions per a la solució d'errors",
    "Language pack author(s), help translating ElevenClock": "Autor(s) del paquet d'idioma, ajudeu a traduir l'ElevenClock",
    "Info, report a bug, submit a feature request, donate, about": "Informació, reportar un problema, suggerir una característica, fer una donació, informació sobre l'ElevenClock",
    "Log, debugging information": "Registre, informació de depuració",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen": "Força el rellotge a mostrar-se a la part de dalt de la pantalla",
    "Show the clock on the primary screen": "Mostra el rellotge a la pantalla principal",
    "Use a custom font color": "Utilitza un color de lletra concret",
    "Use a custom background color": "Utilitza un color de fons concret",
    "Align the clock text to the center": "Alinea el text del rellotge al centre",
    "Select custom color": "Selecciona un color",
    "Hide the clock when a program occupies all screens": "Amaga el rellotge quan una aplicació es mostri a totes les pantalles",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "Utilitza un tipus de lletra concret",
    "Use a custom font size": "Utilitza una mida de lletra concreta",
    "Enable hide when multi-monitor fullscreen apps are running": "Amaga el rellotge quan una pantalla s'executi en mode de pantalla completa multi-monitor",
    "<b>{0}</b> needs to be enabled to change this setting": "<b>{0}</b> ha d'estar activat per a canviar aquesta configuració",
    "<b>{0}</b> needs to be disabled to change this setting": "<b>{0}</b> ha d'estar desactivat per a canviar aquesta configuració",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": "",
    "ElevenClock's language": "Idioma de l'ElevenClock"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Sobre el Qt6 (PySide6)",
    "About": "Sobre",
    "Alternative non-SSL update server (This might help with SSL errors)": "Servidor d'actualitzacions alternatiu sense SSL (Pot ajudar a resoldre problemes amb les actualitzacions)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Característiques experimentals i solucions (Utilitzar només si quelcom no funciona)",
    "Show week number on the clock": "Mostra el número de la setmana al rellotge",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Oculta el rellotge si s'està fent servir el client d'Escriptori Remot o el Citrix Workspace",
    "Clock Appearance:": "Aparença del rellotge:",
    "Force the clock to have black text": "Força el rellotge a tenir el text de color negre",
    " - It is required that the Dark Text checkbox is disabled": " - Es necessita que la opció de Text de Color Negre estigui desactivada",
    "Debbugging information:": "Informació de depuració",
    "Open ElevenClock's log": "Obre el registre de l'ElevenClock",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Mostra el rellotge a la pantalla primària (Útil si tens el rellotge a l'esquerra de la pantalla)",
    "Show weekday on the clock"  :"Mostra el dia de la setmana als rellotges",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"Configuració de l'ElevenClock", # Also settings title
    "Reload Clocks"             :"Recarregar els rellotges",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"Reiniciar l'ElevenClock",
    "Hide ElevenClock"          :"Amagar l'ElevenClock",
    "Quit ElevenClock"          :"Tancar l'ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Configuració general:",
    "Automatically check for updates"                                                   :"Cercar actualitzacions automàticament",
    "Automatically install available updates"                                           :"Instal·lar automàticament les actualitzacions",
    "Enable really silent updates"                                                      :"Activar actualitzacions silencioses",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"No comprovar l'autenticitat de les actualitzacions (NO RECOMANAT, SOTA LA VOSTRA RESPONSABILITAT)",
    "Show ElevenClock on system tray"                                                   :"Mostrar l'ElevenClock a la safata del sistema",
    "Alternative clock alignment (may not work)"                                        :"Alineació alternativa (pot no funcionar)",
    "Change startup behaviour"                                                          :"Canviar el comportament a l'inici",
    "Change"                                                                            :"Canvia",
    "<b>Update to the latest version!</b>"                                             :"<b>Actualitza a la última versió</b>",
    "Install update"                                                                    :"Instal·lar actualització",
    
    #Clock settings
    "Clock Settings:"                                               :"Configuració del rellotge:",
    "Hide the clock in fullscreen mode"                             :"Oculta el rellotge en mode de pantalla completa",
    "Hide the clock when RDP client is active"                      :"Oculta el rellotge si s'està fent servir el client d'Escriptori Remot",
    "Show the clock when the taskbar is set to hide automatically"  :"Mostra el rellotge quan la barra de tasques estigui configurada per a amagar-se",
    "Force the clock to be at the bottom of the screen"             :"Força el rellotge a mostrar-se a la part de sota de la pantalla",
    "Fix the hyphen/dash showing over the month"                    :"Arregla el guió mostrant -se sobre el mes (format de la data)",
    "Force the clock to have white text"                            :"Força el rellotge a tenir text blanc",
    "Show the clock at the left of the screen"                      :"Mostra el rellotge a l'esquerra de la pantalla",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Configuració de data i hora:",
    "Show seconds on the clock"                         :"Mostra els segons al rellotge",
    "Show date on the clock"                            :"Mostra la data al rellotge",
    "Show time on the clock"                            :"Mostra l'hora al rellotge",
    "Change date and time format (Regional settings)"   :"Canvia el format de data i hora (Configuració Regional)",
    "Regional settings"                                 :"Configuració Regional",
    
    #About the language pack
    "About the language pack:"                  :"Sobre el paquet de llengua:",
    "Translated to English by martinet101"      :"Traduït al Català per martinet101", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Tradueix l'ElevenClock al teu idioma",
    "Get started"                               :"Comença",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Sobre l'ElevenClock versió {0}:",
    "View ElevenClock's homepage"               :"Mostra la pàgina web de l'ElevenClock",
    "Open"                                      :"Obre",
    "Report an issue/request a feature"         :"Reporta un problema/proposa una característica",
    "Report"                                    :"Reporta",
    "Support the dev: Give me a coffee☕"       :"Suporta al desenvolupador: compra'm un cafè☕",
    "Open page"                                 :"Obre",
    "Icons by Icons8"                           :"Les icones són una cortesia d'Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Pàgina web",
    "Close settings"                            :"Tanca la configuració",
    "Close"                                     :"Tanca",
}



lang = lang2_3
