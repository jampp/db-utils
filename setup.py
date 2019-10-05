# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from db_utils import __version__


requirements = open('requirements.txt').read(-1).split()

setup(
    name='db-utils',
    version=__version__,
    description='Run the database migrations',
    author='Jampp',
    install_requires=requirements,
    entry_points={
        'console_scripts': {
            'db-utils = db_utils.main:main'
        }
    },
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
    package_data={'': ['VERSION']},
    test_suite='tests',
)
