# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_3 = {
    "Custom format rules:": "",
    "Any text can be placed here. To place items such as date and time, please use the 1989 C standard. More info on the following link": "",
    "Python Date and time values": "",
    "To disable the zero-padding effect, add a # in bethwwn the % and the code: non-zero-padded hours would be %#H, and zero-padded hours would be %H": "", # Here please don't modify the %H and %#H values
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
    "Open online help to troubleshoot problems": "",
    "Reset ElevenClock preferences to defaults": "",
    "Specify a minimum width for the clock": "",
    "Search on the settings": "",
    "No results were found": "",
}

lang_3_2 = lang_3_2_1 | {
    "Use system accent color as background color": "",
    "Check only the focused window on the fullscreen check": "",
    "Clock on monitor {0}": "",
    "Move to the left": "",
    "Show this clock on the left": "",
    "Show this clock on the right": "",
    "Restore clock position": "",
}

lang_3_1 = lang_3_2 | {
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
    "Force the clock to be at the top of the screen": "Forçar o relógio a ficar no topo do ecrã",
    "Show the clock on the primary screen": "Mostrar relógio no ecrã principal",
    "Use a custom font color": "Mudar cor do texto",
    "Use a custom background color": "Mudar cor do fundo do relógio",
    "Align the clock text to the center": "Alinhar o texto do relógio ao centro",
    "Select custom color": "Escolher cor",
    "Hide the clock when a program occupies all screens": "Esconder relógio quando um programa ocupa todos os ecrãs",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "Mudar tipo de letra",
    "Use a custom font size": "Mudar tamanho da letra",
    "Enable hide when multi-monitor fullscreen apps are running": "Esconder relógio quando aplicações multi-monitor estiverem em execução",
    "<b>{0}</b> needs to be enabled to change this setting": "A opção <b>{0}</b> precisa de estar ativada para mudar esta definição",
    "<b>{0}</b> needs to be disabled to change this setting": "A opção <b>{0}</b> precisa de estar desativada para mudar esta definição",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": "  (Funcionalidade desativada porque deve funcionar por predefinição. Caso não funcione, reporte o problema",
    "ElevenClock's language": "Idioma ElevenClock"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Acerca de Qt6 (PySide6)",
    "About": "Acerca de",
    "Alternative non-SSL update server (This might help with SSL errors)": "Servidor de atualização alternativo sem SSL (Pode ajudar com erros de SSL)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Correções e funcionalidades experimentais: (Usar APENAS se algo não funcionar corretamente)",
    "Show week number on the clock": "Mostrar dia da semana no relógio"
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Esconder as horas quando o Ambiente de Trabalho Remoto ou o Citrix Workspace estiverem em execução",
    "Clock Appearance:": "Aspeto do relógio",
    "Force the clock to have black text": "Forçar a cor do relógio a preto",
    " - It is required that the Dark Text checkbox is disabled": " - É necessário que a opção acima esteja desativada",
    "Debbugging information:": "Informação de depuração:",
    "Open ElevenClock's log": "Abrir registo de eventos do ElevenClock",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Mostrar o relógio no ecrã principal (Útil se o relógio estiver definido para aparecer à esquerda)",
    "Show weekday on the clock"  :"Mostrar o dia da semana no relógio",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"Definições ElevenClock", # Also settings title
    "Reload Clocks"             :"Reiniciar relógios",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"Reiniciar ElevenClock",
    "Hide ElevenClock"          :"Esconder ElevenClock",
    "Quit ElevenClock"          :"Sair do ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Definições Gerais:",
    "Automatically check for updates"                                                   :"Procurar atualizações automaticamente",
    "Automatically install available updates"                                           :"Instalar atualizações automaticamente",
    "Enable really silent updates"                                                      :"Ligar atualizações silenciosas",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Não verificar integridade da atualização (NÃO RECOMENDADO, POR SUA CONTA E RISCO)",
    "Show ElevenClock on system tray"                                                   :"Mostrar ElevenClock na área de notificação",
    "Alternative clock alignment (may not work)"                                        :"Alinhamento alternativo (pode não funcionar)",
    "Change startup behaviour"                                                          :"Mudar comportamento de arranque",
    "Change"                                                                            :"Definições",
    "<b>Update to the latest version!</b>"                                             :"<b>Atualize para a versão mais recente!</b>",
    "Install update"                                                                    :"Instalar atualização",
    
    #Clock settings
    "Clock Settings:"                                              :"Definições do relógio:",
    "Hide the clock in fullscreen mode"                            :"Esconder o relógio quando em modo de ecrã inteiro",
    "Hide the clock when RDP client is active"                     :"Esconder o relógio quando o Ambiente de Trabalho Remoto estiver a ser usado",
    "Force the clock to be at the bottom of the screen"            :"Forçar o relógio a ficar na parte de baixo do ecrã",
    "Show the clock when the taskbar is set to hide automatically" :"Mostrar o relógio quando a barra de tarefas estiver definida para se esconder automaticamente",
    "Fix the hyphen/dash showing over the month"                   :"Corrigir problema onde aparece um hífen/traço em cima do mês",
    "Force the clock to have white text"                           :"Forçar a cor do relógio a branco",
    "Show the clock at the left of the screen"                     :"Mostrar relógio à esquerda do ecrã",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Definições de Data e Hora:",
    "Show seconds on the clock"                         :"Mostrar segundos no relógio",
    "Show date on the clock"                            :"Mostrar a data no relógio",
    "Show time on the clock"                            :"Mostrar as horas no relógio",
    "Change date and time format (Regional settings)"   :"Mudar formato de data e hora (Formato Regional)",
    "Regional settings"                                 :"Definições",
    
    #About the language pack
    "About the language pack:"                  :"Acerca do pacote de idiomas:",
    "Translated to English by martinet101"      :"Traduzido para Português por jmlcoliveira", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Traduz o ElevenClock para o teu idioma",
    "Get started"                               :"Traduzir",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Acerca de ElevenClock versão {0}:",
    "View ElevenClock's homepage"               :"Ver página inicial do ElevenClock",
    "Open"                                      :"Abrir",
    "Report an issue/request a feature"         :"Reportar um problema/pedir uma funcionalidade",
    "Report"                                    :"Reportar",
    "Support the dev: Give me a coffee☕"       :"Apoia o desenvolvedor: Compra-me um café☕",
    "Open page"                                 :"Abrir página",
    "Icons by Icons8"                           :"Ícones por Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Website",
    "Close settings"                            :"Fechar definições",
    "Close"                                     :"Fechar",
}

lang = lang2_3
