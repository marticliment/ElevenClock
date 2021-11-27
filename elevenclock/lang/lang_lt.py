# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}"
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_2_8 = {
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
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": " (Ši funkcija išjungta, nes ji turėtų veikti besąlygiškai. Jei neveikia, praneškite apie klaidą)",
    "ElevenClock's language": "ElevenClock kalba"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Apie Qt6 (PySide6)",
    "About": "Apie",
    "Alternative non-SSL update server (This might help with SSL errors)": "Alternatyvus ne-SSL atnaujinimo serveris (Gali padėti su SSL klaidomis)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Pataisymai ir kitos eksperimentinės funkcijos: (Naudokite TIK tuomet kai kažkas neveikia)",
    "Show week number on the clock": "Rodyti savaitės numerį laikrodyje"
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Slėpti laikrodį kai \"RDP Client\" ar \"Citrix Workspace\" veikia",
    "Clock Appearance:": "Laikrodžio išvaizda:",
    "Force the clock to have black text": "Priversti laikrodį rodyti juodą tekstą",
    " - It is required that the Dark Text checkbox is disabled": " - Tamsaus Teksto langelis turi būti nepažymėtas",
    # Source: https://lt.m.wiktionary.org/wiki/derinti
    "Debbugging information:": "Derinimo informacija:",
    "Open ElevenClock's log": "Atidaryti ElevenClock žurnalą",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Rodyti laikrodį pagrindiniam ekrane (Naudinga jei laikrodis kairėje)",
    "Show weekday on the clock": "Rodyti savaitės dieną laikrodyje",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings": "ElevenClock Nustatymai",  # Also settings title
    "Reload Clocks": "Perkurti laikrodžius",
    "ElevenClock v{0}": "ElevenClock v{0}",
    "Restart ElevenClock": "Perkrauti ElevenClock",
    "Hide ElevenClock": "Slėpti ElevenClock",
    "Quit ElevenClock": "Išeiti iš ElevenClock",

    #General settings section
    "General Settings:": "Pagrindiniai nustatymai:",
    "Automatically check for updates": "Automatiškai tikrinti ar nėra atnaujinimų",
    "Automatically install available updates": "Automatiškai diegti atnaujinimus",
    "Enable really silent updates": "Įjungti labai tylius atnaujinimus",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)": "Apeiti atnaujinimų tiekėjo autentiškumo patikrą (NEREKOMENDUOJAMA)",
    "Show ElevenClock on system tray": "Rodyti ElevenClock sistemos dėkle",
    "Alternative clock alignment (may not work)": "Alternatyvus laikrodžio lygiavimas (gali neveikti)",
    "Change startup behaviour": "Keisti paleidimo elgesį",
    "Change": "Keisti",
    "<b>Update to the latest version!</b>": "<b>Atnaujinti į naujausią versiją!</b>",
    "Install update": "Diegti atnaujinimą",

    #Clock settings
    "Clock Settings:": "Laikrodžio Nustatymai:",
    "Hide the clock in fullscreen mode": "Slėpti laikrodį pilno ekrano režime",
    "Hide the clock when RDP client is active": "Slėpti laikrodį kai \"RDP Client\" veikia",
    "Force the clock to be at the bottom of the screen": "Priverstinai rodyti laikrodį ekrano apačioje",
    "Show the clock when the taskbar is set to hide automatically": "Rodyti laikrodį kai užduočių juosta paslėpiama automatiškai",
    "Fix the hyphen/dash showing over the month": "Sutaisyti brūkšnelį rodomą ant mėnesio",
    "Force the clock to have white text": "Priversti laikrodį rodyti baltą tekstą",
    "Show the clock at the left of the screen": "Rodyti laikrodį ekrano kairėje",

    #Date & time settings
    "Date & Time Settings:": "Datos ir Laiko Nustatymai:",
    "Show seconds on the clock": "Rodyti sekundes laikrodyje",
    "Show date on the clock": "Rodyti datą laikrodyje",
    "Show time on the clock": "Rodyti laiką laikrodyje",
    "Change date and time format (Regional settings)": "Keisti datos ir laiko formatą (Regioniniai Nustatymai)",
    "Regional settings": "Regioniniai nustatymai",

    #About the language pack
    "About the language pack:": "Apie kalbos paketą:",
    # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc.
    "Translated to English by martinet101": "Į lietuvių kalbą išvertė generic pleb",
    "Translate ElevenClock to your language": "Išverskite ElevenClock į jūsų kalbą",
    "Get started": "Pradėti",

    #About ElevenClock
    "About ElevenClock version {0}:": "Apie ElevenClock versiją {0}:",
    "View ElevenClock's homepage": "Atidaryti ElevenClock svetainę",
    "Open": "Atidaryti",
    "Report an issue/request a feature": "Pranešti apie klaidą/prašyti funkcijos",
    "Report": "Pranešti",
    "Support the dev: Give me a coffee☕": "Palaikykite kūrėją: Duokite man kavos☕",
    "Open page": "Atidaryti puslapį",
    # Here, the word "Icons8" should not be translated
    "Icons by Icons8": "Ikonėlės Icons8",
    "Webpage": "Svetainė",
    "Close settings": "Uždaryti nustatymus",
    "Close": "Uždaryti",
}

lang = lang2_3
