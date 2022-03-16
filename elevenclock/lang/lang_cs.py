# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}"
#               translation ->  "Tento text je v angličtině: hodnota {0}"

# So it would look like: "ORIGINAL_TEXT" : "TRANSLATED_TEXT",


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
    "Invalid time format\nPlease follow the\nC 1989 Standards": "Špatný formát času.\nProsím, zkontrolujte si\nstandard 1989 C.",
    "Nothing to preview": "Žádný náhled",
    "Invalid time format\nPlease modify it\nin the settings": "Špatný formát času\nProsím, upravte se\njej v nastavení",
    "Disable the tooltip shown when the clock is hovered": "Vypnout popis po najetí myší na hodiny"
}
lang_3_3 = lang_3_3_1 | {
    "Custom format rules:": "Pravidla formátování:",
    "Any text can be placed here. To place items such as date and time, please use the 1989 C standard. More info on the following link": "Zde můžete vložit jakýkoliv text. Chcete-li umístit hodnoty jako je datum a čas, použijte standard 1989 C. Více informací se dozvíte na následujícím odkaze",
    "Python date and time formats": "Formáty datumu a času jazyka Pyhton",
    "To disable the zero-padding effect, add a # in between the % and the code: non-zero-padded hours would be %#H, and zero-padded hours would be %H": "Pokud nechcete doplňovat nuly před čísla, stačí přidat znak \"#\" mezi znak \"%\", například pro hodiny bez počáteční nuly by to bylo %#H, s případnou nulou pak %H", # Here please don't modify the %H and %#H values
    "Click on Apply to apply and preview the format": "Kliknutím na \"Použít\" aplikujete vlastní formát",
    "Apply": "Použít",
    "If you don't understand what is happening, please uncheck the checkbox over the text area": "Pokud nevíte co se děje, tak odškrtněte zaškrtávátko nad textovým polem",
    "Set a custom date and time format": "Nastavit vlastní formát datumu a času",
    "(for advanced users only)": "(pouze pro pokročilé uživatele)",
    "Move this clock to the left": "Přesunout hodiny vlevo",
    "Move this clock to the top": "Přesunout hodiny nahoru",
    "Move this clock to the right": "Přesunout hodiny vpravo",
    "Move this clock to the bottom": "Přesunout hodiny dolu",
    "Restore horizontal position": "Obnovit horizontální pozici",
    "Restore vertical position": "Obnovit vertikální pozici",
}

lang_3_2_1 = lang_3_3 | {
    "Open online help to troubleshoot problems": "Otevřít online nápovědu pro řešení problémů",
    "Reset ElevenClock preferences to defaults": "Obnovit aplikaci do výchozího nastavení",
    "Specify a minimum width for the clock": "Specifikovat minimální šířku pro hodiny",
    "Search on the settings": "Vyhledávání v nastavení",
    "No results were found": "Žádné výsledky",
}

lang_3_2 = lang_3_2_1 | {
    "Use system accent color as background color": "Použít barvu motivu jako barvu pozadí",
    "Check only the focused window on the fullscreen check": "Kontrolovat pouze aktivní okno při kontrole celé obrazovky",
    "Clock on monitor {0}": "Hodiny na monitoru {0}",
    "Move to the left": "Přesunout vlevo",
    "Show this clock on the left": "Zobrazit hodiny na levé straně",
    "Show this clock on the right": "Zobrazit hodiny na pravé straně",
    "Restore clock position": "Obnovit pozici hodin",
}

lang_3_1 = lang_3_2 | {
    "W": "T", # The initial of the word week in your language: W for week, S for setmana, etc.
    "Disable the notification badge": "Vypnout ikonku upozornění notifikací",
    "Override clock default height": "Přepsat výchozí výšku hodin",
    "Adjust horizontal clock position": "Upravit horizontální pozici hodin",
    "Adjust vertical clock position": "Upravit vertikální pozici hodin",
    "Export log as a file": "Exportovat protokol do souboru",
    "Copy log to clipboard": "Zkopírovat protokol do schránky",
    "Announcements:": "Oznámení:",
    "Fetching latest announcement, please wait...": "Získávám poslední oznámení, prosím vyčkejte...",
    "Couldn't load the announcements. Please try again later": "Nelze získat oznámení. Prosím, zkuste to později",
    "ElevenClock's log": "Protokol ElevenClock",
    "Pick a color": "Vybrat barvu"
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "Skrýt hodiny po kliknutí na dobu 10 sekund",
    "Enable low-cpu mode": "Zapnout mód pro počítače se slabším procesorem",
    "You might lose functionalities, like the notification counter or the dynamic background": "Můžete ztratit některé funkce, jako počítadlo notifikací nebo dynamické pozadí",
    "Clock position and size:": "Umístění a velikost hodin",
    "Clock size preferences, position offset, clock at the left, etc.": "Velikost, pozice, umístění z leva a další",
    "Reset monitor blacklisting status": "Obnovit stav blacklistovaných monitorů",
    "Reset": "Obnovit",
    "Third party licenses": "Licence aplikací třetích stran",
    "View": "Zobrazit",
    "ElevenClock": "ElevenClock",
    "Monitor tools": "Nástroje monitoru",
    "Blacklist this monitor": "Umístit tento monitor na blacklist",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "Aplikace s otevřeným zdrojovým kódem třetích stran v ElevenClock {0} (a jejich licence)",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "ElevenClock je aplikace s otevřeným zdrojovým kódem, která vznikla za pomocí dalších knihovem vytvořených komunitou:",
    "Ok": "Ok",
    "More Info": "Více informací",
    "About Qt": "O Qt",
    "Success": "Úspěch",
    "The monitors were unblacklisted successfully.": "Všechny monitory byly odebrány z blacklistu.",
    "Now you should see the clock everywhere": "Hodiny nyní uvidíte všude",
    "Blacklist Monitor": "Blacklist monitoru",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "Blacklistování monitoru trvale skryje hodiny na daném monitoru.",
    "This action can be reverted from the settings window, under <b>Clock position and size</b>": "Tato akce může být změněna z nastavení pod volbou <b>Umístění a velikost hodin</b>",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "Jste si jistí, že chcete umístit monitor \"{0}\" na blacklist?",
    "Yes": "Ano",
    "No": "Ne",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "Znovu načíst protokol",
    "Do not show the clock on secondary monitors": "Nezobrazovat hodiny na sekundárním monitoru",
    "Disable clock taskbar background color (make clock transparent)": "Vypnout barvu pozadí hodin na hlavní liště (hodiny budou průhledné)",
    "Open the welcome wizard": "Otevřít průvodce prvního spuštění",
    " (ALPHA STAGE, MAY NOT WORK)": " (TESTOVACÍ FÁZE, NEMUSÍ FUNGOVAT)",
    "Welcome to ElevenClock": "Vítejte v ElevenClock",
    "Skip": "Přeskočit",
    "Start": "Začít",
    "Next": "Další",
    "Finish": "Dokončit",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "Správce úloh",
    "Change date and time": "Upravit datum a čas",
    "Notification settings": "Nastavení oznámení",
    "Updates, icon tray, language": "Aktualizace, lokalizace a ikonka lišty",
    "Hide extended options from the clock right-click menu (needs a restart to be applied)": "Skrýt rozšířené možnosti z nabídky po kliknutí pravým tlačítkem myši (aplikace vyžaduje restart)",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "Chování na celé obrazovce, pozice hodin a další různá nastavení",
    'Add the "Show Desktop" button on the left corner of every clock': 'Přidat tlačítko "Zobrazit plochu" ke všem hodinám',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': 'Pro správnou funkčnost budete muset nejspíš změnit barvu pozadí.&nbsp;Pro více info <a href="{0}" style="color:DodgerBlue">zde</a>',
    "Clock's font, font size, font color and background, text alignment": "Styl, velikost a barva písma, barva pozadí a zarovnání textu",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "Formát data a času, sekundy, dny v týdnu, číslo dne a regionální nastavení",
    "Testing features and error-fixing tools": "Testovací funkce a nástroje pro opravu chyb",
    "Language pack author(s), help translating ElevenClock": "Autoři lokalizace a pomoc s překladem aplikace ElevenClock",
    "Info, report a bug, submit a feature request, donate, about": "Informace, hlášení chyb, žádosti o nové funknce a darování",
    "Log, debugging information": "Ladící informace a protokoly",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen": "Vynutit, aby byly hodiny ve horní části obrazovky",
    "Show the clock on the primary screen": "Zobrazit hodiny na hlavní obrazovce",
    "Use a custom font color": "Použít vlastní barvu písma",
    "Use a custom background color": "Použít vlastní barvu pozadí",
    "Align the clock text to the center": "Vycentrovat text hodin",
    "Select custom color": "Vybrat vlastní barvu",
    "Hide the clock when a program occupies all screens": "Skrýt hodiny, když je aplikace na všech obrazovkách",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "Použít vlastní styl písma",
    "Use a custom font size": "Použít vlastní velikost písma",
    "Enable hide when multi-monitor fullscreen apps are running": "Umožnit skrytí, když beží celoobrazovkové aplikace pro více monitorů",
    "<b>{0}</b> needs to be enabled to change this setting": "Pro změnu tohoto nastavení je třeba povolit: <b>{0}</b>",
    "<b>{0}</b> needs to be disabled to change this setting": "Pro změnu tohoto nastavení je třeba deaktivovat: <b>{0}</b>",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": "Tato funkce byla deaktivována, protože by měla fungovat ve výchozím nastavení. Pokud ne, nahlaste prosím chybu",
    "ElevenClock's language": "Jazyk ElevenClock"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "O Qt6 (PySide6)",
    "About": "O",
    "Alternative non-SSL update server (This might help with SSL errors)": "Alternativní aktualizační server bez SSL (Může pomoci s SSL chybami)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Opravy a další experimentální funkce (Použijte POUZE v případě, že něco nefunguje)",
    "Show week number on the clock": "Zobrazit číslo týdne na hodinách"
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Skrýt hodiny, když běží RDP Client nebo Citrix Workspace",
    "Clock Appearance:": "Vzhled hodin",
    "Force the clock to have black text": "Vynutit černý text hodin",
    " - It is required that the Dark Text checkbox is disabled": " - Toto vyžaduje vypnuté nastavení zobrazování černého textu",
    "Debbugging information:": "Informace o ladění",
    "Open ElevenClock's log": "Otevřít protokol ElevenClock",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Zobrazit hodiny na hlavní obrazovce (Užitečné, pokud jsou nastaveny hodiny vlevo)",
    "Show weekday on the clock": "Zobrazit den v týdnu na hodinách",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"Nastavení ElevenClock", # Also settings title
    "Reload Clocks"             :"Znovu načíst hodiny",
    "ElevenClock v{0}"          :"ElevenClock verze {0}",
    "Restart ElevenClock"       :"Restartovat ElevenClock",
    "Hide ElevenClock"          :"Skrýt ElevenClock",
    "Quit ElevenClock"          :"Ukončit ElevenClock",

    #General settings section
    "General Settings:"                                                                 :"Obecné nastavení",
    "Automatically check for updates"                                                   :"Automaticky kontrolovat aktualizace",
    "Automatically install available updates"                                           :"Automaticky instalovat dostupné aktualizace",
    "Enable really silent updates"                                                      :"Povolit opravdu tiché aktualizace",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Vynechat kontrolu pravosti poskytovatele aktualizací (NEDOPORUČUJEME, NA VAŠE VLASTNÍ RIZIKO)",
    "Show ElevenClock on system tray"                                                   :"Zobrazit ElevenClock na systémové liště",
    "Alternative clock alignment (may not work)"                                        :"Alternativní zarovnání hodin (nemusí fungovat)",
    "Change startup behaviour"                                                          :"Změňit chování při spouštění",
    "Change"                                                                            :"Změnit",
    "<b>Update to the latest version!</b>"                                             :"<b>Aktualizujte na nejnovější verzi!</b>",
    "Install update"                                                                    :"Instalovat aktualizaci",

    #Clock settings
    "Clock Settings:"                                              :"Nastavení hodin",
    "Hide the clock in fullscreen mode"                            :"Skrýt hodiny v celoobrazovém režimu",
    "Hide the clock when RDP client is active"                     :"Skrýt hodiny, když je RDP client aktivní",
    "Force the clock to be at the bottom of the screen"            :"Vynutit, aby byly hodiny ve spodní části obrazovky",
    "Show the clock when the taskbar is set to hide automatically" :"Zobrazit hodiny, když je hlavní panel nastaven na automatické skrytí",
    "Fix the hyphen/dash showing over the month"                   :"Opravuje pomlčku zobrazovanou v průběhu měsíce",
    "Force the clock to have white text"                           :"Vynutit, aby hodiny měly bílý text",
    "Show the clock at the left of the screen"                     :"Zobrazit hodiny v levé části obrazovky",

    #Date & time settings
    "Date & Time Settings:"                             :"Nastavení data a času",
    "Show seconds on the clock"                         :"Zobrazit sekundy na hodinách",
    "Show date on the clock"                            :"Zobrazit datum na hodinách",
    "Show time on the clock"                            :"Ukázat čas na hodinách",
    "Change date and time format (Regional settings)"   :"Změnit formát data a času (regionální nastavení)",
    "Regional settings"                                 :"Regionální nastavení",

    #About the language pack
    "About the language pack:"                  :"O jazykovém balíčku",
    "Translated to English by martinet101"      :"Do češtiny přeložili Matouš Adamů, panther7 a SunightMC", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc.
    "Translate ElevenClock to your language"    :"Přeložte ElevenClock do svého jazyka",
    "Get started"                               :"Začít",

    #About ElevenClock
    "About ElevenClock version {0}:"            :"O verzi ElevenClock {0}",
    "View ElevenClock's homepage"               :"Zobrazit domovskou stránku aplikace ElevenClock",
    "Open"                                      :"Otevřít",
    "Report an issue/request a feature"         :"Nahlásit problém/požádat o funkci",
    "Report"                                    :"Hlášení",
    "Support the dev: Give me a coffee☕"       :"Podpořte vývojáře: Pošlete mi kávu ☕",
    "Open page"                                 :"Otevřít stránku",
    "Icons by Icons8"                           :"Ikony vytvořil Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Webová stránka",
    "Close settings"                            :"Zavřít nastavení",
    "Close"                                     :"Zavřít",
}

lang = lang2_3
