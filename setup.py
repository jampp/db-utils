# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

requirements = open('requirements.txt').read(-1).split()

setup_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(setup_dir, 'pytest_27_app', 'VERSION'), 'r') as vf:
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
    ],
    package_data={'': ['VERSION']},
    test_suite='tests',
)
