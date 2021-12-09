# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_2_9 = {
    "Task Manager": "",
    "Change date and time": "",
    "Notification settings": "",
    "Updates, icon tray, language": "",
    "Hide extended options from the clock right-click menu (needs a restart to be aplied)": "",
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
    "Force the clock to be at the top of the screen": "画面の最前面に時計の表示を強制する",
    "Show the clock on the primary screen": "プライマリー画面に時計を表示する",
    "Use a custom font color": "カスタムフォント色を使用する",
    "Use a custom background color": "カスタム背景色を使用する",
    "Align the clock text to the center": "時計のテキストを中央寄せにする",
    "Select custom color": "カスタム色の選択",
    "Hide the clock when a program occupies all screens": "全画面アプリケーション使用時に時計を非表示にする",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "カスタムフォントを使用する",
    "Use a custom font size": "カスタムフォントサイズを使用する",
    "Enable hide when multi-monitor fullscreen apps are running": "マルチモニターの全画面アプリを実行中は時計を非表示にする",
    "<b>{0}</b> needs to be enabled to change this setting": "この設定を変更するには<b>{0}</b>を有効にする必要があります",
    "<b>{0}</b> needs to be disabled to change this setting": "この設定を変更するには<b>{0}</b>を無効にする必要があります",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": "（この機能はデフォルトで動作するため無効になっています。動作しない場合はバグとして報告してください）",
    "ElevenClock's language": "ElevenClockの言語"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Qt6（PySide6）について",
    "About": "開く",
    "Alternative non-SSL update server (This might help with SSL errors)": "非SSLの代替サーバーでアップデートする（SSLエラーの対処に役立つ場合があります）",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "修正やその他の試験機能：（上手く動作しない場合のみ使用してください）",
    "Show week number on the clock": "時計に週番号を表示する",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "RDPクライアントまたはCitrix Workspaceの実行中に時計を表示しない",
    "Clock Appearance:": "時計の外観",
    "Force the clock to have black text": "強制的に時計の文字色を黒にする",
    " - It is required that the Dark Text checkbox is disabled": " - 暗い文字色のチェックボックスが無効になっている必要があります",
    "Debbugging information:": "デバッグ情報",
    "Open ElevenClock's log": "ElevenClockのログを開く",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "プライマリー画面に時計を表示する（時計を左に配置しているときに便利）",
    "Show weekday on the clock"  :"時計に曜日を表示する",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"ElevenClockの設定", # Also settings title
    "Reload Clocks"             :"時計を再読み込みする",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"ElevenClockを再起動する",
    "Hide ElevenClock"          :"ElevenClockを非表示にする",
    "Quit ElevenClock"          :"ElevenClockを終了する",
    
    #General settings section
    "General Settings:"                                                                 :"一般設定：",
    "Automatically check for updates"                                                   :"アップデートを自動で確認する",
    "Automatically install available updates"                                           :"利用可能なアップデートを自動でインストールする",
    "Enable really silent updates"                                                      :"とても静かなアップデートを有効にする",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"アップデートプロバイダーの認証をバイパスする（非推奨。自己責任で有効化してください）",
    "Show ElevenClock on system tray"                                                   :"ElevenClockをシステムトレイに表示",
    "Alternative clock alignment (may not work)"                                        :"時計の配置方法を代替の方法にする（動作しない場合があります）",
    "Change startup behaviour"                                                          :"起動時の挙動を変更する",
    "Change"                                                                            :"変更",
    "<b>Update to the latest version!</b>"                                             :"<b>最新のバージョンにアップデートしてください！</b>",
    "Install update"                                                                    :"アップデートをインストールする",
    
    #Clock settings
    "Clock Settings:"                                              :"時計の設定：",
    "Hide the clock in fullscreen mode"                            :"全画面モードで時計を非表示にする",
    "Hide the clock when RDP client is active"                     :"RDPクライアントの動作中に時計を非表示にする",
    "Force the clock to be at the bottom of the screen"            :"時計を強制的に画面下部に配置する",
    "Show the clock when the taskbar is set to hide automatically" :"タスクバーを自動で非表示にする設定の場合にも時計を表示する",
    "Fix the hyphen/dash showing over the month"                   :"月の上に表示されるハイフンやダッシュを修正する",
    "Force the clock to have white text"                           :"時計の文字色を強制的に白にする",
    "Show the clock at the left of the screen"                     :"時計を画面の左側に表示する",
    
    #Date & time settings
    "Date & Time Settings:"                             :"日付と時刻の設定：",
    "Show seconds on the clock"                         :"時計に秒を表示する",
    "Show date on the clock"                            :"時計に日付を表示する",
    "Show time on the clock"                            :"時計に時刻を表示する",
    "Change date and time format (Regional settings)"   :"日付と時刻の形式を変更する（地域設定）",
    "Regional settings"                                 :"地域設定",
    
    #About the language pack
    "About the language pack:"                  :"言語パックについて",
    "Translated to English by martinet101"      :"Robot-Inventor, ShintakuNobuhiro によって日本語に翻訳されました", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"ElevenClockをあなたの言語に翻訳する",
    "Get started"                               :"はじめる",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"ElevenClockバージョン{0}について:",
    "View ElevenClock's homepage"               :"ElevenClockのホームページを表示する",
    "Open"                                      :"開く",
    "Report an issue/request a feature"         :"問題の報告や機能のリクエストをする",
    "Report"                                    :"報告",
    "Support the dev: Give me a coffee☕"       :"開発を支援する: コーヒーをください☕",
    "Open page"                                 :"ページを開く",
    "Icons by Icons8"                           :"Icons8によるアイコン", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Webページ",
    "Close settings"                            :"設定を閉じる",
    "Close"                                     :"閉じる",
}

lang = lang2_3
