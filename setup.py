#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

__version__ = '2.0.0'

setup(
    name = 'persephonep',
    version = __version__,
    description = 'Web Browser developed with Python3 and PyQt5',
    long_description = '''
    Some people are limited with their Web Browser.
    The faster we browse web pages, the more efficient we correct the information.
    ''',
    author = 'Shin Kurita',
    url = 'https://github.com/montblanc18/persephonep',
    license = 'MIT',
    install_package_data = True,
    package_dir = {'input':'input','resource':'resource'},
    packages = find_packages(exclude = ('tests', 'docs')),
    package_data = {'input':['input'],},
    install_requires = ['PyQt5', 'PyQtWebEngine', 'pytest-qt'],
    test_suite = 'tests'
)
