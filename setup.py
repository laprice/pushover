#!/usr/bin/env python

from setuptools import setup

setup(
    name='pushover',
    version='0.5',
    description='Send messages via https://pushover.net/ to phones',
    author='Larry Price, Daniele Sluijters, Josh Kaizoku, Bryce Jasmer',
    author_email='laprice@gmail.com, github@daenney.net, kaizoku@phear.cc, bryce@jasmer.com',
    py_modules=['pushover.pushover'],
    install_requires = ['Requests == 2.32.3'],
    license='BSD',
    url='http://github.com/laprice/pushover',
    entry_points={
        'console_scripts': ['pushover = pushover.pushover:main']
    }
)
