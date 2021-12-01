rmdir /Q /S __init__
cd elevenclock
rmdir /Q /S build
rmdir /Q /S dist
python39 -m PyInstaller __init__.py --icon "resources/icon.ico" --add-binary "*.py;." --add-data "resources;resources" --add-data "lang;lang" --debug all --clean --version-file ../elevenclock-version-info
rem --add-data "%homedrive%%homepath%\AppData\Local\Programs\Python\Python39\Lib\site-packages\PySide6\plugins;PySide6/plugins"
cd dist
move __init__ ../../
cd ..
rmdir /Q /S build
rmdir /Q /S dist
del __init__.spec
cd ..
taskkill /im ElevenClock.exe /f
cd __init__
__init__.exe
pause
