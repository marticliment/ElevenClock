import sys

sys.path.append("elevenclock")

from versions import *


f = open("ElevenClock.iss", "r+", encoding="utf-8")
data = ""
l1 = "#define MyAppVersion"
for line in f.readlines():
    if (line.startswith(l1)):
        data += f"{l1} \"{versionName}\"\n"
    else: data += line
print(data)
f.seek(0)
f.write(data)
f.truncate()
f.close()


f = open("elevenclock-version-info", "r+", encoding="utf-8")
data = ""
l1 = "      StringStruct(u'FileVersion'"
l2 = "      StringStruct(u'ProductVersion'"
for line in f.readlines():
    if (line.startswith(l1)):
        data += f"{l1}, u'{versionName}'),\n"
    elif (line.startswith(l2)):
        data += f"{l2}, u'{versionName}'),\n"
    else: data += line
print(data)
f.seek(0)
f.write(data)
f.truncate()
f.close()
