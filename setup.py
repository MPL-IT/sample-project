#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import exists, dirname, realpath
from setuptools import setup, find_packages

name = 'sample-project'

setup(
    name=name,
    author='Guybrush Threepwood',
    version='0.0.1',
    packages=find_packages(),
    package_dir={name: name},
    include_package_data=True,
    license='MIT',
    description='A sample project',
    long_description='Some longer description for the project',
    install_requires=[
                      'numpy>=1.17.0',
                      ],
    setup_requires=["pytest-runner"],
    python_requires=">=3.6",
    tests_require=["pytest"],
)