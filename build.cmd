@echo off
setlocal EnableDelayedExpansion

set "py=%cd%\venv\Scripts\python.exe"

IF EXIST %py% (
    echo Using VENV Python
) ELSE (
    set "py=python"
    echo Using system Python
)

set "option="
for %%a in (%*) do (
   if not defined option (
      set arg=%%a
      echo %arg%
      if "!arg:~0,2!" equ "--" (
        set "option!arg!=1"
        set "option="
      ) else (
        if "!arg:~0,1!" equ "-" set "option=!arg!"
      )
   ) else (
      set "option!option!=%%a"
      set "option="
   )
)

set option

%py% -m pip install -r requirements.txt
%py% -m pip install packaging
if defined option--only-requirements (
    goto :end
)

%py% scripts/check_python_version.py --min-version "3.11.0"
if %errorlevel% neq 0 (
    exit /b %errorlevel%
)

@echo off

%py% scripts/apply_versions.py

rmdir /Q /S ElevenClockBin
xcopy elevenclock elevenclock_bin /E /H /C /I /Y
pushd elevenclock_bin

%py% -m compileall -b .
if %errorlevel% neq 0 goto:error

del /S *.py
rmdir /Q /S __pycache__
rmdir /Q /S build
rmdir /Q /S dist
rmdir /Q /S external\__pycache__
rmdir /Q /S lang\__pycache__
copy ..\elevenclock\__init__.py .\

%py% -m PyInstaller elevenclock.spec 
if %errorlevel% neq 0 goto:error

timeout 2

move dist\ElevenClock ..\ElevenClockBin
if %errorlevel% neq 0 goto:error
popd

rmdir /Q /S elevenclock_bin

pushd ElevenClockBin\PySide6
del opengl32sw.dll
del Qt6Network.dll
del Qt6OpenGL.dll
del Qt6Pdf.dll
del Qt6Qml.dll
del Qt6QmlModels.dll
del Qt6Quick.dll
del Qt6VirtualKeyboard.dll
del QtNetwork.pyd
popd

pushd ElevenClockBin\tcl
rmdir /Q /S tzdata
popd

pushd ElevenClockBin\lang
del download_translations.pyc
popd

pushd ElevenClockBin\PySide6\plugins\imageformats
move qico.dll filetomaintain
del *.dll
move filetomaintain qico.dll
popd


if defined option--no-installer (
    goto :skip-installer
)

echo You might want to sign your executable now
pause

set INSTALLATOR="%SYSTEMDRIVE%\Program Files (x86)\Inno Setup 6\ISCC.exe"
if exist %INSTALLATOR% (
    %INSTALLATOR% "ElevenClock.iss"
    ElevenClock.Installer.exe
) else (
    echo Make installer is skipped, because installator missing.
    echo Running app...
    start /b ElevenClockBin/ElevenClock.exe
)

echo You might want to sign your installer now
pause

:skip-installer

if defined option--release (
    %py% scripts/generate_release.py
)

goto:end

:error
echo Error!

:end
pause
