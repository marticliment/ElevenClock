import sys
import hashlib
from os.path import exists

sys.path.append("elevenclock")
sys.path.append("elevenclock/lang")
from versions import versionName
from languages import languageReference
from translated_percentage import untranslatedPercentage


languageFlagsRemap = {
    "ca": "ad",
    "cs": "cz",
    "da": "dk",
    "en": "gb",
    "el": "gr",
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
}

# generate list of translations
availableLangs = []
for lang, langName in languageReference.items():
    if (not exists(f"elevenclock/lang/lang_{lang}.json")): continue
    if (lang in untranslatedPercentage):
        if (untranslatedPercentage[lang] == "0%"): continue
    availableLangs.append(langName)

readmeLangs = """
| Language | Translated | |
| :-- | :-- | --- |
"""
print(availableLangs,"\n\n", languageReference)

for lang in availableLangs:
    langName = lang
    lang = list(languageReference.keys())[list(languageReference.values()).index(lang)]
    perc = untranslatedPercentage[lang] if (lang in untranslatedPercentage) else "100%"
    if (perc == "0%"): continue
    flag = languageFlagsRemap[lang] if (lang in languageFlagsRemap) else lang
    readmeLangs += f"| {langName} | {perc} | <img src='https://flagcdn.com/{flag}.svg' width=20> |\n"



# generate checksum
sha256_hash = hashlib.sha256()
f = open("ElevenClock.exe", "rb")
for byte_block in iter(lambda: f.read(4096),b""):
    sha256_hash.update(byte_block)
checksum = sha256_hash.hexdigest()
f.close()


# output
release = f"""
[![Downloads@{versionName}](https://img.shields.io/github/downloads/martinet101/ElevenClock/{versionName}/total?style=for-the-badge)](https://github.com/martinet101/ElevenClock/releases/download/{versionName}/ElevenClock.Installer.exe)

# Changelog:
*
*
*


# Available languages:
{readmeLangs}

<br><br>
Executable SHA256: `{checksum}`
<br>Installer  SHA256: `insert-sha256-here`
"""

# write output
f = open("RELEASE.md", "w", encoding="utf-8")
f.write(release)
f.close()

print()
print("MD result has been saved to RELEASE.md: The contents are:")
print()
print()
print(release)
print()
print()
