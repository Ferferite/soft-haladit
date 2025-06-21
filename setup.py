from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'semi_standalone': True,
    'frameworks': [
        '/Library/Frameworks/Python.framework'    # <–– Python-ul de la python.org
    ],
    'packages': ['moviepy', 'imageio', 'numpy', 'decorator', 'tkinter'],
    'includes': ['moviepy.editor', 'moviepy.video.fx.all', 'imageio_ffmpeg'],
    'plist': {
        'CFBundleName': 'TikTokConverter',
        'CFBundleIdentifier': 'com.exemplu.tiktokconverter',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        # explicităm unde să caute runtime-ul dacă ceva nu e detectat automat
        'PyRuntimeLocations': [
            '@executable_path/../Frameworks/Python.framework/Versions/3.11'
        ]
    }
}

setup(
    app=APP,
    name='TikTokConverter',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
