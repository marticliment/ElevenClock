import sys
import hashlib
from os.path import exists

sys.path.append("elevenclock")
sys.path.append("elevenclock/lang")
from versions import versionName
from languages import languageReference
from translated_percentage import untranslatedPercentage


# generate list of translations
availableLangs = ""
for lang, langName in languageReference.items():
    if (not exists(f"elevenclock/lang/lang_{lang}.json")): continue
    if (lang in untranslatedPercentage):
        if (untranslatedPercentage[lang] == "0%"): continue
    availableLangs += f"* {langName}\n"


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
{availableLangs}


SHA256: `{checksum}`
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
input("Press any key to close")
