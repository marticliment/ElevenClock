# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"

# So it would look like: "ORIGINAL_TEXT" : "TRANSLATED_TEXT",


# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_3_2 = {
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
    "Force the clock to be at the top of the screen": "קבע תצוגת שעון בחלק העליון של המסך",
    "Show the clock on the primary screen": "הצג שעון במסך הראשי",
    "Use a custom font color": "קביעת צבע גופן",
    "Use a custom background color": "קביעת צבע לרקע השעון",
    "Align the clock text to the center": "מרכז את טקסט השעון",
    "Select custom color": "בחר צבע",
    "Hide the clock when a program occupies all screens": "הסתר את השעון כאשר תוכנה תופסת את כל המסכים",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "בחר סוג גופן",
    "Use a custom font size": "בחר גודל גופן",
    "Enable hide when multi-monitor fullscreen apps are running": "הפעל הסתרת שעון, כאשר אפליקציות מסך מלא בריבוי מסכים פועלת",
    "<b>{0}</b> needs to be enabled to change this setting": "<b>{0}</b> חייב להיות פעיל, על מנת לשנות הגדרה זאת",
    "<b>{0}</b> needs to be disabled to change this setting": "<b>{0}</b> חייב להיות כבוי, על מנת לשנות הגדרה זאת",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": "(פיצ'ר זה מכובה, אמור לפעול כברירת מחדל. אם לא, בבקשה לדווח על תקלה)",
    "ElevenClock's language": "ElevenClock's שפה"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "אודות Qt6 (PySide6)",
    "About": "אודות",
    "Alternative non-SSL update server (This might help with SSL errors)": "עדכון שרת חליפי non-SSL (יכול לעזור עם בעיות SSL)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "תיקונים ופיצ'רים ניסיוניים (השתשמש רק אם משהו לא עובד)",
    "Show week number on the clock": "הצג מספר שבוע עם השעון"
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "החבא שעון כאשר RDP Client או Citrix Workspace מופעלים",
    "Clock Appearance:": "נראות שעון",
    "Force the clock to have black text": "קבע צבע טקסט שעון לשחור",
    " - It is required that the Dark Text checkbox is disabled": "תיבת טקסט כהה חייבת להיות כבויה בשביל פעולה זאת",
    "Debbugging information:": "מידע על איתור באגים",
    "Open ElevenClock's log": "פתח לוג ElevenClock's",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "הצג שעון במסך מרכזי (יעיל במצב שהשעון מוגדר על צד שמאל)",
    "Show weekday on the clock"  :"הצג מספר שבוע בשעון",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"ElevenClock הגדרות", # Also settings title
    "Reload Clocks"             :"טען שעונים",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"ElevenClock הפעל מחדש",
    "Hide ElevenClock"          :"ElevenClock הסתר",
    "Quit ElevenClock"          :"ElevenClock יציאה",
    
    #General settings section
    "General Settings:"                                                                 :"הגדרות כלליות",
    "Automatically check for updates"                                                   :"בדוק עדכונים באופן אוטומטי",
    "Automatically install available updates"                                           :"התקן עדכונים זמינים באופן אוטומטי",
    "Enable really silent updates"                                                      :"הפעל עדכונים שקטים",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"עקוף בדיקת תאימות עדכון (לא מומלץ, על אחריות המשתמש בלבד)",
    "Show ElevenClock on system tray"                                                   :"הצג שעון בפינת סרגל המשימות",
    "Alternative clock alignment (may not work)"                                        :"יישור חלופי לשעון (יכול לא לעבוד)",
    "Change startup behaviour"                                                          :"שנה הגדרת התנהגות באתחול",
    "Change"                                                                            :"שנה",
    "<b>Update to the latest version!</b>"                                             :"עדכן לגרסה האחרונה",
    "Install update"                                                                    :"התקן עדכון",
    
    #Clock settings
    "Clock Settings:"                                              :"הגדרות שעון",
    "Hide the clock in fullscreen mode"                            :"החבא שעון במצב מסך מלא",
    "Hide the clock when RDP client is active"                     :"החבא שעון כאשר RDP client פעיל",
    "Force the clock to be at the bottom of the screen"            :"קבע תצוגת שעון בחלק תחתון של המסך",
    "Show the clock when the taskbar is set to hide automatically" :"הצג שעון כאשר שורת משימות מוסרת באופן אוטומטי",
    "Fix the hyphen/dash showing over the month"                   :"תקן מקף שמופיע מעל החודש",
    "Force the clock to have white text"                           :"קבע צבע טקסט שעון ללבן",
    "Show the clock at the left of the screen"                     :"הצג שעון בצד השמאלי של המסך",
    
    #Date & time settings
    "Date & Time Settings:"                             :"הגדרת תאריך ושעה",
    "Show seconds on the clock"                         :"הצג שניות בשעון",
    "Show date on the clock"                            :"הצג תאריך בשעון",
    "Show time on the clock"                            :"הצג שעה בשעון",
    "Change date and time format (Regional settings)"   :"שנה את פורמט התאריך והשעה (הגדרת איזור)",
    "Regional settings"                                 :"הגדרת איזור",
    
    #About the language pack
    "About the language pack:"                  :"אודות ערכת שפות",
    "Translated to English by martinet101"      :"תורגם לעברית על ידי xRLx", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"תרגם ElevenClock לשפה שלך ",
    "Get started"                               :"התחל לתרגם",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"אודות גרסה ElevenClock",
    "View ElevenClock's homepage"               :"הצג דף אינטרנט ElevenClock",
    "Open"                                      :"פתח",
    "Report an issue/request a feature"         :"דווח על בעיה\בקשה",
    "Report"                                    :"דווח",
    "Support the dev: Give me a coffee☕"       :"תמיכה במפתח: תזמין אותי לכוס קפה☕",
    "Open page"                                 :"פתח עמוד",
    "Icons by Icons8"                           :"אייקונים נוצרו על ידי Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"עמוד אינטרנט",
    "Close settings"                            :"סגור הגדרות",
    "Close"                                     :"סגור",
}

lang = lang2_3
