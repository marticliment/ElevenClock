# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}"
#               translation ->  "Aquest text està en anglès: valor {0}"

# So it would look like: "ORIGINAL_TEXT" : "TRANSLATED_TEXT",


# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_5_0 = {
    "Tooltip Appearance:": "",
    "Tooltip's font, font size, font color and background": "",
    "Disable tooltip's blurry background": "",
    "Sync time with the internet": "",
    "Internet date and time": "",
    "Select internet time provider, change sync frequency": "",
    "Enable internet time sync": "",
    "Paste a URL from the world clock api or equivalent": "",
    "Help": "",
    "Internet sync frequency": "",
    "10 minutes": "",
    "30 minutes": "",
    "1 hour": "",
    "2 hours": "",
    "4 hours": "",
    "10 hours": "",
    "24 hours": "",
}

lang_3_4_0 = lang_3_5_0 | {
    "Show calendar": "",
    "Disabled": "",
    "Open quick settings": "",
    "Show desktop": "",
    "Open run dialog": "",
    "Open task manager": "",
    "Open start menu": "",
    "Open search menu": "",
    "Change task": "",
    "Change the action done when the clock is clicked": "",
}

lang_3_3_2 = lang_3_4_0 | {
    "ElevenClock Updater": "",
    "ElevenClock is downloading updates": "",
    "ElevenClock has updated to version {0} successfully\nPlease see GitHub for the changelog": "",
    "Customize the clock on Windows 11": "",
    "Disable the new instance checker method": "",
    "Import settings from a local file": "",
    "Export settings to a local file": "",
    "Export": "",
    "Import": "",
}

lang_3_3_1 = lang_3_3_2 | {
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
    "This action can be reverted from the settings window, under <b>Clock position and size</b>": "",
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
    "Hide extended options from the clock right-click menu (needs a restart to be applied)": "",
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
    "Force the clock to be at the top of the screen": "",
    "Show the clock on the primary screen": "",
    "Use a custom font color": "",
    "Use a custom background color": "",
    "Align the clock text to the center": "",
    "Select custom color": "",
    "Hide the clock when a program occupies all screens": "",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "Використовувати спеціальний шрифт",
    "Use a custom font size": "Використовувати спеціальний розмір шрифту",
    "Enable hide when multi-monitor fullscreen apps are running": "Приховати коли мультимоніторні повноекранні програми запущені",
    "<b>{0}</b> needs to be enabled to change this setting": "<b>{0}</b> мусить бути увімкненим щоб змінювати це налаштування",
    "<b>{0}</b> needs to be disabled to change this setting": "<b>{0}</b> мусить бути вимкненим щоб змінювати це налаштування",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": " (Ця опція була вимкнена тому, що вона має працювати за замвочуванням. Якщо вона не працює, повідомте про баг, будь ласка)",
    "ElevenClock's language": "Мова ElevenClock"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Про Qt6 (PySide6)",
    "About": "Перейти",
    "Alternative non-SSL update server (This might help with SSL errors)": "Альтернативний не-SSl сервер для оновлень (Це може допмогти при помилках SSL)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Експерементальні налаштування для виправлення помилок (Викорстовувати лише, коли щось не працює)",
    "Show week number on the clock": "Показувати номер тижня на годиннику"
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Приховувати годинник коли RDP Client або Citrix Workspace запущені",
    "Clock Appearance:": "Зовнішній вигляд годинника",
    "Force the clock to have black text": "Примусово увімкнути чорний колір шрифту годинника",
    " - It is required that the Dark Text checkbox is disabled": " - Потрібно щоб чорний колір шрифту був вимкнений",
    "Debbugging information:": "Інформація для дебагінгу",
    "Open ElevenClock's log": "Відкрити log ElevenClock",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Показувати годинник на головному екрані (Корисно коли годинник перенесений вліво)",
    "Show weekday on the clock": "Показувати день тижня на годиннику",
}

lang2_3 = lang2_4 | {
    # Context menu
    "ElevenClock Settings": "Налаштування ElevenClock",  # Also settings title
    "Reload Clocks": "Перезапусти годинник",
    "ElevenClock v{0}": "ElevenClock v{0}",
    "Restart ElevenClock": "Перезапустити ElevenClock",
    "Hide ElevenClock": "Приховати ElevenClock",
    "Quit ElevenClock": "Вийти з ElevenClock",

    # General settings section
    "General Settings:": "Загальні налаштування",
    "Automatically check for updates": "Автоматично перевіряти оновлення",
    "Automatically install available updates": "Автоматично встановлювати оновлення",
    "Enable really silent updates": "Увімкнути справді тихі оновлення",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)": "Обходити перевірку автентичності постачальника онвлень (НЕ РЕКОМЕНДОВАНО, РОБІТЬ НА ВЛАСНИЙ РИЗИК)",
    "Show ElevenClock on system tray": "Показувати ElevenClock у системному треї",
    "Alternative clock alignment (may not work)": "Альтернативне розташування годинника (Може не працювати)",
    "Change startup behaviour": "Змінити поведінку при запуску",
    "Change": "Змінити",
    "<b>Update to the latest version!</b>": "<b>Оновитися до останньої версії</b>",
    "Install update": "Установити оновлення",

    # Clock settings
    "Clock Settings:": "Налаштування годинника",
    "Hide the clock in fullscreen mode": "Приховувати годинник у повноекранному режимі",
    "Hide the clock when RDP client is active": "Приховувати годинник коли RDP клієнт активний",
    "Force the clock to be at the bottom of the screen": "Примусово перенести годинник вниз екрану",
    "Show the clock when the taskbar is set to hide automatically": "Показувати годинник коли панель завдань приховується автоматично",
    "Fix the hyphen/dash showing over the month": "Виправлення показу дефісу/тире над відображенням місяця",
    "Force the clock to have white text": "Примусово увімкнити білий колір шрифту на годиннику",
    "Show the clock at the left of the screen": "Показувати годинник зліва екрану",

    # Date & time settings
    "Date & Time Settings:": "Налаштування дати та часу",
    "Show seconds on the clock": "Показувати секунди на годиннику",
    "Show date on the clock": "Показувати дату на годиннику",
    "Show time on the clock": "Показувати час на годиннику",
    "Change date and time format (Regional settings)": "Змінити формат дати та часу(Налаштування регіону)",
    "Regional settings": "Налаштування регіону",

    # About the language pack
    "About the language pack:": "Про мовний пакет",
    "Translated to English by martinet101": "Переклав українською p4rzivalll",
    # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc.
    "Translate ElevenClock to your language": "Перекласти ElevenClock вашою мовою",
    "Get started": "Почати",

    # About ElevenClock
    "About ElevenClock version {0}:": "Про версію ElevenClock {0}",
    "View ElevenClock's homepage": "Переглянути домашню сторінку ElevenClock",
    "Open": "Відкрити",
    "Report an issue/request a feature": "Сповістити про проблему/запропонувати нову функцію",
    "Report": "Перейти",
    "Support the dev: Give me a coffee☕": "Підримати розробника",
    "Open page": "Відкрити сторінку",
    "Icons by Icons8": "Іконки від Icons8",  # Here, the word "Icons8" should not be translated
    "Webpage": "Вебсторінка",
    "Close settings": "Закрити налаштування",
    "Close": "Закрити",
}

lang = lang2_3
