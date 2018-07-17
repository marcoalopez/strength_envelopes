#!/usr/bin/env python
import sys
import os
from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

with open('LICENSE.txt') as fh:
    license = fh.read()

# Check for Python 3
v = sys.version_info
if (v[0] >= 3 and v[:2] < (3, 5)):
    error = "ERROR: GrainSizeTools requires Python version 3.5 or above."
    print(error, file=sys.stderr)
    sys.exit(1)

sys.path.append(os.path.join(sys.path[0], 'strength_envelopes'))

setup(
    name="strength_envelopes",
    version="1.0",
    author="Marco A. Lopez-Sanchez",
    author_email="marcoalopez@outlook.com",
    description="A Python script to generate crust and lithoshere strenght envelopes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcoalopez/strength_envelopes",
    license=license,
    packages=find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License Version 2.0",
        "Operating System :: OS Independent",
    ),
)
