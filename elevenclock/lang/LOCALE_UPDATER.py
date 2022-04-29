import glob, os




OLDSTR = b"""lang_3_4_0 = {"""

NEWSTR = b"""lang_3_5_0 = {
    "Tooltip Appearance:": "",
    "Tooltip's font, font size, font color and background": "",
    "Disable tooltip's blurry background": "",
    "Sync time with the internet": "",
    "Internet date and time": "",
    "Select internet time provider, change sync frequency": "",
    "Enable atomic clock-based internet time": "",
    "Paste a URL from the world clock api or equivalent": "",
    "Help": "",
    "Internet sync frequency": "",
    "10 minutes": "",
    "30 minutes": "",
    "1 hour": "",
    "2 hours": "",
    "4 hours": "",
    "10 hours": "",
    "24 hours": "",
}

lang_3_4_0 = lang_3_5_0 | {"""

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
