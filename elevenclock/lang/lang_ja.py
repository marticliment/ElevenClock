# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
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
    "Invalid time format\nPlease follow the\nC 1989 Standards": "時刻形式の誤り\nC 1989標準形式に\n従ってください",
    "Nothing to preview": "プレビューはありません",
    "Invalid time format\nPlease modify it\nin the settings": "時刻形式の誤り\n設定画面にて\n変更してください",
    "Disable the tooltip shown when the clock is hovered": "時計にマウスホバーしたときに表示されるツールチップを無効にする"
}
lang_3_3 = lang_3_3_1 | {
    "Custom format rules:": "カスタム形式ルール",
    "Any text can be placed here. To place items such as date and time, please use the 1989 C standard. More info on the following link": "ここには任意のテキストを配置できます。日付や時刻などを配置するには、1989 C Standard を使用してください。詳細は次のリンクをご参照ください",
    "Python date and time formats": "Python の日時形式",
    "To disable the zero-padding effect, add a # in between the % and the code: non-zero-padded hours would be %#H, and zero-padded hours would be %H": "0の追加を無効化するには、 # を % と文字の間に追加してください: 1桁のときに0の追加をしない「○時」表記 (例:9) は %#H, 1桁のときに0の追加をする「○時」表記 (例:09) は %H のようになります。", # Here please don't modify the %H and %#H values
    "Click on Apply to apply and preview the format": "適用・プレビューするには「適用」をクリックしてください",
    "Apply": "適用",
    "If you don't understand what is happening, please uncheck the checkbox over the text area": "何が起こるかを理解していない場合は、入力欄上のチェックボックスをオフにしてください。",
    "Set a custom date and time format": "カスタム日時形式を設定",
    "(for advanced users only)": "(上級者向け)",
    "Move this clock to the left": "この時計を画面左に移動",
    "Move this clock to the top": "この時計を画面上に移動",
    "Move this clock to the right": "この時計を画面右に移動",
    "Move this clock to the bottom": "この時計を画面下に移動",
    "Restore horizontal position": "水平位置を復元する",
    "Restore vertical position": "垂直位置を復元する",
}

lang_3_2_1 = lang_3_3 | {
    "Open online help to troubleshoot problems": "オンラインヘルプを開いて問題のトラブルシューティングを行う",
    "Reset ElevenClock preferences to defaults": "ElevenClockの設定を既定にリセットする",
    "Specify a minimum width for the clock": "特定の時計の最小幅を指定する",
    "Search on the settings": "設定項目を検索",
    "No results were found": "該当する結果はありません",
}

lang_3_2 = lang_3_2_1 | {
    "Use system accent color as background color": "背景色にシステムアクセントカラーを使用する",
    "Check only the focused window on the fullscreen check": "全画面の確認をアクティブなウィンドウの確認のみにする",
    "Clock on monitor {0}": "モニター {0} の時計",
    "Move to the left": "左に移動する",
    "Show this clock on the left": "この時計を左に表示する",
    "Show this clock on the right": "この時計を右に表示する",
    "Restore clock position": "時計の位置を復元する",
}

lang_3_1 = lang_3_2 | {
    "W": "週", # The initial of the word week in your language: W for week, S for setmana, etc.
    "Disable the notification badge": "通知バッジを無効にする",
    "Override clock default height": "時計の既定の高さを上書きする",
    "Adjust horizontal clock position": "時計の水平位置を調整する",
    "Adjust vertical clock position": "時計の垂直位置を調整する",
    "Export log as a file": "ログをファイルにエクスポート",
    "Copy log to clipboard": "ログをクリップボードにコピー",
    "Announcements:": "お知らせ",
    "Fetching latest announcement, please wait...": "最新のお知らせを取得中です。しばらくお待ちください。",
    "Couldn't load the announcements. Please try again later": "お知らせを読み込めませんでした。後ほど再度お試しください。",
    "ElevenClock's log": "ElevenClockのログ",
    "Pick a color": "色を選択"
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "クリック時に10秒間時計を非表示にする",
    "Enable low-cpu mode": "低CPUモードを有効にする",
    "You might lose functionalities, like the notification counter or the dynamic background": "通知カウンターや動的な背景などの機能が失われる可能性があります",
    "Clock position and size:": "時計の位置とサイズ",
    "Clock size preferences, position offset, clock at the left, etc.": "時計の位置の設定、位置オフセット、時計を左に表示、その他",
    "Reset monitor blacklisting status": "モニターのブラックリストの状態をリセットする",
    "Reset": "リセット",
    "Third party licenses": "サードパーティーのライセンス",
    "View": "表示",
    "ElevenClock": "ElevenClock",
    "Monitor tools": "モニターツール",
    "Blacklist this monitor": "このモニターをブラックリストに登録する",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "Elevenclock {0}のサードパーティーオープンソースソフトウェア(とそれらのライセンス)",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "ElevenClockはコミュニティによって作成された他のライブラリの助けを借りて作成されたオープンソースアプリケーションです",
    "Ok": "OK",
    "More Info": "詳細情報",
    "About Qt": "Qtについて",
    "Success": "成功",
    "The monitors were unblacklisted successfully.": "このモニターのブラックリスト登録解除に成功しました。",
    "Now you should see the clock everywhere": "これですべてに時計が表示されるはずです",
    "Ok": "OK",
    "Blacklist Monitor": "モニターのブラックリスト登録",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "モニターをブラックリストに登録すると、このモニターで完全に時計が非表示になります。",
    "This action can be reverted from the settings window, under <b>Clock position and size</b>": "この操作は設定ウィンドウから元に戻すことができます。<b>時計の位置とサイズ</b>の中に含まれています。",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "モニター \"{0}\"をブラックリストに登録しますか?",
    "Yes": "はい",
    "No": "いいえ",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "ログを再読み込み",
    "Do not show the clock on secondary monitors": "セカンダリー画面に時計を表示しない",
    "Disable clock taskbar background color (make clock transparent)": "時計のタスクバーの背景色を無効にする (時計が透明になります)",
    "Open the welcome wizard": "ようこそウィザードを開く",
    " (ALPHA STAGE, MAY NOT WORK)": "(アルファ版のため、動作しません)",
    "Welcome to ElevenClock": "ElevenClock へようこそ",
    "Skip": "スキップ",
    "Start": "スタート",
    "Next": "次へ",
    "Finish": "完了",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "タスク マネージャー",
    "Change date and time": "日付と時刻の変更",
    "Notification settings": "通知設定",
    "Updates, icon tray, language": "更新、トレイ アイコン、言語",
    "Hide extended options from the clock right-click menu (needs a restart to be applied)": "時計を右クリックメニューから拡張オプションを隠す (適用のために再起動が必要)",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "全画面時の動作、時計の位置、プライマリー画面の時計、その他の設定",
    'Add the "Show Desktop" button on the left corner of every clock': 'すべての時計の左端に「デスクトップを表示」ボタンを追加する',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': 'これを正しく機能させるためにカスタム背景色を設定する必要がある場合があります。&nbsp;詳細情報は<a href="{0}" style="color:DodgerBlue">こちら</a>',
    "Clock's font, font size, font color and background, text alignment": "時計のフォント、フォント サイズ、フォントの色と背景、テキストの配置",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "日付の形式、時刻の形式、秒、曜日、週番号、地域の設定",
    "Testing features and error-fixing tools": "テスト中の機能とエラー修正用のツール",
    "Language pack author(s), help translating ElevenClock": "言語パックの編集者、ElevenClock の翻訳を手伝う",
    "Info, report a bug, submit a feature request, donate, about": "情報、バグの報告、機能リクエストの投稿、寄付、その他に関して",
    "Log, debugging information": "ログ、デバッグ情報",
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
