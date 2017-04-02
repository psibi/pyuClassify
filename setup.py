#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

__author__ = 'Sibi <sibi@psibi.in>'
__version__ = '1.0.0'  #major.minor.micro

setup(
    # Basic package information.
    name='uclassify',
    version=__version__,
    packages=find_packages(),

    # Packaging options.
    include_package_data=True,

    # Package dependencies.
    install_requires=['requests'],

    # Metadata for PyPI.
    author='Sibi',
    author_email='sibi@psibi.in',
    license='GNU GPLv3',
    url='https://github.com/psibi/pyuClassify',
    keywords='uClassify API',
    description='Python Wrapper for accessing uClassify services',
    long_description=open('README.txt').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet'
    ]
)
