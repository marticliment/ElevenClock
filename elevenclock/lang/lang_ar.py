# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"

# So it would look like: "ORIGINAL_TEXT" : "TRANSLATED_TEXT",


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
    "W": "أ", # The initial of the word week in your language: W for week, S for setmana, etc.
    "Disable the notification badge": "عطل شارة الاشعارات",
    "Override clock default height": "تجاهل الارتفاع الافتراضي للساعة",
    "Adjust horizontal clock position": "ضبط وضع الساعة الأفقي",
    "Adjust vertical clock position": "ضبط وضع الساعة الرأسي",
    "Export log as a file": "تصدير السجل كملف",
    "Copy log to clipboard": "انسخ السجل الي الحافظة",
    "Announcements:": "اعلانات",
    "Fetching latest announcement, please wait...": "يأتي باحدث الاعلانات, برجاء الانتظار",
    "Couldn't load the announcements. Please try again later": "لم يستطع تحميل الاعلانات. برجاء المحاولة لاحقا",
    "ElevenClock's log": "سجل ElevenClock",
    "Pick a color": "اختر لون"
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "اخفاء الساعة خلال 10 ثوان عند النقر فوقها",
    "Enable low-cpu mode": "تفعيل وضع وحدة المعالجة المنخفضة",
    "You might lose functionalities, like the notification counter or the dynamic background": "يمكن ان تخسر بعض الوظائف, مثل عدد الاشعارات او الخلفية الديناميكية",
    "Clock position and size:": ":حجم و موضع الساعة",
    "Clock size preferences, position offset, clock at the left, etc.": "تفضيلات حجم الساعة, ازاحة الموضع, الساعة علي اليسار, الخ.",
    "Reset monitor blacklisting status": "إعادة تعيين حالة القائمة السوداء للشاشة",
    "Reset": "إعادة تعيين",
    "Third party licenses": "تراخيص الطرف الثالث",
    "View": "معاينة",
    "ElevenClock": "ElevenClock",
    "Monitor tools": "أدوات المراقبة",
    "Blacklist this monitor": "اضافة الشاشة الي القائمة السوداء",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "برامج الطرف الثالث مفتوحة المصدر في Elevenclock {0} (و ترخيصهم)",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "ElevenClock هو برنامج مفتوح المصدر صنع بمساعدة برمجيات اخري صنعها مجتمع المبرمجين",
    "Ok": "حسنا",
    "More Info": "مزيد من المعلومات",
    "About Qt": "عن Qt",
    "Success": "نجح",
    "The monitors were unblacklisted successfully.": "الشاشة تم ازلتها من القائمة السوداء بنجاح",
    "Now you should see the clock everywhere": "الان يمكنك روئية الشاشة في اي مكان",
    "Ok": "حسنا",
    "Blacklist Monitor": "اضافة الشاشة الي القائمة السوداء",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "اضافة الشاشة الي القائمة السوداء سوف يخفي الساعة عليها نهائيا",
    "This action can be reverted from the settings window. under <b>Clock position and size</b>": "هذا الاختيار يمكن الغائة من قائمة الاعدادات. تحت <b>حجم وموضع الساعة</b>",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "هل انت متأكد من انك تريد اضافة الشاشة الي القائمة السوداء \"{0}\"?",
    "Yes": "نعم",
    "No": "لا",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "اعادة تحميل السجل",
    "Do not show the clock on secondary monitors": "لا تظهر الساعه علي الشاشات الثانوية",
    "Disable clock taskbar background color (make clock transparent)": "ازالة لون خلفية ساعة شريط المهام (حول الساعة الي شفافة)",
    "Open the welcome wizard": "افتح مساعد الاعداد الترحيبي",
    " (ALPHA STAGE, MAY NOT WORK)": " (في مرحلة الترجبة, يمكن الا يعمل)",
    "Welcome to ElevenClock": "مرحبا بك في ElevenClock",
    "Skip": "اختصر",
    "Start": "ابداء",
    "Next": "التالي",
    "Finish": "انهاء",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "مدير المهام",
    "Change date and time": "تغير الوقت والتاريخ",
    "Notification settings": "اعدادات الاشعارات",
    "Updates, icon tray, language": "تحديثات, منطقة الاشعارات, اللغات",
    "Hide extended options from the clock right-click menu (needs a restart to be aplied)": "إخفاء الخيارات الموسعة من قائمة النقر بزر الماوس الأيمن (يحتاج إلى إعادة تشغيل ليتم تطبيقها)",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "سلوك ملء الشاشة ، موضع الساعة ، ساعة الشاشة الرئيسية ، إعدادات متنوعة أخرى",
    'Add the "Show Desktop" button on the left corner of every clock': 'أضف زر "إظهار سطح المكتب" في الزاوية اليسرى من كل ساعة',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': 'قد تحتاج إلى تعيين لون خلفية مخصص حتى يعمل هذا.&nbsp;؛ مزيد من المعلومات <a href="{0}" style="color:DodgerBlue"> هنا </a>',
    "Clock's font, font size, font color and background, text alignment": "خط الساعة وحجم الخط ولون الخط والخلفية ومحاذاة النص",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "تنسيق التاريخ ، تنسيق الوقت، الثواني، أيام الأسبوع، رقم الأسبوع، الإعدادات الإقليمية",
    "Testing features and error-fixing tools": "ميزات الاختبار وأدوات إصلاح الأخطاء",
    "Language pack author(s), help translating ElevenClock": "مؤلفو  حزم اللغات ، ساعدوا في ترجمة ElevenClock",
    "Info, report a bug, submit a feature request, donate, about": "معلومات، إبلاغ عن خطأ، إرسال طلب ميزة، تبرع، حول",
    "Log, debugging information": "السجل، معلومات التصحيح",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen": "فرض الساعة في الجزء العلوي من الشاشة",
    "Show the clock on the primary screen": "اعرض الساعة على الشاشة الرئيسية",
    "Use a custom font color": "استخدم لون خط مخصص",
    "Use a custom background color": "استخدم لون خلفية مخصص",
    "Align the clock text to the center": "قم بمحاذاة نص الساعة إلى المركز",
    "Select custom color": "حدد لونًا مخصصًا",
    "Hide the clock when a program occupies all screens": "إخفاء الساعة عندما يشغل برنامج جميع الشاشات",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "استخدم خطًا مخصصًا",
    "Use a custom font size": "استخدم حجم خط مخصص",
    "Enable hide when multi-monitor fullscreen apps are running": "تمكين الإخفاء عند تشغيل تطبيقات متعددة الشاشات في وضع ملء الشاشة",
    "<b>{0}</b> needs to be enabled to change this setting": "<b>{0}</b> يحتاج إلى التمكين لتغيير هذا الإعداد",
    "<b>{0}</b> needs to be disabled to change this setting": "<b>{0}</b> يحتاج إلى التعطيل لتغيير هذا الإعداد",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": "(تم تعطيل هذه الميزة لأنها يجب أن تعمل بشكل افتراضي. إذا لم يكن كذلك ، الرجاء الإبلاغ عن خطأ)",
    "ElevenClock's language": "لغات ElevenClock"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "عن Qt6 (PySide6)",
    "About": "عن",
    "Alternative non-SSL update server (This might help with SSL errors)": "خادم تحديث بديل بدون SSL (يمكن ان يساعد ذلك في حل مشاكل SSL)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "الإصلاحات والميزات التجريبية الأخرى: (استخدم فقط إذا كان هناك شيء لا يعمل)",
    "Show week number on the clock": "إظهار رقم الأسبوع على الساعة"
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "إخفاء الساعة عند تشغيل RDP Client أو Citrix Workspace",
    "Clock Appearance:": "مظهر الساعة",
    "Force the clock to have black text": "اجبار الساعة علي استخدام لون خط اسود",
    " - It is required that the Dark Text checkbox is disabled": "- يلزم الغاء تمكين اعداد الخط الاسود",
    "Debbugging information:": "معلومات التصحيح",
    "Open ElevenClock's log": "فتح سجل ElevenClock",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "إظهار الساعة على الشاشة الرئيسية (مفيد إذا تم ضبط الساعة على اليسار)",
    "Show weekday on the clock"  :"عرض أيام الأسبوع على مدار الساعة",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"إعدادات ElevenClock", # Also settings title
    "Reload Clocks"             :"إعادة تحميل الساعات",
    "ElevenClock v{0}"          :"ElevenClock اصدار{0}",
    "Restart ElevenClock"       :"اعادة تشغيل ElevenClock",
    "Hide ElevenClock"          :"اخفاء ElevenClock",
    "Quit ElevenClock"          :"اغلاق ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"اعدادات عامة",
    "Automatically check for updates"                                                   :"البحث عن التحديثات تلقائيا",
    "Automatically install available updates"                                           :"تثبيت التحديثات المتوفرة تلقائيا",
    "Enable really silent updates"                                                      :"تفعيل التحديث بصمت",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"تجاوز التحقق من مصداقية مزود التحديث (غير مستحسن ، على مسؤوليتك الخاصة)",
    "Show ElevenClock on system tray"                                                   :"اظهار ElevenClock في منطقة الاشعارت",
    "Alternative clock alignment (may not work)"                                        :"محاذاة الساعة البديلة (قد لا تعمل)",
    "Change startup behaviour"                                                          :"تغيير سلوك بدء التشغيل",
    "Change"                                                                            :"تغير",
    "<b>Update to the latest version!</b>"                                             :"<b>حدث الي احدث اصدار</b>",
    "Install update"                                                                    :"تثبيت التحديثات",
    
    #Clock settings
    "Clock Settings:"                                              :"اعدادات الساعة",
    "Hide the clock in fullscreen mode"                            :"اخفاء الساعة في وضع ملء الشاشة",
    "Hide the clock when RDP client is active"                     :"إخفاء الساعة عندما يكون عميل RDP نشطًا",
    "Force the clock to be at the bottom of the screen"            :"فرض الساعة في أسفل الشاشة",
    "Show the clock when the taskbar is set to hide automatically" :"إظهار الساعة عندما يكون شريط المهام مضبوطًا على الإخفاء تلقائيًا",
    "Fix the hyphen/dash showing over the month"                   :"إصلاح الواصلة / الشرطة التي تظهر على مدار الشهر",
    "Force the clock to have white text"                           :"إجبار الساعة على الحصول على لون خط أبيض",
    "Show the clock at the left of the screen"                     :"اعرض الساعة على يسار الشاشة",
    
    #Date & time settings
    "Date & Time Settings:"                             :"إعدادات التاريخ والوقت:",
    "Show seconds on the clock"                         :"عرض الثواني على الساعة",
    "Show date on the clock"                            :"عرض التاريخ على الساعة",
    "Show time on the clock"                            :"عرض الوقت على الساعة",
    "Change date and time format (Regional settings)"   :"تغيير تنسيق التاريخ والوقت (الإعدادات الإقليمية)",
    "Regional settings"                                 :"الإعدادات الإقليمية",
    
    #About the language pack
    "About the language pack:"                  :"حول حزمة اللغة:",
    "Translated to English by martinet101"      :"ترجمت الي الانجيليزية بفضل martinet101", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"ترجمت الي لغتك",
    "Get started"                               :"البدء",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"حول إصدار ElevenClock {0}:",
    "View ElevenClock's homepage"               :"عرض الصفحة الرئيسية ElevenClock",
    "Open"                                      :"فتح",
    "Report an issue/request a feature"         :"ابلاغ عن مشكلة/طلب اضافة ميزة",
    "Report"                                    :"ابلاغ",
    "Support the dev: Give me a coffee☕"       :"☕ادعم المطور:اشتري لي كوب من القهوة",
    "Open page"                                 :"افتح صفحة",
    "Icons by Icons8"                           :"الايقونات من Icon8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"صفحة انترنت",
    "Close settings"                            :"اغلاق الاعدادات",
    "Close"                                     :"اغلاق",
}

lang = lang2_3