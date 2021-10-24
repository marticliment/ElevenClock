# INSTRUCTIONS

# Translate the text and write it between the "
# EXAMPLE:      original    ->  "This text is in english: value {0}" 
#               translation ->  "Aquest text està en anglès: valor {0}"
# If you see sth like {0}, {1}, maintain it on the translated sentence
# Meke special attention to elements like ":", etc.

lang2_4 = {
    # Added text in version 2.4
    "Show the clock on the primary screen (Useful if clock is set on the left)": "",
    "Show weekday on the clock"  :"Προβολή ημέρας της εβδομάδας στο ρολόι",
}

lang2_3 = lang2_4 | {
    #Context menu
    "ElevenClock Settings"      :"Ρυθμίσεις ElevenClock", # Also settings title
    "Reload Clocks"             :"Επαναφόρτωση Ρολογιών",
    "ElevenClock v{0}"          :"Έκδοση ElevenClock: {0}",
    "Restart ElevenClock"       :"Επανεκκίνηση ElevenClock",
    "Hide ElevenClock"          :"Απόκρυψη ElevenClock",
    "Quit ElevenClock"          :"Τερματισμός ElevenClock",
    
    #General settings section
    "General Settings:"                                                                 :"Γενικές Ρυθμίσεις",
    "Automatically check for updates"                                                   :"Αυτόματος έλεγχος για ενημερώσεις",
    "Automatically install available updates"                                           :"Αυτόματη εγκατάσταση διαθέισμων ενημερώσεων",
    "Enable really silent updates"                                                      :"Ενεργοποίηση πραγματικά σιωπηλών ενημερώσεων",
    "Bypass update provider authenticity check (NOT RECOMMENDED, AT YOUR OWN RISK)"     :"Παράκαμψη ελέγχου πιστοποίησης παρόχου ενημερώσεων (ΔΕΝ ΠΡΟΤΕΊΝΕΤΑΙ, ΜΕ ΔΙΚΗ ΣΑΣ ΕΥΘΥΝΗ)",
    "Show ElevenClock on system tray"                                                   :"Προβολή του ElevenClock στη γραμμή εργασιών",
    "Alternative clock alignment (may not work)"                                        :"Εναλλακτική ευθυγράμμιση ρολογιού (ίσως να μην λειτουργεί)",
    "Change startup behaviour"                                                          :"Αλλαγή συμπεριφοράς κατά την εκκίνηση",
    "Change"                                                                            :"Αλλαγή",
    "<b>Update to the lastest version!</b>"                                             :"<b>Ενημέρωση στην τελευταία έκδοση!</b>",
    "Install update"                                                                    :"Εγκατάστσαη ενημέρωσης",
    
    #Clock settings
    "Clock Settings:"                                              :"Ρυθμίσεις Ρολογιού",
    "Hide the clock in fullscreen mode"                            :"Απόκρυψη ρολογιού σε κατάσταση πλήρους οθόνης",
    "Hide the clock when RDP client is active"                     :"Απόκρυψη ρολογιού όταν χρησιμοποιείται η Απομακρυσμένη Πρόσβαση",
    "Force the clock to be at the bottom of the screen"            :"Εξαναγκασμός ρολογιού στο κάτω μέρος της οθόνης",
    "Show the clock when the taskbar is set to hide automatically" :"Προβολή ρολογιού όταν η γραμμή εργασιών είναι ορισμένη για αυτόματη απόκρυψη",
    "Fix the hyphen/dash showing over the month"                   :"Διόρθωση της καθέτου που προβάλεται πάνω από τον μήνα",
    "Force the clock to have white text"                           :"Εξαναγκασμός ρολογίου για χρήση κειμένου σε λευκό χρώμα",
    "Show the clock at the left of the screen"                     :"Προβολή ρολογιού στα αριστερά της οθόνης",
    
    #Date & time settings
    "Date & Time Settings:"                             :"Ρυθμίσεις Ημερομηνίας & Ώρας",
    "Show seconds on the clock"                         :"Προβολή δευτερολέπτων στο ρολόι",
    "Show date on the clock"                            :"Προβολή ημερομηνίας στο ρολόι",
    "Show time on the clock"                            :"Προβολή ώρας στο ρολόι",
    "Change date and time format (Regional settings)"   :"Αλλαγή μορφής ημερομηνίας και ώρας (Τοπικές ρυθμίσεις)",
    "Regional settings"                                 :"Τοπικές ρυθμίσεις",
    
    #About the language pack
    "About the language pack:"                  :"Σχετικά με το πακέτο γλώσσας",
    "Translated to English by martinet101"      :"Μετάφραση ελληνικών από panos78", # Here, make sute to give you some credits:  Translated to LANGUAGE by USER/NAME/PSEUDONYM/etc. 
    "Translate ElevenClock to your language"    :"Μεταφραση του ElevenClock στη γλώσσα σας",
    "Get started"                               :"Ξεκινήστε",
    
    #About ElevenClock
    "About ElevenClock version {0}:"            :"Σχετικά με την έκδοση {0} του ElevenClock:",
    "View ElevenClock's homepage"               :"Μετάβαση στην ιστοσελίδα του ElevenClock",
    "Open"                                      :"Άνοιγμα",
    "Report an issue/request a feature"         :"Αναφορά θέματος / Αίτημα χαρακτηριστικού",
    "Report"                                    :"Αναφορά",
    "Support the dev: Give me a coffee☕"       :"Υποστηρίξτε τον δημιουργό: Κεράστε τον ένα καφέ☕",
    "Open page"                                 :"Άνοιγμα σελίδας",
    "Icons by Icons8"                           :"Εικονίδια από Icons8", # Here, the word "Icons8" should not be translated
    "Webpage"                                   :"Ιστοσελίδα",
    "Close settings"                            :"Κλείσιμο ρυθμίσεων",
    "Close"                                     :"Κλείσιμο",
}

lang = lang2_3