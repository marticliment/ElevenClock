# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}"
#               translation ->  "Aquest text està en anglès: valor {0}"

# So it would look like: "ORIGINAL_TEXT" : "TRANSLATED_TEXT",


# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.
lang_3_4_0 = {
    "Show calendar": "แสดงปฏิทิน",
    "Disabled": "ปิดการใช้งาน",
    "Open quick settings": "เปิดการตั้งค่าด่วน",
    "Show desktop": "แสดงเดสก์ท็อป",
    "Open run dialog": "เปิดหน้าต่างรัน",
    "Open task manager": "เปิดตัวจัดการงาน",
    "Open start menu": "เปิดเมนูเริ่มต้น",
    "Open search menu": "เปิดเมนูค้นหา",
    "Change task": "เปลี่ยนทาสก์",
    "Change the action done when the clock is clicked": "เปลี่ยนการทำงานเมื่อมีการคลิกนาฬิกา",
}

lang_3_3_2 = lang_3_4_0 | {
    "ElevenClock Updater": "ตัวช่วยอัปเดต ElevenClock",
    "ElevenClock is downloading updates": "ElevenClock กำลังดาวน์โหลดการอัปเดต",
    "ElevenClock has updated to version {0} successfully\nPlease see GitHub for the changelog": "ElevenClock อัปเดตเป็นเวอร์ชัน {0} สำเร็จแล้ว\nโปรดดูบันทึกการเปลี่ยนแปลงที่ GitHub",
    "Customize the clock on Windows 11": "ปรับแต่งนาฬิกาใน Windows 11",
    "Disable the new instance checker method": "ปิดการใช้งานคำสั่งการตรวจสอบอินสแตนซ์ใหม่",
    "Import settings from a local file": "นำเข้าการตั้งค่าจากไฟล์ในเครื่อง",
    "Export settings to a local file": "ส่งออกการตั้งค่าไปยังไฟล์ในเครื่อง",
    "Export": "ส่งออก",
    "Import": "นำเข้า",
}

lang_3_3_1 = lang_3_3_2 | {
    "Invalid time format\nPlease follow the\nC 1989 Standards": "รูปแบบเวลาไม่ถูกต้อง\nโปรดปฏิบัติตาม\nมาตรฐาน C 1989",
    "Nothing to preview": "ไม่มีตัวอย่างให้ดู",
    "Invalid time format\nPlease modify it\nin the settings": "รูปแบบเวลาไม่ถูกต้อง\nโปรดแก้ไข\nในการตั้งค่า",
    "Disable the tooltip shown when the clock is hovered": "ปิดใช้งานการแสดงคำแนะนำเครื่องมือเมื่อวางเมาส์บนนาฬิกา",
}
lang_3_3 = lang_3_3_1 | {
    "Custom format rules:": "กฎรูปแบบที่กำหนดเอง:",
    "Any text can be placed here. To place items such as date and time, please use the 1989 C standard. More info on the following link": "สามารถใส่ข้อความใด ๆ ได้ที่นี่ หากต้องใส่รายการต่าง ๆ เช่น วันที่และเวลา โปรดใช้มาตรฐาน 1989 C ข้อมูลเพิ่มเติมตามลิงก์ต่อไปนี้",
    "Python date and time formats": "รูปแบบวันที่และเวลาของ Python",
    "To disable the zero-padding effect, add a # in between the % and the code: non-zero-padded hours would be %#H, and zero-padded hours would be %H": "หากต้องการปิดเอฟเฟกต์การเติมศูนย์ ให้เพิ่ม # ระหว่าง % และโค้ด: ชั่วโมงที่ไม่เติมศูนย์จะเป็น %#H และชั่วโมงที่เติมศูนย์จะเป็น %H",  # Here please don't modify the %H and %#H values
    "Click on Apply to apply and preview the format": "คลิก นำมาใช้ เพื่อนำมาใช้และดูตัวอย่างรูปแบบ",
    "Apply": "นำมาใช้",
    "If you don't understand what is happening, please uncheck the checkbox over the text area": "หากคุณไม่เข้าใจว่ากำลังเกิดอะไรขึ้น โปรดยกเลิกการเลือกช่องทำเครื่องหมายเหนือพื้นที่ข้อความ",
    "Set a custom date and time format": "กำหนดรูปแบบวันที่และเวลาเอง",
    "(for advanced users only)": "(สำหรับผู้ใช้ขั้นสูงเท่านั้น)",
    "Move this clock to the left": "เลื่อนนาฬิกานี้ไปทางซ้าย",
    "Move this clock to the top": "เลื่อนนาฬิกานี้ขึ้นด้านบน",
    "Move this clock to the right": "เลื่อนนาฬิกานี้ไปทางขวา",
    "Move this clock to the bottom": "เลื่อนนาฬิกานี้ไปที่ด้านล่าง",
    "Restore horizontal position": "เรียกคืนตำแหน่งแนวนอน",
    "Restore vertical position": "เรียกคืนตำแหน่งแนวตั้ง",
}

lang_3_2_1 = lang_3_3 | {
    "Open online help to troubleshoot problems": "เปิดความช่วยเหลือออนไลน์เพื่อแก้ไขปัญหา",
    "Reset ElevenClock preferences to defaults": "รีเซ็ตการตั้งค่า ElevenClock เป็นค่าเริ่มต้น",
    "Specify a minimum width for the clock": "ระบุความกว้างขั้นต่ำสำหรับนาฬิกา",
    "Search on the settings": "ค้นหารายการตั้งค่า",
    "No results were found": "ไม่พบผลลัพธ์",
}

lang_3_2 = lang_3_2_1 | {
    "Use system accent color as background color": "ใช้สีที่เน้นของระบบเป็นสีพื้นหลัง",
    "Check only the focused window on the fullscreen check": "ตรวจสอบเฉพาะหน้าต่างที่โฟกัสเมื่อตรวจสอบแบบเต็มหน้าจอ",
    "Clock on monitor {0}": "นาฬิกาบนจอมอนิเตอร์ {0}",
    "Move to the left": "เลื่อนไปทางซ้าย",
    "Show this clock on the left": "แสดงนาฬิกานี้ทางซ้าย",
    "Show this clock on the right": "แสดงนาฬิกานี้ทางขวา",
    "Restore clock position": "เรียกคืนตำแหน่งนาฬิกา",
}

lang_3_1 = lang_3_2 | {
    # The initial of the word week in your language: W for week, S for setmana, etc.
    "W": "ส",
    "Disable the notification badge": "ปิดการใช้งานป้ายการแจ้งเตือน",
    "Override clock default height": "แทนที่ความสูงเริ่มต้นของนาฬิกา",
    "Adjust horizontal clock position": "ปรับตำแหน่งนาฬิกาแนวนอน",
    "Adjust vertical clock position": "ปรับตำแหน่งนาฬิกาแนวตั้ง",
    "Export log as a file": "บันทึกไฟล์ล็อก",
    "Copy log to clipboard": "คัดลอกล็อกไปยังคลิปบอร์ด",
    "Announcements:": "ประกาศ:",
    "Fetching latest announcement, please wait...": "กำลังโหลดประกาศล่าสุด กรุณารอสักครู่...",
    "Couldn't load the announcements. Please try again later": "ไม่สามารถโหลดประกาศได้ โปรดลองอีกครั้งในภายหลัง",
    "ElevenClock's log": "ล็อกของ ElevenClock",
    "Pick a color": "เลือกสี"
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "ซ่อนนาฬิกาในช่วง 10 วินาทีเมื่อคลิก",
    "Enable low-cpu mode": "เปิดใช้งานโหมดซีพียูต่ำ",
    "You might lose functionalities, like the notification counter or the dynamic background": "คุณอาจสูญเสียฟังก์ชันการทำงาน เช่น ตัวนับการแจ้งเตือนหรือพื้นหลังแบบไดนามิก",
    "Clock position and size:": "ตำแหน่งและขนาดของนาฬิกา:",
    "Clock size preferences, position offset, clock at the left, etc.": "การตั้งค่าขนาดนาฬิกา, ออฟเซ็ตตำแหน่ง, นาฬิกาทางด้านซ้าย, ฯลฯ",
    "Reset monitor blacklisting status": "รีเซ็ตสถานะการขึ้นบัญชีดำของจอมอนิเตอร์",
    "Reset": "รีเซ็ต",
    "Third party licenses": "สัญญาอนุญาตบุคคลที่สาม",
    "View": "ดู",
    "ElevenClock": "ElevenClock",
    "Monitor tools": "เครื่องมือจอมอนิเตอร์",
    "Blacklist this monitor": "ขึ้นบัญชีดำจอมอนิเตอร์นี้",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "ซอฟต์แวร์โอเพนซอร์สบุคคลที่สามใน ElevenClock {0} (และสัญญาอนุญาตของพวกเขา)",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "ElevenClock เป็นแอปพลิเคชันโอเพนซอร์สที่สร้างโดยความช่วยเหลือของไลบรารีอื่นที่สร้างโดยชุมชน:",
    "Ok": "ตกลง",
    "More Info": "ข้อมูลเพิ่มเติม",
    "About Qt": "เกี่ยวกับ Qt",
    "Success": "สำเร็จ",
    "The monitors were unblacklisted successfully.": "จอมอนิเตอร์ถูกยกเลิกการขึ้นบัญชีดำเรียบร้อยแล้ว",
    "Now you should see the clock everywhere": "ตอนนี้คุณควรเห็นนาฬิกาทุกที่",
    "Ok": "ตกลง",
    "Blacklist Monitor": "ขึ้นบัญชีดำจอมอนิเตอร์",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "การขึ้นบัญชีดำจอมอนิเตอร์จะซ่อนนาฬิกาบนจอมอนิเตอร์นี้อย่างถาวร",
    "This action can be reverted from the settings window, under <b>Clock position and size</b>": "การดำเนินการนี้สามารถเปลี่ยนกลับได้จากหน้าต่างการตั้งค่าใน <b>ตำแหน่งและขนาดของนาฬิกา</b>",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "คุณแน่ใจหรือว่าต้องการขึ้นบัญชีดำจอมอนิเตอร์ \"{0}\"?",
    "Yes": "ใช่",
    "No": "ไม่",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "รีโหลดล็อก",
    "Do not show the clock on secondary monitors": "อย่าแสดงนาฬิกาบนจอมอนิเตอร์รอง",
    "Disable clock taskbar background color (make clock transparent)": "ปิดใช้งานสีพื้นหลังทาสก์บาร์ของนาฬิกา (ทำให้นาฬิกาโปร่งใส)",
    "Open the welcome wizard": "เปิดหน้าต่างวิซาร์ดต้อนรับ",
    " (ALPHA STAGE, MAY NOT WORK)": " (อยู่ในสถานะแอลฟา อาจใช้งานไม่ได้)",
    "Welcome to ElevenClock": "ยินดีต้อนรับสู่ ElevenClock",
    "Skip": "ข้าม",
    "Start": "เริ่ม",
    "Next": "ต่อไป",
    "Finish": "เสร็จสิ้น",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "ตัวจัดการงาน",
    "Change date and time": "เปลี่ยนวันที่และเวลา",
    "Notification settings": "การตั้งค่าการแจ้งเตือน",
    "Updates, icon tray, language": "อัปเดต, ถาดไอคอน, ภาษา",
    "Hide extended options from the clock right-click menu (needs a restart to be applied)": "ซ่อนตัวเลือกเพิ่มเติมจากเมนูคลิกขวาของนาฬิกา (จำเป็นต้องเริ่มระบบใหม่เพื่อใช้งาน)",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "ลักษณะการทำงานเต็มจอ, ตำแหน่งนาฬิกา, นาฬิกาบนจอมอนิเตอร์ที่ 1, การตั้งค่าเบ็ดเตล็ดอื่น ๆ",
    'Add the "Show Desktop" button on the left corner of every clock': 'เพิ่มปุ่ม "แสดงเดสก์ท็อป" ที่มุมซ้ายของทุกนาฬิกา',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': 'คุณอาจต้องตั้งค่าสีพื้นหลังที่กำหนดเองเพื่อให้ใช้งานได้&nbsp;ข้อมูลเพิ่มเติม<a href="{0}" style="color:DodgerBlue">ที่นี่</a>',
    "Clock's font, font size, font color and background, text alignment": "ฟอนต์ของนาฬิกา, ขนาดฟอนต์, สีฟอนต์และพื้นหลัง, การจัดตำแหน่งข้อความ",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "รูปแบบวันที่, รูปแบบเวลา, วินาที, วันในสัปดาห์, หมายเลขสัปดาห์, การตั้งค่าภูมิภาค",
    "Testing features and error-fixing tools": "ฟีเจอร์ทดสอบและเครื่องมือแก้ไขข้อผิดพลาด",
    "Language pack author(s), help translating ElevenClock": "ผู้เขียนชุดภาษา, ช่วยแปล ElevenClock",
    "Info, report a bug, submit a feature request, donate, about": "ข้อมูล, รายงานบั๊ก, ส่งคำขอฟีเจอร์, บริจาค, เกี่ยวกับ",
    "Log, debugging information": "บันทึกล็อก, ข้อมูลการดีบั๊ก",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen": "บังคับนาฬิกาให้อยู่ด้านบนของหน้าจอ",
    "Show the clock on the primary screen": "แสดงนาฬิกาบนหน้าจอหลัก",
    "Use a custom font color": "ใช้สีตัวอักษรที่กำหนดเอง",
    "Use a custom background color": "ใช้สีพื้นหลังที่กำหนดเอง",
    "Align the clock text to the center": "จัดข้อความนาฬิกาให้อยู่ตรงกลาง",
    "Select custom color": "เลือกสีที่กำหนดเอง",
    "Hide the clock when a program occupies all screens": "ซ่อนนาฬิกาเมื่อโปรแกรมใช้งานทุกหน้าจอ",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "ใช้ฟอนต์ที่กำหนดเอง",
    "Use a custom font size": "ใช้ขนาดฟอนต์ที่กำหนดเอง",
    "Enable hide when multi-monitor fullscreen apps are running": "เปิดใช้งานการซ่อนเมื่อแอปเต็มจอหลายหน้าจอทำงาน",
    "<b>{0}</b> needs to be enabled to change this setting": "ต้องเปิดใช้งาน <b>{0}</b> เพื่อเปลี่ยนการตั้งค่านี้",
    "<b>{0}</b> needs to be disabled to change this setting": "ต้องปิดใช้งาน <b>{0}</b> เพื่อเปลี่ยนการตั้งค่านี้",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": " (ฟีเจอร์นี้ถูกปิดใช้งานเนื่องจากควรใช้งานได้โดยค่าเริ่มต้น หากไม่เป็นเช่นนั้น โปรดรายงานบั๊ก)",
    "ElevenClock's language": "ภาษาของ ElevenClock"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "เกี่ยวกับ Qt6 (PySide6)",
    "About": "เกี่ยวกับ",
    "Alternative non-SSL update server (This might help with SSL errors)": "เซิร์ฟเวอร์ non-SSL ทางเลือกสำหรับการอัปเดต (อาจช่วยเรื่องข้อผิดพลาด SSL)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "การแก้ไขและฟีเจอร์ทดลองอื่น ๆ: (ใช้เฉพาะในกรณีที่บางอย่างไม่ทำงาน)",
    "Show week number on the clock": "แสดงเลขสัปดาห์บนนาฬิกา"
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "ซ่อนนาฬิกาเมื่อ RDP Client หรือ Citrix Workspace กำลังทำงาน",
    "Clock Appearance:": "ลักษณะนาฬิกา:",
    "Force the clock to have black text": "บังคับนาฬิกาให้มีข้อความสีดำ",
    " - It is required that the Dark Text checkbox is disabled": " - จำเป็นต้องปิดการใช้งานช่องทำเครื่องหมายข้อความสีเข้ม",
    "Debbugging information:": "ข้อมูลการดีบั๊ก:",
    "Open ElevenClock's log": "เปิดบันทึกล็อกของ ElevenClock",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "แสดงนาฬิกาบนหน้าจอหลัก (มีประโยชน์หากตั้งนาฬิกาไว้ทางซ้าย)",
    "Show weekday on the clock": "แสดงวันในสัปดาห์บนนาฬิกา",
}

lang2_3 = lang2_4 | {
    # Context menu
    "ElevenClock Settings": "การตั้งค่า ElevenClock",  # Also settings title
    "Reload Clocks": "รีโหลดนาฬิกา",
    "ElevenClock v{0}": "ElevenClock v{0}",
    "Restart ElevenClock": "รีสตาร์ต ElevenClock",
    "Hide ElevenClock": "ซ่อน ElevenClock",
    "Quit ElevenClock": "ออกจาก ElevenClock",

    # General settings section
    "General Settings:": "การตั้งค่าทั่วไป:",
    "Automatically check for updates": "ตรวจสอบการอัปเดตโดยอัตโนมัติ",
    "Automatically install available updates": "ติดตั้งการอัปเดตที่มีโดยอัตโนมัติ",
    "Enable really silent updates": "เปิดใช้งานการอัปเดตที่เงียบจริง ๆ",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)": "บายพาสการตรวจสอบความถูกต้องของผู้ให้บริการอัปเดต (ไม่แนะนำ รับความเสี่ยงของคุณเอง)",
    "Show ElevenClock on system tray": "แสดง ElevenClock บนถาดของระบบ",
    "Alternative clock alignment (may not work)": "การจัดตำแหน่งนาฬิกาทางเลือก (อาจใช้งานไม่ได้)",
    "Change startup behaviour": "เปลี่ยนลักษณะการทำงานในการเริ่มต้นระบบ",
    "Change": "เปลี่ยน",
    "<b>Update to the latest version!</b>": "<b>อัปเดตเป็นเวอร์ชันล่าสุด!</b>",
    "Install update": "ติดตั้งการอัปเดต",

    # Clock settings
    "Clock Settings:": "การตั้งค่านาฬิกา:",
    "Hide the clock in fullscreen mode": "ซ่อนนาฬิกาในโหมดเต็มหน้าจอ",
    "Hide the clock when RDP client is active": "ซ่อนนาฬิกาเมื่อไคลเอนต์ RDP ทำงาน",
    "Force the clock to be at the bottom of the screen": "บังคับนาฬิกาให้อยู่ด้านล่างหน้าจอ",
    "Show the clock when the taskbar is set to hide automatically": "แสดงนาฬิกาเมื่อตั้งค่าแถบงานให้ซ่อนโดยอัตโนมัติ",
    "Fix the hyphen/dash showing over the month": "แก้ไขเครื่องหมาย ยัติภังค์/ขีดกลาง ที่แสดงตลอดทั้งเดือน",
    "Force the clock to have white text": "บังคับนาฬิกาให้มีข้อความสีขาว",
    "Show the clock at the left of the screen": "แสดงนาฬิกาทางด้านซ้ายของหน้าจอ",

    # Date & time settings
    "Date & Time Settings:": "การตั้งค่าวันที่และเวลา:",
    "Show seconds on the clock": "แสดงวินาทีบนนาฬิกา",
    "Show date on the clock": "แสดงวันที่บนนาฬิกา",
    "Show time on the clock": "แสดงเวลาบนนาฬิกา",
    "Change date and time format (Regional settings)": "เปลี่ยนรูปแบบวันที่และเวลา (การตั้งค่าภูมิภาค)",
    "Regional settings": "การตั้งค่าภูมิภาค",

    # About the language pack
    "About the language pack:": "เกี่ยวกับชุดภาษา:",
    # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc.
    "Translated to English by martinet101": "แปลเป็นภาษาไทยโดย @richeyphu",
    "Translate ElevenClock to your language": "แปล ElevenClock เป็นภาษาของคุณ",
    "Get started": "เริ่มต้น",

    # About ElevenClock
    "About ElevenClock version {0}:": "เกี่ยวกับ ElevenClock เวอร์ชัน {0}:",
    "View ElevenClock's homepage": "ดูโฮมเพจของ ElevenClock",
    "Open": "เปิด",
    "Report an issue/request a feature": "รายงานปัญหา/ร้องขอฟีเจอร์",
    "Report": "รายงาน",
    "Support the dev: Give me a coffee☕": "สนับสนุนผู้พัฒนา: เลี้ยงค่ากาแฟ☕",
    "Open page": "เปิดหน้าเพจ",
    # Here, the word "Icons8" should not be translated
    "Icons by Icons8": "ไอคอนโดย Icons8",
    "Webpage": "หน้าเว็บ",
    "Close settings": "ปิดการตั้งค่า",
    "Close": "ปิด",
}

lang = lang2_3
