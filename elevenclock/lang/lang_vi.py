# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang2_7 = {
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
