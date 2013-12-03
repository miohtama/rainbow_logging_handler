#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name             = 'rainbow_logging_handler',
    description      = 'Ultimate Python colorized logger',
    long_description = open('README.rst').read(),
    url              = 'https://github.com/laysakura/rainbow_logging_handler',
    license          = 'LICENSE.txt',
    version          = '1.0.0',
    author           = 'Mikko Ohtamaa, Sho Nakatani',
    author_email     = 'mikko@opensourcehacker.com, lay.sakura@gmail.com',
    install_requires = [
        'logutils',
    ],
    tests_require    = [
        'nose',
    ],
    packages         = [
        'rainbow_logging_handler',
        'rainbow_logging_handler.test',
    ],
    scripts          = [
    ],
    classifiers      = '''
Programming Language :: Python
Development Status :: 5 - Production/Stable
License :: Public Domain
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: Implementation :: PyPy
Operating System :: POSIX :: Linux
'''.strip().splitlines()
)