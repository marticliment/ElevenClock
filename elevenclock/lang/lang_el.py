# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_3 = {
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
    "Show weekday on the clock"  :"Προβολή ημέρας της εβδομάδας στο ρολόι",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"Ρυθμίσεις ElevenClock", # Also settings title
    "Reload Clocks"             :"Επαναφόρτωση Ρολογιών",
    "ElevenClock v{0}"          :"Έκδοση ElevenClock: {0}",
    "Restart ElevenClock"       :"Επανεκκίνηση ElevenClock",
    "Hide ElevenClock"          :"Απόκρυψη ElevenClock",
    "Quit ElevenClock"          :"Τερματισμός ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Γενικές Ρυθμίσεις",
    "Automatically check for updates"                                                   :"Αυτόματος έλεγχος για ενημερώσεις",
    "Automatically install available updates"                                           :"Αυτόματη εγκατάσταση διαθέισμων ενημερώσεων",
    "Enable really silent updates"                                                      :"Ενεργοποίηση πραγματικά σιωπηλών ενημερώσεων",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Παράκαμψη ελέγχου πιστοποίησης παρόχου ενημερώσεων (ΔΕΝ ΠΡΟΤΕΊΝΕΤΑΙ, ΜΕ ΔΙΚΗ ΣΑΣ ΕΥΘΥΝΗ)",
    "Show ElevenClock on system tray"                                                   :"Προβολή του ElevenClock στη γραμμή εργασιών",
    "Alternative clock alignment (may not work)"                                        :"Εναλλακτική ευθυγράμμιση ρολογιού (ίσως να μην λειτουργεί)",
    "Change startup behaviour"                                                          :"Αλλαγή συμπεριφοράς κατά την εκκίνηση",
    "Change"                                                                            :"Αλλαγή",
    "<b>Update to the latest version!</b>"                                             :"<b>Ενημέρωση στην τελευταία έκδοση!</b>",
    "Install update"                                                                    :"Εγκατάστσαη ενημέρωσης",
    
    #Clock settings
    "Clock Settings:"                                              :"Ρυθμίσεις Ρολογιού",
    "Hide the clock in fullscreen mode"                            :"Απόκρυψη ρολογιού σε κατάσταση πλήρους οθόνης",
    "Hide the clock when RDP client is active"                     :"Απόκρυψη ρολογιού όταν χρησιμοποιείται η Απομακρυσμένη Πρόσβαση",
    "Force the clock to be at the bottom of the screen"            :"Εξαναγκασμός ρολογιού στο κάτω μέρος της οθόνης",
    "Show the clock when the taskbar is set to hide automatically" :"Προβολή ρολογιού όταν η γραμμή εργασιών είναι ορισμένη για αυτόματη απόκρυψη",
    "Fix the hyphen/dash showing over the month"                   :"Διόρθωση της καθέτου που προβάλεται πάνω από τον μήνα",
    "Force the clock to have white text"                           :"Εξαναγκασμός ρολογίου για χρήση κειμένου σε λευκό χρώμα",
    "Show the clock at the left of the screen"                     :"Προβολή ρολογιού στα αριστερά της οθόνης",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Ρυθμίσεις Ημερομηνίας & Ώρας",
    "Show seconds on the clock"                         :"Προβολή δευτερολέπτων στο ρολόι",
    "Show date on the clock"                            :"Προβολή ημερομηνίας στο ρολόι",
    "Show time on the clock"                            :"Προβολή ώρας στο ρολόι",
    "Change date and time format (Regional settings)"   :"Αλλαγή μορφής ημερομηνίας και ώρας (Τοπικές ρυθμίσεις)",
    "Regional settings"                                 :"Τοπικές ρυθμίσεις",
    
    #About the language pack
    "About the language pack:"                  :"Σχετικά με το πακέτο γλώσσας",
    "Translated to English by martinet101"      :"Μετάφραση ελληνικών από panos78", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Μεταφραση του ElevenClock στη γλώσσα σας",
    "Get started"                               :"Ξεκινήστε",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Σχετικά με την έκδοση {0} του ElevenClock:",
    "View ElevenClock's homepage"               :"Μετάβαση στην ιστοσελίδα του ElevenClock",
    "Open"                                      :"Άνοιγμα",
    "Report an issue/request a feature"         :"Αναφορά θέματος / Αίτημα χαρακτηριστικού",
    "Report"                                    :"Αναφορά",
    "Support the dev: Give me a coffee☕"       :"Υποστηρίξτε τον δημιουργό: Κεράστε τον ένα καφέ☕",
    "Open page"                                 :"Άνοιγμα σελίδας",
    "Icons by Icons8"                           :"Εικονίδια από Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Ιστοσελίδα",
    "Close settings"                            :"Κλείσιμο ρυθμίσεων",
    "Close"                                     :"Κλείσιμο",
}

lang = lang2_3
