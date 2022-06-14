languageReference = {
    "default": "System language",
    "ar"    : "Arabic",
    "ca"    : "Catalan - Català",
    "cs"    : "Czech - Čeština",
    "da"    : "Danish",
    "de"    : "German",
    "el"    : "Greek",
    "en"    : "English",
    "es"    : "Spanish - Español",
    "fi"    : "Finnish",
    "fr"    : "French - Français",
    "he"    : "Hebrew",
    "hu"    : "Hungarian",
    "id"    : "Indonesian",
    "it"    : "Italian - Italiano",
    "ja"    : "Japanese",
    "ko"    : "Korean",
    "lt"    : "Lithuanian",
    "lv"    : "Latvian",
    "nb"    : "Norwegian (bokmål)",
    "nl"    : "Dutch",
    "nn"    : "Norwegian (nynorsk)",
    "pl"    : "Polish",
    "pt_BR" : "Portuguese (Brazil)",
    "pt_PT" : "Portuguese (Portugal)",
    "ru"    : "Russian",
    "sk"    : "Slovak - Slovenčina)",
    "sr"    : "Serbian",
    "sv"    : "Swedish",
    "th"    : "Thai",
    "tr"    : "Turkish",
    "ua"    : "Ukranian",
    "vi"    : "Vietnamese",
    "zh_CN" : "Simplified Chinese (China)",
    "zh_TW" : "Traditional Chinese (Taiwan)",
}

lang = {}
englang = {}
languages = {} # will be auto-generated

## auto-generate map of files
for key in languageReference.keys():
    if (key != "default"):
        languages[key] = f"lang_{key}.json"

debugLang = False

