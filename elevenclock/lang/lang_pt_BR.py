# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3 = {
    "Hide the clock during 10 seconds when clicked": "Esconder o relógio durante 10 segundos quando clicado",
    "Enable low-cpu mode": "Habilitar modo de baixo consumo de cpu",
    "You might lose functionalities, like the notification counter or the dynamic background": "Você pode perder funcionalidades, como o contador de notificações ou o plano de fundo dinâmico",
    "Clock position and size:": "Posição e tamanho do relógio:",
    "Clock size preferences, position offset, clock at the left, etc.": "Preferências de tamanho do relógio, deslocamento de posição, relógio à esquerda, etc.",
    "Reset monitor blacklisting status": "Redefinir o status do monitor da lista negra",
    "Reset": "Resetar",
    "Third party licenses": "Licenças de terceiros",
    "View": "Visualizar",
    "ElevenClock": "ElevenClock",
    "Monitor tools": "Ferramentas do monitor",
    "Blacklist this monitor": "Colocar monitor em lista negra",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "Software de código aberto de terceiros no Elevenclock {0} (e suas licenças)",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "ElevenClock é um aplicativo de código aberto feito com a ajuda de outras bibliotecas feitas pela comunidade:",
    "Ok": "Ok",
    "More Info": "Mais informações",
    "About Qt": "Sobre o Qt",
    "Success": "Sucesso",
    "The monitors were unblacklisted successfully.": "Os monitores foram retirados da lista negra com sucesso.",
    "Now you should see the clock everywhere": "Agora você deve conseguir visualizar o relógio em todos os monitores",
    "Ok": "Ok",
    "Blacklist Monitor": "Lista Negra de Monitor",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "Colocar um monitor na lista negra ocultará o relógio neste monitor permanentemente.",
    "This action can be reverted from the settings window. under <b>Clock position and size</b>": "Esta ação pode ser revertida na janela de configurações. Em <b>Posição e tamanho do relógio</b>",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "Você tem certeza que deseja colocar o monitor \"{0}\" na lista negra?",
    "Yes": "Sim",
    "No": "Não",
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
    "Task Manager": "Gerenciador de Tarefas",
    "Change date and time": "Alterar Data e Hora",
    "Notification settings": "Configurações de Notificação",
    "Updates, icon tray, language": "Atualizações, bandeja de ícones, idioma",
    "Hide extended options from the clock right-click menu (needs a restart to be aplied)": "Ocultar opções avançadas do menu ao clicar com o botão direito do mouse (é necessário reiniciar para ser aplicado)",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "Comportamento em tela cheia, posição do relógio, relógio do monitor principal, outras configurações",
    'Add the "Show Desktop" button on the left corner of every clock': 'Adicione o botão "Mostrar área de trabalho" no canto esquerdo de cada relógio',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': 'Pode ser necessário definir uma cor de fundo personalizada para que isso funcione. &nbsp;Mais informações <a href="{0}" style="color:DodgerBlue">CLIQUE AQUI</a>',
    "Clock's font, font size, font color and background, text alignment": "Fonte do relógio, tamanho da fonte, cor e fundo da fonte, alinhamento do texto",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "Formato de data, formato de hora, segundos, dia da semana, número da semana, configurações regionais",
    "Testing features and error-fixing tools": "Recursos de teste e ferramentas de correção de erros",
    "Language pack author(s), help translating ElevenClock": "Autor(es) do pacote de idiomas, ajuda na tradução do ElevenClock",
    "Info, report a bug, submit a feature request, donate, about": "Informações, relatar bugs, enviar uma solicitação de recurso, doar, sobre",
    "Log, debugging information": "Registro, informações de depuração",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen": "Force the clock to be at the top of the screen",
    "Show the clock on the primary screen": "Mostra o relógio na tela principal",
    "Use a custom font color": "Use uma cor de fonte personalizada",
    "Use a custom background color": "Use uma cor de fundo personalizada",
    "Align the clock text to the center": "Alinhar o texto do relógio ao centro",
    "Select custom color": "Selecione uma cor personalizada",
    "Hide the clock when a program occupies all screens": "Esconder o relógio quando um programa ocupar todas as telas",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "Alterar o tipo da fonte",
    "Use a custom font size": "Alterar o tamanho da fonte",
    "Enable hide when multi-monitor fullscreen apps are running": "Esconder o relógio quando aplicações multi-telas estiverem em execução",
    "<b>{0}</b> needs to be enabled to change this setting": "A opção <b>{0}</b> precisa de estar ativada para mudar esta definição",
    "<b>{0}</b> needs to be disabled to change this setting": "A opção <b>{0}</b> precisa de estar desativada para mudar esta definição",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": " (Funcionalidade desativada porque deve funcionar por predefinição. Caso não funcione, reporte o problema",
    "ElevenClock's language": "Idioma ElevenClock"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Acerca de Qt6 (PySide6)",
    "About": "Sobre",
    "Alternative non-SSL update server (This might help with SSL errors)": "Servidor de atualização alternativo sem SSL (Pode ajudar com erros de SSL)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Correções e funcionalidades experimentais: (Usar APENAS se algo não funcionar corretamente)",
    "Show week number on the clock": "Mostrar dia da semana no relógio"
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Esconder as horas quando o Ambiente de Trabalho Remoto ou o Citrix Workspace estiverem em execução",
    "Clock Appearance:": "Aparência do relógio",
    "Force the clock to have black text": "Forçar a cor preta para o relógio",
    " - It is required that the Dark Text checkbox is disabled": " - É necessário que a opção acima esteja desativada",
    "Debbugging information:": "Informação de depuração:",
    "Open ElevenClock's log": "Abrir registro de eventos do ElevenClock",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Mostrar o relógio na tela principal (Útil se o relógio estiver definido para aparecer à esquerda)",
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
    "Change startup behaviour"                                                          :"Mudar comportamento de inicialização",
    "Change"                                                                            :"Definições",
    "<b>Update to the latest version!</b>"                                             :"<b>Atualize para a versão mais recente!</b>",
    "Install update"                                                                    :"Instalar atualização",
    
    #Clock settings
    "Clock Settings:"                                              :"Definições do relógio:",
    "Hide the clock in fullscreen mode"                            :"Esconder o relógio quando estiver em tela cheia",
    "Hide the clock when RDP client is active"                     :"Esconder o relógio quando o Ambiente de Trabalho Remoto estiver sendo usado",
    "Force the clock to be at the bottom of the screen"            :"Forçar o relógio a ficar na parte de baixo da tela",
    "Show the clock when the taskbar is set to hide automatically" :"Mostrar o relógio quando a barra de tarefas estiver definida para se esconder automaticamente",
    "Fix the hyphen/dash showing over the month"                   :"Corrigir problema onde aparece um hífen/traço em cima do mês",
    "Force the clock to have white text"                           :"Forçar a cor branca para o relógio",
    "Show the clock at the left of the screen"                     :"Mostrar relógio à esquerda da tela",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Definições de Data e Hora:",
    "Show seconds on the clock"                         :"Mostrar segundos no relógio",
    "Show date on the clock"                            :"Mostrar a data no relógio",
    "Show time on the clock"                            :"Mostrar as horas no relógio",
    "Change date and time format (Regional settings)"   :"Mudar formato de data e hora (Formato Regional)",
    "Regional settings"                                 :"Definições",
    
    #About the language pack
    "About the language pack:"                  :"Sobre o pacote de idiomas:",
    "Translated to English by martinet101"      :"Traduzido para Português do Brasil por Wanderlei Hüttel", # Here, make sure to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Traduzir o ElevenClock para o seu idioma",
    "Get started"                               :"Traduzir",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Sobre a versão {0} do ElevenClock:",
    "View ElevenClock's homepage"               :"Ver página inicial do ElevenClock",
    "Open"                                      :"Abrir",
    "Report an issue/request a feature"         :"Reportar um problema/solicitar uma funcionalidade",
    "Report"                                    :"Reportar",
    "Support the dev: Give me a coffee☕"       :"Apoiar o desenvolvedor: Me pague um café☕",
    "Open page"                                 :"Abrir página",
    "Icons by Icons8"                           :"Ícones por Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Website",
    "Close settings"                            :"Fechar definições",
    "Close"                                     :"Fechar",
}

lang = lang2_3
