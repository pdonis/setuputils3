#!/usr/bin/python3 -u
"""
Setup script for setuputils
Copyright (C) 2012-2013 by Peter A. Donis

Released under the Python Software Foundation License.
"""


name = "setuputils3"
version = "0.9.4"
description = "A utility to automate away boilerplate in Python 3 setup scripts."
startline = 4

author = "Peter A. Donis"
author_email = "peterdonis@alum.mit.edu"

license = "PSF"

dev_status = "Beta"

classifiers = """
Environment :: Console
Intended Audience :: Developers
Intended Audience :: System Administrators
Operating System :: OS Independent
Topic :: Software Development :: Libraries :: Python Modules
Topic :: System :: Systems Administration
Topic :: Utilities
"""

py_modules = ["setuputils"]


if __name__ == '__main__':
    from subprocess import call
    from distutils.core import setup
    from setuputils import convert_md_to_rst, setup_vars
    convert_md_to_rst()
    call(['sed', '-i', 's/github.com\/pdonis/pypi.python.org\/pypi/', 'README'])
    setup(**setup_vars(globals()))
