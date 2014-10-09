# -*- coding=utf-8 -*-
from distutils.core import setup

setup(
    # Application name:
    name="TimeDiff",

    # Version number (initial):
    version="0.9.3", 

    # Packages
    packages=["timediff"],

    # Package data
    package_data={
    "timediff":['README.md',
'LICENSE.txt',
'timediff/doc/*.html',
'timediff/*.py',
'timediff/*.json',
'bin/*']
    },

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

    # License
    license=open("LICENSE.txt").read(),

    # Description
    description="Program for login and plotting time-differences in log-files.",

    # Long description
    long_description=open("README.md").read(),

    # Scripts
    scripts=["bin/time-diff", "bin/time-diff-plot"]

)
