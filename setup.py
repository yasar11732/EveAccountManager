# -*- coding: utf-8 -*-
#!/usr/bin/env python

from setuptools import setup, find_packages
import sys

DESCRIPTION = ("""Extension for Python EVE Framework that provides account and session management
    functionality
    """)
# LONG_DESCRIPTION = open('README.rst').read()
VERSION = __import__('eve_account_manager').__version__

setup(
    name='EveAccountManager',
    version=VERSION,
    description=DESCRIPTION,
    # long_description=LONG_DESCRIPTION,
    author='Yaşar Arabacı',
    author_email='yasar11732@gmail.com',
    url='https://github.com/yasar11732/EveAccountManager',
    license='ISC',
    platforms=["any"],
    packages=find_packages(),
    include_package_data=True,
    tests_require=['pytest'],
    test_suite="eve_account_manager.tests",
    install_requires=['eve'],
    keywords=['authorization'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
)