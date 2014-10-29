#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import repo_name
version = repo_name.__version__

setup(
    name='breezo',
    version=version,
    author='',
    author_email='movemountains4321@gmail.com',
    packages=[
        'repo_name',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['repo_name/manage.py'],
)