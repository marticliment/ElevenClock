try:
    apikey = open("APIKEY.txt", "r").read()
    print("  API key found in APIKEY.txt")
except FileNotFoundError:
    apikey = input("Write api key and press enter: ")

apiurl = f"https://app.tolgee.io/v2/projects/688/export?format=JSON&splitByScope=false&splitByScopeDelimiter=~&splitByScopeDepth=0&filterState=UNTRANSLATED&filterState=TRANSLATED&filterState=REVIEWED&zip=true&ak={apikey}"

import os
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests
import glob, time, shutil, zipfile

print()
print("-------------------------------------------------------")
print()
print("  Downloading updated translations...")

zipcontent = requests.get(apiurl)
open("langs.zip", "wb").write(zipcontent.content)

print("  Download complete!")
print()
print("-------------------------------------------------------")
print()
print("  Making a backup of the olf files...")



file_equivalent = {
    "ar.json":    "lang_ar.json",
    "ca.json":    "lang_ca.json",
    "cs.json":    "lang_cs.json",    
    "da.json":    "lang_da.json",
    "de.json":    "lang_de.json",
    "el.json":    "lang_el.json",
    "en.json":    "lang_en.json",
    "es.json":    "lang_es.json",
    "fi.json":    "lang_fi.json",
    "he.json":    "lang_he.json",
    "fr.json":    "lang_fr.json",
    "hu.json":    "lang_hu.json",
    "id.json":    "lang_id.json",
    "it.json":    "lang_it.json",
    "ja.json":    "lang_ja.json",
    "ko.json":    "lang_ko.json",
    "lt.json":    "lang_lt.json",
    "lv.json":    "lang_lv.json",
    "nb.json":    "lang_nb.json",
    "nl.json":    "lang_nl.json",
    "nn.json":    "lang_nn.json",
    "pl.json":    "lang_pl.json",
    "pt-PT.json": "lang_pt_PT.json",
    "pt-BR.json": "lang_pt_BR.json",
    "ru.json":    "lang_ru.json",
    "sk.json":    "lang_sk.json",
    "sr.json":    "lang_sr.json",
    "sv.json":    "lang_sv.json",
    "th.json":    "lang_th.json",
    "tr.json":    "lang_tr.json",
    "uk.json":    "lang_ua.json",
    "vi.json":    "lang_vi.json",
    "zh-Hant-TW.json": "lang_zh_TW.json",
    "zh-Hans-CN.json": "lang_zh_CN.json",
}



olddir = "lang_backup"+str(int(time.time()))
os.mkdir(olddir)
for file in glob.glob('lang_*.json'):                           
    shutil.move(file, olddir)           

print(f"  Backup complete. The old files were moved to {olddir}")
print()
print("-------------------------------------------------------")
print()
print("  Extracting language files...")


zip_file = zipfile.ZipFile("langs.zip")
for name in zip_file.namelist():
    try:
        zip_file.extract(name, "./")
        os.rename(name, file_equivalent[str(name)])
        print(f"  Extracted {file_equivalent[str(name)]}")
    except KeyError as e:
        print(type(name))
        f = input(f"  The file {name} was not expected to be in here. Please write the name for the file. It should follow the following structure: lang_[CODE].json: ")
        zip_file.extract(f, "./")
        os.rename(f, file_equivalent[str(name)])
        print(f"  Extracted {f}")
zip_file.close() 
os.remove("langs.zip")

print("  Process complete!")
print()
print("-------------------------------------------------------")
print()
os.system("pause")