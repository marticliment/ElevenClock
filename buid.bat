cd elevenclock
rmdir /Q /S build
rmdir /Q /S dist
PyInstaller __init__.py --icon icon.ico --onefile --windowed --clean
cd dist
move __init__.exe ../../
cd ..
rmdir /Q /S build
rmdir /Q /S dist
cd ..
rename __init__.exe ElevenClock.exe
ElevenClock.exe
pause
