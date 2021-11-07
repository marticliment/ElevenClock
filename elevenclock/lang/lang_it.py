# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang2_6 = {
    "About Qt6 (PySide6)": "",
    "About": "",
    "Alternative non-SSL update server (This might help with SSL errors)": "",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "",
    "Show week number on the clock": "",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "",
    "Clock Appearance:": "",
    "Force the clock to have black text": "",
    " - It is required that the Dark Text checkbox is disabled": "",
    "Debbugging information:": "",
    "Open ElevenClock's log": "",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "",
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
    "<b>Update to the lastest version!</b>"                                             :"<b>Aggiorna all'ultima versione!</b>",
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
    "Translated to English by martinet101"      :"Tradotto in Italiano da Parapongo", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
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