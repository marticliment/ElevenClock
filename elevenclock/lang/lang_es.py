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
    "Force the clock to be at the top of the screen": "Fuerza al reloj a mostrarse a la parte de arriba de la pantalla",
    "Show the clock on the primary screen": "Muestra el reloj en la pantalla principal",
    "Use a custom font color": "Usa un color de fuente específico",
    "Use a custom background color": "Usa un color de fondo específico",
    "Align the clock text to the center": "Alinea el texto del reloj al centro",
    "Select custom color": "Selecciona un color",
    "Hide the clock when a program occupies all screens": "Oculta el reloj cuando una aplicación ocupe todas las pantallas",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "Usar un tipo de letra personalizado",
    "Use a custom font size": "Usar un tamaño de letra personalizado",
    "Enable hide when multi-monitor fullscreen apps are running": "Ocultar el reloj cuando una aplicación se ejecute en pantalla completa a través de diversos monitores",
    "<b>{0}</b> needs to be enabled to change this setting": "<b>{0}</b> tiene que estar activado para cambiar esta opción",
    "<b>{0}</b> needs to be disabled to change this setting": "<b>{0}</b> tiene que estar desactivado para cambiar esta opción",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": "",
    "ElevenClock's language": "Idioma de ElevenClock"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Sobre Qt6 (PySide6)",
    "About": "Sobre",
    "Alternative non-SSL update server (This might help with SSL errors)": "Servidor de actualitzaciones alternativo sin SSL (Puede ayudar a resolver problemas con las actualizaciones)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Características experimentales y solución de errores (Usar solo si hay algo que no funciona)",
    "Show week number on the clock": "Muestra el número de la semana en el reloj",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Ocultar el reloj si se está ejecutando el cliente de Escritorio Remoto o Citrix Workspace",
    "Clock Appearance:": "Apariencia del reloj:",
    "Force the clock to have black text": "Fuerza al reloj a mostrar el texto en negro",
    " - It is required that the Dark Text checkbox is disabled": " - Se necesita que la opción de Texto en Negro esté desactivada",
    "Debbugging information:": "Información de depuración",
    "Open ElevenClock's log": "Abrir el regostro de ElevenClock",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Muestra el reloj en la pantalla principal (Útil si usted tiene el reloj en la parte izquierda de la pantalla)",
    "Show weekday on the clock"  :"Muestra el día de la semana en el reloj",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"Configuración de ElevenClock", # Also settings title
    "Reload Clocks"             :"Recargar relojes",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"Reiniciar ElevenClock",
    "Hide ElevenClock"          :"Ocultar ElevenClock",
    "Quit ElevenClock"          :"Cerrar ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Configuración general:",
    "Automatically check for updates"                                                   :"Buscar actualizaciones automáticamente",
    "Automatically install available updates"                                           :"Instalar automáticamente las actualizaciones",
    "Enable really silent updates"                                                      :"Activar actualizaciones silenciosas",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"No comprobar la autenticidad de las actualizaciones (NO RECOMENDADO, BAJO VUESTRA RESPONSABILIDAD)",
    "Show ElevenClock on system tray"                                                   :"Mostrar ElevenClock en la bandeja del sistema",
    "Alternative clock alignment (may not work)"                                        :"Alineación alternativa (puede no funcionar)",
    "Change startup behaviour"                                                          :"Cambiar el comportamiento al inicio",
    "Change"                                                                            :"Cambiar",
    "<b>Update to the latest version!</b>"                                             :"<b>Actualiza a la última versión</b>",
    "Install update"                                                                    :"Instalar actualización",
    
    #Clock settings
    "Clock Settings:"                                               :"Configuración del reloj:",
    "Hide the clock in fullscreen mode"                             :"Ocultar el reloj en modo de pantalla completa",
    "Hide the clock when RDP client is active"                      :"Ocultar el reloj si se está ejecutando el cliente de Escritorio Remoto",
    "Force the clock to be at the bottom of the screen"             :"Fuerza al reloj a mostrarse a la parte inferior de la pantalla",
    "Show the clock when the taskbar is set to hide automatically"  :"Muestra el reloj cuando la barra de tareas esté configurada para ocultarse",
    "Fix the hyphen/dash showing over the month"                    :"Arregla el guión mostrandose sobre el mes (formato de la fecha)",
    "Force the clock to have white text"                            :"Fuerza el reloj a tenir el texto blanco",
    "Show the clock at the left of the screen"                      :"Muestra el reloj a la parte izquierda de la pantalla",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Configuración de fecha y la hora:",
    "Show seconds on the clock"                         :"Muestra los segundos en el reloj",
    "Show date on the clock"                            :"Muestra la fecha en el reloj",
    "Show time on the clock"                            :"Muestra la hora en el reloj",
    "Change date and time format (Regional settings)"   :"Cambia el formato de la fecha y la hora (Configuración Regional)",
    "Regional settings"                                 :"Configuración Regional",
    
    #About the language pack
    "About the language pack:"                  :"Sobre el paquete de idioma:",
    "Translated to English by martinet101"      :"Traducido al Castellano por martinet101", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Traduce ElevenClock a tu idioma",
    "Get started"                               :"Empezar",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Sobre ElevenClock versión {0}:",
    "View ElevenClock's homepage"               :"Abre la página web de ElevenClock",
    "Open"                                      :"Abre",
    "Report an issue/request a feature"         :"Reporta un problema/proponer una característica",
    "Report"                                    :"Reportar",
    "Support the dev: Give me a coffee☕"       :"Suporta al desarrollador: cómprame un café☕",
    "Open page"                                 :"Abre",
    "Icons by Icons8"                           :"Los iconos son una cortesia de Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Página web",
    "Close settings"                            :"Cerrar la configuración",
    "Close"                                     :"Cerrar",
}



lang = lang2_3
