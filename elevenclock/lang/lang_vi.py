# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_3_2 = {
    "ElevenClock Updater": "",
    "ElevenClock is downloading updates": "",
    "ElevenClock has updated to version {0} successfully
Please see GitHub for the changelog": "",
    "Customize the clock on Windows 11": "",
    "Disable the new instance checker method": "",
    "ElevenClock is downloading updates": "",
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
    "Show weekday on the clock"  :"",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"Cài đặt", # Also settings title
    "Reload Clocks"             :"Tải lại đồng hồ",
    "ElevenClock v{0}"          :"Phiên bản:{0}",
    "Restart ElevenClock"       :"Khởi động lại ElevenClock",
    "Hide ElevenClock"          :"Ẩn ElevenClock",
    "Quit ElevenClock"          :"Thoát ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Cài đặt chung",
    "Automatically check for updates"                                                   :"Tự động kiểm tra phiên bản cập nhật mới",
    "Automatically install available updates"                                           :"Tự động cài đặt phiên bản mới",
    "Enable really silent updates"                                                      :"Bật cài đặt trong nền",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Bỏ qua kiểm tra tính xác thực của nhà cung cấp bản cập nhật (KHÔNG ĐƯỢC KHUYẾN NGHỊ, BẠN PHẢI TỰ CHỊU RỦI RO CỦA BẠN)",
    "Show ElevenClock on system tray"                                                   :"Hiện trong tray hệ thống",
    "Alternative clock alignment (may not work)"                                        :"Vị trí khác cho đồng hồ (có thể không hoạt động)",
    "Change startup behaviour"                                                          :"Thay đổi hành vi khởi động",
    "Change"                                                                            :"Thay đổi",
    "<b>Update to the latest version!</b>"                                             :"<b>Cập nhật phiên bản mới nhất!</b>",
    "Install update"                                                                    :"Cài đặt cập nhật",
    
    #Clock settings
    "Clock Settings:"                                              :"Cài đặt đồng hồ",
    "Hide the clock in fullscreen mode"                            :"Ẩn đồng hồ ở chế độ toàn màn hình",
    "Hide the clock when RDP client is active"                     :"Ẩn đồng hồ khi RDP client đang bật",
    "Force the clock to be at the bottom of the screen"            :"Giữ đồng hồ ở dưới màn hình",
    "Show the clock when the taskbar is set to hide automatically" :"Hiện đồng hồ khi taskbar được cài thành ẩn tự động",
    "Fix the hyphen/dash showing over the month"                   :"Sửa lỗi dấu gạch nối/gạch ngang ở phần tháng ",
    "Force the clock to have white text"                           :"Buộc đồng hồ phải có chữ màu trắng",
    "Show the clock at the left of the screen"                     :"Hiển thị đồng hồ ở bên trái màn hình",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Cài đặt Ngày & Giờ",
    "Show seconds on the clock"                         :"Hiển thị giây trên đồng hồ",
    "Show date on the clock"                            :"Hiển thị ngày trên đồng hồ",
    "Show time on the clock"                            :"Hiển thị thời gian trên đồng hồ",
    "Change date and time format (Regional settings)"   :"Thay đổi định dạng ngày và giờ (Cài đặt khu vực)",
    "Regional settings"                                 :"Thiết lập khu vực",
    
    #About the language pack
    "About the language pack:"                  :"Về bản dịch:",
    "Translated to English by martinet101"      :"Được dịch về tiếng việt bởi Leoodz", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Dịch ElevenClock sang ngôn ngữ của bạn",
    "Get started"                               :"Bắt đầu",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Về ElevenClock phiên bản {}:",
    "View ElevenClock's homepage"               :"Xem trang chủ của ElevenClock",
    "Open"                                      :"Mở",
    "Report an issue/request a feature"         :"Báo cáo lỗi / yêu cầu một tính năng",
    "Report"                                    :"Báo cáo",
    "Support the dev: Give me a coffee☕"       :"Ủng hộ lập trình viên: Give me a coffee☕",
    "Open page"                                 :"Mở trang",
    "Icons by Icons8"                           :"Icons bởi Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Trang web",
    "Close settings"                            :"Đóng cài đặt",
    "Close"                                     :"Đóng",
}

lang = lang2_3
