# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"

# So it would look like: "ORIGINAL_TEXT" : "TRANSLATED_TEXT",


# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang_3_5_0 = {
    "Tooltip Appearance:": "",
    "Tooltip's font, font size, font color and background": "",
    "Disable tooltip's blurry background": "",
    "Sync time with the internet": "",
    "Internet date and time": "",
    "Select internet time provider, change sync frequency": "",
    "Enable atomic clock-based internet time": "",
    "Paste a URL from the world clock api or equivalent": "",
    "Help": "",
    "Internet sync frequency": "",
    "10 minutes": "",
    "30 minutes": "",
    "1 hour": "",
    "2 hours": "",
    "4 hours": "",
    "10 hours": "",
    "24 hours": "",
}

lang_3_4_0 = lang_3_5_0 | {
    "Show calendar": "Visa kalender",
    "Disabled": "Inaktiverad",
    "Open quick settings": "Öppna snabbinställningar",
    "Show desktop": "Visa skrivbord",
    "Open run dialog": "Öppna kör",
    "Open task manager": "Öppna aktivitetshanteraren",
    "Open start menu": "Öppna startmenyn",
    "Open search menu": "Öppna sökmenyn",
    "Change task": "Ändra uppgift",
    "Change the action done when the clock is clicked": "Ändra vad som händer när klockan klickas",
}

lang_3_3_2 = lang_3_4_0 | {
    "ElevenClock Updater": "ElevenClock uppdaterare",
    "ElevenClock is downloading updates": "ElevenClock hämtar uppdateringar",
    "ElevenClock has updated to version {0} successfully\nPlease see GitHub for the changelog": "ElevenClock har uppdaterats till version {0}\nSe GitHub för ändringar",
    "Customize the clock on Windows 11": "Anpassa klockan på Windows 11",
    "Disable the new instance checker method": "Inaktivera den nya instance checker metoden",
    "Import settings from a local file": "Importera inställningar från en lokal fil",
    "Export settings to a local file": "Exportera inställningar från en lokal fil",
    "Export": "Exportera",
    "Import": "Importera",
}

lang_3_3_1 = lang_3_3_2 | {
    "Invalid time format\nPlease follow the\nC 1989 Standards": "Ogiltigt tidsformat\nVänligen följ\n1989 C standarden",
    "Nothing to preview": "Inget att förhandsvisa",
    "Invalid time format\nPlease modify it\nin the settings": "Ogiltigt tidsformat\nVänligen modifiera\nformatet i inställningarna",
    "Disable the tooltip shown when the clock is hovered": "Inaktivera tooltip som visas när klockan hålls över"
}
lang_3_3 = lang_3_3_1 | {
    "Custom format rules:": "Regler för anpassad formatering",
    "Any text can be placed here. To place items such as date and time, please use the 1989 C standard. More info on the following link": "Valfri text kan placeras här. För att placera saker som datum och tid, vänligen använd 1989 C standarden. Mer info finns på följande länk:",
    "Python date and time formats": "Python datum och tidsformat",
    "To disable the zero-padding effect, add a # in between the % and the code: non-zero-padded hours would be %#H, and zero-padded hours would be %H": "För att inaktivera zero-padding, lägg till ett # mellan % och koden: non-zero-padded timmar skrivs %#H, och zero-padded timmar skrivs %H", # Here please don't modify the %H and %#H values
    "Click on Apply to apply and preview the format": "Klicka på Verkställ för att förhandsgranska formateringen",
    "Apply": "Verkställ",
    "If you don't understand what is happening, please uncheck the checkbox over the text area": "Om du inte förstår vad som händer, vänligen avmarkera kryssrutan över textområdet",
    "Set a custom date and time format": "Ange ett anpassat format för datum och tid",
    "(for advanced users only)": "(för avancerade användare)",
    "Move this clock to the left": "Flytta den här klockan till vänster",
    "Move this clock to the top": "Flytta den här klockan till toppen",
    "Move this clock to the right": "Flytta den här klockan till höger",
    "Move this clock to the bottom": "Flytta den här klockan till botten",
    "Restore horizontal position": "Återställ horisontell position",
    "Restore vertical position": "Återställ vertikal position",
}

lang_3_2_1 = lang_3_3 | {
    "Open online help to troubleshoot problems": "Öppna online hjälp för att felsöka problem",
    "Reset ElevenClock preferences to defaults": "Återställ ElevenClock till standardinställningar",
    "Specify a minimum width for the clock": "Specificera en minimi-bredd för klockan",
    "Search on the settings": "Sök i inställningar",
    "No results were found": "Inga resultat hittades",
}

lang_3_2 = lang_3_2_1 | {
    "Use system accent color as background color": "Använd systemets accentfärg som bakgrundsfärg",
    "Check only the focused window on the fullscreen check": "Kolla endast fokuserade fönstret vid fullscreen check",
    "Clock on monitor {0}": "Klocka på bildskärm {0}",
    "Move to the left": "Flytta till vänster",
    "Show this clock on the left": "Visa den här klockan till vänster",
    "Show this clock on the right": "Visa den här klockan till höger",
    "Restore clock position": "Återställ klockans position",
}

lang_3_1 = lang_3_2 | {
    "W": "v", # The initial of the word week in your language: W for week, S for setmana, etc.
    "Disable the notification badge": "Inaktivera notification badge",
    "Override clock default height": "Override klockans standardhöjd",
    "Adjust horizontal clock position": "Justera klockans position horisontellt",
    "Adjust vertical clock position": "Justera klockans position vertikalt",
    "Export log as a file": "Exportera log som en fil",
    "Copy log to clipboard": "Kopiera log till urklipp",
    "Announcements:": "Meddelanden",
    "Fetching latest announcement, please wait...": "Hämtar senaste meddelande, vänligen vänta",
    "Couldn't load the announcements. Please try again later": "Kunde inte ladda meddelanden, vänligen försök igen senare",
    "ElevenClock's log": "ElevenClocks log",
    "Pick a color": "Välj en färg"
}

lang_3 = lang_3_1 | {
    "Hide the clock during 10 seconds when clicked": "Göm klockan i 10 sekunder vid klick",
    "Enable low-cpu mode": "Aktivera low-cpu mode",
    "You might lose functionalities, like the notification counter or the dynamic background": "Du kan gå miste om funktioner som meddelanderäknaren eller dynamisk bakgrund",
    "Clock position and size:": "Klockans position och storlek",
    "Clock size preferences, position offset, clock at the left, etc.": "Inställningar för klockstorlek, position offset, klocka till vänster, osv.",
    "Reset monitor blacklisting status": "Återställ skärmens svartlist status",
    "Reset": "Återställ",
    "Third party licenses": "Tredjeparts licenser",
    "View": "Visa",
    "ElevenClock": "ElevenClock",
    "Monitor tools": "Skärmverktyg",
    "Blacklist this monitor": "Svartlista den här skärmen",
    "Third Party Open-Source Software in Elevenclock {0} (And their licenses)": "Tredjeparts Open-Source mjukvara i ElevenClock {0} (och deras licenser)",
    "ElevenClock is an Open-Source application made with the help of other libraries made by the community:": "ElevenClock är en Open-Source applikation utvecklad med hjälp av bibliotek skapad av communityn",
    "Ok": "Ok",
    "More Info": "Mer info",
    "About Qt": "Om Qt",
    "Success": "Lyckades",
    "The monitors were unblacklisted successfully.": "Skärmarna togs bort från svartlistning",
    "Now you should see the clock everywhere": "Nu borde du se klockan överallt",
    "Ok": "Ok",
    "Blacklist Monitor": "Svarlista skärm",
    "Blacklisting a monitor will hide the clock on this monitor permanently.": "Att svartlista en skärm döljer klockan från den här skärmen permanent",
    "This action can be reverted from the settings window, under <b>Clock position and size</b>": "Denna handling kan ångras från inställningarna, under <b>Klockans position och storlek</b>",
    "Are you sure do you want to blacklist the monitor \"{0}\"?": "Är du säker på att du vill svartlista skärmen \"{0}\"?",
    "Yes": "Ja",
    "No": "Nej",
}

lang_2_9_2 = lang_3 | {
    "Reload log": "Ladda om log",
    "Do not show the clock on secondary monitors": "Visa inte klockan på sekundära skärmar",
    "Disable clock taskbar background color (make clock transparent)": "Inaktivera klockans bakgrundsfärg i aktivitetsfältet (gör klockan transparent",
    "Open the welcome wizard": "Öppna välkomstguiden",
    " (ALPHA STAGE, MAY NOT WORK)": " (ALPHA STADIE, KANSKE INTE FUNGERAR)",
    "Welcome to ElevenClock": "Välkommen till ElevenClock",
    "Skip": "Hoppa Över",
    "Start": "Start",
    "Next": "Nästa",
    "Finish": "Klar",
}

lang_2_9 = lang_2_9_2 | {
    "Task Manager": "Aktivitetshanteraren",
    "Change date and time": "Ändra datum och tid",
    "Notification settings": "Notifikationsinställningar",
    "Updates, icon tray, language": "Uppdateringar, ikon, språk",
    "Hide extended options from the clock right-click menu (needs a restart to be applied)": "Göm utökade inställnigar från klockans högerklickmeny (behöver omstart för att tillämpas)",
    "Fullscreen behaviour, clock position, 1st monitor clock, other miscellanious settings": "Fullskärmsbeteende, klockans position, huvudskärmsklocka, andra diverse inställningar",
    'Add the "Show Desktop" button on the left corner of every clock': 'Lägg till "Visa skrivbord" knapp till vänstra hörnet av varje klocka',
    'You might need to set a custom background color for this to work.&nbsp;More info <a href="{0}" style="color:DodgerBlue">HERE</a>': 'Du kan behöva sätta en anpassad bakgrundsfärg för att det ska fungera.&nbsp;Mer info <a href="{0}" style="color:DodgerBlue">HÄR</a> ',
    "Clock's font, font size, font color and background, text alignment": "Klockans font, teckenstorlek, färg på font och bakgrund, textjustering",
    "Date format, Time format, seconds,weekday, weeknumber, regional settings": "Datum och tidsformatering, sekunder, veckodag, veckonummer, regionala inställningar",
    "Testing features and error-fixing tools": "Testar funktioner och felhanteringsverktyg",
    "Language pack author(s), help translating ElevenClock": "Språkpakets författare, hjälp översätt ElevenClock",
    "Info, report a bug, submit a feature request, donate, about": "Info, rapportera en bug, skicka in en funktionsbegäran, donera, om",
    "Log, debugging information": "Log, debugging information",
}

lang_2_8 = lang_2_9 | {
    "Force the clock to be at the top of the screen": "Tvinga klockan att vara på toppen av skärmen",
    "Show the clock on the primary screen": "Visa klockan på primärskärmen",
    "Use a custom font color": "Använd anpassad teckenfärg",
    "Use a custom background color": "Använd anpassad bakgrundsfärg",
    "Align the clock text to the center": "Justera placering av text till klockans centrum",
    "Select custom color": "Välj anpassad färg",
    "Hide the clock when a program occupies all screens": "Dölj klockan när ett program tar upp alla skärmar",
}

lang2_7_bis = lang_2_8 | {
    "Use a custom font": "Använd en anpassad font",
    "Use a custom font size": "Använd en anpassad font storlek",
    "Enable hide when multi-monitor fullscreen apps are running": "Aktivera dölj när helskärmsappar med flera skärmar körs",
    "<b>{0}</b> needs to be enabled to change this setting": "<b>{0}</b> måste vara aktiverat för att ändra denna inställning",
    "<b>{0}</b> needs to be disabled to change this setting": "<b>{0}</b> måste inaktiveras för att ändra den här inställningen",
}

lang2_7 = lang2_7_bis | {
    " (This feature has been disabled because it should work by default. If it is not, please report a bug)": " (Den här funktionen har inaktiverats eftersom den borde fungera som standard. Om den inte är det, rapportera ett fel)",
    "ElevenClock's language": "ElevenClocks språk"
}

lang2_6 = lang2_7 | {
    "About Qt6 (PySide6)": "Om Qt6 (PySide6)",
    "About": "Om",
    "Alternative non-SSL update server (This might help with SSL errors)": "Alternativ icke-SSL-uppdateringsserver (Detta kan hjälpa till med SSL-fel)",
    "Fixes and other experimental features: (Use ONLY if something is not working)": "Fixar och andra experimentella funktioner: (Använd ENDAST om något inte fungerar)",
    "Show week number on the clock": "Visa veckonummer på klockan"
}

lang2_5 = lang2_6 | {
    "Hide the clock when RDP Client or Citrix Workspace are running": "Dölj klockan när RDP Client eller Citrix Workspace körs",
    "Clock Appearance:": "Klockans utseende",
    "Force the clock to have black text": "Tvinga klockan att ha svart text",
    " - It is required that the Dark Text checkbox is disabled": " - Det krävs att kryssrutan Mörk text är inaktiverad",
    "Debbugging information:": "Debugging information",
    "Open ElevenClock's log": "Öppna ElevenClocks logg",
}

lang2_4 = lang2_5 | {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "Visa klockan på den primära skärmen (Användbart om klockan är inställd till vänster)",
    "Show weekday on the clock"  :"Visa veckodag på klockan",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"ElevenClock Inställningar", # Also settings title
    "Reload Clocks"             :"Ladda om klockor",
    "ElevenClock v{0}"          :"ElevenClock v{0}",
    "Restart ElevenClock"       :"Starta om ElevenClock",
    "Hide ElevenClock"          :"Göm ElevenClock",
    "Quit ElevenClock"          :"Avsluta ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Allmänna Inställningar:",
    "Automatically check for updates"                                                   :"Sök automatiskt efter uppdateringar",
    "Automatically install available updates"                                           :"Installera tillgängliga uppdateringar automatiskt",
    "Enable really silent updates"                                                      :"Aktivera riktigt tysta uppdateringar",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Kringgå uppdateringsleverantörens äkthetskontroll (REKOMMENDERAS INTE, PÅ DIN EGEN RISK)",
    "Show ElevenClock on system tray"                                                   :"Visa ElevenClock i systemfältet",
    "Alternative clock alignment (may not work)"                                        :"Alternativ klockjustering (fungerar kanske inte)",
    "Change startup behaviour"                                                          :"Ändra startbeteende",
    "Change"                                                                            :"Förändra",
    "<b>Update to the latest version!</b>"                                              :"<b>Uppdatera till den senaste versionen!</b>",
    "Install update"                                                                    :"Installera uppdatering",
    
    #Clock settings
    "Clock Settings:"                                              :"Klockinställningar:",
    "Hide the clock in fullscreen mode"                            :"Dölj klockan i helskärmsläge",
    "Hide the clock when RDP client is active"                     :"Dölj klockan när RDP-klienten är aktiv",
    "Force the clock to be at the bottom of the screen"            :"Tvinga klockan att vara längst ner på skärmen",
    "Show the clock when the taskbar is set to hide automatically" :"Visa klockan när aktivitetsfältet är inställt på att döljas automatiskt",
    "Fix the hyphen/dash showing over the month"                   :"Åtgärda bindestrecket/strecket som visas under månaden",
    "Force the clock to have white text"                           :"Tvinga klockan att ha vit text",
    "Show the clock at the left of the screen"                     :"Visa klockan till vänster på skärmen",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Inställningar för datum och tid:",
    "Show seconds on the clock"                         :"Visa sekunder på klockan",
    "Show date on the clock"                            :"Visa datum på klockan",
    "Show time on the clock"                            :"Visa tid på klockan",
    "Change date and time format (Regional settings)"   :"Ändra datum och tidsformat (regionala inställningar)",
    "Regional settings"                                 :"Regionala inställningar",
    
    #About the language pack
    "About the language pack:"                  :"Om språkpaketet:",
    "Translated to English by martinet101"      :"Översatt till Svenska av Noffe och cjal95", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Översätt ElevenClock till ditt språk",
    "Get started"                               :"Kom igång",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Om ElevenClock version {0}:",
    "View ElevenClock's homepage"               :"Visa ElevenClocks hemsida",
    "Open"                                      :"Öppna",
    "Report an issue/request a feature"         :"Rapportera ett problem/begär en funktion",
    "Report"                                    :"Rapportera",
    "Support the dev: Give me a coffee☕"       :"Stöd utvecklaren: Ge mig en kaffe☕",
    "Open page"                                 :"Öppna sida",
    "Icons by Icons8"                           :"Ikoner av Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Webbsida",
    "Close settings"                            :"Stäng inställningar",
    "Close"                                     :"Stäng",
}

lang = lang2_3
