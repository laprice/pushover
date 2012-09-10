#!/usr/bin/env python

from setuptools import setup

setup(name='pushover',
      version='0.2',
      description='Send messages via https://pushover.net/ to phones',
      author='Larry Price, Daniele Sluijters',
      author_email='laprice@gmail.com, github@daenney.net',
      py_modules=['pushover'],
      install_requires = ['Requests >= 0.14.0'],
      license='BSD',
      url='http://github.com/daenney/pushover',
)
