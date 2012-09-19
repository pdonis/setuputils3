#!/usr/bin/python -u
"""
Setup script for setuputils
Copyright (C) 2012 by Peter A. Donis

Released under the Python Software Foundation License.
"""


name = "setuputils"
version = "0.9"
description = "A utility module to automate away boilerplate in Python setup scripts."

author = "Peter A. Donis"
author_email = "peterdonis@alum.mit.edu"

license = "PSF"

dev_status = "Beta"

classifiers = """
Environment :: Console
Intended Audience :: Developers
Operating System :: MacOS :: MacOS X
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: POSIX :: Linux
Topic :: Software Development :: Libraries :: Python Modules
"""

py_modules = ["setuputils"]


if __name__ == '__main__':
    from distutils.core import setup
    from setuputils import convert_md_to_rst, setup_vars
    convert_md_to_rst()
    setup(**setup_vars(globals()))