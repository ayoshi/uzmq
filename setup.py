# -*- coding: utf-8 -
#
# This file is part of uvzmq. See the NOTICE for more information.

import os
import sys

from setuptools import setup, find_packages

with open(
        os.path.join(
            os.path.dirname(__file__), "uzmq", "__version__.py"
        )
) as version_file:
    exec(version_file.read())


py_version = sys.version_info[:2]

if py_version < (2, 6):
    raise RuntimeError('On Python 2, Gaffer requires Python 2.6 or better')


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.0',
    'Programming Language :: Python :: 3.1',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Topic :: System :: Boot',
    'Topic :: System :: Monitoring',
    'Topic :: System :: Systems Administration',
    'Topic :: Software Development :: Libraries']


# read long description
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    long_description = f.read()

DATA_FILES = [
        ('uzmq', ["LICENSE", "MANIFEST.in", "NOTICE", "README.rst",
                        "THANKS", "UNLICENSE"])
        ]


setup(name='uzmq',
      version = __version__,
      description = 'libuv interface for ZeroMQ',
      long_description = long_description,
      classifiers = CLASSIFIERS,
      license = 'BSD',
      url = 'http://github.com/benoitc/uzmq',
      author = 'Benoit Chesneau',
      author_email = 'benoitc@e-engura.org',
      packages=find_packages(),
      install_requires = [
          'pyuv>=0.8.3',
          'pyzmq'
      ],
      data_files = DATA_FILES)
