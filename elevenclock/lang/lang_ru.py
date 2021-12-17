# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_2_9 = {
    "Task Manager": "Диспетчер задач",
    "Change date and time": "Сменить дату и время",
    "Notification settings": "Настройки уведомлений",
    "Updates, icon tray, language": "Обновления, иконка трея, язык",
    "Hide extended options from the clock right-click menu (needs a restart to be aplied)": "Не отображать расширенное меню по правому клику мыши (нужен перезапуск)",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "Поведение при работы с полноэкранными приложениями, позиционирование, разное",
    'Add the "Show Desktop" button on the left corner of every clock': 'Отображать кнопку "Показать рабочий стол" в левом углу всех часов',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': 'Вам придется выбрать свой цвет фона, чтобы это работало.&nbsp;Больше информации <a href="{0}" style="color:DodgerBlue">здесь</a>',
    "Clock's font, font size, font color and background, text alignment": "Настройки шрифта, размера шрифта, цвета, выравнивание",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "Формат даты, формат времени, секунды, дни недели, номер недели, региональные настройки",
    "Testing features and error-fixing tools": "Исправления проблем и тестирование новых возможностей",
    "Language pack author(s), help translating ElevenClock": "Авторы переводов, помощь при переводе",
    "Info, report a bug, submit a feature request, donate, about": "Больше информации, создать баг, предложить функцию, подкинуть на расходы",
    "Log, debugging information": "Логи, ифнормация для дебага",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen": "Отображать часы в верхней части экрана",
    "Show the clock on the primary screen": "Отображать часы на главном мониторе",
    "Use a custom font color": "Сменить цвет шрифта",
    "Use a custom background color": "Сменить цвет фона",
    "Align the clock text to the center": "Выровнять текст по центру",
    "Select custom color": "Выберите цвет",
    "Hide the clock when a program occupies all screens": "Скрывать, когда программа занимает все экраны",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "Сменить шрифт",
    "Use a custom font size": "Сменить размер шрифта",
    "Enable hide when multi-monitor fullscreen apps are running": "Скрывать при запущенном приложении, которое развернуто на все мониторы",
    "<b>{0}</b> needs to be enabled to change this setting": "Включите <b>{0}</b>, чтобы изменить это",
    "<b>{0}</b> needs to be disabled to change this setting": "Отключите <b>{0}</b>, чтобы изменить это",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": " (Эта настройка отключена, так как она должна работать по умолчанию. В противном случае откройте баг)",
    "ElevenClock's language": "Язык ElevenClock"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "О Qt6 (PySide6)",
    "About": "О приложении",
    "Alternative non-SSL update server (This might help with SSL errors)": "Сервер обновлений без SSL (если есть ошибки SSL)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Исправления/экспериментальные возможности: (Используйте, если ТОЛЬКО что-то не работает)",
    "Show week number on the clock": "Отображать номер недели",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Скрывать часы при открытом RDP клиенте или Citrix Workspace",
    "Clock Appearance:": "Внешний вид часов",
    "Force the clock to have black text": "Принудительно Темный Цвет текста",
    " - It is required that the Dark Text checkbox is disabled": " - Необходимо, чтобы настройка Темный Цвет была выключена",
    "Debbugging information:": "Информация для дебага",
    "Open ElevenClock's log": "Открыть логи ElevenClock",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Отображать на главном экране (полезно, если часы выставить слева)",
    "Show weekday on the clock"  :"Отображать день недели",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"Настройки ElevenClock", # Also settings title
    "Reload Clocks"             :"Перезагрузить часы",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"Перезапустить ElevenClock",
    "Hide ElevenClock"          :"Скрыть ElevenClock",
    "Quit ElevenClock"          :"Выйти из ElevenClock",
    
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
    "<b>Update to the latest version!</b>"                                              :"Обновить до последней версии!",
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
    "Translated to English by martinet101"      :"Перевод на русский: Иван (Risen), Кирилл (kira)", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Переведите ElevenClock на свой язык",
    "Get started"                               :"Начать",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"О ElevenClock version {0}:",
    "View ElevenClock's homepage"               :"Посетить сайт ElevenClock",
    "Open"                                      :"Открыть",
    "Report an issue/request a feature"         :"Сообщить о проблеме / запросить функцию",
    "Report"                                    :"Отчет",
    "Support the dev: Give me a coffee☕"       :"Поддержать разработчика чашечкой кофе☕",
    "Open page"                                 :"Открыть страницу",
    "Icons by Icons8"                           :"Иконки от Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Страница в Интернете",
    "Close settings"                            :"Закрыть настройки",
    "Close"                                     :"Закрыть",
}

lang = lang2_3
