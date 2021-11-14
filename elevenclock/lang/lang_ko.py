# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang2_7_bis = {
    "Use a custom font": "",
    "Use a custom font size": "",
    "Enable hide when multi-monitor fullscreen apps are running": "",
    "<b>{0}</b> needs to be enabled to change this setting": "",
    "<b>{0}</b> needs to be disabled to change this setting": "",
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
