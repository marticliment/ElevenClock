import sys

sys.path.append("elevenclock")

from versions import *


def fileReplaceLinesWith(filename: str, list: dict[str, str]):
    f = open(filename, "r+", encoding="utf-8")
    data = ""
    for line in f.readlines():
        match = False
        for key, value in list.items():
            if (line.startswith(key)):
                data += f"{key}{value}"
                match = True
                continue
        if (not match):
            data += line
    f.seek(0)
    f.write(data)
    f.truncate()
    f.close()


fileReplaceLinesWith("ElevenClock.iss", {
    "#define MyAppVersion": f" \"{versionName}\"\n",
})

fileReplaceLinesWith("elevenclock-version-info", {
    "      StringStruct(u'FileVersion'": f", u'{versionName}'),\n",
    "      StringStruct(u'ProductVersion'": f", u'{versionName}'),\n",
})
