#!/usr/bin/env python3

from setuptools import setup

setup(name='gitd',
      version='1.0',
      packages=['gitd'],
      entry_points={
          'console_scripts': [
              'gitd=gitd.cli:main'
          ]
      }
      )
