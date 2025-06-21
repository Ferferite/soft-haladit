from setuptools import setup

APP = ['main.py']   # aici pui numele script-ului principal
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'includes': ['moviepy.editor', 'moviepy.video.fx.all', 'tkinter'],
    'packages': ['moviepy', 'tkinter'],
    # dacă ai iconiţă, de ex. resources/icon.icns
    # 'iconfile': 'resources/icon.icns',
    'plist': {
        'CFBundleName': 'TikTokConverter',
        'CFBundleIdentifier': 'com.exemplu.tiktokconverter',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
    }
}

setup(
    app=APP,
    name='TikTokConverter',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
