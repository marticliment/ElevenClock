import sys
import hashlib
import os
from os.path import exists

os.chdir(os.path.dirname(__file__) + "/..") # move to root project

sys.path.append("elevenclock")
sys.path.append("elevenclock/lang")
from versions import versionName
from lang_tools import *


# generate list of translations
readmeLangs = getMarkdownSupportLangs()


# generate checksum
sha256_hash = hashlib.sha256()
checksum = "missing"
shafiles = [
    "ElevenClock.Installer.exe",
    "ElevenClock.exe",
]
for filename in shafiles:
    if (not exists(filename)): continue
    f = open(filename, "rb")
    for byte_block in iter(lambda: f.read(4096),b""):
        sha256_hash.update(byte_block)
    checksum = sha256_hash.hexdigest()
    f.close()
    break


# output
release = f"""
[![Downloads@{versionName}](https://img.shields.io/github/downloads/martinet101/ElevenClock/{versionName}/total?style=for-the-badge)](https://github.com/martinet101/ElevenClock/releases/download/{versionName}/ElevenClock.Installer.exe)

# Changelog:
*
*
*


# Available languages:
(Please note that this languages might be updated in the future by the app itself. The languages listed here are the bundled ones)
{readmeLangs}

<br><br>
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
