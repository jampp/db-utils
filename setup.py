#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


setup_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(setup_dir, "README.rst")) as readme_file:
    readme = readme_file.read()

with open(os.path.join(setup_dir, "CHANGELOG.rst")) as history_file:
    history = history_file.read()

with open(os.path.join(setup_dir, "migratron", "VERSION")) as version_file:
    version = version_file.read().strip()


setup(
    name="migratron",
    description="Run the database migrations",
    version=version,
    author="Jampp",
    author_email="tech@jampp.com",
    # this should include the same requirements as requirements.txt
    # but without the fixed version. For more info check
    # https://packaging.python.org/discussions/install-requires-vs-requirements/
    install_requires=["pygments", "psycopg2",],
    license="BSD 3-Clause",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    package_data={"migratron": ["VERSION"],},
    packages=find_packages(),
    test_suite="tests",
    url="https://github.com/jampp/migratron",
    zip_safe=False,
    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Database",
        "Topic :: Software Development",
    ],
)
