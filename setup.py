#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

NAME = 'corruptor'
DESCRIPTION = 'Realistic data corruption (based on GeCo).'
URL = 'https://github.com/onnovalkering/corruptor'
EMAIL = 'onnovalkering@users.noreply.github.com'
AUTHOR = 'Onno Valkering'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = None

REQUIRED = [
    'future',
]

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')
        
        sys.exit()

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=[
        'corruptor',
        'corruptor.geco',
        'corruptor.utils'
    ],
    package_data={
        'corruptor': [
            'geco/lookup-files/ocr-variations.csv',
            'geco/lookup-files/phonetic-variations.csv',
            'geco/lookup-files/surname-misspell.csv'
        ]
    },
    install_requires=REQUIRED,
    include_package_data=True,
    license='MPL-2.0',
    classifiers=[
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    cmdclass={
        'upload': UploadCommand,
    },
)