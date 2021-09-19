cd elevenclock
rmdir /Q /S build
rmdir /Q /S dist
PyInstaller __init__.py --icon icon.ico --onefile --windowed
cd dist
rmdir /Q /S build
rmdir /Q /S dist
move __init__.exe ../../
cd ..
cd ..
rename __init__.exe ElevenClock.exe
pause
