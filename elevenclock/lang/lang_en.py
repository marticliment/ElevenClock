# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
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
    "This action can be reverted from the settings window. under <b>Clock position and size</b>": "This action can be reverted from the settings window, under <b>Clock position and size</b>",
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
    "Hide extended options from the clock right-click menu (needs a restart to be aplied)": "Hide extended options from the clock right-click menu (needs a restart to be applied)",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "",
    'Add the "Show Desktop" button on the left corner of every clock': '',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': '',
    "Clock's font, font size, font color and background, text alignment": "",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "Date format, Time format, seconds, weekday, weeknumber, regional settings",
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
    "ElevenClock Settings"      :"", # Also settings title
    "Reload Clocks"             :"",
    "ElevenClock v{0}"          :"",
    "Restart ElevenClock"       :"",
    "Hide ElevenClock"          :"",
    "Quit ElevenClock"          :"",
    
    #General settings section
    "General Settings:"                                                                 :"",
    "Automatically check for updates"                                                   :"",
    "Automatically install available updates"                                           :"",
    "Enable really silent updates"                                                      :"",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"",
    "Show ElevenClock on system tray"                                                   :"Show ElevenClock icon on system tray",
    "Alternative clock alignment (may not work)"                                        :"",
    "Change startup behaviour"                                                          :"",
    "Change"                                                                            :"",
    "<b>Update to the latest version!</b>"                                             :"",
    "Install update"                                                                    :"",
    
    #Clock settings
    "Clock Settings:"                                              :"",
    "Hide the clock in fullscreen mode"                            :"",
    "Hide the clock when RDP client is active"                     :"",
    "Force the clock to be at the bottom of the screen"            :"",
    "Show the clock when the taskbar is set to hide automatically" :"",
    "Fix the hyphen/dash showing over the month"                   :"",
    "Force the clock to have white text"                           :"",
    "Show the clock at the left of the screen"                     :"",
    
    #Date & time settings
    "Date & Time Settings:"                             :"",
    "Show seconds on the clock"                         :"",
    "Show date on the clock"                            :"",
    "Show time on the clock"                            :"",
    "Change date and time format (Regional settings)"   :"",
    "Regional settings"                                 :"",
    
    #About the language pack
    "About the language pack:"                  :"",
    "Translated to English by martinet101"      :"", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"",
    "Get started"                               :"",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"",
    "View ElevenClock's homepage"               :"",
    "Open"                                      :"",
    "Report an issue/request a feature"         :"",
    "Report"                                    :"",
    "Support the dev: Give me a coffee☕"       :"",
    "Open page"                                 :"",
    "Icons by Icons8"                           :"", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"",
    "Close settings"                            :"",
    "Close"                                     :"",
}

lang = lang2_3
