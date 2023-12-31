#Configure APP cerator for macos
from setuptools import setup

APP = ['main.py']
OPTIONS = {
    'argv_emulation': False,
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
