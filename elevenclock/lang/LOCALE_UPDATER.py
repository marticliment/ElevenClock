import glob, os




OLDSTR = b"""lang_3_1 = {"""

NEWSTR = b"""lang_3_2 = {
    "Use system accent color as background color": "",
    "Check only the focused window on the fullscreen check": "",
    "Clock on monitor {0}": "",
    "Move to the left": "",
    "Show this clock on the left": "",
    "Show this clock on the right": "",
    "Restore clock position": "",
}

lang_3_1 = lang_3_2 | {"""

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
