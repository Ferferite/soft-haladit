from setuptools import setup

APP = ['main.py']   # script-ul tău principal
DATA_FILES = []
OPTIONS = {
    # semi‐standalone înseamnă “încorporează Python.framework și pachete pip”
    'semi_standalone': True,
    'argv_emulation': True,

    # bundează aceste pachete întregi
    'packages': [
        'moviepy',
        'imageio',
        'imageio_ffmpeg',
        'numpy',
        'decorator',
        'tkinter',
    ],

    # asigură-te că includi modulele interne folosite de MoviePy
    'includes': [
        'moviepy.editor',
        'moviepy.video.fx.all',
    ],

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
