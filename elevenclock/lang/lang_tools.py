from os.path import exists
from pathlib import Path


languageReference = {
    "default": "System language",
    "ar"    : "Arabic - عربي‎",
    "bg"    : "Bulgarian - български",
    "ca"    : "Catalan - Català",
    "cs"    : "Czech - Čeština",
    "da"    : "Danish - Dansk",
    "nl"    : "Dutch - Nederlands",
    "en"    : "English - English",
    "et"    : "Estonian - eesti",
    "fi"    : "Finnish - Suomi",
    "fr"    : "French - Français",
    "de"    : "German - Deutsch",
    "el"    : "Greek - Ελληνικά",
    "he"    : "Hebrew - עִבְרִית‎",
    "hu"    : "Hungarian - Magyar",
    "id"    : "Indonesian - Bahasa Indonesia",
    "it"    : "Italian - Italiano",
    "ja"    : "Japanese - 日本語",
    "ko"    : "Korean - 한국어",
    "lt"    : "Lithuanian - Lietuvių",
    "lv"    : "Latvian - Latviski",
    "nb"    : "Norwegian (bokmål)",
    "nn"    : "Norwegian (nynorsk)",
    "fa"    : "Persian - فارسی‎",
    "pl"    : "Polish - Polski",
    "pt_BR" : "Portuguese (Brazil)",
    "pt_PT" : "Portuguese (Portugal)",
    "ro"    : "Romanian - Română",
    "ru"    : "Russian - Русский",
    "sr"    : "Serbian - Srpski",
    "si"    : "Sinhala - සිංහල",
    "sk"    : "Slovak - Slovenčina",
    "es"    : "Spanish - Español",
    "sv"    : "Swedish - Svenska",
    "th"    : "Thai - ภาษาไทย",
    "tr"    : "Turkish - Türkçe",
    "ua"    : "Ukranian - Yкраї́нська",
    "vi"    : "Vietnamese - Tiếng Việt",
    "zh_CN" : "Simplified Chinese (China)",
    "zh_TW" : "Traditional Chinese (Taiwan)",
}


languageRemap = {
    "pt-PT":      "pt_PT",
    "pt-BR":      "pt_BR",
    "uk":         "ua",
    "zh-Hant-TW": "zh_TW",
    "zh-Hans-CN": "zh_CN",
}


# ISO 3166-1
languageFlagsRemap = {
    "ar": "sa",
    "ca": "ad",
    "cs": "cz",
    "da": "dk",
    "en": "gb",
    "el": "gr",
    "et": "ee",
    "fa": "ir",
    "he": "il",
    "ja": "jp",
    "ko": "kr",
    "nb": "no",
    "nn": "no",
    "pt_BR": "br",
    "pt_PT": "pt",
    "si": "lk",
    "zh_CN": "cn",
    "zh_TW": "tw",
    "vi": "vn",
}


def getMarkdownSupportLangs():
    from translated_percentage import untranslatedPercentage

    readmeLangs = [
        "| Language | Translated | |",
        "| :-- | :-- | --- |",
    ]

    dir = str(Path(__file__).parent)
    for lang, langName in languageReference.items():
        if (not exists(f"{dir}/lang_{lang}.json")): continue
        perc = untranslatedPercentage[lang] if (lang in untranslatedPercentage) else "100%"
        if (perc == "0%"): continue
        langName = languageReference[lang] if (lang in languageReference) else lang
        flag = languageFlagsRemap[lang] if (lang in languageFlagsRemap) else lang
        readmeLangs.append(f"| {langName} | {perc} | <img src='https://flagcdn.com/{flag}.svg' width=20> |")
    readmeLangs.append("")

    return "\n".join(readmeLangs)
