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
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": "（この機能はデフォルトで動作するため無効になっています。動作しない場合はバグとして報告してください）",
    "ElevenClock's language": "ElevenClockの言語"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Qt6（PySide6）について",
    "About": "開く",
    "Alternative non-SSL update server (This might help with SSL errors)": "非SSLの代替サーバーでアップデートする（SSLエラーの対処に役立つ場合があります）",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "修正やその他の試験機能：（上手く動作しない場合のみ使用してください）",
    "Show week number on the clock": "時計に曜日の番号を表示する",
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
    "Alternative clock alignment (may not work)"                                        :"時計を別の配置にする（動作しない場合があります）",
    "Change startup behaviour"                                                          :"起動時の挙動を変更する",
    "Change"                                                                            :"変更",
    "<b>Update to the latest version!</b>"                                             :"<b>最新のバージョンにアップデートする</b>",
    "Install update"                                                                    :"アップデートをインストールする",
    
    #Clock settings
    "Clock Settings:"                                              :"時計の設定：",
    "Hide the clock in fullscreen mode"                            :"全画面モードで時計を非表示にする",
    "Hide the clock when RDP client is active"                     :"RDPクライアントの動作中に時計を非表示にする",
    "Force the clock to be at the bottom of the screen"            :"時計を強制的に画面下部に配置する",
    "Show the clock when the taskbar is set to hide automatically" :"タスクバーを自動で非表示にする設定の場合に時計を表示する",
    "Fix the hyphen/dash showing over the month"                   :"月の上に表示されるハイフンやダッシュを修正する",
    "Force the clock to have white text"                           :"時計の文字色を強制的に白にする",
    "Show the clock at the left of the screen"                     :"時計を画面の左側に表示する",
    
    #Date & time settings
    "Date & Time Settings:"                             :"日付と時刻の設定：",
    "Show seconds on the clock"                         :"時計に秒を表示する",
    "Show date on the clock"                            :"時計に日付を表示する",
    "Show time on the clock"                            :"時計に時刻を表示する",
    "Change date and time format (Regional settings)"   :"日付と時刻のフォーマットを変更する（地域設定）",
    "Regional settings"                                 :"地域設定",
    
    #About the language pack
    "About the language pack:"                  :"言語パックについて",
    "Translated to English by martinet101"      :"Robot-Inventorによって日本語に翻訳されました", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"ElevenClockをあなたの言語に翻訳する",
    "Get started"                               :"はじめる",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"ElevenClockバージョン{0}について:",
    "View ElevenClock's homepage"               :"ElevenClockのホームページを表示する",
    "Open"                                      :"表示",
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
