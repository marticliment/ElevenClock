# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang2_5 = {
    "Hide the clock when RDP Client or Citrix Workspace are running": "",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "",
    "Show weekday on the clock"  :"",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"Настройки ElevenClock", # Also settings title
    "Reload Clocks"             :"Перезагрузить часы",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"Перезапустить ElevenClock",
    "Hide ElevenClock"          :"Скрыть ElevenClock",
    "Quit ElevenClock"          :"Выход ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Основные настройки",
    "Automatically check for updates"                                                   :"Автоматически проверять обновления",
    "Automatically install available updates"                                           :"Автоматически устанавливать доступные обновления",
    "Enable really silent updates"                                                      :"Обновлять без предупреждения",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Не проверять подлинность поставщика обновлений (НЕ РЕКОМЕНДУЕТСЯ, НА ВАШ СТРАХ И РИСК)",
    "Show ElevenClock on system tray"                                                   :"Показать ElevenClock на панели задач",
    "Alternative clock alignment (may not work)"                                        :"Синхронизация часов с альтернативным сервером (может не работать)",
    "Change startup behaviour"                                                          :"Настройка запуска",
    "Change"                                                                            :"Изменить",
    "<b>Update to the lastest version!</b>"                                             :"Обновить до последней версии!",
    "Install update"                                                                    :"Установить обновление",
    
    #Clock settings
    "Clock Settings:"                                              :"Настройки часов",
    "Hide the clock in fullscreen mode"                            :"Скрыть часы в полноэкранном режиме",
    "Hide the clock when RDP client is active"                     :"Скрыть часы при работе с RDP-клиентом",
    "Force the clock to be at the bottom of the screen"            :"Установить часы в нижней части экрана",
    "Show the clock when the taskbar is set to hide automatically" :"Показывать часы, когда панель задач настроена на автоматическое скрытие",
    "Fix the hyphen/dash showing over the month"                   :"Изменить дефис / тире при отображении месяца",
    "Force the clock to have white text"                           :"Включить белый цвет часов",
    "Show the clock at the left of the screen"                     :"Показать часы в левой части экрана",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Настройки времени и даты",
    "Show seconds on the clock"                         :"Показывать секунды",
    "Show date on the clock"                            :"Показывать дату",
    "Show time on the clock"                            :"Показывать время",
    "Change date and time format (Regional settings)"   :"Изменить формат даты и времени (региональные настройки)",
    "Regional settings"                                 :"Региональные настройки",
    
    #About the language pack
    "About the language pack:"                  :"О языковом пакете",
    "Translated to English by martinet101"      :"Перевод на русский: Иван (Risen)", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Переведите ElevenClock на свой язык",
    "Get started"                               :"Начать",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"О ElevenClock version {0}:",
    "View ElevenClock's homepage"               :"Посетать сайт ElevenClock",
    "Open"                                      :"Открыть",
    "Report an issue/request a feature"         :"Сообщить о проблеме / запросить функцию",
    "Report"                                    :"Отчет",
    "Support the dev: Give me a coffee☕"       :"Поддержать разработчика ",
    "Open page"                                 :"Открыть страницу",
    "Icons by Icons8"                           :"Иконки от Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Страница в Интернете",
    "Close settings"                            :"Закрыть настройки",
    "Close"                                     :"Закрыть",
}

lang = lang2_3