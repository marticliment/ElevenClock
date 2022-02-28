import glob, os




OLDSTR = b"""aplied"""

NEWSTR = b"""applied"""

input(f"Path is \"{os.getcwd()}\" Press [INTRO] to continue")
print()
print()
print("Lang files to update: ")

for ext in ["py", "txt", "md", "html", "js"]:
    for file in glob.glob(f"**/*.{ext}", recursive=True):
        if "year_update" not in file:
            print(" -", file)
print()
input("Press [INTRO] to continue")

print()
print()
print("old string:", OLDSTR)
print("new string:", NEWSTR)
print()
input("Press [INTRO] to continue")

for ext in ["py", "txt", "md", "html", "js"]:
    for file in glob.glob(f"**/*.{ext}", recursive=True):
        print("Processing", file, "...")
        if "year_update" not in file:
            try:
                with open(file, "rb") as f:
                    contents = f.read()
                if OLDSTR in contents:
                    with open(file, "wb") as f:
                        f.write(contents.replace(OLDSTR, NEWSTR))
                    
                    print("🟢", file, "has been updated successfully")
                else:
                    print("⚪", file, "has no occurrences of the substring")
            except Exception as e:
                print("🟥", file, "has not been updated:", str(e))
            
input("Finished, press [INTRO] to close")
