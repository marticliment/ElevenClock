# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_1 = {
    "W": "", # The initial of the word week in your language: W for week, S for setmana, etc.
    "Disable the notification badge": "",
    "Override clock default height": "",
    "Adjust horizontal clock position": "",
    "Adjust vertical clock position": "",
    "Export log as a file": "",
    "Copy log to clipboard": "",
    "Announcements:": "",
    "Fetching latest announcement, please wait...": "",
    "Couldn't load the announcements. Please try again later": "",
    "ElevenClock's log": "",
    "Pick a color": ""
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "",
    "Enable low-cpu mode": "",
    "You might lose functionalities, like the notification counter or the dynamic background": "",
    "Clock position and size:": "",
    "Clock size preferences, position offset, clock at the left, etc.": "",
    "Reset monitor blacklisting status": "",
    "Reset": "",
    "Third party licenses": "",
    "View": "",
    "ElevenClock": "",
    "Monitor tools": "",
    "Blacklist this monitor": "",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "",
    "Ok": "",
    "More Info": "",
    "About Qt": "",
    "Success": "",
    "The monitors were unblacklisted successfully.": "",
    "Now you should see the clock everywhere": "",
    "Ok": "",
    "Blacklist Monitor": "",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "",
    "This action can be reverted from the settings window. under <b>Clock position and size</b>": "",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "",
    "Yes": "",
    "No": "",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "",
    "Do not show the clock on secondary monitors": "",
    "Disable clock taskbar background color (make clock transparent)": "",
    "Open the welcome wizard": "",
    " (ALPHA STAGE, MAY NOT WORK)": "",
    "Welcome to ElevenClock": "",
    "Skip": "",
    "Start": "",
    "Next": "",
    "Finish": "",
}

lang_2_9 = lang_2_9_2 | {
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
    "Force the clock to be at the top of the screen": "Forza l'orologio ad essere nella parte superiore dello schermo",
    "Show the clock on the primary screen": "Mostra l'orologio sullo schermo principale",
    "Use a custom font color": "Usa un colore personalizzato per il font",
    "Use a custom background color": "Usa un colore personalizzato per lo sfondo",
    "Align the clock text to the center": "Allinea il testo dell'orologio al centro",
    "Select custom color": "Seleziona un colore personalizzato",
    "Hide the clock when a program occupies all screens": "Nascondi l'orologio quando un programma occupa tutte le schermate",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "Usa un font personalizzato",
    "Use a custom font size": "Usa una dimensione del font personalizzata",
    "Enable hide when multi-monitor fullscreen apps are running": "Abilita Nascondi quando sono in esecuzione app a schermo intero multi-monitor",
    "<b>{0}</b> needs to be enabled to change this setting": "<b>{0}</b> deve essere abilitato per modificare questa impostazione",
    "<b>{0}</b> needs to be disabled to change this setting": "<b>{0}</b> deve essere disabilitato per modificare questa impostazione",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": "(Questa funzionalità è stata disabilitata perchè dovrebbe funzionare di default. Se non funziona, segnala un bug)",
    "ElevenClock's language": "Lingua di ElevenClock"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Circa Qt6 (PySide6)",
    "About": "Circa",
    "Alternative non-SSL update server (This might help with SSL errors)": "Server di aggiornamento non SSL alternativo (potrebbe aiutare con gli errori SSL)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Correzioni e altre funzionalità sperimentali: (Usale SOLO se qualcosa non funziona)",
    "Show week number on the clock": "Mostra il numero della settimana",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Nascondi l'orologio quando RDP Client o Citrix Workspace sono in esecuzione",
    "Clock Appearance:": "Aspetto dell'orlogio",
    "Force the clock to have black text": "Forza l'orologio ad avere il testo scuro",
    " - It is required that the Dark Text checkbox is disabled": "È richiesto che la casella Testo Scuro sia disabilitata",
    "Debbugging information:": "Informazioni di debug",
    "Open ElevenClock's log": "Apri i log di ElevenClock",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Mostra l'orologio sullo schermo principale (Utile se l'orologio è impostato a sinistra)",
    "Show weekday on the clock"  :"Visualizza il giorno della settimana",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"Impostazioni ElevenClock", # Also settings title
    "Reload Clocks"             :"Ricarica",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"Riavvia ElevenClock",
    "Hide ElevenClock"          :"Nascondi ElevenClock",
    "Quit ElevenClock"          :"Esci",
    
    #General settings section
    "General Settings:"                                                                 :"Impostazioni generali:",
    "Automatically check for updates"                                                   :"Rileva automaticamente gli aggiornamenti",
    "Automatically install available updates"                                           :"Installa automaticamente gli aggiornamenti",
    "Enable really silent updates"                                                      :"Abilita aggiornamenti silenziosi",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Ignora il controllo di autenticità del provider di aggiornamento (NON RACCOMANDATO, A TUO RISCHIO)",
    "Show ElevenClock on system tray"                                                   :"Visualizza ElevenClock sulla barra di sistema",
    "Alternative clock alignment (may not work)"                                        :"Allineamento alternativo dell'orologio (potrebbe non funzionare)",
    "Change startup behaviour"                                                          :"Cambia il comportamento in avvio",
    "Change"                                                                            :"Cambia",
    "<b>Update to the latest version!</b>"                                             :"<b>Aggiorna all'ultima versione!</b>",
    "Install update"                                                                    :"Installa l'aggiornamento",
    
    #Clock settings
    "Clock Settings:"                                              :"Impostazioni orologio:",
    "Hide the clock in fullscreen mode"                            :"Nascondi l'orologio in modalità a schermo intero",
    "Hide the clock when RDP client is active"                     :"Nascondi l'orologio quando il client RDP è attivo",
    "Force the clock to be at the bottom of the screen"            :"Forza l'orologio ad essere al fondo dello schermo",
    "Show the clock when the taskbar is set to hide automatically" :"Visualizza l'orologio quando la barra delle applicazioni è impostata a Nascondi",
    "Fix the hyphen/dash showing over the month"                   :"Corregge la visualizzazione del trattino sul mese",
    "Force the clock to have white text"                           :"Forza l'orologio ad usare testo bianco",
    "Show the clock at the left of the screen"                     :"Visualizza l'orologio alla sinistra dello schermo",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Impostazioni data e Ora:",
    "Show seconds on the clock"                         :"Visualizza i secondi",
    "Show date on the clock"                            :"Visualizza la data",
    "Show time on the clock"                            :"Visualizza l'ora",
    "Change date and time format (Regional settings)"   :"Cambia il formato di visualizzazione della data e dell'ora (Impostazioni regionali)",
    "Regional settings"                                 :"Impostazioni regionali",
    
    #About the language pack
    "About the language pack:"                  :"Informazioni sulla traduzione",
    "Translated to English by martinet101"      :"Tradotto in Italiano da Parapongo, zuidstroopwafel", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Traduci ElevenClock nella tua lingua",
    "Get started"                               :"Inizia",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Informazioni sulla versione {0} di ElevenClock",
    "View ElevenClock's homepage"               :"Visualizza l'homepage di ElevenClock",
    "Open"                                      :"Apri",
    "Report an issue/request a feature"         :"Segnala un problema/richiedi una nuova funzionalità",
    "Report"                                    :"Segnala",
    "Support the dev: Give me a coffee☕"       :"Supporta lo sviluppatore: donami un caffè☕",
    "Open page"                                 :"Apri la pagina",
    "Icons by Icons8"                           :"Icone tratte da Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Pagina Web",
    "Close settings"                            :"Chiudi le impostazioni",
    "Close"                                     :"Chiudi",
}

lang = lang2_3
