import glob, os




OLDSTR = b""""ElevenClock has updated to version {0} successfully
Please see GitHub for the changelog": "","""

NEWSTR = b""""ElevenClock has updated to version {0} successfully\\nPlease see GitHub for the changelog": "","""

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
