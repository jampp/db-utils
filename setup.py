# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

current_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(current_dir, 'db_utils', 'VERSION'), 'r') as vf:
    version = vf.read().strip()


def parse_requirements_txt(filename='requirements.txt'):
    with open(os.path.join(current_dir, filename)) as requirements_file:
        requirements = requirements_file.readlines()
        # remove whitespaces
        requirements = [line.strip().replace(' ', '') for line in requirements]
        # remove all the requirements that are comments
        requirements = [line for line in requirements if not line.startswith('#')]
        # remove empty lines
        requirements = list(filter(None, requirements))
        return requirements


setup(
    name='db-utils',
    version=version,
    description='Run the database migrations',
    author='Jampp',
    install_requires=parse_requirements_txt(),
    extras_require={'dev': parse_requirements_txt('requirements-dev.txt')},
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
