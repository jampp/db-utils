# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

requirements = open('requirements.txt').read(-1).split()

setup_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(setup_dir, 'db_utils', 'VERSION'), 'r') as vf:
    version = vf.read().strip()


setup(
    name='db-utils',
    version=version,
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
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    license='BSD 3-Clause',
    package_data={'': ['VERSION', 'requirements.txt', 'LICENSE']},
    test_suite='tests',
)
