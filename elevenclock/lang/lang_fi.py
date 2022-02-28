# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_3 = {
    "Custom format rules:": "",
    "Any text can be placed here. To place items such as date and time, please use the 1989 C standard. More info on the following link": "",
    "Python date and time formats": "",
    "To disable the zero-padding effect, add a # in between the % and the code: non-zero-padded hours would be %#H, and zero-padded hours would be %H": "", # Here please don't modify the %H and %#H values
    "Click on Apply to apply and preview the format": "",
    "Apply": "",
    "If you don't understand what is happening, please uncheck the checkbox over the text area": "",
    "Set a custom date and time format": "",
    "(for advanced users only)": "",
    "Move this clock to the left": "",
    "Move this clock to the top": "",
    "Move this clock to the right": "",
    "Move this clock to the bottom": "",
    "Restore horizontal position": "",
    "Restore vertical position": "",
}

lang_3_2_1 = lang_3_3 | {
    "Open online help to troubleshoot problems": "",
    "Reset ElevenClock preferences to defaults": "",
    "Specify a minimum width for the clock": "",
    "Search on the settings": "",
    "No results were found": "",
}

lang_3_2 = lang_3_2_1 | {
    "Use system accent color as background color": "",
    "Check only the focused window on the fullscreen check": "",
    "Clock on monitor {0}": "",
    "Move to the left": "",
    "Show this clock on the left": "",
    "Show this clock on the right": "",
    "Restore clock position": "",
}

lang_3_1 = lang_3_2 | {
    "W": "vko", # The initial of the word week in your language: W for week, S for setmana, etc.
    "Disable the notification badge": "Poista ilmoitusmerkki käytöstä",
    "Override clock default height": "Ohita kellon oletuskorkeus",
    "Adjust horizontal clock position": "Säädä kellon vaakasuorainen sijainti",
    "Adjust vertical clock position": "Säädä kellon pystysuorainen sijainti",
    "Export log as a file": "Vie loki tiedostona",
    "Copy log to clipboard": "Kopioi loki leikepöydälle",
    "Announcements:": "Tiedotteet",
    "Fetching latest announcement, please wait...": "Haetaan viimeisimpiä tiedotteita, odota...",
    "Couldn't load the announcements. Please try again later": "Tiedotteita ei voitu ladata. Yritä myöhemmin uudelleen.",
    "ElevenClock's log": "ElevenClockin loki",
    "Pick a color": "Valitse väri"
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "Piilota kello 10 sekunnin ajaksi, kun sitä napsauttaa",
    "Enable low-cpu mode": "Ota käyttöön low-cpu-tila",
    "You might lose functionalities, like the notification counter or the dynamic background": "Saatat menettää joitain toimintoja, kuten ilmoituslaskurin tai dynaamisen taustan",
    "Clock position and size:": "Kellon sijainti ja koko:",
    "Clock size preferences, position offset, clock at the left, etc.": "Kellon koon asetukset, sijainnin siirto, kello vasemmalla jne.",
    "Reset monitor blacklisting status": "Palauta näytön mustan listan tila",
    "Reset": "Palauta",
    "Third party licenses": "Kolmannen osapuolen lisenssit",
    "View": "Näytä",
    "ElevenClock": "ElevenClock",
    "Monitor tools": "Näytön työkalut",
    "Blacklist this monitor": "Lisää tämä näyttö mustalle listalle",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "Kolmannen osapuolen avoimen lähdekoodin ohjelmistot ElevenClockissa {0} (ja niiden lisenssit)",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "ElevenClock on avoimen lähdekoodin sovellus, joka on tehty muiden yhteisön tekemien kirjastojen avulla:",
    "Ok": "Ok",
    "More Info": "Lisätietoja",
    "About Qt": "Tietoja Qt:stä",
    "Success": "Onnistui",
    "The monitors were unblacklisted successfully.": "Näytöt lisättiin mustalle listalle onnistuneesti.",
    "Now you should see the clock everywhere": "Nyt sinun pitäisi nähdä kello kaikkialla",
    "Ok": "Ok",
    "Blacklist Monitor": "Lisää näyttö mustalle listalle",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "Näytön lisääminen mustalle listalle piilottaa kyseisen näytön kellon pysyvästi.",
    "This action can be reverted from the settings window, under <b>Clock position and size</b>": "Tämä toiminto voidaan peruuttaa asetusikkunasta, kohdan <b>Kellon sijainti ja koko</b> alta.",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "Oletko varma että haluat lisätä näytön \"{0}\" mustalle listalle?",
    "Yes": "Kyllä",
    "No": "En",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "Lataa loki uudelleen",
    "Do not show the clock on secondary monitors": "Älä näytä kelloa toissijaisissa näytöissä",
    "Disable clock taskbar background color (make clock transparent)": "Poista kellon tehtäväpalkin taustaväri käytöstä (tee kellosta läpinäkyvä)",
    "Open the welcome wizard": "Avaa tervetuloikkuna",
    " (ALPHA STAGE, MAY NOT WORK)": " (ALFA VAIHEESSA, EI VÄLTTÄMÄTTÄ TOIMI)",
    "Welcome to ElevenClock": "Tervetuloa ElevenClockiin",
    "Skip": "Ohita",
    "Start": "Aloita",
    "Next": "Seuraava",
    "Finish": "Lopeta",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "Tehtävienhallinta",
    "Change date and time": "Vaihda pävämäärää ja kellonaikaa",
    "Notification settings": "Ilmoitusasetukset",
    "Updates, icon tray, language": "Päivitykset, pikkukuvake, kieli",
    "Hide extended options from the clock right-click menu (needs a restart to be applied)": "Laajennettujen vaihtoehtojen piilottaminen kellon hiiren oikealla painikkeella napsautettavasta valikosta (vaatii uudelleenkäynnistyksen toimiakseen)",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "Koko näytön -tilan käyttäytyminen, kellon sijainti, ensisijaisen näytön kello, muut sekalaiset asetukset",
    'Add the "Show Desktop" button on the left corner of every clock': 'Lisää "Näytä työpöytä" -painike jokaisen kellon vasempaan kulmaan',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': 'Sinun on ehkä asetettava mukautettu taustaväri, jotta tämä toimii.&nbsp;Lisätietoja <a href="{0}" style="color:DodgerBlue">täällä</a>',
    "Clock's font, font size, font color and background, text alignment": "Kellon fontti, fonttikoko, fontin väri ja tausta, tekstin sijoittelu",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "Päivämäärän ja ajan formaatti, sekunnit, viikonpäivä, vikkonumero, alueelliset asetukset",
    "Testing features and error-fixing tools": "Testausominaisuudet ja virheenkorjaustyökalut",
    "Language pack author(s), help translating ElevenClock": "Kielipaketin kirjoittaja(t), apua ElevenClockin kääntämisessä",
    "Info, report a bug, submit a feature request, donate, about": "Info, ilmoita virheestä, lähetä ominaisuuspyyntö, lahjoita, tietoja",
    "Log, debugging information": "Loki, virheenkorjaustiedot",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen": "Pakota kkello näytön yläreunaan",
    "Show the clock on the primary screen": "Näytä kello ensisijaisessa näytössä",
    "Use a custom font color": "Käytä mukautettua fontin väriä",
    "Use a custom background color": "Käytä mukautettua taustaväriä",
    "Align the clock text to the center": "Kohdista kelloteksti keskelle",
    "Select custom color": "Valitse mukautettu väri",
    "Hide the clock when a program occupies all screens": "Piilota kello, kun ohjelma vie kaikki näytöt",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "Käytä mukautettua fonttia",
    "Use a custom font size": "Käytä mukautettua fonttikokoa",
    "Enable hide when multi-monitor fullscreen apps are running": "Ota piilotus käyttöön, kun usean näytön kokoruudun sovellukset ovat käynnissä",
    "<b>{0}</b> needs to be enabled to change this setting": "<b>{0}</b>:n on oltava käytössä tämän asetuksen muuttamiseksi",
    "<b>{0}</b> needs to be disabled to change this setting": "<b>{0}</b>:n on oltava poissa käytössä tämän asetuksen muuttamiseksi",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": " (Tämä ominaisuus on poistettu käytöstä, koska sen pitäisi toimia oletusarvoisesti. Jos se ei toimi, ilmoita virheestä.)",
    "ElevenClock's language": "ElevenClockin kieli"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Tietoa Qt6:sta (PySide6)",
    "About": "Tietoa",
    "Alternative non-SSL update server (This might help with SSL errors)": "Vaihtoehtoinen ei-SSL-päivityspalvelin (Tämä saattaa auttaa SSL-virheiden kanssa)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Korjauksia ja muita kokeellisia ominaisuuksia: (Käytä VAIN silloin, jos jokin ei toimi)",
    "Show week number on the clock": "Näytä viikkonumerot kellossa",
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Piilota kello, kun RDP-asiakasohjelma tai Citrix Workspace on käynnissä",
    "Clock Appearance:": "Kellon ulkonäkö:",
    "Force the clock to have black text": "Pakota kellon fontti mustaksi",
    " - It is required that the Dark Text checkbox is disabled": " - Tumma teksti -valintaruudun on oltava pois käytöstä.",
    "Debbugging information:": "Tietoja virheenkorjauksesta:",
    "Open ElevenClock's log": "Avaa ElevenClokin logi",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Näytä kello ensisijaisessa näytössä (Hyödyllinen, jos kello on asetettu vasemmalle).",
    "Show weekday on the clock"  :"Näytä viikonpäivä kellossa",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"ElevenClock-asetukset", # Also settings title
    "Reload Clocks"             :"Päivitä kellot",
    "ElevenClock v{0}"          :"Versio: ElevenClock v{0}",
    "Restart ElevenClock"       :"Käynnistä ElevenClock uudelleen",
    "Hide ElevenClock"          :"Piilota ElevenClock",
    "Quit ElevenClock"          :"Sulje ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Yleiset asetukset",
    "Automatically check for updates"                                                   :"Tarkista päivitykset automaattisesti",
    "Automatically install available updates"                                           :"Asenna saatavilla olevat päivitykset automaattisesti",
    "Enable really silent updates"                                                      :"Ota käyttöön hiljaiset päivitykset",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Ohita päivityksen tarjoajan aitoustarkastus (EI SUOSITELLA, OMALLA VASTUULLA)",
    "Show ElevenClock on system tray"                                                   :"Näytä ElevenClock-kuvake tehtäväpalkissa",
    "Alternative clock alignment (may not work)"                                        :"Vaihtoehtoinen kellon tasaus (ei välttämättä toimi)",
    "Change startup behaviour"                                                          :"Muuta käyttäytymistä käynnistäessä",
    "Change"                                                                            :"Muuta",
    "<b>Update to the latest version!</b>"                                             :"<b>Päivitä viimeisinpään versioon!</b>",
    "Install update"                                                                    :"Asenna päivitys",
    
    #Clock settings
    "Clock Settings:"                                              :"Kellon asetukset:",
    "Hide the clock in fullscreen mode"                            :"Piilota kello koko näytön tilassa",
    "Hide the clock when RDP client is active"                     :"Piilota kello, kun RDP-asiakasohjelma on käynnissä",
    "Force the clock to be at the bottom of the screen"            :"Pakota kello näytön alareunaan",
    "Show the clock when the taskbar is set to hide automatically" :"Näytä kello, kun tehtäväpalkki on asetettu piilotettavaksi automaattisesti",
    "Fix the hyphen/dash showing over the month"                   :"Korjaa viiva kuukauden kohdalla",
    "Force the clock to have white text"                           :"Pakota kellon fontti valkoiseksi",
    "Show the clock at the left of the screen"                     :"Näytä kello ruudun vasemmassa reunassa",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Päivämäärän ja Kellonajan Asetukset:",
    "Show seconds on the clock"                         :"Näytä sekunnit kellossa",
    "Show date on the clock"                            :"Näytä päivämäärä kellossa",
    "Show time on the clock"                            :"Näytä kellonaika kellossa",
    "Change date and time format (Regional settings)"   :"Vaihda päivämäärän ja kellonajan formaattia (Alueelliset asetukset)",
    "Regional settings"                                 :"Alueelliset asetukset",
    
    #About the language pack
    "About the language pack:"                  :"Tietoja kielipaketista:",
    "Translated to English by martinet101"      :"Suomentanut: npsand", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Käännä ElevenClock omalle kielellesi",
    "Get started"                               :"Aloita",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Tietoja ElevenClock-verisosta {0}:",
    "View ElevenClock's homepage"               :"Näytä ElevenClokin kotisivu",
    "Open"                                      :"Avaa",
    "Report an issue/request a feature"         :"Ilmoita ongelmasta tai pyydä ominaisuutta",
    "Report"                                    :"Ilmoita",
    "Support the dev: Give me a coffee☕"       :"Tue kehittäjää: Tarjoa minulle kahvi☕",
    "Open page"                                 :"Avaa sivu",
    "Icons by Icons8"                           :"Kuvakkeet Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Verkkosivu",
    "Close settings"                            :"Sulje asetukset",
    "Close"                                     :"Sulje",
}

lang = lang2_3