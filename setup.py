# -*- coding=utf-8 -*-
from setuptools import setup

setup(
    # Application name:
    name="TimeDiff",

    # Version number (initial):
    version="1.17", 

    # Packages
    packages=["timediff"],

    data_files=[('/etc/timediff', ['timediff/timediff.json'])],

    # Details
    url="https://github.com/nomelif/time-diff",

    # Application author details:
    author="Théo Friberg",
    author_email="theo.friberg@gmail.com",

    # Dependent packages (distributions)
    requires=[
        "matplotlib", "numpy", "scipy"
    ],

    provides=["timediff",],

    # License
    license=open("LICENSE.txt").read(),

    # Description
    description="Program for login and plotting time-differences in log-files.",

    # Long description
    long_description=open("README.md").read(),

    # Scripts
    scripts=["bin/timedifftext", "bin/timediffplot"]

)
