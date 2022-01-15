import glob, os




OLDSTR = b"""lang_3 = {"""

NEWSTR = b"""lang_3_1 = {
    "W": "", # The initial of the word week in your language: W for week, S for setmana, etc.
    "Disable the notification badge": "",
    "Override clock default height": "",
    "Adjust horizontal clock position": "",
    "Adjust vertical clock position": "",
    "Export log as a file": "",
    "Copy log to clipboard": "",
    "Announcements:": "",
    "Fetching latest announcement, please wait...": "",
    "Couldn't load the announcements. Please try again later": "",
    "ElevenClock's log": "",
    "Pick a color": ""
}

lang_3 = lang_3_1 | {"""

input(f"Path is \"{os.getcwd()}\" Press [INTRO] to contniue")
print()
print()
print("Lang files to update: ")

for file in glob.glob("lang_*.py"):
    print(" -", file)
print()
input("Press [INTRO] to contniue")

print()
print()
print("old string:", OLDSTR)
print("new string:", NEWSTR)
print()
input("Press [INTRO] to contniue")

for file in glob.glob("lang_*.py"):
    print("Processing", file, "...")
    try:
        with open(file, "rb") as f:
            contents = f.read()
        with open(file, "wb") as f:
            f.write(contents.replace(OLDSTR, NEWSTR))
            
        print(file, "has been updated successfully")
    except:
        print("🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥", file, "has been updated successfully")
        
input("Finished, press [INTRO] to close")
