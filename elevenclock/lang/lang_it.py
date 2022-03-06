# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}"
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_3_1 = {
    "Invalid time format\nPlease follow the\nC 1989 Standards": "",
    "Nothing to preview": "",
    "Invalid time format\nPlease modify it\nin the settings": "",
    "Disable the tooltip shown when the clock is hovered": ""
}
lang_3_3 = lang_3_3_1 | {
    "Custom format rules:": "",
    "Any text can be placed here. To place items such as date and time, please use the 1989 C standard. More info on the following link": "",
    "Python date and time formats": "",
    "To disable the zero-padding effect, add a # in between the % and the code: non-zero-padded hours would be %#H, and zero-padded hours would be %H": "", # Here please don't modify the %H and %#H values
    "Click on Apply to apply and preview the format": "",
    "Apply": "",
    "If you don't understand what is happening, please uncheck the checkbox over the text area": "",
    "Set a custom date and time format": "",
    "(for advanced users only)": "",
    "Move this clock to the left": "",
    "Move this clock to the top": "",
    "Move this clock to the right": "",
    "Move this clock to the bottom": "",
    "Restore horizontal position": "",
    "Restore vertical position": "",
}

lang_3_2_1 = lang_3_3 | {
    "Open online help to troubleshoot problems": "Apri la guida in linea per risolvere i problemi",
    "Reset ElevenClock preferences to defaults": "Ripristina le preferenze di ElevanClock per i valori predefiniti",
    "Specify a minimum width for the clock": "Specificare una larghezza minima per l'orologio",
    "Search on the settings": "Cerca sulle impostazioni",
    "No results were found": "Nessun risultato trovato",
}

lang_3_2 = lang_3_2_1 | {
    "Use system accent color as background color": "Utilizzare il colore di accento del sistema come colore di sfondo",
    "Check only the focused window on the fullscreen check": "Controllare solo la finestra focalizzata sul controllo completo",
    "Clock on monitor {0}": "Orologio sul monitor {0}",
    "Move to the left": "Passa a sinistra",
    "Show this clock on the left": "Mostra questo orologio a sinistra",
    "Show this clock on the right": "Mostra questo orologio a destra",
    "Restore clock position": "Ripristina la posizione dell'orologio",
}

lang_3_1 = lang_3_2 | {
    # The initial of the word week in your language: W for week, S for setmana, etc.
    "W": "S",
    "Disable the notification badge": "Disabilita il distintivo della notifica",
    "Override clock default height": "Override Orologio Altezza predefinita",
    "Adjust horizontal clock position": "Regola la posizione dell'orologio orizzontale",
    "Adjust vertical clock position": "Regola la posizione dell'orologio verticale",
    "Export log as a file": "Esporta log come file",
    "Copy log to clipboard": "Copia log negli Appunti",
    "Announcements:": "Annunci:",
    "Fetching latest announcement, please wait...": "Recuperando l'ultimo annuncio, per favore aspetta ...",
    "Couldn't load the announcements. Please try again later": "Non poteva caricare gli annunci. Per favore riprova più tardi",
    "ElevenClock's log": "Log ElevenClock",
    "Pick a color": "Scegli un colore"
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "Nascondi l'orologio durante 10 secondi quando cliccato",
    "Enable low-cpu mode": "Abilita la modalità a bassa cpu",
    "You might lose functionalities, like the notification counter or the dynamic background": "Potresti perdere funzionalità, come il contatore di notifica o lo sfondo dinamico",
    "Clock position and size:": "Posizione e dimensione dell'orologio:",
    "Clock size preferences, position offset, clock at the left, etc.": "Preferenze di dimensioni dell'orologio, offset di posizione, orologio a sinistra, ecc.",
    "Reset monitor blacklisting status": "Reset Monitor Blacklisting Status",
    "Reset": "Ripristina",
    "Third party licenses": "Licenze di terze parti",
    "View": "Visualizza",
    "ElevenClock": "ElevenClock",
    "Monitor tools": "Monitor strumenti",
    "Blacklist this monitor": "Blacklist questo monitor.",
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
    "This action can be reverted from the settings window, under <b>Clock position and size</b>": "",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "",
    "Yes": "",
    "No": "",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "Ricarica log",
    "Do not show the clock on secondary monitors": "Non mostrare l'orologio sui monitor secondari",
    "Disable clock taskbar background color (make clock transparent)": "Disabilita il colore dello sfondo della barra delle applicazioni dell'orologio (crea orologio trasparente)",
    "Open the welcome wizard": "Apri il wizard di benvenuto",
    " (ALPHA STAGE, MAY NOT WORK)": "(Fase alfa, potrebbe non funzionare)",
    "Welcome to ElevenClock": "Benvenuti in ElevenClock.",
    "Skip": "Salta",
    "Start": "Inizio",
    "Next": "Prossima",
    "Finish": "Fine",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "Task Manager",
    "Change date and time": "Cambia data e ora",
    "Notification settings": "Impostazioni di notifica",
    "Updates, icon tray, language": "Aggiornamenti, Icona Vassoio, Lingua",
    "Hide extended options from the clock right-click menu (needs a restart to be applied)": "Nascondi opzioni estese dal menu del tasto destro del mouse dell'orologio (ha bisogno di un riavvio da applicare)",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "Comportamento a schermo intero, posizione dell'orologio, 1 ° monitor clock, altre impostazioni miscellanee",
    'Add the "Show Desktop" button on the left corner of every clock': 'Aggiungi il pulsante "Mostra desktop" sull\'angolo sinistro di ogni orologio',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': '',
    "Clock's font, font size, font color and background, text alignment": "Carattere dell'orologio, dimensione del carattere, colore del carattere e sfondo, allineamento del testo",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "Formato data, formato orario, secondi, giorni feriali, Numero della settimana, Impostazioni regionali",
    "Testing features and error-fixing tools": "Caratteristiche di prova e strumenti di fissaggio degli errori",
    "Language pack author(s), help translating ElevenClock": "Autore del pacchetto di lingue, aiuto per la traduzioneElevenClock ",
    "Info, report a bug, submit a feature request, donate, about": "Info, segnala un bug, inviare una richiesta di funzionalità, donare, circa",
    "Log, debugging information": "Log, informazioni di debug",
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
    "Clock Appearance:": "Aspetto dell'orologio",
    "Force the clock to have black text": "Forza l'orologio ad avere il testo scuro",
    " - It is required that the Dark Text checkbox is disabled": "È richiesto che la casella Testo Scuro sia disabilitata",
    "Debbugging information:": "Informazioni di debug",
    "Open ElevenClock's log": "Apri i log di ElevenClock",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Mostra l'orologio sullo schermo principale (Utile se l'orologio è impostato a sinistra)",
    "Show weekday on the clock": "Visualizza il giorno della settimana",
}

lang2_3 = lang2_4 | {
    # Context menu
    "ElevenClock Settings": "Impostazioni ElevenClock",  # Also settings title
    "Reload Clocks": "Ricarica",
    "ElevenClock v{0}": "ElevenClock v{0}",
    "Restart ElevenClock": "Riavvia ElevenClock",
    "Hide ElevenClock": "Nascondi ElevenClock",
    "Quit ElevenClock": "Esci",

    # General settings section
    "General Settings:": "Impostazioni generali:",
    "Automatically check for updates": "Rileva automaticamente gli aggiornamenti",
    "Automatically install available updates": "Installa automaticamente gli aggiornamenti",
    "Enable really silent updates": "Abilita aggiornamenti silenziosi",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)": "Ignora il controllo di autenticità del provider di aggiornamento (NON RACCOMANDATO, A TUO RISCHIO)",
    "Show ElevenClock on system tray": "Visualizza ElevenClock sulla barra di sistema",
    "Alternative clock alignment (may not work)": "Allineamento alternativo dell'orologio (potrebbe non funzionare)",
    "Change startup behaviour": "Cambia il comportamento in avvio",
    "Change": "Cambia",
    "<b>Update to the latest version!</b>": "<b>Aggiorna all'ultima versione!</b>",
    "Install update": "Installa l'aggiornamento",

    # Clock settings
    "Clock Settings:": "Impostazioni orologio:",
    "Hide the clock in fullscreen mode": "Nascondi l'orologio in modalità a schermo intero",
    "Hide the clock when RDP client is active": "Nascondi l'orologio quando il client RDP è attivo",
    "Force the clock to be at the bottom of the screen": "Forza l'orologio ad essere al fondo dello schermo",
    "Show the clock when the taskbar is set to hide automatically": "Visualizza l'orologio quando la barra delle applicazioni è impostata a Nascondi",
    "Fix the hyphen/dash showing over the month": "Corregge la visualizzazione del trattino sul mese",
    "Force the clock to have white text": "Forza l'orologio ad usare testo bianco",
    "Show the clock at the left of the screen": "Visualizza l'orologio alla sinistra dello schermo",

    # Date & time settings
    "Date & Time Settings:": "Impostazioni data e Ora:",
    "Show seconds on the clock": "Visualizza i secondi",
    "Show date on the clock": "Visualizza la data",
    "Show time on the clock": "Visualizza l'ora",
    "Change date and time format (Regional settings)": "Cambia il formato di visualizzazione della data e dell'ora (Impostazioni regionali)",
    "Regional settings": "Impostazioni regionali",

    # About the language pack
    "About the language pack:": "Informazioni sulla traduzione",
    # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc.
    "Translated to English by martinet101": "Tradotto in Italiano da Parapongo, zuidstroopwafel",
    "Translate ElevenClock to your language": "Traduci ElevenClock nella tua lingua",
    "Get started": "Inizia",

    # About ElevenClock
    "About ElevenClock version {0}:": "Informazioni sulla versione {0} di ElevenClock",
    "View ElevenClock's homepage": "Visualizza l'homepage di ElevenClock",
    "Open": "Apri",
    "Report an issue/request a feature": "Segnala un problema/richiedi una nuova funzionalità",
    "Report": "Segnala",
    "Support the dev: Give me a coffee☕": "Supporta lo sviluppatore: donami un caffè☕",
    "Open page": "Apri la pagina",
    # Here, the word "Icons8" should not be translated
    "Icons by Icons8": "Icone tratte da Icons8",
    "Webpage": "Pagina Web",
    "Close settings": "Chiudi le impostazioni",
    "Close": "Chiudi",
}

lang = lang2_3
