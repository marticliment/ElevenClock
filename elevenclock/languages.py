languageReference = {
    "default": "System language",
    "ar"    : "Arabic - عربي‎",
    "ca"    : "Catalan - Català",
    "cs"    : "Czech - Čeština",
    "da"    : "Danish - Dansk",
    "de"    : "German - Deutsch",
    "el"    : "Greek - Ελληνικά",
    "en"    : "English - English",
    "es"    : "Spanish - Español",
    "fi"    : "Finnish - Suomi",
    "fr"    : "French - Français",
    "he"    : "Hebrew - עִבְרִית‎",
    "hu"    : "Hungarian - Magyar",
    "id"    : "Indonesian - Bahasa Indonesia",
    "it"    : "Italian - Italiano",
    "ja"    : "Japanese - 日本語",
    "ko"    : "Korean - 한국어",
    "lt"    : "Lithuanian - Lietuvių",
    "lv"    : "Latvian - Latviski",
    "nb"    : "Norwegian (bokmål)",
    "nl"    : "Dutch - Nederlands",
    "nn"    : "Norwegian (nynorsk)",
    "pl"    : "Polish - Polski",
    "pt_BR" : "Portuguese (Brazil)",
    "pt_PT" : "Portuguese (Portugal)",
    "ro"    : "Romanian - Română",
    "ru"    : "Russian - Русский",
    "si"    : "Sinhala - සිංහල",
    "sk"    : "Slovak - Slovenčina",
    "sr"    : "Serbian - Srpski",
    "sv"    : "Swedish - Svenska",
    "th"    : "Thai - ภาษาไทย",
    "tr"    : "Turkish - Türkçe",
    "ua"    : "Ukranian - Yкраї́нська",
    "vi"    : "Vietnamese - Tiếng Việt",
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

