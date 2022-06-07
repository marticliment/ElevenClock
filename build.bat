python -m pip install -r requirements.txt
python -m pip install setuptools==49.1.3
xcopy elevenclock elevenclock_bin  /E /H /C /I 
cd elevenclock_bin
python -m compileall -b .
del /S *.py
rmdir /Q /S __pycache__
rmdir /Q /S external\__pycache__
rmdir /Q /S lang\__pycache__
rmdir /Q /S build
rmdir /Q /S dist
python -m PyInstaller ../elevenclock/__init__.py --icon "resources/icon.ico" --add-binary "*.pyc;." --add-data "resources;resources" --add-data "lang;lang" --onefile --windowed --clean --version-file ../elevenclock-version-info
rem --add-data "%homedrive%%homepath%\AppData\Local\Programs\Python\Python39\Lib\site-packages\PySide6\plugins;PySide6/plugins"
cd dist
move __init__.exe ../../
cd ..
rmdir /Q /S build
rmdir /Q /S dist
del __init__.spec
cd ..
rmdir /Q /S elevenclock_bin
taskkill /im ElevenClock.exe /f
del ElevenClock.exe
rename __init__.exe ElevenClock.exe
ElevenClock.exe
pause
