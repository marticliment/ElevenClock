# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import importlib, os

#package_imports = [['qtmodern', ['resources/frameless.qss', 'resources/style.qss']]]



a = Analysis(['__init__.py'],
             pathex=['Y:\ElevenClock-Store\elevenclock_bin'],
#             binaries=[('*.pyc', '.')],
             datas=[('resources/', 'resources/'), ("lang/", "lang/")],
             hiddenimports=['pkg_resources.py2_warn', "win32gui"],
             hookspath=[],
             runtime_hooks=[],
             excludes=['eel', 'tkinter', "PyQt5", "PySide2", "pygame", "numpy", "matplotlib", "elevenclock", "zroya"],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)


pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='elevenclock',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon="resources/icon.ico",
    version="../elevenclock-version-info"
)


coll = COLLECT(
    exe,
    a.binaries,
#    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ElevenClock',
)