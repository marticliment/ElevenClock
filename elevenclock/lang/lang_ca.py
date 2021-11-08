# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang2_7 = {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": "",
    "ElevenClock's language": ""
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
