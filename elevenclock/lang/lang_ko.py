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
    "최신 공지사항을 가져오는 중입니다. 잠시 기다려 주십시오...": "",
    "Couldn't load the announcements. Please try again later": "공지사항을 불러올 수 없습니다. 나중에 다시 시도해 주십시오",
    "ElevenClock's log": "ElevenClock 로그",
    "Pick a color": "색상 선택"
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "클릭 시 10초간 시계 숨기기",
    "Enable low-cpu mode": "저성능 모드 사용",
    "You might lose functionalities, like the notification counter or the dynamic background": "알림 카운터, 동적 배경 등의 기능이 비활성화됩니다",
    "Clock position and size:": "시계 위치 및 크기:",
    "Clock size preferences, position offset, clock at the left, etc.": "시계 크기, 위치 조정, 왼쪽에 표시하기 등",
    "Reset monitor blacklisting status": "모니터 블랙리스트 초기화",
    "Reset": "초기화",
    "Third party licenses": "제3자 라이선스",
    "View": "보기",
    "ElevenClock": "ElevenClock",
    "Monitor tools": "모니터 도구",
    "Blacklist this monitor": "이 모니터를 블랙리스트에 추가",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "ElevenClock {0}에 사용된 제3자 오픈 소스 소프트웨어 (및 그 라이선스)",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "ElevenClock은 오픈 소스 애플리케이션이며 아래 커뮤니티 라이브러리들을 활용하여 제작되었습니다:",
    "Ok": "확인",
    "More Info": "자세히",
    "About Qt": "Qt 정보",
    "Success": "성공",
    "The monitors were unblacklisted successfully.": "모든 모니터를 블랙리스트에서 제거하였습니다.",
    "Now you should see the clock everywhere": "이제 모든 모니터에 시계가 표시될 것입니다",
    "Ok": "확인",
    "Blacklist Monitor": "모니터 블랙리스트에 추가",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "블랙리스트에 추가된 모니터에는 시계가 표시되지 않습니다.",
    "This action can be reverted from the settings window. under <b>Clock position and size</b>": "이 선택은 설정 창의 <b>시계 위치 및 크기</b>에서 되돌릴 수 있습니다.",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "모니터 \"{0}\"을(를) 블랙리스트에 추가하시겠습니까?",
    "Yes": "예",
    "No": "아니오",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "로그 새로 고침",
    "Do not show the clock on secondary monitors": "보조 모니터에 시계 표시 안 함",
    "Disable clock taskbar background color (make clock transparent)": "시계 배경 색상 사용 안 함 (시계를 투명하게 표시)",
    "Open the welcome wizard": "환영 마법사 열기",
    " (ALPHA STAGE, MAY NOT WORK)": " (알파 단계, 작동하지 않을 수 있음)",
    "Welcome to ElevenClock": "ElevenClock에 오신 것을 환영합니다",
    "Skip": "건너뛰기",
    "Start": "시작",
    "Next": "다음",
    "Finish": "마침",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "작업 관리자",
    "Change date and time": "날짜 및 시간 조정",
    "Notification settings": "알림 설정",
    "Updates, icon tray, language": "업데이트, 트레이 아이콘, 언어",
    "Hide extended options from the clock right-click menu (needs a restart to be aplied)": "시계 우클릭 메뉴에서 추가 옵션 숨기기 (재시작 필요)",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "전체화면 시 행동, 시계 위치, 주 모니터 시계, 기타 등",
    'Add the "Show Desktop" button on the left corner of every clock': '모든 시계 왼쪽에 "바탕 화면 보기" 버튼 추가',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': '이 설정은 배경 색상을 설정해야 정상 작동할 수 있습니다.&nbsp;<a href="{0}" style="color:DodgerBlue">자세한 정보</a>',
    "Clock's font, font size, font color and background, text alignment": "시계 폰트, 폰트 크기, 폰트 및 배경 색상, 정렬",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "날짜 형식, 시간 형식, 초, 요일, 주 번호 표시, 지역 설정",
    "Testing features and error-fixing tools": "테스트 기능 및 문제 해결 도구",
    "Language pack author(s), help translating ElevenClock": "언어 팩 작성자(들), ElevenClock 번역 돕기",
    "Info, report a bug, submit a feature request, donate, about": "문제 제보, 기능 요청, 기부, 정보",
    "Log, debugging information": "로그, 디버깅 정보",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen": "시계를 무조건 화면 상단에 표시하기",
    "Show the clock on the primary screen": "주 화면에 시계 표시",
    "Use a custom font color": "사용자 정의 폰트 색상",
    "Use a custom background color": "사용자 정의 배경 색상",
    "Align the clock text to the center": "시계 텍스트 가운데 정렬",
    "Select custom color": "색상 선택",
    "Hide the clock when a program occupies all screens": "한 프로그램이 모든 화면을 채울 경우 시계 숨기기",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "사용자 정의 폰트",
    "Use a custom font size": "사용자 정의 폰트 크기",
    "Enable hide when multi-monitor fullscreen apps are running": "다중 모니터 전체 화면 앱이 실행 중일 때 숨기기",
    "<b>{0}</b> needs to be enabled to change this setting": "이 설정을 변경하려면 <b>{0}</b>이(가) 활성화되어야 합니다",
    "<b>{0}</b> needs to be disabled to change this setting": "이 설정을 변경하려면 <b>{0}</b>이(가) 비활성화되어야 합니다",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": " (이 옵션은 기본적으로 작동할 것이므로 비활성화되어 있습니다. 작동하지 않는다면 버그 제보해 주세요)",
    "ElevenClock's language": "ElevenClock 언어"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Qt6 정보 (PySide6)",
    "About": "정보",
    "Alternative non-SSL update server (This might help with SSL errors)": "SSL 없는 대체 업데이트 서버 사용 (SSL 오류 해결에 도움이 될 수 있음)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "문제 해결 및 실험적 기능 (문제가 있을 경우에만 사용하세요)",
    "Show week number on the clock": "시계에 주 번호 표시",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "RDP 클라이언트 또는 Citrix Workspace 실행 중일 때 시계 숨기기",
    "Clock Appearance:": "시계 모양",
    "Force the clock to have black text": "시계를 무조건 검은 색으로 표시하기",
    " - It is required that the Dark Text checkbox is disabled": " - 검은 색으로 표시하기 옵션과 동시에 사용할 수 없음",
    "Debbugging information:": "디버그 정보",
    "Open ElevenClock's log": "ElevenClock 로그 열기",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "주 화면에 시계 표시 (시계를 왼쪽에 표시할 경우 유용함)",
    "Show weekday on the clock"  :"시계에 요일 표시",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"ElevenClock 설정", # Also settings title
    "Reload Clocks"             :"시계 다시 로드하기",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"ElevenClock 재시작",
    "Hide ElevenClock"          :"ElevenClock 숨기기",
    "Quit ElevenClock"          :"ElevenClock 종료",
    
    #General settings section
    "General Settings:"                                                                 :"일반 설정:",
    "Automatically check for updates"                                                   :"업데이트 자동으로 확인",
    "Automatically install available updates"                                           :"업데이트가 존재할 경우 자동으로 설치",
    "Enable really silent updates"                                                      :"업데이트 조용히 설치",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"업데이트 공급자 신뢰성 검증 안 함 (추천하지 않으며 책임지지 않습니다)",
    "Show ElevenClock on system tray"                                                   :"ElevenClock을 알림 영역에 표시",
    "Alternative clock alignment (may not work)"                                        :"다른 시계 정렬 사용 (작동하지 않을 수도 있음)",
    "Change startup behaviour"                                                          :"자동 시작 동작 변경",
    "Change"                                                                            :"변경",
    "<b>Update to the latest version!</b>"                                             :"<b>최신 버전으로 업데이트하세요!</b>",
    "Install update"                                                                    :"업데이트 설치",
    
    #Clock settings
    "Clock Settings:"                                              :"시계 설정:",
    "Hide the clock in fullscreen mode"                            :"전체 화면 사용 시 시계 숨기기",
    "Hide the clock when RDP client is active"                     :"RDP 클라이언트 활성 시 시계 숨기기",
    "Force the clock to be at the bottom of the screen"            :"시계를 무조건 화면 하단에 표시하기",
    "Show the clock when the taskbar is set to hide automatically" :"작업 표시줄 자동 숨김 사용 시 시계 표시하기",
    "Fix the hyphen/dash showing over the month"                   :"월 표시 뒤 하이픈/대시 표시 문제 고치기",
    "Force the clock to have white text"                           :"시계를 무조건 흰 색으로 표시하기",
    "Show the clock at the left of the screen"                     :"시계를 화면 왼쪽에 표시하기",
    
    #Date & time settings
    "Date & Time Settings:"                             :"날짜 및 시간 설정:",
    "Show seconds on the clock"                         :"시계에 초 표시",
    "Show date on the clock"                            :"시계에 날짜 표시",
    "Show time on the clock"                            :"시계에 시간 표시",
    "Change date and time format (Regional settings)"   :"날짜 및 시간 형식 변경 (지역 설정)",
    "Regional settings"                                 :"지역 설정",
    
    #About the language pack
    "About the language pack:"                  :"언어 팩 정보:",
    "Translated to English by martinet101"      :"한국어 번역: sinusinu", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"ElevenClock을 당신의 언어로 번역해주세요",
    "Get started"                               :"시작하기",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"ElevenClock 버전 {0} 정보:",
    "View ElevenClock's homepage"               :"ElevenClock 홈페이지",
    "Open"                                      :"열기",
    "Report an issue/request a feature"         :"문제 제보/기능 요청",
    "Report"                                    :"제보",
    "Support the dev: Give me a coffee☕"       :"개발자 지원: 커피 한 잔 사주기☕",
    "Open page"                                 :"페이지 열기",
    "Icons by Icons8"                           :"아이콘 제공: Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"웹페이지",
    "Close settings"                            :"설정 닫기",
    "Close"                                     :"닫기",
}

lang = lang2_3
