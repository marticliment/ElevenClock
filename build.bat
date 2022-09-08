python -m pip install -r requirements.txt
python -m pip install setuptools==49.1.3
python -m pip uninstall python-dateutil -y
python -m easy_install python-dateutil
python apply_version.py
xcopy elevenclock elevenclock_bin /E /H /C /I /Y
cd elevenclock_bin
python -m compileall -b .
del /S *.py
rmdir /Q /S __pycache__
rmdir /Q /S external\__pycache__
rmdir /Q /S lang\__pycache__
rmdir /Q /S build
rmdir /Q /S dist
del lang/APIKEY.txt
python -m PyInstaller ../elevenclock/__init__.py --icon "resources/icon.ico" --add-binary "*.pyc;." --add-data "resources;resources" --add-data "lang;lang" --clean --exclude-module PySide2 --windowed --version-file ../elevenclock-version-info --name ElevenClock
cd dist
rename ElevenClock ElevenClockBin
cd ..
cd ..
rmdir /Q /S ElevenClockBin
cd elevenclock_bin
cd dist
move ElevenClockBin ../../
cd ..
rmdir /Q /S build
rmdir /Q /S dist
del ElevenClock.spec
cd ..
rmdir /Q /S elevenclock_bin
cd ElevenClockBin
cd tcl
rmdir /Q /S tzdata
cd ..
cd lang
del APIKEY.txt
del download_translations.pyc
cd ..
del opengl32sw.dll
del Qt6Quick.dll
del Qt6Qml.dll
del Qt6OpenGL.dll
del Qt6QmlModels.dll
del Qt6Network.dll
del Qt6DataVisualization.dll
del Qt6VirtualKeyboard.dll
cd PySide6
del QtDataVisualization.pyd
del QtOpenGL.pyd
cd ..
cd ..
set INSTALLATOR="%SYSTEMDRIVE%\Program Files (x86)\Inno Setup 6\ISCC.exe"
if exist %INSTALLATOR% (
    %INSTALLATOR% "ElevenClock.iss"
    ElevenClock.Installer.exe
) else (
    echo "Make installer is skipped, because installator missing."
    echo "Running app..."
    start /b ElevenClockBin/ElevenClock.exe
)
python generate_release.py
pause
