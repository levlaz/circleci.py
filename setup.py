#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
:copyright: (c) 2017 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""
from setuptools import setup

def readme():
    """print long description"""
    with open('README.rst') as f:
        return f.read()

setup(
    name="circleci.py",
    version="1.1.0",
    description="Python wrapper for the CircleCI API",
    long_description=readme(),
    url="https://github.com/levlaz/circleci.py",
    author="Lev Lazinskiy",
    author_email="lev@levlaz.org",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independentn",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
        "Programming Language :: Python",
        "Programming Langauge :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    keywords='circleci ci cd api sdk',
    packages=['circleci'],
    install_requires=[
        'requests==2.18.4',
    ],
)
