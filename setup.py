#!/usr/bin/env python

from setuptools import setup

setup(name='pushover',
      version='0.1',
      description='send messages via https://pushover.net/ to phones',
      author='Larry Price',
      author_email='laprice@gmail.com',
      py_modules=['pushover'],
      install_requires = ['Requests >= 0.14.0'],
      license='BSD',
      url='http://github.com/laprice/pushover',
)
