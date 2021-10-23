# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang2_4 = {
    # Added text in version 2.4
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
    "Show ElevenClock on system tray"                                                   :"",
    "Alternative clock alignment (may not work)"                                        :"",
    "Change startup behaviour"                                                          :"",
    "Change"                                                                            :"",
    "<b>Update to the lastest version!</b>"                                             :"",
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