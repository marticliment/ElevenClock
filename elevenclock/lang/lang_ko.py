# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_1 = {
    "W": "주", # The initial of the word week in your language: W for week, S for setmana, etc.
    "Disable the notification badge": "알림 배지 사용 안 함",
    "Override clock default height": "시계 기본 높이 재정의",
    "Adjust horizontal clock position": "수평 시계 위치 조정",
    "Adjust vertical clock position": "수직 시계 위치 조정",
    "Export log as a file": "로그를 파일로 내보내기",
    "Copy log to clipboard": "로그를 클립보드에 복사",
    "Announcements:": "공지사항",
    "Fetching latest announcement, please wait...": "최신 공지사항을 가져오는 중입니다. 잠시 기다려 주십시오...",
    "Couldn't load the announcements. Please try again later": "공지사항을 불러올 수 없습니다. 나중에 다시 시도해 주십시오",
    "ElevenClock's log": "ElevenClock 로그",
    "Pick a color": "색상 선택"
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "클릭하면 10초 동안 시계 숨기기",
    "Enable low-cpu mode": "저성능 CPU 모드 사용",
    "You might lose functionalities, like the notification counter or the dynamic background": "알림 카운터 또는 동적 배경과 같은 기능을 잃을 수 있습니다.",
    "Clock position and size:": "시계 위치 및 크기:",
    "Clock size preferences, position offset, clock at the left, etc.": "시계 크기 환경 설정, 위치 조정, 왼쪽 시계 등",
    "Reset monitor blacklisting status": "모니터 블랙리스트 상태 초기화",
    "Reset": "초기화",
    "Third party licenses": "타사 라이센스",
    "View": "보기",
    "ElevenClock": "ElevenClock",
    "Monitor tools": "모니터 도구",
    "Blacklist this monitor": "이 모니터 블랙리스트 지정",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "ElevenClock {0}의 타사 오픈 소스 소프트웨어 (및 해당 라이센스)",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "ElevenClock은 커뮤니티에서 만든 다른 라이브러리의 도움을 받아 만든 오픈 소스 응용 프로그램입니다",
    "Ok": "확인",
    "More Info": "추가 정보",
    "About Qt": "Qt 정보",
    "Success": "성공",
    "The monitors were unblacklisted successfully.": "모니터가 블랙리스트 해제되었습니다.",
    "Now you should see the clock everywhere": "이제 당신은 어디에서나 시계를 볼 수 있습니다.",
    "Ok": "확인",
    "Blacklist Monitor": "블랙리스트 모니터",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "모니터를 블랙리스트에 올리면 이 모니터의 시계가 영구적으로 숨겨집니다.",
    "This action can be reverted from the settings window. under <b>Clock position and size</b>": "설정 창의 <b>시계 위치 및 크기</b> 에서 이 동작을 되돌릴 수 있습니다.",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "모니터를 \"{0}\" 블랙리스트에 표시하시겠습니까?",
    "Yes": "예",
    "No": "아니오",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "로그 새로 고침",
    "Do not show the clock on secondary monitors": "보조 모니터에 시계 표시 안 함",
    "Disable clock taskbar background color (make clock transparent)": "시계 작업 표시줄 배경색 사용 안 함 (시계를 투명하게 표시)",
    "Open the welcome wizard": "시작 마법사 열기",
    " (ALPHA STAGE, MAY NOT WORK)": " (알파 단계, 작동하지 않을 수 있음)",
    "Welcome to ElevenClock": "ElevenClock에 오신 것을 환영합니다",
    "Skip": "건너뛰기",
    "Start": "시작",
    "Next": "다음",
    "Finish": "마침",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "작업 관리자",
    "Change date and time": "날짜 및 시간 변경",
    "Notification settings": "알림",
    "Updates, icon tray, language": "업데이트, 아이콘 트레이, 언어",
    "Hide extended options from the clock right-click menu (needs a restart to be aplied)": "시계 오른쪽 버튼 메뉴에서 확장 옵션 숨기기 (적용하려면 재시작 필요)",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "전체 화면 동작, 시계 위치, 첫 번째 모니터 시계, 다른 여러가지 설정",
    'Add the "Show Desktop" button on the left corner of every clock': '모든 시계의 왼쪽 모서리에 "바탕 화면 표시" 버튼 추가',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': '이 작업을 수행하려면 사용자 지정 배경색을 설정해야 할 수 있습니다.&nbsp;추가 정보는 <a href="{0}" style="color:DodgerBlue">여기</a>',
    "Clock's font, font size, font color and background, text alignment": "시계의 글꼴, 글꼴 크기, 글꼴 색상 및 배경, 텍스트 정렬",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "날짜 형식, 시간 형식, 초, 요일, 주 번호, 지역 설정",
    "Testing features and error-fixing tools": " 기능 및 오류 테스트 - 수정 도구",
    "Language pack author(s), help translating ElevenClock": "언어 팩 작성자, ElevenClock 번역 돕기",
    "Info, report a bug, submit a feature request, donate, about": "정보, 버그 보고, 기능 요청 제출, 기부, 정보",
    "Log, debugging information": "로그, 디버깅 정보",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen": "화면 상단에 시계를 강제로 표시",
    "Show the clock on the primary screen": "주 화면에 시계 표시",
    "Use a custom font color": "사용자 지정 글꼴 색 사용",
    "Use a custom background color": "사용자 지정 배경색 사용",
    "Align the clock text to the center": "시계 텍스트를 가운데에 정렬",
    "Select custom color": "사용자 지정 색상 선택",
    "Hide the clock when a program occupies all screens": "프로그램이 모든 화면을 차지할 때 시계 숨기기",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "사용자 지정 글꼴 사용",
    "Use a custom font size": "사용자 지정 글꼴 크기 사용",
    "Enable hide when multi-monitor fullscreen apps are running": "다중 모니터 전체 화면 앱이 실행 중일 때 숨기기 사용",
    "<b>{0}</b> needs to be enabled to change this setting": "이 설정을 변경하려면 <b>{0}</b>을 사용하도록 설정해야 합니다",
    "<b>{0}</b> needs to be disabled to change this setting": "이 설정을 변경하려면 <b>{0}</b>을 사용하지 않도록 설정해야 합니다",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": "이 기능은 기본적으로 작동해야 하므로 사용할 수 없습니다. 그렇지 않다면 버그를 보고해 주세요.)",
    "ElevenClock's language": "ElevenClock 언어"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Qt6 (PySide6) 정보",
    "About": "정보",
    "Alternative non-SSL update server (This might help with SSL errors)": "SSL이 아닌 업데이트 서버 대체 (SSL 오류에 도움이 될 수 있음)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "수정 및 기타 실험 기능: (작동하지 않는 경우에만 사용)",
    "Show week number on the clock": "시계에 주 번호 표시"
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "RDP 클라이언트 또는 Citrix Workspace가 실행 중일 때 시계 숨기기",
    "Clock Appearance:": "시계 모양",
    "Force the clock to have black text": "시계를 검은색 텍스트로 강제 설정",
    " - It is required that the Dark Text checkbox is disabled": " - 어두운 텍스트 확인란이 비활성화되어 있어야 합니다",
    "Debbugging information:": "디버깅 정보",
    "Open ElevenClock's log": "ElevenClock 로그 열기",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "주 화면에 시계 표시 (시계가 왼쪽에 설정된 경우 유용)",
    "Show weekday on the clock"  :"시계에 요일 표시",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"ElevenClock 설정", # Also settings title
    "Reload Clocks"             :"시계 다시 불러오기",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"ElevenClock 재시작",
    "Hide ElevenClock"          :"ElevenClock 숨기기",
    "Quit ElevenClock"          :"ElevenClock 끝내기",
    
    #General settings section
    "General Settings:"                                                                 :"일반 설정:",
    "Automatically check for updates"                                                   :"업데이트 자동 확인",
    "Automatically install available updates"                                           :"사용 가능한 업데이트 자동 설치",
    "Enable really silent updates"                                                      :"조용한 업데이트 사용함",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"업데이트 공급자 신뢰성 검사 무시 (권장하지 않음, 위험 감수)",
    "Show ElevenClock on system tray"                                                   :"시스템 트레이에 ElevenClock 아이콘 표시",
    "Alternative clock alignment (may not work)"                                        :"대체 시계 정렬 (작동하지 않을 수 있음)",
    "Change startup behaviour"                                                          :"시작 동작 변경",
    "Change"                                                                            :"변경",
    "<b>Update to the latest version!</b>"                                             :"<b>최신 버전으로 업데이트하십시오!</b>",
    "Install update"                                                                    :"업데이트 설치",
    
    #Clock settings
    "Clock Settings:"                                              :"시계 설정",
    "Hide the clock in fullscreen mode"                            :"전체 화면 모드에서 시계 숨기기",
    "Hide the clock when RDP client is active"                     :"RDP 클라이언트가 활성 상태일 때 시계 숨기기",
    "Force the clock to be at the bottom of the screen"            :"화면 하단에 시계를 강제로 표시",
    "Show the clock when the taskbar is set to hide automatically" :"작업 표시줄이 자동으로 숨기도록 설정되어도 시계 표시",
    "Fix the hyphen/dash showing over the month"                   :"월 표시로된 하이픈/대시 수정",
    "Force the clock to have white text"                           :"시계를 흰색 텍스트로 강제 설정",
    "Show the clock at the left of the screen"                     :"화면 왼쪽에 시계 표시",
    
    #Date & time settings
    "Date & Time Settings:"                             :"날짜 및 시간 설정",
    "Show seconds on the clock"                         :"시계에 초 표시",
    "Show date on the clock"                            :"시계에 날짜 표시",
    "Show time on the clock"                            :"시계에 시간 표시",
    "Change date and time format (Regional settings)"   :"",
    "Regional settings"                                 :"",
    
    #About the language pack
    "About the language pack:"                  :"언어 팩 정보",
    "Translated to English by martinet101"      :"한국어 번역 - VᴇɴᴜꜱGɪʀʟ💗비너스걸", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"ElevenClock을 당신의 언어로 번역하세요",
    "Get started"                               :"",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"ElevenClock 버전 {0} 정보:",
    "View ElevenClock's homepage"               :"ElevenClock 홈페이지 보기",
    "Open"                                      :"열기",
    "Report an issue/request a feature"         :"문제 보고/기능 요청",
    "Report"                                    :"보고",
    "Support the dev: Give me a coffee☕"       :"개발 지원: 커피값 기부하기☕",
    "Open page"                                 :"페이지 열기",
    "Icons by Icons8"                           :"", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"웹페이지",
    "Close settings"                            :"설정 닫기",
    "Close"                                     :"닫기",
}

lang = lang2_3
