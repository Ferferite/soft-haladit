from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'semi_standalone': True,
    'argv_emulation': True,
    'packages': [
        'moviepy',
        'imageio',
        'imageio_ffmpeg',
        'numpy',
        'decorator',
        'tkinter'
    ],
    'includes': [
        'moviepy.editor',
        'moviepy.video.fx.all'
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
