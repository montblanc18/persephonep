#!/usr/bin/env python

from glob import glob

from setuptools import setup
from setuptools import find_packages

__version__ = '2.0.1'

setup(
    name='persephonep',
    version=__version__,
    description='Web Browser developed with Python3 and PyQt5',
    long_description='''
    Some people are limited with their Web Browser.
    The faster we browse web pages, the more efficient we correct the information.
    ''',
    author='Shin Kurita',
    url='https://github.com/montblanc18/persephonep',
    license='MIT',
    # install_package_data = True,
    # py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    package_dir={'':'src', 'resource':'resource'},
    packages = find_packages(where='src', exclude = ('tests', 'docs')),
    # package_data = {'input':['input'],},
    # install_requires = ['PyQt5', 'PyQtWebEngine', 'pytest-qt'],
    # test_suite = 'tests'
)
