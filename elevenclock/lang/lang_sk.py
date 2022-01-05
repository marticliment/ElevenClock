# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"

# So it would look like: "ORIGINAL_TEXT" : "TRANSLATED_TEXT",


# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3 = {
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
    "Force the clock to be at the top of the screen": "",
    "Show the clock on the primary screen": "",
    "Use a custom font color": "",
    "Use a custom background color": "",
    "Align the clock text to the center": "",
    "Select custom color": "",
    "Hide the clock when a program occupies all screens": "",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "",
    "Use a custom font size": "",
    "Enable hide when multi-monitor fullscreen apps are running": "",
    "<b>{0}</b> needs to be enabled to change this setting": "",
    "<b>{0}</b> needs to be disabled to change this setting": "",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": "",
    "ElevenClock's language": ""
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "",
    "About": "",
    "Alternative non-SSL update server (This might help with SSL errors)": "",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "",
    "Show week number on the clock": ""
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
    "Show weekday on the clock"  :"",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"Nastavenia ElevenClock", # Also settings title
    "Reload Clocks"             :"Obnoviť hodiny",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"Reštartovať ElevenClock",
    "Hide ElevenClock"          :"Skryť ElevenClock",
    "Quit ElevenClock"          :"Zavrieť ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Všeobecné nastavenia:",
    "Automatically check for updates"                                                   :"Automaticky vyhľadať aktualizácie",
    "Automatically install available updates"                                           :"Automaticky inštalovať aktualizácie",
    "Enable really silent updates"                                                      :"Povoliť tiché aktualizácie",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Preskočiť kontrolu autenticity aktualizácií (NEODPORÚČANÉ, NA VLASTNÚ ZODPOVEDNOSŤ)",
    "Show ElevenClock on system tray"                                                   :"Zobrazivať ElevenClock na paneli úloh",
    "Alternative clock alignment (may not work)"                                        :"Alternatívne zarovnanie hodiniek (nemusí fungovať)",
    "Change startup behaviour"                                                          :"Zmeniť správanie pri zapnutí počítača",
    "Change"                                                                            :"Zmeniť",
    "<b>Update to the latest version!</b>"                                             :"<b>Aktualizujte na najnovšiu verziu!</b>",
    "Install update"                                                                    :"Inštalovať aktualizáciu",
    
    #Clock settings
    "Clock Settings:"                                              :"Nastavenia hodiniek:",
    "Hide the clock in fullscreen mode"                            :"Skryť hodinky pri režime na celú obrazovku",
    "Hide the clock when RDP client is active"                     :"Skryť hodinky pri aktívnom RDP kliente",
    "Force the clock to be at the bottom of the screen"            :"Vynútiť hodinky byť na spodku obrazovky",
    "Show the clock when the taskbar is set to hide automatically" :"Zobrazovať hodinky, keď je panel úloh nastavený na automatické skrývanie",
    "Fix the hyphen/dash showing over the month"                   :"Opraviť pomlčku zobrazovanú cez mesiac",
    "Force the clock to have white text"                           :"Vynútiť hodinky mať biely text",
    "Show the clock at the left of the screen"                     :"Zobrazovať hodinky na ľavej strane obrazovky",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Nastavenia dátumu a času:",
    "Show seconds on the clock"                         :"Zobrazovať sekundy na hodinkách",
    "Show date on the clock"                            :"Zobrazovať dátum na hodinkách",
    "Show time on the clock"                            :"Zobrazovať čas na hodinkách",
    "Change date and time format (Regional settings)"   :"Zmeniť formát dátumu a času (Miestne nastavenia)",
    "Regional settings"                                 :"Miestne nastavenia",
    
    #About the language pack
    "About the language pack:"                  :"O jazykovom balíčku:",
    "Translated to English by martinet101"      :"Preložené do slovenčiny užívateľom metmanik", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Preložte ElevenClock do vášho jazyku",
    "Get started"                               :"Začať",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"O ElevenClock, verzia {0}:",
    "View ElevenClock's homepage"               :"Zobraziť domovskú stránku ElevenClock",
    "Open"                                      :"Otvoriť",
    "Report an issue/request a feature"         :"Nahlásiť chybu/požiadať o funkciu",
    "Report"                                    :"Nahlásiť",
    "Support the dev: Give me a coffee☕"       :"Podporte vývojára: Kúpte mi kávu ☕",
    "Open page"                                 :"Otvoriť stránku",
    "Icons by Icons8"                           :"Ikony od Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Webová stránka",
    "Close settings"                            :"Zatvoriť nastavenia",
    "Close"                                     :"Zatvoriť",
}

lang = lang2_3