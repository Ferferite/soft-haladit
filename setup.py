from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    # Încearcă semi-standalone ca să incluzi toate modulele Python necesare
    'semi_standalone': True,

    # Bundlează întreg pachetul moviepy și dependenţele sale Python
    'packages': [
        'moviepy',
        'imageio',
        'numpy',
        'decorator',
        'tkinter'
    ],
    # Include explicit modulele folosite
    'includes': [
        'moviepy.editor',
        'moviepy.video.fx.all',
        'imageio_ffmpeg'    # binding-ul care pornește ffmpeg
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
