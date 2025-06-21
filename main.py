# setup.py
from setuptools import setup

APP = ['main.py']
OPTIONS = {
    'argv_emulation': True,
    'standalone': True,              # build complet standalone
    'packages': ['moviepy', 'tkinter'],
    'includes': [
        'moviepy.editor',
        'moviepy.video.fx.all',
        'imageio_ffmpeg'
    ],
    'plist': {
        'CFBundleName': 'TikTokConverter',
        'CFBundleIdentifier': 'com.yourdomain.tiktokconverter',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
    }
}

setup(
    app=APP,
    name='TikTokConverter',
    data_files=[],
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
