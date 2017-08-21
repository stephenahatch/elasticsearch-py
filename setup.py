# -*- coding: utf-8 -*-
from os.path import join, dirname
from setuptools import setup, find_packages
import sys

VERSION = (5, 4, 0, 5248)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

f = open(join(dirname(__file__), 'README'))
long_description = f.read().strip()
f.close()

install_requires = [
    'urllib3<1.22,>=1.21.1',
]
tests_require = [
    'requests>=2.0.0, <3.0.0',
    'nose',
    'coverage',
    'mock',
    'pyaml',
    'nosexcover'
]

# use external unittest for 2.6
if sys.version_info[:2] == (2, 6):
    install_requires.append('unittest2')

setup(
    name = 'elasticsearch',
    description = "Python client for Elasticsearch (with Sherlock specific bug fixed), this should go away once elasticsearch client PRs merged.",
    license="Apache License, Version 2.0",
    url = "https://github.com/stephenahatch/elasticsearch-py/",
    long_description = long_description,
    version = __versionstr__,
    author = "Tyler Harden",
    author_email = "tyler.harden@vertical-knowledge.com",
    packages=find_packages(
        where='.',
        exclude=('test_elasticsearch*', )
    ),
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    install_requires=install_requires,

    test_suite='test_elasticsearch.run_tests.run_all',
    tests_require=tests_require,

    extras_require={
        'develop': tests_require + ["sphinx", "sphinx_rtd_theme"]
    },
)
